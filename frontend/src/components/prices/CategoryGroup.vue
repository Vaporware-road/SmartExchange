<template>
  <section class="rounded-xl border border-[var(--border-color)] bg-[var(--bg-card)]/60 p-3 sm:p-4">
    <header class="mb-3 flex items-center justify-between gap-3">
      <div class="min-w-0 flex items-center gap-2">
        <span class="inline-flex h-7 w-7 items-center justify-center rounded-lg bg-primary-muted text-gold">
          <CategoryIcon :category-name="category.name" size-class="h-4 w-4" />
        </span>
        <div class="min-w-0">
          <h3 class="truncate text-sm font-semibold text-[var(--text-primary)]">
            {{ category.name }}
          </h3>
          <p class="text-xs text-[var(--text-secondary)]">
            {{ priceTypes.length }} {{ $t('analysis.priceType') }}
          </p>
        </div>
      </div>
      <router-link
        :to="`/prices/category/${category.id}/update`"
        class="rounded-lg border border-gold/60 bg-gold/15 px-3.5 py-2 text-sm font-semibold text-gold shadow-sm transition hover:bg-gold/25 hover:shadow"
      >
        {{ $t('common.update') }}
      </router-link>
    </header>

    <div v-if="priceTypes.length" class="space-y-2">
      <PriceTypeRow
        v-for="pt in priceTypes"
        :key="pt.id"
        :category-id="category.id"
        :price-type="pt"
        :is-editing="editingPriceTypeId === pt.id"
        :saving="savingPriceTypeId === pt.id"
        @edit="$emit('edit-start', { categoryId: category.id, priceTypeId: pt.id })"
        @cancel="$emit('edit-cancel')"
        @save="(value) => $emit('edit-save', { categoryId: category.id, priceTypeId: pt.id, value })"
      />
    </div>

    <p v-else class="py-4 text-center text-sm text-[var(--text-secondary)]">
      {{ $t('emptyState.noPrices') }}
    </p>
  </section>
</template>

<script setup>
import { computed } from 'vue'
import PriceTypeRow from '@/components/prices/PriceTypeRow.vue'
import CategoryIcon from '@/components/ui/CategoryIcon.vue'

const props = defineProps({
  category: {
    type: Object,
    required: true,
  },
  editingPriceTypeId: {
    type: [Number, String],
    default: null,
  },
  savingPriceTypeId: {
    type: [Number, String],
    default: null,
  },
})

defineEmits(['edit-start', 'edit-cancel', 'edit-save'])

const priceTypes = computed(() => {
  const items = Array.isArray(props.category?.price_types) ? props.category.price_types : []
  return [...items].sort((a, b) => {
    const orderA = Number.isFinite(Number(a?.order)) ? Number(a.order) : 0
    const orderB = Number.isFinite(Number(b?.order)) ? Number(b.order) : 0
    if (orderA !== orderB) return orderA - orderB
    return (a?.name || '').localeCompare(b?.name || '')
  })
})
</script>
