<template>
  <div class="wb-list">
    <div class="wb-list__head">
      <span>{{ label }}</span>
      <span class="wb-list__count">{{ rows.length }}/{{ field.max || 12 }}</span>
    </div>

    <VueDraggable v-model="rows" handle=".wb-list__grip" :animation="160" @end="commit">
      <details v-for="(row, index) in rows" :key="index" class="wb-list__row">
        <summary>
          <span class="wb-list__grip" title="Drag"><i class="fas fa-grip-vertical" /></span>
          <span class="wb-list__title">{{ rowTitle(row, index) }}</span>
          <button type="button" class="wb-list__remove" @click.prevent.stop="remove(index)">
            <i class="fas fa-trash" />
          </button>
        </summary>
        <div class="wb-list__body">
          <template v-for="sub in field.fields" :key="sub.key">
            <ListField
              v-if="sub.type === 'list'"
              :field="sub"
              :model-value="row[sub.key] || []"
              :locale="locale"
              :label-prefix="labelPrefix"
              @update:model-value="(value) => setCell(index, sub.key, value)"
            />
            <FieldControl
              v-else
              :field="sub"
              :model-value="row[sub.key]"
              :locale="locale"
              :show-locale-tag="showLocaleTag"
              :label-prefix="labelPrefix"
              @update:model-value="(value) => setCell(index, sub.key, value)"
            />
          </template>
        </div>
      </details>
    </VueDraggable>

    <button type="button" class="btn-luxury-outline wb-list__add" :disabled="atLimit" @click="add">
      <i class="fas fa-plus" /> {{ $t('website.builder.addItem') }}
    </button>
  </div>
</template>

<script setup>
import { computed, ref, watch } from 'vue'
import { useI18n } from 'vue-i18n'
import { VueDraggable } from 'vue-draggable-plus'
import FieldControl from './FieldControl.vue'

/**
 * A repeating group — services, FAQ entries, footer columns.
 *
 * Recursive on purpose: a footer column holds its own list of links, and the
 * catalog can nest a list inside a list without this component learning about
 * that particular shape.
 */
const props = defineProps({
  field: { type: Object, required: true },
  modelValue: { type: Array, default: () => [] },
  locale: { type: String, default: 'en' },
  showLocaleTag: { type: Boolean, default: false },
  labelPrefix: { type: String, default: '' },
})
const emit = defineEmits(['update:modelValue'])

const { t, te } = useI18n()
const rows = ref([...props.modelValue])

watch(
  () => props.modelValue,
  (value) => {
    // Only adopt an outside change when it is genuinely different, or the
    // server echo of our own save would fight the row being typed into.
    if (JSON.stringify(value) !== JSON.stringify(rows.value)) rows.value = [...(value || [])]
  },
)

const label = computed(() => {
  const key = `website.fields.${props.field.key}`
  return te(key) ? t(key) : props.field.key
})
const atLimit = computed(() => rows.value.length >= (props.field.max || 12))

function commit() {
  emit('update:modelValue', rows.value.map((row) => ({ ...row })))
}

function add() {
  if (atLimit.value) return
  rows.value.push({})
  commit()
}

function remove(index) {
  rows.value.splice(index, 1)
  commit()
}

function setCell(index, key, value) {
  rows.value[index] = { ...rows.value[index], [key]: value }
  commit()
}

/** A recognisable summary line so a collapsed row is still identifiable. */
function rowTitle(row, index) {
  for (const key of ['title', 'label', 'question', 'author', 'value', 'caption', 'text']) {
    const value = row[key]
    if (typeof value === 'string' && value) return value
    if (value && typeof value === 'object') {
      const found = value[props.locale] || Object.values(value).find(Boolean)
      if (found) return found
    }
  }
  return `${t('website.builder.item')} ${index + 1}`
}
</script>

<style scoped>
.wb-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.wb-list__head {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.82rem;
  color: var(--text-secondary);
}

.wb-list__count {
  font-variant-numeric: tabular-nums;
  opacity: 0.75;
}

.wb-list__row {
  border: 1px solid var(--border-card);
  border-radius: 10px;
  background: var(--bg-input);
  margin-bottom: 6px;
}

.wb-list__row summary {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 9px 11px;
  cursor: pointer;
  list-style: none;
}

.wb-list__row summary::-webkit-details-marker {
  display: none;
}

.wb-list__grip {
  cursor: grab;
  color: var(--text-secondary);
  opacity: 0.65;
}

.wb-list__title {
  flex: 1;
  min-width: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  font-size: 0.88rem;
  color: var(--text-primary);
}

.wb-list__remove {
  border: 0;
  background: transparent;
  color: var(--color-sell, #f43f5e);
  cursor: pointer;
  padding: 4px 6px;
}

.wb-list__body {
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding: 4px 12px 14px;
}

.wb-list__add {
  align-self: flex-start;
  font-size: 0.85rem;
  padding: 7px 14px;
}
</style>
