<template>
  <div class="wb animate-fade-in-up">
    <header class="wb__head">
      <div>
        <h1>{{ $t('website.builder.title') }}</h1>
        <p>{{ $t('website.builder.subtitle') }}</p>
      </div>
      <div class="wb__head-actions">
        <a v-if="store.isPublished" class="btn-luxury-outline" :href="store.publicUrl" target="_blank" rel="noopener">
          <i class="fas fa-arrow-up-right-from-square" /> {{ $t('website.builder.viewSite') }}
        </a>
        <button type="button" class="btn-luxury" :disabled="store.saving" @click="publish">
          <i class="fas fa-rocket" />
          {{ store.isPublished ? $t('website.builder.republish') : $t('website.builder.publish') }}
        </button>
      </div>
    </header>

    <AlertMessage v-if="store.error" type="error" :message="store.error" />
    <LoadingSpinner v-if="store.loading" />

    <div v-else class="wb__grid">
      <aside class="wb__side">
        <WebsiteStepRail v-model="step" :steps="STEPS" />
      </aside>

      <section class="card-luxury wb__editor">
        <Transition name="fade-slide" mode="out-in">
          <DesignStep v-if="step === 'design'" key="design" />
          <ThemeStep v-else-if="step === 'theme'" key="theme" />
          <BrandingStep v-else-if="step === 'branding'" key="branding" :locale="locale" />
          <SectionsStep v-else-if="step === 'sections'" key="sections" @edit="editSection" />
          <ContentStep
            v-else-if="step === 'content'"
            key="content"
            :selected-id="selectedSectionId"
            :locale="locale"
            @select="selectedSectionId = $event"
          />
          <PricesStep v-else-if="step === 'prices'" key="prices" :locale="locale" />
          <PublishStep v-else key="publish" :locale="locale" />
        </Transition>
      </section>

      <section class="wb__preview">
        <WebsiteCanvas
          :snapshot="snapshot"
          :locale="locale"
          :locales="store.locales"
          :account-slug="store.site?.slug || ''"
          :saving="store.saving"
          @update:locale="locale = $event"
        />
      </section>
    </div>
  </div>
</template>

<script setup>
import { computed, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { onBeforeRouteLeave } from 'vue-router'
import AlertMessage from '@/components/ui/AlertMessage.vue'
import LoadingSpinner from '@/components/ui/LoadingSpinner.vue'
import WebsiteStepRail from './components/WebsiteStepRail.vue'
import WebsiteCanvas from './components/WebsiteCanvas.vue'
import DesignStep from './components/steps/DesignStep.vue'
import ThemeStep from './components/steps/ThemeStep.vue'
import BrandingStep from './components/steps/BrandingStep.vue'
import SectionsStep from './components/steps/SectionsStep.vue'
import ContentStep from './components/steps/ContentStep.vue'
import PricesStep from './components/steps/PricesStep.vue'
import PublishStep from './components/steps/PublishStep.vue'
import { websiteApi } from '@/services/api'
import { useWebsiteStore } from '@/stores/website'

/**
 * The website builder: seven steps on the left, the real site on the right.
 *
 * The preview is not a mock — it is the same `SiteRenderer` the published page
 * uses, fed by the draft. What the owner approves here is literally what ships.
 */
const STEPS = [
  { key: 'design', icon: 'fas fa-shapes' },
  { key: 'theme', icon: 'fas fa-palette' },
  { key: 'branding', icon: 'fas fa-copyright' },
  { key: 'sections', icon: 'fas fa-layer-group' },
  { key: 'content', icon: 'fas fa-pen-to-square' },
  { key: 'prices', icon: 'fas fa-coins' },
  { key: 'publish', icon: 'fas fa-rocket' },
]

const store = useWebsiteStore()
const step = ref('design')
const locale = ref('')
const selectedSectionId = ref(0)

/**
 * Theme, branding and chrome are resolved server-side, so they are fetched.
 * Section content is already in the store verbatim, so it is overlaid locally —
 * which is what makes typing show up in the preview with no round trip.
 */
const previewBase = ref(null)

const snapshot = computed(() => {
  if (!previewBase.value) return null
  return {
    ...previewBase.value,
    sections: store.sections
      .filter((section) => section.is_enabled && section.resolved_variant)
      .map((section) => ({
        id: section.id,
        type: section.section_type,
        key: section.key,
        variant: section.variant || section.resolved_variant,
        content: section.content || {},
      })),
  }
})

async function refreshPreviewBase() {
  const { data } = await websiteApi.preview()
  previewBase.value = data
}

onMounted(async () => {
  await store.load()
  await refreshPreviewBase()
  locale.value = store.primaryLocale
  selectedSectionId.value = store.sections[0]?.id || 0
})

/* Anything the server resolves — theme tokens, branding, the chrome a layout
   picks — needs a fresh base; content changes do not. */
watch(
  () => [
    store.site?.layout_slug,
    store.site?.theme_slug,
    JSON.stringify(store.site?.theme_overrides || {}),
    store.site?.logo_url,
    store.site?.favicon_url,
    JSON.stringify(store.site?.business_name || {}),
    JSON.stringify(store.site?.tagline || {}),
    store.site?.inherit_panel_branding,
    JSON.stringify(store.site?.locales || []),
  ].join('|'),
  () => {
    refreshPreviewBase().catch(() => {})
  },
)

function editSection(id) {
  selectedSectionId.value = id
  step.value = 'content'
}

async function publish() {
  await store.publish()
  step.value = 'publish'
}

/* A debounced edit that has not fired yet would be lost on navigation. */
onBeforeRouteLeave(() => store.flush())
onBeforeUnmount(() => store.flush())
</script>

<style scoped>
.wb {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.wb__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 18px;
  flex-wrap: wrap;
}

.wb__head h1 {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--text-primary);
  margin: 0;
}

.wb__head p {
  margin: 4px 0 0;
  color: var(--text-secondary);
  font-size: 0.88rem;
}

.wb__head-actions {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.wb__grid {
  display: grid;
  grid-template-columns: 232px minmax(320px, 380px) minmax(0, 1fr);
  gap: 16px;
  align-items: start;
  min-height: 0;
}

.wb__editor {
  max-height: calc(100vh - 210px);
  overflow-y: auto;
}

.wb__preview {
  height: calc(100vh - 210px);
  position: sticky;
  top: 18px;
}

@media (max-width: 1400px) {
  .wb__grid {
    grid-template-columns: 210px minmax(0, 1fr);
  }

  .wb__preview {
    grid-column: 1 / -1;
    position: static;
    height: 70vh;
  }
}

@media (max-width: 1100px) {
  .wb__grid {
    grid-template-columns: minmax(0, 1fr);
  }

  .wb__editor {
    max-height: none;
  }
}
</style>

<style>
/* Shared by every step panel; unscoped so the step components can use them
   without each one repeating the same twelve rules. */
.wb-panel {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.wb-panel > section {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.wb-panel__title {
  font-size: 0.8rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--text-secondary);
  margin: 0;
}

.wb-panel__note {
  display: flex;
  gap: 9px;
  margin: 0;
  padding: 10px 12px;
  border-radius: 10px;
  background: var(--bg-input);
  color: var(--text-secondary);
  font-size: 0.8rem;
  line-height: 1.5;
}

.wb-panel__note i {
  color: var(--primary);
  margin-top: 2px;
}
</style>
