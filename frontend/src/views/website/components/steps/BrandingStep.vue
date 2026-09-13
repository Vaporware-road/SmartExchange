<template>
  <div class="wb-panel">
    <label class="wb-field wb-field--inline">
      <span class="wb-field__label">{{ $t('website.builder.inheritPanel') }}</span>
      <BaseSwitch
        :model-value="site.inherit_panel_branding !== false"
        @update:model-value="(value) => store.patchSite({ inherit_panel_branding: value }, { immediate: true })"
      />
    </label>
    <p class="wb-panel__note">
      <i class="fas fa-circle-info" /> {{ $t('website.builder.inheritPanelNote') }}
    </p>

    <label class="wb-field">
      <span class="wb-field__label">
        {{ $t('website.fields.business_name') }}
        <em v-if="store.locales.length > 1">{{ locale.toUpperCase() }}</em>
      </span>
      <input
        class="input-luxury"
        type="text"
        :value="site.business_name?.[locale] || ''"
        @input="patchLocalized('business_name', $event.target.value)"
      />
    </label>

    <label class="wb-field">
      <span class="wb-field__label">
        {{ $t('website.fields.tagline') }}
        <em v-if="store.locales.length > 1">{{ locale.toUpperCase() }}</em>
      </span>
      <input
        class="input-luxury"
        type="text"
        :value="site.tagline?.[locale] || ''"
        @input="patchLocalized('tagline', $event.target.value)"
      />
    </label>

    <div class="wb-brandfiles">
      <div class="wb-field">
        <span class="wb-field__label">{{ $t('website.fields.logo') }}</span>
        <UploadBox :url="site.logo_url" field="logo" @uploaded="store.load()" />
      </div>
      <div class="wb-field">
        <span class="wb-field__label">{{ $t('website.fields.favicon') }}</span>
        <UploadBox :url="site.favicon_url" field="favicon" @uploaded="store.load()" />
      </div>
    </div>

    <section>
      <h3 class="wb-panel__title">{{ $t('website.builder.languages') }}</h3>
      <p class="wb-panel__note">{{ $t('website.builder.languagesNote') }}</p>
      <div class="wb-chips">
        <button
          v-for="code in SUPPORTED"
          :key="code"
          type="button"
          class="wb-chip"
          :class="{ 'is-active': store.locales.includes(code), 'is-primary': code === store.primaryLocale }"
          @click="toggleLocale(code)"
        >
          {{ code.toUpperCase() }}
          <i v-if="code === store.primaryLocale" class="fas fa-star" />
        </button>
      </div>
      <label class="wb-field">
        <span class="wb-field__label">{{ $t('website.builder.primaryLanguage') }}</span>
        <select
          class="input-luxury"
          :value="store.primaryLocale"
          @change="store.patchSite({ primary_locale: $event.target.value }, { immediate: true })"
        >
          <option v-for="code in store.locales" :key="code" :value="code">{{ code.toUpperCase() }}</option>
        </select>
      </label>
    </section>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import BaseSwitch from '@/components/ui/BaseSwitch.vue'
import UploadBox from '../UploadBox.vue'
import { useWebsiteStore } from '@/stores/website'

const props = defineProps({ locale: { type: String, default: 'en' } })

const SUPPORTED = ['en', 'fa', 'ar', 'de', 'fr', 'es', 'tr']
const store = useWebsiteStore()
const site = computed(() => store.site || {})

function patchLocalized(field, value) {
  store.patchSite({ [field]: { ...(site.value[field] || {}), [props.locale]: value } })
}

function toggleLocale(code) {
  const current = new Set(store.locales)
  if (current.has(code)) {
    // The primary language is what every other one falls back to, so it cannot
    // be the one that is switched off.
    if (code === store.primaryLocale) return
    current.delete(code)
  } else {
    current.add(code)
  }
  store.patchSite({ locales: [...current] }, { immediate: true })
}
</script>

<style scoped>
.wb-brandfiles {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 14px;
}

.wb-chip.is-primary {
  font-weight: 700;
}

.wb-chip i {
  font-size: 0.66rem;
  margin-inline-start: 5px;
}
</style>
