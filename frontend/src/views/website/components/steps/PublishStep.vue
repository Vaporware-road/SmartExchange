<template>
  <div class="wb-panel">
    <section class="wb-live">
      <div class="wb-live__state" :class="store.isPublished ? 'is-live' : 'is-draft'">
        <i :class="store.isPublished ? 'fas fa-circle-check' : 'fas fa-pen-ruler'" />
        <span>{{ store.isPublished ? $t('website.builder.live') : $t('website.builder.draft') }}</span>
      </div>

      <div v-if="store.isPublished" class="wb-live__url">
        <a :href="store.publicUrl" target="_blank" rel="noopener" dir="ltr">{{ store.publicUrl }}</a>
        <button type="button" :title="$t('common.copy')" @click="copy">
          <i :class="copied ? 'fas fa-check' : 'fas fa-copy'" />
        </button>
      </div>

      <p v-if="store.hasUnpublishedChanges" class="wb-live__pending">
        <i class="fas fa-triangle-exclamation" /> {{ $t('website.builder.pendingChanges') }}
      </p>

      <div class="wb-live__actions">
        <button type="button" class="btn-luxury" :disabled="store.saving" @click="publish">
          <i class="fas fa-rocket" />
          {{ store.isPublished ? $t('website.builder.republish') : $t('website.builder.publish') }}
        </button>
        <button
          v-if="store.isPublished"
          type="button"
          class="btn-luxury-outline"
          @click="store.unpublish()"
        >
          {{ $t('website.builder.unpublish') }}
        </button>
      </div>
    </section>

    <section>
      <h3 class="wb-panel__title">{{ $t('website.builder.seo') }}</h3>
      <label class="wb-field">
        <span class="wb-field__label">
          {{ $t('website.fields.seo_title') }}
          <em v-if="multiLocale">{{ locale.toUpperCase() }}</em>
        </span>
        <input class="input-luxury" type="text" :value="seo.title?.[locale] || ''" @input="setSeoText('title', $event.target.value)" />
      </label>
      <label class="wb-field">
        <span class="wb-field__label">
          {{ $t('website.fields.seo_description') }}
          <em v-if="multiLocale">{{ locale.toUpperCase() }}</em>
        </span>
        <textarea class="input-luxury" rows="3" :value="seo.description?.[locale] || ''" @input="setSeoText('description', $event.target.value)" />
      </label>
      <label class="wb-field">
        <span class="wb-field__label">{{ $t('website.fields.keywords') }}</span>
        <input class="input-luxury" type="text" :value="seo.keywords || ''" @input="setSeo('keywords', $event.target.value)" />
      </label>
      <div class="wb-field">
        <span class="wb-field__label">{{ $t('website.fields.og_image') }}</span>
        <AssetField :model-value="seo.og_image || ''" @update:model-value="(value) => setSeo('og_image', value)" />
      </div>
    </section>

    <section v-if="store.publications.length">
      <h3 class="wb-panel__title">{{ $t('website.builder.history') }}</h3>
      <ul class="wb-history">
        <li v-for="item in store.publications" :key="item.version">
          <span class="wb-history__v ws-num">v{{ item.version }}</span>
          <span class="wb-history__meta">
            <span>{{ formatDate(item.published_at) }}</span>
            <small>{{ item.published_by_name || '—' }}{{ item.note ? ` · ${item.note}` : '' }}</small>
          </span>
          <button
            v-if="item.version !== store.site?.published_version"
            type="button"
            class="btn-luxury-outline wb-history__restore"
            @click="store.restore(item.version)"
          >
            {{ $t('website.builder.restore') }}
          </button>
        </li>
      </ul>
    </section>
  </div>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue'
import AssetField from '../AssetField.vue'
import { useWebsiteStore } from '@/stores/website'

const props = defineProps({ locale: { type: String, default: 'en' } })

const store = useWebsiteStore()
const copied = ref(false)
const seo = computed(() => store.site?.seo || {})
const multiLocale = computed(() => store.locales.length > 1)

onMounted(() => {
  if (!store.publications.length) store.loadPublications().catch(() => {})
})

function setSeo(key, value) {
  store.patchSite({ seo: { ...seo.value, [key]: value } })
}

function setSeoText(key, value) {
  setSeo(key, { ...(seo.value[key] || {}), [props.locale]: value })
}

async function publish() {
  await store.publish()
}

async function copy() {
  await navigator.clipboard?.writeText(new URL(store.publicUrl, window.location.origin).href)
  copied.value = true
  setTimeout(() => {
    copied.value = false
  }, 1600)
}

function formatDate(iso) {
  if (!iso) return ''
  return new Date(iso).toLocaleString()
}
</script>

<style scoped>
.wb-live {
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding: 16px;
  border: 1px solid var(--border-card);
  border-radius: 13px;
  background: var(--bg-card);
}

.wb-live__state {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-weight: 600;
  font-size: 0.92rem;
}

.wb-live__state.is-live {
  color: var(--color-buy, #10b981);
}

.wb-live__state.is-draft {
  color: var(--text-secondary);
}

.wb-live__url {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 11px;
  border-radius: 9px;
  background: var(--bg-input);
  font-size: 0.85rem;
}

.wb-live__url a {
  flex: 1;
  min-width: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  color: var(--primary);
}

.wb-live__url button {
  border: 0;
  background: transparent;
  color: var(--text-secondary);
  cursor: pointer;
}

.wb-live__pending {
  margin: 0;
  font-size: 0.82rem;
  color: var(--color-warning, #f59e0b);
}

.wb-live__actions {
  display: flex;
  gap: 9px;
  flex-wrap: wrap;
}

.wb-history {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.wb-history li {
  display: flex;
  align-items: center;
  gap: 11px;
  padding: 9px 11px;
  border: 1px solid var(--border-card);
  border-radius: 10px;
}

.wb-history__v {
  font-weight: 700;
  color: var(--primary);
  font-size: 0.85rem;
}

.wb-history__meta {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
}

.wb-history__meta span {
  font-size: 0.84rem;
}

.wb-history__meta small {
  font-size: 0.74rem;
  color: var(--text-secondary);
}

.wb-history__restore {
  font-size: 0.78rem;
  padding: 5px 11px;
}
</style>
