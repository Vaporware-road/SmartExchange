<template>
  <div class="finalize-dashboard mx-auto flex w-full max-w-4xl flex-col items-center px-1 pb-6">
    <h1 class="mb-6 w-full text-center text-2xl font-bold text-gold">{{ $t('finalize.title') }}</h1>

    <div v-if="loading" class="card-luxury w-full max-w-xl space-y-4 p-6">
      <BaseSkeleton variant="text" class="!h-4 !max-w-full" />
      <BaseSkeleton variant="text" class="!h-12 !max-w-full" />
      <BaseSkeleton variant="text" class="!h-12 !max-w-full" />
    </div>

    <template v-else>
      <div
        v-if="!data?.has_telegram_channel"
        class="card-luxury w-full max-w-xl space-y-4 p-6 text-center"
      >
        <i class="fab fa-telegram-plane text-4xl text-gold" />
        <p class="text-lg font-semibold text-[var(--text-primary)]">
          {{ $t('finalize.wizard.noChannelTitle') }}
        </p>
        <p class="text-sm text-[var(--text-secondary)]">
          {{ $t('finalize.wizard.noChannelHint') }}
        </p>
        <router-link
          to="/telegram/send?section=tools&tab=channels"
          class="btn-luxury inline-flex"
        >
          {{ $t('finalize.addChannelLink') }}
        </router-link>
      </div>

      <template v-else>
        <ol class="mb-6 flex w-full max-w-xl flex-wrap justify-center gap-2 text-xs font-medium">
          <li
            v-for="(label, idx) in stepLabels"
            :key="label"
            class="rounded-full px-3 py-1"
            :class="stepIndex >= idx
              ? 'bg-gold/20 text-gold'
              : 'bg-[var(--bg-input)] text-[var(--text-secondary)]'"
          >
            {{ idx + 1 }}. {{ label }}
          </li>
        </ol>

        <section v-if="step === 'choose'" class="w-full space-y-4">
          <div v-if="!pendingCategories.length" class="finalize-empty w-full max-w-xl mx-auto text-center">
            <i class="fas fa-check-circle mb-3 text-4xl text-gold" />
            <p class="text-[var(--text-secondary)]">{{ $t('finalizeDashboard.allUpToDate') }}</p>
            <p class="mt-2 text-sm text-[var(--text-secondary)]">{{ $t('finalize.wizard.updatePricesHint') }}</p>
          </div>
          <template v-else>
            <h2 class="text-center text-lg font-semibold text-gold">
              {{ $t('finalize.wizard.chooseCategory') }}
            </h2>
            <div class="grid grid-cols-1 gap-3 md:grid-cols-2">
              <button
                v-for="cat in pendingCategories"
                :key="cat.category_id"
                type="button"
                class="finalize-card w-full text-start transition hover:border-gold/50"
                :class="{ 'ring-2 ring-gold': selectedCategoryId === cat.category_id }"
                @click="selectCategory(cat.category_id)"
              >
                <span class="text-xs font-medium uppercase tracking-wide text-[var(--text-secondary)]">
                  {{ $t('finalizeDashboard.categoryLabel') }}
                </span>
                <h3 class="mt-0.5 mb-2 inline-flex items-center gap-2 text-base font-semibold text-gold">
                  <CategoryIcon :category-name="cat.category_name" size-class="h-3.5 w-3.5" />
                  <span>{{ cat.category_name }}</span>
                </h3>
                <p class="mb-3 text-sm text-[var(--text-secondary)]">
                  {{ cat.pending_prices?.length ?? 0 }} {{ $t('finalizeDashboard.pendingPricesCount') }}
                </p>
                <span class="btn-luxury-outline inline-flex text-sm py-1.5 px-3">
                  {{ $t('finalize.wizard.select') }}
                </span>
              </button>
            </div>
          </template>

          <div v-if="data?.pending_special_prices?.length" class="mt-8 w-full">
            <h2 class="mb-3 text-center text-lg font-semibold text-gold">
              {{ $t('finalizeDashboard.pendingSpecialPrices') }}
            </h2>
            <div class="grid grid-cols-1 gap-3 md:grid-cols-2">
              <div
                v-for="sp in data.pending_special_prices"
                :key="sp.special_price_type_id"
                class="finalize-card w-full"
              >
                <h3 class="mb-2 text-base font-semibold text-gold">{{ sp.special_price_type_name }}</h3>
                <router-link
                  :to="`/finalize/special-price/${sp.price_history_id}`"
                  class="btn-luxury-outline finalize-link-btn text-sm py-2"
                >
                  <i class="fas fa-check-circle" /> {{ $t('finalize.startFinalize') }}
                </router-link>
              </div>
            </div>
          </div>
        </section>

        <section v-else-if="step === 'selected' && selectedCategory" class="w-full max-w-xl space-y-4">
          <button type="button" class="text-sm text-gray-400 hover:text-gold" @click="backToChoose">
            <i class="fas" :class="isRtl ? 'fa-arrow-right' : 'fa-arrow-left'" />
            {{ $t('finalize.wizard.backToCategories') }}
          </button>

          <div class="card-luxury p-5 space-y-4">
            <h2 class="text-xl font-bold text-gold">{{ selectedCategory.category_name }}</h2>
            <p class="text-sm text-[var(--text-secondary)]">
              {{ $t('finalize.pendingCount', { count: selectedCategory.pending_prices?.length ?? 0 }) }}
            </p>
            <ul class="space-y-2 text-sm">
              <li
                v-for="pp in selectedCategory.pending_prices"
                :key="pp.price_history_id"
                class="flex flex-wrap items-baseline gap-x-2"
              >
                <span class="font-medium text-[var(--text-primary)]">{{ pp.price_type_name }}</span>
                <span class="text-gold font-bold">{{ formatPrice(pp.price) }}</span>
              </li>
            </ul>
            <div class="flex flex-wrap gap-3 justify-center pt-2">
              <button type="button" class="btn-luxury" @click="openDetails">
                <i class="fas fa-eye" />
                {{ $t('finalize.wizard.details') }}
              </button>
            </div>
          </div>
        </section>

        <section v-else-if="step === 'details' && selectedCategory" class="w-full max-w-2xl space-y-4">
          <button
            type="button"
            class="text-sm text-gray-400 hover:text-gold"
            :disabled="publishing"
            @click="step = 'selected'"
          >
            <i class="fas" :class="isRtl ? 'fa-arrow-right' : 'fa-arrow-left'" />
            {{ $t('common.back') }}
          </button>

          <div class="card-luxury p-5 space-y-4">
            <h2 class="text-lg font-semibold text-gold">
              {{ $t('finalize.wizard.telegramContentTitle') }}
            </h2>
            <p class="text-sm text-[var(--text-secondary)]">
              {{ $t('finalize.wizard.telegramContentHint') }}
            </p>

            <TelegramMockup
              :image-url="selectedCategory.template_media_url"
              :description="selectedCategory.telegram_message_description"
              :buttons="validButtons"
              :variable-values="variableValues"
            />

            <div class="flex flex-wrap gap-3 justify-center pt-2">
              <button
                type="button"
                class="btn-luxury"
                :class="{ 'ring-2 ring-emerald-400': contentConfirmed }"
                :disabled="publishing"
                @click="confirmContent"
              >
                <i class="fas fa-check" />
                {{ contentConfirmed ? $t('finalize.wizard.confirmed') : $t('finalize.wizard.confirmContent') }}
              </button>
              <router-link
                :to="{
                  path: `/categories/${selectedCategory.category_id}/telegram-studio`,
                  query: { return: '/finalize', category: String(selectedCategory.category_id) },
                }"
                class="btn-luxury-outline"
                :class="{ 'pointer-events-none opacity-50': publishing }"
              >
                <i class="fas fa-edit" />
                {{ $t('finalize.wizard.editContent') }}
              </router-link>
            </div>
          </div>

          <div v-if="contentConfirmed" class="card-luxury p-5 space-y-4">
            <h3 class="font-semibold text-gold">{{ $t('finalize.wizard.publishTitle') }}</h3>
            <div>
              <label class="mb-2 block text-sm font-medium text-[var(--text-secondary)]">
                {{ $t('finalize.channel') }}
              </label>
              <select v-model="channelId" class="input-luxury" :disabled="publishing">
                <option disabled value="">{{ $t('finalize.selectChannel') }}</option>
                <option v-for="ch in channels" :key="ch.id" :value="String(ch.id)">
                  {{ ch.name }}
                </option>
              </select>
            </div>
            <FloatingInput v-model="notes" :label="$t('finalize.notes')" :disabled="publishing" />
            <p v-if="publishing" class="text-center text-sm text-gold">
              {{ $t('finalize.wizard.publishingHint') }}
            </p>
            <div class="flex justify-center gap-3">
              <button
                type="button"
                class="btn-luxury"
                :disabled="!channelId || publishing"
                @click="publish"
              >
                <LoadingSpinner v-if="publishing" class="w-5 h-5" />
                <template v-else>
                  <i class="fas fa-paper-plane" />
                  {{ $t('finalize.wizard.publish') }}
                </template>
              </button>
            </div>
            <p
              v-if="publishMessage"
              class="text-center text-sm"
              :class="publishOk ? 'text-success' : 'text-danger'"
            >
              {{ publishMessage }}
            </p>
          </div>
        </section>

        <!-- Mid-publish: category may already be cleared from pending list -->
        <section
          v-else-if="step === 'details' && publishing && !selectedCategory"
          class="w-full max-w-xl space-y-4"
        >
          <div class="card-luxury p-5 space-y-4 text-center">
            <LoadingSpinner class="mx-auto w-8 h-8 text-gold" />
            <p class="text-sm text-gold">{{ $t('finalize.wizard.publishingHint') }}</p>
          </div>
        </section>
      </template>
    </template>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { storeToRefs } from 'pinia'
import { useRoute, useRouter } from 'vue-router'
import { useToast } from 'vue-toastification'
import { useI18n } from 'vue-i18n'
import { finalizeApi } from '@/services/api'
import { useFinalizeStore } from '@/stores/finalize'
import BaseSkeleton from '@/components/ui/BaseSkeleton.vue'
import CategoryIcon from '@/components/ui/CategoryIcon.vue'
import TelegramMockup from '@/components/telegram/TelegramMockup.vue'
import FloatingInput from '@/components/ui/FloatingInput.vue'
import LoadingSpinner from '@/components/ui/LoadingSpinner.vue'
import { formatAppDecimal } from '@/utils/localeFormat.js'

const toast = useToast()
const route = useRoute()
const router = useRouter()
const { t, locale } = useI18n()
const finalizeStore = useFinalizeStore()

const {
  step,
  selectedCategoryId,
  contentConfirmed,
  channelId,
  notes,
  publishing,
  publishMessage,
  publishOk,
} = storeToRefs(finalizeStore)

const loading = ref(true)
const data = ref(null)
const hydrating = ref(false)

const isRtl = computed(() => locale.value === 'fa')
const pendingCategories = computed(() => data.value?.pending_by_category ?? [])
const channels = computed(() => data.value?.channels ?? [])

const selectedCategory = computed(() =>
  pendingCategories.value.find((c) => String(c.category_id) === String(selectedCategoryId.value))
  ?? null,
)

const stepIndex = computed(() => {
  if (step.value === 'choose') return 0
  if (step.value === 'selected') return 1
  return 2
})

const stepLabels = computed(() => [
  t('finalize.wizard.stepChoose'),
  t('finalize.wizard.stepReview'),
  t('finalize.wizard.stepPublish'),
])

const validButtons = computed(() => {
  const buttons = selectedCategory.value?.inline_buttons
  if (!Array.isArray(buttons)) return []
  return buttons.filter((b) => b && (b.label || b.url))
})

const variableValues = computed(() => {
  const values = {
    date: new Date().toLocaleDateString(locale.value === 'fa' ? 'fa-IR' : 'en-GB'),
  }
  const prices = selectedCategory.value?.pending_prices ?? []
  prices.forEach((pp) => {
    if (pp.price_type_name) values[pp.price_type_name] = formatPrice(pp.price)
  })
  return values
})

function formatPrice(value) {
  if (value == null || value === '') return '—'
  const num = typeof value === 'string' ? parseFloat(value) : value
  if (Number.isNaN(num)) return String(value)
  return formatAppDecimal(locale.value === 'fa' ? 'fa' : 'en', num, 2)
}

function selectCategory(id) {
  if (publishing.value) return
  finalizeStore.selectCategory(id)
  router.replace({
    query: {
      category: String(id),
    },
  })
}

function openDetails() {
  if (publishing.value) return
  finalizeStore.openDetails()
  router.replace({
    query: {
      category: String(selectedCategoryId.value),
      details: '1',
    },
  })
}

function backToChoose() {
  if (publishing.value) return
  finalizeStore.resetToChoose()
  router.replace({ query: {} })
}

function confirmContent() {
  if (publishing.value) return
  finalizeStore.confirmContent(channels.value)
}

async function publish() {
  if (!selectedCategory.value) {
    toast.error(t('finalize.wizard.chooseCategory'))
    return
  }
  if (!channelId.value) {
    toast.error(t('finalize.selectChannel'))
    return
  }
  // Persist route so returning mid-publish lands on the same step.
  router.replace({
    query: {
      category: String(selectedCategory.value.category_id),
      details: '1',
    },
  })
  await finalizeStore.publishCategory(selectedCategory.value.category_id)
}

async function fetchData({ preserveSelection = true } = {}) {
  try {
    const { data: res } = await finalizeApi.dashboard()
    if (res?.degraded) {
      toast.warning(res.detail || t('apiErrors.fallback.server'))
    }
    data.value = res
    if (res?.channels?.length && !channelId.value) {
      channelId.value = String(res.channels[0].id)
    }
    if (preserveSelection) {
      finalizeStore.restoreFromQuery(route.query, pendingCategories.value)
      syncRouteToStore()
    }
  } catch {
    data.value = { pending_by_category: [], channels: [], has_telegram_channel: false }
  } finally {
    loading.value = false
  }
}

function syncRouteToStore() {
  if (publishing.value && selectedCategoryId.value != null) {
    const nextQuery = {
      category: String(selectedCategoryId.value),
      details: '1',
    }
    const same =
      String(route.query.category || '') === nextQuery.category
      && String(route.query.details || '') === nextQuery.details
    if (!same) {
      router.replace({ query: nextQuery })
    }
  }
}

watch(pendingCategories, () => {
  if (
    selectedCategoryId.value
    && !selectedCategory.value
    && !publishing.value
  ) {
    backToChoose()
  }
})

onMounted(async () => {
  hydrating.value = true
  await fetchData()
  hydrating.value = false
})

watch(
  () => [route.query.category, route.query.details],
  () => {
    if (loading.value || hydrating.value || publishing.value) return
    hydrating.value = true
    try {
      finalizeStore.restoreFromQuery(route.query, pendingCategories.value)
    } finally {
      hydrating.value = false
    }
  },
)

// Refresh dashboard when an in-flight publish finishes (including while remounted).
watch(publishing, async (busy, wasBusy) => {
  if (!wasBusy || busy) return
  if (step.value !== 'choose') return
  await fetchData({ preserveSelection: false })
  if (route.query.category || route.query.details) {
    router.replace({ query: {} })
  }
})
</script>

<style scoped>
.finalize-card,
.finalize-empty {
  border: 1px solid var(--border-card);
  border-radius: 1rem;
  background: color-mix(in srgb, var(--bg-card) 92%, transparent);
  padding: 0.9rem;
  box-shadow: 0 8px 20px -18px rgba(15, 23, 42, 0.8);
}

.finalize-link-btn {
  width: 100%;
  justify-content: center;
}
</style>
