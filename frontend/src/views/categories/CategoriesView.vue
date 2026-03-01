<template>
  <div>
    <h1 class="text-2xl font-bold text-gold mb-8 animate-fade-in-up">{{ $t('sidebar.categories') }}</h1>

    <div v-if="loading" class="space-y-10">
      <div>
        <BaseSkeleton variant="text" class="!h-7 !max-w-[200px] mb-4" />
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <BaseSkeleton v-for="i in 6" :key="i" variant="card" class="!h-40" />
        </div>
      </div>
      <div>
        <BaseSkeleton variant="text" class="!h-7 !max-w-[180px] mb-4" />
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <BaseSkeleton v-for="i in 6" :key="'sp-' + i" variant="card" class="!h-40" />
        </div>
      </div>
    </div>

    <template v-else>
      <!-- Section 1: Standard Categories -->
      <section class="mb-12 animate-fade-in-up">
        <div class="flex justify-between items-center mb-5">
          <h2 class="text-lg font-bold text-[var(--text-primary)] uppercase tracking-wider flex items-center gap-2">
            <i class="fas fa-coins text-[var(--primary)]" />
            {{ $t('categories.standardCategories') }}
          </h2>
          <button type="button" class="btn-luxury" @click="$router.push('/categories/new')">
            <i class="fas fa-plus"></i> {{ $t('emptyState.createCategory') }}
          </button>
        </div>

        <div v-if="categories.length" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <div
            v-for="(cat, index) in categories"
            :key="'cat-' + cat.id"
            class="card-vip p-5 flex flex-col overflow-hidden hover-lift animate-fade-in-up border border-[var(--glass-border)]"
            :style="{ animationDelay: `${index * 0.05}s` }"
          >
            <div class="flex items-start justify-between gap-3 mb-4">
              <div class="flex items-center gap-3 min-w-0 flex-1">
                <div
                  class="w-12 h-12 rounded-xl flex items-center justify-center text-xl text-[var(--primary)] shrink-0 bg-primary-muted border border-[var(--glass-border)]"
                >
                  <i class="fas fa-coins" />
                </div>
                <div class="min-w-0 flex-1">
                  <h3 class="font-semibold text-[var(--primary)] truncate">{{ cat.name }}</h3>
                </div>
              </div>
              <span
                class="inline-flex items-center gap-1.5 rounded-full px-2.5 py-0.5 text-xs font-medium shrink-0 bg-emerald-500/20 text-emerald-400 border border-emerald-500/30"
              >
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-400" />
                {{ $t('dashboard.active') }}
              </span>
            </div>
            <router-link
              :to="`/categories/${cat.id}/template`"
              class="btn-luxury w-full flex items-center justify-center gap-2 py-2.5 mb-2"
            >
              <i class="fas fa-palette" />
              {{ $t('specialPrices.designTemplate') }}
            </router-link>
            <router-link
              :to="`/categories/${cat.id}/telegram-studio`"
              class="btn-luxury w-full flex items-center justify-center gap-2 py-2.5 mb-4"
            >
              <i class="fab fa-telegram-plane" />
              {{ $t('specialPrices.telegramContent') }}
            </router-link>
            <div class="flex gap-2 flex-wrap mt-auto">
              <router-link :to="`/categories/${cat.id}/edit`" class="btn-luxury-outline text-sm py-1.5 flex-1 min-w-0">
                {{ $t('common.edit') }}
              </router-link>
              <router-link :to="`/categories/${cat.id}/price-types/new`" class="btn-luxury-outline text-sm py-1.5" :aria-label="$t('common.create')">
                <i class="fas fa-plus" />
              </router-link>
              <button
                v-if="auth.canDeleteItems"
                type="button"
                class="btn-luxury-outline text-sm py-1.5 !border-red-500/50 !text-red-400 hover:!bg-red-500/10"
                @click="openDeleteModal(cat)"
              >
                <i class="fas fa-trash" aria-hidden="true" />
              </button>
            </div>
          </div>
        </div>

        <div v-else class="empty-state-section flex flex-col items-center justify-center py-16 px-4 text-center rounded-2xl border border-dashed border-[var(--glass-border)]">
          <div class="w-20 h-20 rounded-2xl flex items-center justify-center mb-4 bg-primary-muted border border-[var(--glass-border)]">
            <i class="fas fa-tags text-4xl text-[var(--primary)] opacity-80" />
          </div>
          <h3 class="text-lg font-bold text-[var(--text-primary)] mb-2">{{ $t('emptyState.noCategories') }}</h3>
          <p class="text-sm text-[var(--text-secondary)] mb-6 max-w-sm">{{ $t('emptyState.noCategoriesDesc') }}</p>
          <button type="button" class="btn-luxury" @click="$router.push('/categories/new')">
            <i class="fas fa-plus" /> {{ $t('emptyState.createCategory') }}
          </button>
        </div>
      </section>

      <!-- Section 2: Special Offers -->
      <section class="animate-fade-in-up" style="animation-delay: 0.1s">
        <div class="flex justify-between items-center mb-5">
          <h2 class="text-lg font-bold text-[var(--text-primary)] uppercase tracking-wider flex items-center gap-2">
            <i class="fas fa-star text-[var(--primary)]" />
            {{ $t('categories.specialOffers') }}
          </h2>
          <button type="button" class="btn-luxury" @click="$router.push('/special-prices/new')">
            <i class="fas fa-plus"></i> {{ $t('emptyState.createSpecialOffer') }}
          </button>
        </div>

        <div v-if="specialPrices.length" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <div
            v-for="(sp, index) in specialPrices"
            :key="'sp-' + sp.id"
            class="card-vip p-5 flex flex-col overflow-hidden hover-lift animate-fade-in-up border border-[var(--glass-border)]"
            :style="{ animationDelay: `${index * 0.05}s` }"
          >
            <div class="flex items-start justify-between gap-3 mb-4">
              <div class="flex items-center gap-3 min-w-0 flex-1">
                <div
                  class="w-12 h-12 rounded-xl flex items-center justify-center text-xl text-[var(--primary)] shrink-0 bg-primary-muted border border-[var(--glass-border)]"
                >
                  <i :class="sp.icon || 'fas fa-star'" />
                </div>
                <div class="min-w-0 flex-1">
                  <h3 class="font-semibold text-[var(--primary)] truncate">{{ sp.name }}</h3>
                </div>
              </div>
              <span
                class="inline-flex items-center gap-1.5 rounded-full px-2.5 py-0.5 text-xs font-medium shrink-0 bg-emerald-500/20 text-emerald-400 border border-emerald-500/30"
              >
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-400" />
                {{ $t('dashboard.active') }}
              </span>
            </div>
            <router-link
              :to="`/special-prices/${sp.id}/template`"
              class="btn-luxury w-full flex items-center justify-center gap-2 py-2.5 mb-2"
            >
              <i class="fas fa-palette" />
              {{ $t('specialPrices.designTemplate') }}
            </router-link>
            <router-link
              :to="`/special-prices/${sp.id}/telegram-studio`"
              class="btn-luxury w-full flex items-center justify-center gap-2 py-2.5 mb-4"
            >
              <i class="fab fa-telegram-plane" />
              {{ $t('specialPrices.telegramContent') }}
            </router-link>
            <div class="flex gap-2 flex-wrap mt-auto">
              <router-link
                :to="`/special-prices/${sp.id}/history`"
                class="btn-luxury-outline text-sm py-1.5 flex-1 min-w-0"
              >
                <i class="fas fa-history" />
                {{ $t('specialPrices.history') }}
              </router-link>
            </div>
          </div>
        </div>

        <div v-else class="empty-state-section flex flex-col items-center justify-center py-16 px-4 text-center rounded-2xl border border-dashed border-[var(--glass-border)]">
          <div class="w-20 h-20 rounded-2xl flex items-center justify-center mb-4 bg-primary-muted border border-[var(--glass-border)]">
            <i class="fas fa-star text-4xl text-[var(--primary)] opacity-60" style="filter: blur(1px);" />
          </div>
          <h3 class="text-lg font-bold text-[var(--text-primary)] mb-2">{{ $t('emptyState.noSpecialOffers') }}</h3>
          <p class="text-sm text-[var(--text-secondary)] mb-6 max-w-sm">{{ $t('emptyState.noSpecialOffersDesc') }}</p>
          <button type="button" class="btn-luxury-gradient" @click="$router.push('/special-prices/new')">
            <i class="fas fa-plus" /> {{ $t('emptyState.createSpecialOffer') }}
          </button>
        </div>
      </section>
    </template>

    <BaseModal
      v-model="showDeleteModal"
      :title="$t('categories.deleteConfirmTitle')"
      aria-label="Delete category confirmation"
    >
      <p class="text-[var(--text-secondary)] mb-6">
        {{ deleteConfirmMessage }}
      </p>
      <div class="flex gap-3 justify-end">
        <button type="button" class="btn-luxury-outline" @click="showDeleteModal = false">
          {{ $t('common.cancel') }}
        </button>
        <button
          type="button"
          class="inline-flex items-center justify-center gap-2 px-6 py-2.5 font-semibold rounded-2xl transition-all duration-300 border border-red-500/50 text-red-400 hover:bg-red-500/10 focus:outline-none focus:ring-2 focus:ring-red-500/50"
          @click="confirmDelete"
        >
          <i class="fas fa-trash" aria-hidden="true" />
          {{ $t('common.delete') }}
        </button>
      </div>
    </BaseModal>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useI18n } from 'vue-i18n'
import { useToast } from 'vue-toastification'
import { categoryApi, specialPriceApi } from '@/services/api'
import { useAuthStore } from '@/stores/auth'
import BaseSkeleton from '@/components/ui/BaseSkeleton.vue'
import BaseModal from '@/components/ui/BaseModal.vue'

const { t } = useI18n()
const toast = useToast()
const auth = useAuthStore()
const loading = ref(true)
const categories = ref([])
const specialPrices = ref([])
const showDeleteModal = ref(false)
const categoryToDelete = ref(null)

const deleteConfirmMessage = computed(() =>
  categoryToDelete.value
    ? t('categories.deleteConfirmMessage', { name: categoryToDelete.value.name })
    : ''
)

onMounted(async () => {
  try {
    const [catRes, spRes] = await Promise.all([categoryApi.list(), specialPriceApi.list()])
    categories.value = Array.isArray(catRes.data) ? catRes.data : (catRes.data?.results ?? [])
    specialPrices.value = Array.isArray(spRes.data) ? spRes.data : (spRes.data?.results ?? [])
  } catch {
    categories.value = []
    specialPrices.value = []
  } finally {
    loading.value = false
  }
})

function openDeleteModal(cat) {
  categoryToDelete.value = cat
  showDeleteModal.value = true
}

async function confirmDelete() {
  const cat = categoryToDelete.value
  if (!cat) return
  showDeleteModal.value = false
  try {
    await categoryApi.delete(cat.id)
    categories.value = categories.value.filter((c) => c.id !== cat.id)
    toast.success(t('toast.deleteSuccess'))
  } catch {
    toast.error(t('toast.serverError'))
  } finally {
    categoryToDelete.value = null
  }
}
</script>

<style scoped>
.empty-state-section {
  background: var(--bg-card);
}
</style>
