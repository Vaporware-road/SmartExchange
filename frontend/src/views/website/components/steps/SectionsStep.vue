<template>
  <div class="wb-panel">
    <p class="wb-panel__note">
      <i class="fas fa-circle-info" /> {{ $t('website.builder.sectionsNote') }}
    </p>

    <VueDraggable
      :model-value="store.sections"
      handle=".wb-sec__grip"
      :animation="160"
      @update:model-value="onReorder"
    >
      <article
        v-for="section in store.sections"
        :key="section.id"
        class="wb-sec"
        :class="{ 'is-off': !section.is_enabled, 'is-unsupported': !supported(section) }"
      >
        <span class="wb-sec__grip"><i class="fas fa-grip-vertical" /></span>

        <span class="wb-sec__body">
          <strong>{{ $t(`website.sections.${section.section_type}`) }}</strong>
          <span v-if="!supported(section)" class="wb-sec__warn">
            {{ $t('website.builder.notInLayout') }}
          </span>
          <select
            v-else
            class="wb-sec__variant"
            :value="section.variant || ''"
            @change="setVariant(section, $event.target.value)"
          >
            <option value="">
              {{ $t('website.builder.layoutDefault', { name: $t(`website.variants.${section.resolved_variant}`) }) }}
            </option>
            <option v-for="variant in variantsFor(section)" :key="variant" :value="variant">
              {{ $t(`website.variants.${variant}`) }}
            </option>
          </select>
        </span>

        <BaseSwitch
          :model-value="section.is_enabled"
          :disabled="!supported(section)"
          @update:model-value="(value) => store.patchSection(section.id, { is_enabled: value }, { immediate: true })"
        />

        <button type="button" class="wb-sec__edit" :title="$t('website.builder.step.content')" @click="$emit('edit', section.id)">
          <i class="fas fa-pen" />
        </button>

        <button
          v-if="!isSingleton(section)"
          type="button"
          class="wb-sec__remove"
          :title="$t('common.delete')"
          @click="remove(section)"
        >
          <i class="fas fa-trash" />
        </button>
      </article>
    </VueDraggable>

    <div v-if="addable.length" class="wb-add">
      <h3 class="wb-panel__title">{{ $t('website.builder.addSection') }}</h3>
      <div class="wb-chips">
        <button
          v-for="type in addable"
          :key="type"
          type="button"
          class="wb-chip"
          @click="store.addSection(type)"
        >
          <i class="fas fa-plus" /> {{ $t(`website.sections.${type}`) }}
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { VueDraggable } from 'vue-draggable-plus'
import layouts from '@catalog/layouts.json'
import sectionCatalog from '@catalog/sections.json'
import BaseSwitch from '@/components/ui/BaseSwitch.vue'
import { useWebsiteStore } from '@/stores/website'

defineEmits(['edit'])

const store = useWebsiteStore()

const manifest = computed(() => layouts[store.layoutSlug] || {})
const present = computed(() => new Set(store.sections.map((section) => section.section_type)))

/**
 * A section the current layout cannot draw is disabled, not deleted, so
 * switching back to a design that supports it brings the content home.
 */
function supported(section) {
  return (manifest.value.supports || []).includes(section.section_type)
}

function variantsFor(section) {
  return sectionCatalog[section.section_type]?.variants || []
}

function isSingleton(section) {
  return Boolean(sectionCatalog[section.section_type]?.singleton)
}

const addable = computed(() =>
  (manifest.value.supports || []).filter((type) => !present.value.has(type)),
)

function setVariant(section, variant) {
  store.patchSection(section.id, { variant }, { immediate: true })
}

function onReorder(next) {
  store.reorder(next.map((section) => section.id))
}

async function remove(section) {
  await store.removeSection(section.id)
}
</script>

<style scoped>
.wb-sec {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 12px;
  margin-bottom: 7px;
  border: 1px solid var(--border-card);
  border-radius: 11px;
  background: var(--bg-card);
}

.wb-sec.is-off {
  opacity: 0.55;
}

.wb-sec.is-unsupported {
  border-style: dashed;
}

.wb-sec__grip {
  cursor: grab;
  color: var(--text-secondary);
  opacity: 0.6;
}

.wb-sec__body {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
  gap: 3px;
}

.wb-sec__body strong {
  font-size: 0.9rem;
  color: var(--text-primary);
}

.wb-sec__variant {
  background: transparent;
  border: 0;
  color: var(--text-secondary);
  font: inherit;
  font-size: 0.76rem;
  padding: 0;
  cursor: pointer;
  max-width: 100%;
}

.wb-sec__warn {
  font-size: 0.74rem;
  color: var(--color-warning, #f59e0b);
}

.wb-sec__edit,
.wb-sec__remove {
  border: 1px solid var(--border-card);
  background: transparent;
  color: var(--text-secondary);
  border-radius: 8px;
  width: 30px;
  height: 30px;
  cursor: pointer;
  flex: none;
}

.wb-sec__remove {
  color: var(--color-sell, #f43f5e);
}

.wb-add {
  margin-top: 14px;
}
</style>
