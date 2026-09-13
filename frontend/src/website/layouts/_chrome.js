import { computed } from 'vue'
import { sectionComponent } from '../registry.js'
import { isSectionBlank } from '../localize.js'
import { useSiteContext } from '../composables/useSiteContext.js'

const PINNED = { header: 'header', footer: 'footer' }

/**
 * Split a site's sections into the pieces a page chrome arranges.
 *
 * Header and footer are pulled out because every chrome frames them
 * differently — a sidebar layout puts the nav down the side, a one-pager pins
 * it — while the body sections are just a list to lay out in order.
 */
export function usePageSections() {
  const { sections, isEditing, branding } = useSiteContext()

  const resolved = computed(() =>
    sections.value
      .map((section) => ({ ...section, component: sectionComponent(section.type, section.variant) }))
      .filter((section) => section.component)
      // In the builder every block stays visible with its placeholders, because
      // an owner cannot fill in a section they cannot see.
      .filter((section) => isEditing.value || !isSectionBlank(section, branding.value)),
  )

  return {
    header: computed(() => resolved.value.find((s) => s.type === PINNED.header) || null),
    footer: computed(() => resolved.value.find((s) => s.type === PINNED.footer) || null),
    body: computed(() => resolved.value.filter((s) => s.type !== PINNED.header && s.type !== PINNED.footer)),
    all: resolved,
  }
}

/** A stable key so Vue reuses a section's DOM across content edits. */
export function sectionKey(section) {
  return `${section.type}:${section.key}:${section.variant}`
}
