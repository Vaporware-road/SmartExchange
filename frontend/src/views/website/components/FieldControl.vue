<template>
  <label class="wb-field" :class="{ 'wb-field--inline': field.type === 'bool' }">
    <span class="wb-field__label">
      {{ label }}
      <em v-if="field.localized && showLocaleTag">{{ locale.toUpperCase() }}</em>
    </span>

    <template v-if="field.type === 'bool'">
      <BaseSwitch :model-value="Boolean(modelValue)" @update:model-value="emitRaw" />
    </template>

    <textarea
      v-else-if="field.type === 'textarea'"
      class="input-luxury"
      rows="3"
      :value="text"
      @input="emitText($event.target.value)"
    />

    <select
      v-else-if="field.type === 'select'"
      class="input-luxury"
      :value="modelValue ?? field.default"
      @change="emitRaw($event.target.value)"
    >
      <option v-for="option in field.options" :key="option" :value="option">
        {{ $t(`website.options.${field.key}.${option}`) }}
      </option>
    </select>

    <input
      v-else-if="field.type === 'number'"
      class="input-luxury"
      type="number"
      :min="field.min"
      :max="field.max"
      :value="modelValue ?? field.default"
      @input="emitRaw(Number($event.target.value))"
    />

    <AssetField
      v-else-if="field.type === 'image'"
      :model-value="modelValue || ''"
      @update:model-value="emitRaw"
    />

    <IconField
      v-else-if="field.type === 'icon'"
      :model-value="modelValue || ''"
      @update:model-value="emitRaw"
    />

    <CategoryField
      v-else-if="field.type === 'category_picker' || field.type === 'price_type_picker'"
      :mode="field.type === 'category_picker' ? 'category' : 'price-type'"
      :model-value="modelValue || []"
      @update:model-value="emitRaw"
    />

    <input
      v-else
      class="input-luxury"
      type="text"
      :value="text"
      :dir="field.type === 'url' ? 'ltr' : null"
      @input="field.localized ? emitText($event.target.value) : emitRaw($event.target.value)"
    />
  </label>
</template>

<script setup>
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'
import BaseSwitch from '@/components/ui/BaseSwitch.vue'
import AssetField from './AssetField.vue'
import IconField from './IconField.vue'
import CategoryField from './CategoryField.vue'

/**
 * One editor control, chosen from the field's declared type in
 * `catalog/sections.json`. Adding a field to a section therefore means editing
 * that JSON, not writing another form.
 */
const props = defineProps({
  field: { type: Object, required: true },
  modelValue: { type: [String, Number, Boolean, Object, Array], default: '' },
  locale: { type: String, default: 'en' },
  showLocaleTag: { type: Boolean, default: false },
  labelPrefix: { type: String, default: '' },
})
const emit = defineEmits(['update:modelValue'])

const { t, te } = useI18n()

const label = computed(() => {
  const specific = `${props.labelPrefix}.${props.field.key}`
  if (te(specific)) return t(specific)
  const shared = `website.fields.${props.field.key}`
  return te(shared) ? t(shared) : props.field.key
})

/** Localized fields store a per-locale map; everything else stores a scalar. */
const text = computed(() => {
  if (!props.field.localized) return props.modelValue ?? ''
  const value = props.modelValue
  if (typeof value === 'string') return value
  return value?.[props.locale] ?? ''
})

function emitRaw(value) {
  emit('update:modelValue', value)
}

function emitText(value) {
  if (!props.field.localized) return emitRaw(value)
  const existing = typeof props.modelValue === 'object' && props.modelValue ? props.modelValue : {}
  emit('update:modelValue', { ...existing, [props.locale]: value })
}
</script>

<style scoped>
.wb-field {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.wb-field--inline {
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
}

.wb-field__label {
  font-size: 0.82rem;
  color: var(--text-secondary);
  display: inline-flex;
  align-items: center;
  gap: 7px;
}

.wb-field__label em {
  font-style: normal;
  font-size: 0.66rem;
  letter-spacing: 0.08em;
  padding: 1px 6px;
  border-radius: 5px;
  background: var(--bg-input);
  color: var(--primary);
}

textarea.input-luxury {
  resize: vertical;
  min-height: 84px;
}
</style>
