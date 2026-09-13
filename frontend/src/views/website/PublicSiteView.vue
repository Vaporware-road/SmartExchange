<template>
  <LoadingSpinner v-if="loading" />

  <div v-else-if="error" class="ws-missing">
    <h1>{{ $t('website.public.missingTitle') }}</h1>
    <p>{{ $t('website.public.missingBody') }}</p>
  </div>

  <SiteRenderer v-else :snapshot="snapshot" :account-slug="slug" />
</template>

<script setup>
import { computed, onMounted, ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import LoadingSpinner from '@/components/ui/LoadingSpinner.vue'
import SiteRenderer from '@/website/SiteRenderer.vue'

/**
 * A desk's published website at `/site/` or `/site/<slug>/`.
 *
 * Fetched with a bare `fetch` rather than the panel's axios client on purpose:
 * this page is for the desk's customers, and the shared client attaches the
 * staff bearer token and redirects on 401, neither of which belongs on a public
 * marketing page.
 */
const route = useRoute()
const snapshot = ref(null)
const loading = ref(true)
const error = ref(false)
const slug = computed(() => String(route.params.slug || ''))

async function load() {
  loading.value = true
  error.value = false
  try {
    const query = slug.value ? `?account=${encodeURIComponent(slug.value)}` : ''
    const response = await fetch(`/api/public/website/${query}`, {
      headers: { Accept: 'application/json' },
    })
    if (!response.ok) throw new Error(`HTTP ${response.status}`)
    snapshot.value = await response.json()
    applyDocumentChrome(snapshot.value)
  } catch {
    error.value = true
  } finally {
    loading.value = false
  }
}

/**
 * Django already put the real metadata in `<head>` for crawlers; this is for
 * the browser tab after a client-side navigation, where that never ran.
 */
function applyDocumentChrome(site) {
  const locale = site?.primary_locale || 'en'
  const name = site?.branding?.business_name
  const title = site?.seo?.title?.[locale] || name?.[locale] || Object.values(name || {})[0]
  if (title) document.title = title
  const favicon = site?.branding?.favicon
  if (favicon) {
    const link = document.querySelector("link[rel='icon']") || document.createElement('link')
    link.rel = 'icon'
    link.href = favicon
    document.head.appendChild(link)
  }
}

onMounted(load)
watch(slug, load)
</script>

<style scoped>
.ws-missing {
  min-height: 70vh;
  display: grid;
  place-content: center;
  gap: 10px;
  text-align: center;
  padding: 40px;
  color: var(--text-secondary);
}

.ws-missing h1 {
  font-size: 1.6rem;
  color: var(--text-primary);
}
</style>
