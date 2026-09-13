<template>
  <div class="wb-panel">
    <label class="wb-field">
      <span class="wb-field__label">{{ $t('website.builder.editingSection') }}</span>
      <select class="input-luxury" :value="selectedId" @change="$emit('select', Number($event.target.value))">
        <option v-for="section in editable" :key="section.id" :value="section.id">
          {{ $t(`website.sections.${section.section_type}`) }}
        </option>
      </select>
    </label>

    <template v-if="section">
      <template v-for="field in fields" :key="field.key">
        <ListField
          v-if="field.type === 'list'"
          :field="field"
          :model-value="content[field.key] || []"
          :locale="locale"
          :show-locale-tag="multiLocale"
          :label-prefix="labelPrefix"
          @update:model-value="(value) => set(field.key, value)"
        />
        <FieldControl
          v-else
          :field="field"
          :model-value="content[field.key]"
          :locale="locale"
          :show-locale-tag="multiLocale"
          :label-prefix="labelPrefix"
          @update:model-value="(value) => set(field.key, value)"
        />
      </template>
    </template>

    <EmptyState v-else title-key="website.builder.noSectionSelected" icon="fas fa-pen-to-square" />
  </div>
</template>

<script setup>
import { computed } from 'vue'
import sectionCatalog from '@catalog/sections.json'
import EmptyState from '@/components/ui/EmptyState.vue'
import FieldControl from '../FieldControl.vue'
import ListField from '../ListField.vue'
import { useWebsiteStore } from '@/stores/website'

/**
 * The content form, generated from the section's field list.
 *
 * Price-widget settings live on the `rates` section too, but they get their own
 * step, so they are filtered out here — an owner editing their headline should
 * not have to scroll past a decimal-places box.
 */
const props = defineProps({
  selectedId: { type: Number, default: 0 },
  locale: { type: String, default: 'en' },
})
defineEmits(['select'])

const WIDGET_FIELDS = new Set([
  'source', 'category_ids', 'price_type_ids', 'show_buy_sell', 'show_currency_icons',
  'show_updated_at', 'decimals', 'columns', 'refresh_seconds',
])

const store = useWebsiteStore()

const editable = computed(() => store.sections.filter((section) => sectionCatalog[section.section_type]))
const section = computed(() => editable.value.find((item) => item.id === props.selectedId) || null)
const content = computed(() => section.value?.content || {})
const multiLocale = computed(() => store.locales.length > 1)
const labelPrefix = computed(() =>
  section.value ? `website.sectionFields.${section.value.section_type}` : '',
)

const fields = computed(() => {
  if (!section.value) return []
  const spec = sectionCatalog[section.value.section_type]
  return spec.fields.filter((field) => !WIDGET_FIELDS.has(field.key))
})

function set(key, value) {
  store.patchSection(section.value.id, { content: { ...content.value, [key]: value } })
}
</script>
