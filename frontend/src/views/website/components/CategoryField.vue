<template>
  <div class="wb-cats">
    <p class="wb-cats__hint">
      {{ selected.size ? $t('website.builder.someSelected', { n: selected.size }) : $t('website.builder.allSelected') }}
    </p>

    <div v-if="options.length" class="wb-cats__list">
      <label v-for="option in options" :key="option.id">
        <input
          type="checkbox"
          :checked="selected.has(option.id)"
          @change="toggle(option.id)"
        />
        <span>{{ option.label }}</span>
      </label>
    </div>
    <p v-else-if="!loading" class="wb-cats__hint">{{ $t('website.builder.noCategories') }}</p>
  </div>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue'
import { categoryApi } from '@/services/api'

/**
 * Which categories (or price types) the board shows.
 *
 * An empty selection means "everything", which is the right default: a desk
 * that adds a new category next month wants it on the site without having to
 * remember to tick a box here.
 */
const props = defineProps({
  modelValue: { type: Array, default: () => [] },
  mode: { type: String, default: 'category' },
})
const emit = defineEmits(['update:modelValue'])

const categories = ref([])
const loading = ref(true)
const selected = computed(() => new Set((props.modelValue || []).map(Number)))

const options = computed(() => {
  if (props.mode === 'category') {
    return categories.value.map((category) => ({ id: category.id, label: category.name }))
  }
  return categories.value.flatMap((category) =>
    (category.price_types || []).map((type) => ({
      id: type.id,
      label: `${category.name} · ${type.name}`,
    })),
  )
})

function toggle(id) {
  const next = new Set(selected.value)
  if (next.has(id)) next.delete(id)
  else next.add(id)
  emit('update:modelValue', [...next])
}

onMounted(async () => {
  try {
    const { data } = await categoryApi.list()
    categories.value = Array.isArray(data) ? data : data?.results || []
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
.wb-cats {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.wb-cats__hint {
  margin: 0;
  font-size: 0.78rem;
  color: var(--text-secondary);
}

.wb-cats__list {
  display: flex;
  flex-direction: column;
  gap: 6px;
  max-height: 190px;
  overflow-y: auto;
  padding: 10px;
  border: 1px solid var(--border-card);
  border-radius: 10px;
  background: var(--bg-input);
}

.wb-cats__list label {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 0.88rem;
  cursor: pointer;
}
</style>
