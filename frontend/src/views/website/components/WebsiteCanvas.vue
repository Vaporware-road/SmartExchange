<template>
  <div class="wb-canvas">
    <div class="wb-canvas__bar">
      <div class="wb-canvas__devices">
        <button
          v-for="device in devices"
          :key="device.key"
          type="button"
          :class="{ 'is-active': device.key === width }"
          :title="$t(`website.builder.device.${device.key}`)"
          @click="width = device.key"
        >
          <i :class="device.icon" />
        </button>
      </div>

      <div v-if="locales.length > 1" class="wb-canvas__locales">
        <button
          v-for="code in locales"
          :key="code"
          type="button"
          :class="{ 'is-active': code === locale }"
          @click="$emit('update:locale', code)"
        >
          {{ code.toUpperCase() }}
        </button>
      </div>

      <span class="wb-canvas__status">
        <i v-if="saving" class="fas fa-circle-notch fa-spin" />
        {{ saving ? $t('website.builder.saving') : $t('website.builder.saved') }}
      </span>
    </div>

    <div ref="stage" class="wb-canvas__stage">
      <div class="wb-canvas__sizer" :style="sizerStyle">
        <div class="wb-canvas__frame" :style="frameStyle">
        <SiteRenderer
          v-if="snapshot"
          :key="renderKey"
          :snapshot="snapshot"
          :locale="locale"
          :account-slug="accountSlug"
          is-editing
        />
          <LoadingSpinner v-else />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, onBeforeUnmount, onMounted, ref } from 'vue'
import LoadingSpinner from '@/components/ui/LoadingSpinner.vue'
import SiteRenderer from '@/website/SiteRenderer.vue'

const props = defineProps({
  snapshot: { type: Object, default: null },
  locale: { type: String, default: '' },
  locales: { type: Array, default: () => [] },
  accountSlug: { type: String, default: '' },
  saving: { type: Boolean, default: false },
})
defineEmits(['update:locale'])

const devices = [
  { key: 'desktop', icon: 'fas fa-desktop', width: 1280 },
  { key: 'tablet', icon: 'fas fa-tablet-screen-button', width: 834 },
  { key: 'mobile', icon: 'fas fa-mobile-screen', width: 414 },
]
const width = ref('desktop')
const stage = ref(null)
const stageWidth = ref(0)
let observer = null

/**
 * The frame always lays out at the real device width and is then scaled to fit
 * the panel. Letting it simply be narrow would be a lie: the site is built on
 * container queries, so a 450px-wide "desktop" preview would show the phone
 * layout and the owner would be approving a page nobody will see.
 */
const deviceWidth = computed(
  () => devices.find((device) => device.key === width.value)?.width || 1280,
)
const scale = computed(() => {
  if (!stageWidth.value) return 1
  return Math.min(1, stageWidth.value / deviceWidth.value)
})
const frameStyle = computed(() => ({
  width: `${deviceWidth.value}px`,
  transform: `scale(${scale.value})`,
}))
/* The scaled frame still occupies its unscaled box, so the wrapper is given the
   painted width to keep the stage from scrolling sideways. */
const sizerStyle = computed(() => ({
  width: `${deviceWidth.value * scale.value}px`,
}))

onMounted(() => {
  observer = new ResizeObserver(([entry]) => {
    stageWidth.value = entry.contentRect.width
  })
  if (stage.value) observer.observe(stage.value)
})

onBeforeUnmount(() => observer?.disconnect())

/* Re-mount the renderer when the design changes so chrome-level state — a
   sticky observer, an open drawer — does not survive into a different layout. */
const renderKey = computed(() => `${props.snapshot?.layout}:${props.snapshot?.theme?.slug}`)
</script>

<style scoped>
.wb-canvas {
  display: flex;
  flex-direction: column;
  min-height: 0;
  height: 100%;
  border: 1px solid var(--border-card);
  border-radius: 16px;
  overflow: hidden;
  background: var(--bg-input);
}

.wb-canvas__bar {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 10px 14px;
  background: var(--bg-card);
  border-bottom: 1px solid var(--border-card);
}

.wb-canvas__devices,
.wb-canvas__locales {
  display: inline-flex;
  border: 1px solid var(--border-card);
  border-radius: 9px;
  overflow: hidden;
}

.wb-canvas__devices button,
.wb-canvas__locales button {
  border: 0;
  background: transparent;
  color: var(--text-secondary);
  font: inherit;
  font-size: 0.8rem;
  padding: 6px 11px;
  cursor: pointer;
}

.wb-canvas__devices button.is-active,
.wb-canvas__locales button.is-active {
  background: var(--primary);
  color: var(--text-on-primary, #fff);
}

.wb-canvas__status {
  margin-inline-start: auto;
  font-size: 0.78rem;
  color: var(--text-secondary);
  display: inline-flex;
  align-items: center;
  gap: 7px;
}

.wb-canvas__stage {
  flex: 1;
  min-height: 0;
  overflow: auto;
  padding: 18px;
  display: flex;
  justify-content: center;
}

.wb-canvas__sizer {
  align-self: flex-start;
}

.wb-canvas__frame {
  background: var(--bg-card);
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 18px 48px -28px rgba(0, 0, 0, 0.6);
  transform-origin: top left;
  transition: width 0.2s ease;
}
</style>
