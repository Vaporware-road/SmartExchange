<template>
  <WebAppLayout>
    <div v-if="loading" class="flex flex-col items-center justify-center py-16 gap-4">
      <LoadingSpinner class="w-10 h-10" />
      <p class="text-sm text-[var(--text-secondary)]">{{ $t('common.loading') }}</p>
    </div>

    <div v-else-if="authError" class="card-luxury text-center py-10 px-4">
      <i class="fas fa-exclamation-circle text-4xl text-red-400 mb-4" />
      <p class="text-red-400">{{ authError }}</p>
    </div>

    <div v-else-if="submitted" class="card-luxury text-center py-10 px-4 space-y-4">
      <div
        class="mx-auto w-16 h-16 rounded-full flex items-center justify-center"
        style="background: color-mix(in srgb, var(--color-buy) 18%, transparent);"
      >
        <i class="fas fa-check text-3xl text-buy" />
      </div>
      <div>
        <h2 class="text-xl font-bold text-gold mb-2">{{ $t('webapp.orderSubmitted') }}</h2>
        <p class="text-[var(--text-secondary)] leading-relaxed">
          {{ isBotMode ? $t('webapp.orderContactMessageBot') : $t('webapp.orderContactMessage') }}
        </p>
      </div>
      <p class="text-xs text-[var(--text-secondary)] pt-2 border-t" style="border-color: var(--border-card);">
        {{ $t('webapp.orderPendingReview') }}
      </p>
    </div>

    <div v-else class="space-y-5 pb-6">
      <section class="text-center">
        <h1 class="text-2xl font-bold text-gold mb-1">{{ $t('webapp.orderTitle') }}</h1>
        <p v-if="customerName && isBotMode" class="text-sm text-[var(--text-secondary)]">
          {{ $t('webapp.welcome', { name: customerName }) }}
        </p>
        <p v-else class="text-sm text-[var(--text-secondary)]">
          {{ $t('webapp.publicIntro') }}
        </p>
      </section>

      <!-- Live rates board -->
      <section class="card-luxury overflow-hidden">
        <div class="flex items-center justify-between gap-2 mb-4">
          <div class="flex items-center gap-2">
            <i class="fas fa-chart-line text-gold" />
            <h2 class="font-semibold text-gold">{{ $t('webapp.liveRates') }}</h2>
          </div>
          <span v-if="ratesUpdatedAt" class="text-[10px] text-[var(--text-secondary)]">
            {{ $t('webapp.ratesUpdated') }} {{ ratesUpdatedAt }}
          </span>
        </div>

        <div v-if="!priceCatalog.length" class="text-sm text-center py-6 text-[var(--text-secondary)]">
          {{ $t('webapp.noRatesYet') }}
        </div>

        <div v-else class="space-y-3 max-h-72 overflow-y-auto pe-1">
          <div
            v-for="cat in ratesByCategory"
            :key="cat.id"
            class="rounded-xl border p-3"
            style="border-color: var(--border-card); background: var(--bg-input);"
          >
            <p class="font-medium text-sm mb-2 flex items-center gap-2">
              <i class="fas fa-coins text-gold text-xs" />
              {{ cat.name }}
            </p>
            <div class="space-y-1.5">
              <div
                v-for="pt in cat.price_types"
                :key="pt.id"
                class="flex items-center justify-between text-sm gap-2"
              >
                <span class="truncate opacity-90">{{ pt.name }}</span>
                <span class="font-bold text-gold shrink-0 tabular-nums">
                  {{ formatPrice(pt.latest_price) }}
                </span>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Selected rate highlight -->
      <div
        v-if="highlightedRate"
        class="rounded-xl border px-4 py-3 flex items-center justify-between gap-3"
        style="border-color: var(--border-card-hover); background: color-mix(in srgb, var(--primary) 8%, var(--bg-card));"
      >
        <div class="text-sm">
          <p class="text-[var(--text-secondary)] text-xs mb-0.5">{{ $t('webapp.selectedRate') }}</p>
          <p class="font-medium">{{ highlightedRate.label }}</p>
        </div>
        <p class="text-xl font-bold text-gold tabular-nums">{{ highlightedRate.price }}</p>
      </div>

      <!-- Order form -->
      <form class="card-luxury space-y-4" @submit.prevent="handleSubmit">
        <AlertMessage v-if="error" type="error" :show="true" @dismiss="error = ''">
          {{ error }}
        </AlertMessage>

        <p class="text-sm font-medium text-gold flex items-center gap-2">
          <i class="fas fa-edit" />
          {{ $t('webapp.formSection') }}
        </p>

        <template v-if="!isBotMode">
          <div>
            <label class="block text-sm font-medium text-[var(--text-secondary)] mb-2">
              <i class="fas fa-user me-1 opacity-70" />
              {{ $t('webapp.customerName') }}
            </label>
            <input
              v-model="form.customer_name"
              type="text"
              class="input-luxury w-full"
              :placeholder="$t('webapp.customerNamePlaceholder')"
              required
            />
          </div>
          <div>
            <label class="block text-sm font-medium text-[var(--text-secondary)] mb-2">
              <i class="fas fa-phone me-1 opacity-70" />
              {{ $t('webapp.customerPhone') }}
            </label>
            <input
              v-model="form.customer_phone"
              type="tel"
              dir="ltr"
              class="input-luxury w-full text-start"
              placeholder="0912..."
              required
            />
          </div>
        </template>

        <div>
          <label class="block text-sm font-medium text-[var(--text-secondary)] mb-2">
            {{ $t('webapp.selectPriceTypeLabel') }}
          </label>
          <p v-if="!priceCatalog.length" class="text-sm text-[var(--text-secondary)] py-4 text-center">
            {{ $t('webapp.noRatesYet') }}
          </p>
          <div v-else class="grid gap-2">
            <button
              v-for="pt in priceCatalog"
              :key="pt.id"
              type="button"
              class="w-full text-start rounded-xl border-2 px-4 py-3 transition-all"
              :class="String(form.price_type) === String(pt.id)
                ? (pt.trade_type === 'buy'
                  ? 'border-buy bg-buy/10'
                  : 'border-sell bg-sell/10')
                : 'border-[var(--border-card)] hover:border-[var(--border-card-hover)]'"
              style="background: var(--bg-input);"
              @click="selectPriceType(pt)"
            >
              <div class="flex items-center justify-between gap-3">
                <div class="min-w-0">
                  <p class="font-medium truncate">{{ pt.name }}</p>
                  <p v-if="showCategoryNames" class="text-xs text-[var(--text-secondary)] mt-0.5">
                    {{ pt.category_name }}
                  </p>
                </div>
                <p class="text-lg font-bold text-gold tabular-nums shrink-0">
                  {{ formatPrice(pt.latest_price) }}
                </p>
              </div>
            </button>
          </div>
        </div>

        <div>
          <label class="block text-sm font-medium text-[var(--text-secondary)] mb-2">
            {{ $t('webapp.amount') }}
          </label>
          <input
            v-model="form.amount"
            type="number"
            step="any"
            min="0"
            dir="ltr"
            class="input-luxury w-full text-start"
            :placeholder="$t('webapp.amountPlaceholder')"
            required
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-[var(--text-secondary)] mb-2">
            {{ $t('webapp.note') }}
          </label>
          <textarea
            v-model="form.customer_note"
            class="input-luxury w-full min-h-[88px]"
            rows="3"
            :placeholder="$t('webapp.notePlaceholder')"
          />
        </div>

        <button
          type="submit"
          class="btn-luxury w-full min-h-[52px] text-base"
          :disabled="submitting || !form.price_type"
        >
          <LoadingSpinner v-if="submitting" class="w-5 h-5" />
          <template v-else>
            <i class="fas fa-paper-plane me-2" />
            {{ $t('webapp.submitOrder') }}
          </template>
        </button>
      </form>
    </div>
  </WebAppLayout>
</template>

<script setup>
import { computed, onMounted, reactive, ref } from 'vue'
import { useRoute } from 'vue-router'
import { useI18n } from 'vue-i18n'
import WebAppLayout from '@/layouts/WebAppLayout.vue'
import LoadingSpinner from '@/components/ui/LoadingSpinner.vue'
import AlertMessage from '@/components/ui/AlertMessage.vue'
import { botGatewayApi, getApiErrorDetails } from '@/services/api'
import { setLocale } from '@/i18n'

const { t, locale } = useI18n()
const route = useRoute()

const loading = ref(true)
const submitting = ref(false)
const submitted = ref(false)
const error = ref('')
const authError = ref('')
const customerName = ref('')
const ratesData = ref({ categories: [], generated_at: null })
const priceCatalog = ref([])
const authToken = ref('')
const isBotMode = ref(false)

const form = reactive({
  customer_name: '',
  customer_phone: '',
  trade_type: 'buy',
  category: '',
  price_type: '',
  amount: '',
  customer_note: '',
})

const showCategoryNames = computed(() => {
  const ids = new Set(priceCatalog.value.map((pt) => pt.category_id))
  return ids.size > 1
})

const ratesByCategory = computed(() => {
  const map = new Map()
  for (const pt of priceCatalog.value) {
    if (!map.has(pt.category_id)) {
      map.set(pt.category_id, {
        id: pt.category_id,
        name: pt.category_name,
        price_types: [],
      })
    }
    map.get(pt.category_id).price_types.push(pt)
  }
  return [...map.values()]
})

const ratesUpdatedAt = computed(() => {
  const raw = ratesData.value.generated_at
  if (!raw) return ''
  try {
    return new Date(raw).toLocaleString(locale.value === 'fa' ? 'fa-IR' : undefined, {
      hour: '2-digit',
      minute: '2-digit',
    })
  } catch {
    return ''
  }
})

const highlightedRate = computed(() => {
  const pt = priceCatalog.value.find((p) => String(p.id) === String(form.price_type))
  if (!pt) return null
  return {
    label: pt.name,
    price: formatPrice(pt.latest_price),
  }
})

function formatPrice(value) {
  if (value == null || value === '') return '—'
  const num = Number(String(value).replace(/,/g, ''))
  if (Number.isNaN(num)) return String(value)
  return num.toLocaleString(locale.value === 'fa' ? 'fa-IR' : undefined)
}

function buildCatalogFromRates(rates) {
  const catalog = []
  for (const cat of rates?.categories || []) {
    for (const pt of cat.price_types || []) {
      if (pt.is_active === false || pt.latest_price == null || pt.latest_price === '') continue
      const target = pt.target_currency || {}
      const source = pt.source_currency || {}
      catalog.push({
        id: pt.id,
        name: pt.name,
        slug: pt.slug,
        trade_type: pt.trade_type,
        latest_price: pt.latest_price,
        category_id: cat.id,
        category_name: cat.name,
        currency_code: target.code || source.code || '',
      })
    }
  }
  return catalog
}

function selectPriceType(pt) {
  if (!pt) return
  form.price_type = pt.id
  form.category = pt.category_id
  form.trade_type = pt.trade_type
}

function applyIntakeData(data) {
  ratesData.value = data.rates || { categories: [] }
  priceCatalog.value = data.price_catalog?.length
    ? data.price_catalog
    : buildCatalogFromRates(ratesData.value)
  if (priceCatalog.value.length) {
    selectPriceType(priceCatalog.value[0])
  }
}

onMounted(async () => {
  authToken.value = (route.query.auth_token || '').toString()
  isBotMode.value = Boolean(authToken.value)

  setLocale('fa')

  try {
    if (isBotMode.value) {
      const { data } = await botGatewayApi.verifyAuth(authToken.value)
      customerName.value = data.display_name || data.username || ''
      applyIntakeData(data)
    } else {
      const { data } = await botGatewayApi.publicIntake()
      applyIntakeData(data)
    }
  } catch (e) {
    authError.value = getApiErrorDetails(e).message || t('webapp.authFailed')
  } finally {
    loading.value = false
  }
})

function buildPayload() {
  const payload = {
    trade_type: form.trade_type,
    category: Number(form.category),
    amount: form.amount,
    customer_note: form.customer_note,
  }
  payload.price_type = Number(form.price_type)
  const selected = priceCatalog.value.find((p) => String(p.id) === String(form.price_type))
  if (selected?.currency_code) {
    payload.currency_code = selected.currency_code
  }
  if (!isBotMode.value) {
    payload.customer_name = form.customer_name.trim()
    payload.customer_phone = form.customer_phone.trim()
  }
  return payload
}

async function handleSubmit() {
  error.value = ''
  submitting.value = true
  try {
    if (isBotMode.value) {
      await botGatewayApi.submitOrder(authToken.value, buildPayload())
    } else {
      await botGatewayApi.submitPublicOrder(buildPayload())
    }
    submitted.value = true
    window.Telegram?.WebApp?.HapticFeedback?.notificationOccurred('success')
  } catch (e) {
    error.value = getApiErrorDetails(e).message || t('webapp.submitFailed')
  } finally {
    submitting.value = false
  }
}
</script>
