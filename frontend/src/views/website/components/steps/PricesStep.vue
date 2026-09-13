<template>
  <div class="wb-panel">
    <p class="wb-panel__note">
      <i class="fas fa-bolt" /> {{ $t('website.builder.pricesNote') }}
    </p>

    <template v-if="section">
      <label class="wb-field">
        <span class="wb-field__label">{{ $t('website.builder.boardStyle') }}</span>
        <select
          class="input-luxury"
          :value="section.variant || ''"
          @change="store.patchSection(section.id, { variant: $event.target.value }, { immediate: true })"
        >
          <option value="">
            {{ $t('website.builder.layoutDefault', { name: $t(`website.variants.${section.resolved_variant}`) }) }}
          </option>
          <option v-for="variant in variants" :key="variant" :value="variant">
            {{ $t(`website.variants.${variant}`) }}
          </option>
        </select>
      </label>

      <template v-for="field in fields" :key="field.key">
        <FieldControl
          :field="field"
          :model-value="content[field.key]"
          :locale="locale"
          label-prefix="website.sectionFields.rates"
          @update:model-value="(value) => set(field.key, value)"
        />
      </template>
    </template>

    <div v-else class="wb-panel__missing">
      <EmptyState title-key="website.builder.noRatesSection" icon="fas fa-coins" />
      <button type="button" class="btn-luxury" @click="store.addSection('rates')">
        <i class="fas fa-plus" /> {{ $t('website.builder.addRates') }}
      </button>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import sectionCatalog from '@catalog/sections.json'
import EmptyState from '@/components/ui/EmptyState.vue'
import FieldControl from '../FieldControl.vue'
import { useWebsiteStore } from '@/stores/website'

/** Everything about the rate board: which prices, how many columns, how often. */
defineProps({ locale: { type: String, default: 'en' } })

const WIDGET_FIELDS = [
  'source', 'category_ids', 'price_type_ids', 'show_buy_sell', 'show_currency_icons',
  'show_updated_at', 'decimals', 'columns', 'refresh_seconds', 'note',
]

const store = useWebsiteStore()
const section = computed(() => store.sections.find((item) => item.section_type === 'rates') || null)
const content = computed(() => section.value?.content || {})
const variants = computed(() => sectionCatalog.rates.variants)
const fields = computed(() =>
  sectionCatalog.rates.fields.filter((field) => WIDGET_FIELDS.includes(field.key)),
)

function set(key, value) {
  store.patchSection(section.value.id, { content: { ...content.value, [key]: value } })
}
</script>

<style scoped>
.wb-panel__missing {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 14px;
}
</style>
