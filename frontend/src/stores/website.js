import { defineStore } from 'pinia'
import { websiteApi } from '@/services/api'

const AUTOSAVE_MS = 700

/**
 * Builder state for the desk's website.
 *
 * The builder edits a draft and the canvas has to reflect it instantly, so
 * changes are applied locally first and pushed on a debounce. The server is
 * still the authority: every save replaces the local row with what came back,
 * which is how a field the API rejected or narrowed shows up in the form
 * instead of silently disagreeing with what is stored.
 */
export const useWebsiteStore = defineStore('website', {
  state: () => ({
    site: null,
    sections: [],
    assets: [],
    publications: [],
    loading: false,
    saving: false,
    error: '',
    /** Section ids with a save in flight, so the UI can show per-card progress. */
    pending: new Set(),
    timers: {},
  }),

  getters: {
    layoutSlug: (state) => state.site?.layout_slug || '',
    themeSlug: (state) => state.site?.theme_slug || '',
    overrides: (state) => state.site?.theme_overrides || {},
    primaryLocale: (state) => state.site?.primary_locale || 'en',
    locales: (state) => state.site?.locales || ['en'],
    isPublished: (state) => state.site?.status === 'published',
    publicUrl: (state) => state.site?.public_url || '/site/',
    hasUnpublishedChanges: (state) => {
      if (!state.site || state.site.status !== 'published') return false
      return new Date(state.site.updated_at) > new Date(state.site.published_at)
    },
  },

  actions: {
    async load() {
      this.loading = true
      this.error = ''
      try {
        const [site, sections] = await Promise.all([websiteApi.site(), websiteApi.sections()])
        this.site = site.data
        this.sections = sections.data
      } catch (err) {
        this.error = err?.message || 'load_failed'
      } finally {
        this.loading = false
      }
    },

    async loadAssets() {
      const { data } = await websiteApi.assets()
      this.assets = data
    },

    async loadPublications() {
      const { data } = await websiteApi.publications()
      this.publications = data
    },

    /** Merge a site change locally, then push it once typing settles. */
    patchSite(changes, { immediate = false } = {}) {
      this.site = { ...this.site, ...changes }
      this._debounce('site', immediate, async () => {
        const { data } = await websiteApi.updateSite(changes)
        this.site = data
      })
    },

    patchSection(id, changes, { immediate = false } = {}) {
      const index = this.sections.findIndex((section) => section.id === id)
      if (index === -1) return
      this.sections[index] = { ...this.sections[index], ...changes }
      this.pending.add(id)
      this._debounce(`section:${id}`, immediate, async () => {
        try {
          const { data } = await websiteApi.updateSection(id, changes)
          const at = this.sections.findIndex((section) => section.id === id)
          if (at !== -1) this.sections[at] = data
        } finally {
          this.pending.delete(id)
        }
      })
    },

    async applyLayout(layoutSlug) {
      this.saving = true
      try {
        const { data } = await websiteApi.applyLayout(layoutSlug)
        this.site = data
        // Switching layout re-binds variants and may seed new sections, so the
        // list is refetched rather than guessed at from the client side.
        const { data: sections } = await websiteApi.sections()
        this.sections = sections
      } finally {
        this.saving = false
      }
    },

    async addSection(sectionType) {
      const { data } = await websiteApi.addSection({ section_type: sectionType })
      this.sections.push(data)
      return data
    },

    async removeSection(id) {
      await websiteApi.deleteSection(id)
      this.sections = this.sections.filter((section) => section.id !== id)
    },

    async reorder(orderedIds) {
      const byId = new Map(this.sections.map((section) => [section.id, section]))
      this.sections = orderedIds.map((id) => byId.get(id)).filter(Boolean)
      const { data } = await websiteApi.reorderSections(orderedIds)
      this.sections = data
    },

    async uploadAsset(file, role = 'image') {
      const form = new FormData()
      form.append('image', file)
      form.append('role', role)
      const { data } = await websiteApi.uploadAsset(form)
      this.assets.unshift(data)
      return data
    },

    async deleteAsset(id) {
      await websiteApi.deleteAsset(id)
      this.assets = this.assets.filter((asset) => asset.id !== id)
    },

    async publish(note = '') {
      await this.flush()
      this.saving = true
      try {
        const { data } = await websiteApi.publish(note)
        this.site = data.site
        this.publications.unshift(data.publication)
      } finally {
        this.saving = false
      }
    },

    async unpublish() {
      const { data } = await websiteApi.unpublish()
      this.site = data
    },

    async restore(version) {
      const { data } = await websiteApi.restore(version)
      this.site = data.site
      this.publications.unshift(data.publication)
      await this.load()
    },

    /** Run every pending debounce now — used before publishing or leaving. */
    async flush() {
      const runners = Object.values(this.timers).map((entry) => entry.run())
      this.timers = {}
      await Promise.all(runners)
    },

    _debounce(key, immediate, run) {
      const existing = this.timers[key]
      if (existing) clearTimeout(existing.handle)

      const entry = {
        handle: 0,
        run: async () => {
          clearTimeout(entry.handle)
          delete this.timers[key]
          this.saving = true
          try {
            await run()
            this.error = ''
          } catch (err) {
            this.error = err?.message || 'save_failed'
          } finally {
            this.saving = false
          }
        },
      }
      this.timers[key] = entry
      if (immediate) return entry.run()
      entry.handle = setTimeout(entry.run, AUTOSAVE_MS)
      return Promise.resolve()
    },
  },
})
