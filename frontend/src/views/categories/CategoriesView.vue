<template>
  <div>
    <div class="flex justify-between items-center mb-6 animate-fade-in-up">
      <h1 class="text-2xl font-bold text-gold">{{ $t('sidebar.categories') }}</h1>
      <button type="button" class="btn-luxury" @click="showCreateModal = true">
        <i class="fas fa-plus"></i> {{ $t('common.create') }}
      </button>
    </div>

    <div v-if="loading" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      <BaseSkeleton v-for="i in 6" :key="i" variant="card" class="!h-24" />
    </div>

    <div v-else-if="categories.length" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      <BaseCard
        v-for="(cat, index) in categories"
        :key="cat.id"
        variant="glass"
        padding="sm"
        class="hover-lift animate-fade-in-up border border-[var(--glass-border)]"
        :style="{ animationDelay: `${index * 0.06}s` }"
      >
        <div class="flex items-center justify-between gap-4">
          <div class="min-w-0">
            <h3 class="font-semibold text-gold truncate">{{ cat.name }}</h3>
            <p class="text-sm text-[var(--text-secondary)] mt-0.5">
              {{ cat.price_type_count ?? cat.price_types?.length ?? 0 }} {{ $t('analysis.priceType') }}
            </p>
          </div>
          <div class="flex gap-2 shrink-0">
            <router-link :to="`/categories/${cat.id}/edit`" class="btn-luxury-outline text-sm py-1.5">
              {{ $t('common.edit') }}
            </router-link>
            <router-link :to="`/categories/${cat.id}/price-types/new`" class="btn-luxury-outline text-sm py-1.5" :aria-label="$t('common.create')">
              <i class="fas fa-plus" />
            </router-link>
            <button
              v-if="auth.canDeleteItems"
              type="button"
              class="btn-luxury-outline text-sm py-1.5 !border-red-500/50 !text-red-400 hover:!bg-red-500/10"
              @click="handleDelete(cat)"
            >
              <i class="fas fa-trash" aria-hidden="true" />
            </button>
          </div>
        </div>
      </BaseCard>
    </div>

    <div v-else class="empty-state-categories flex flex-col items-center justify-center py-20 px-4 text-center animate-fade-in-up">
      <div
        class="empty-state-icon w-28 h-28 rounded-2xl flex items-center justify-center mb-6"
        style="background: rgba(255, 215, 0, 0.1); border: 1px solid var(--glass-border);"
      >
        <i class="fas fa-tags text-5xl text-[var(--primary)] opacity-80" />
      </div>
      <h3 class="text-xl font-bold text-[var(--text-primary)] mb-2">
        {{ $t('emptyState.noCategories') }}
      </h3>
      <p class="text-sm text-[var(--text-secondary)] mb-8 max-w-sm">
        {{ $t('emptyState.noCategoriesDesc') }}
      </p>
      <button type="button" class="btn-luxury" @click="showCreateModal = true">
        <i class="fas fa-plus" />
        {{ $t('emptyState.createCategory') }}
      </button>
    </div>

    <BaseModal
      v-model="showCreateModal"
      :title="$t('categories.newTitle')"
      aria-label="Create category"
    >
      <p class="text-[var(--text-secondary)] mb-6">
        {{ $t('categories.modalPlaceholder') }}
      </p>
      <div class="flex gap-3">
        <router-link to="/categories/new" class="btn-luxury" @click="showCreateModal = false">
          {{ $t('categories.openFullForm') }}
        </router-link>
        <button type="button" class="btn-luxury-outline" @click="showCreateModal = false">
          {{ $t('common.cancel') }}
        </button>
      </div>
    </BaseModal>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useI18n } from 'vue-i18n'
import { useToast } from 'vue-toastification'
import { categoryApi } from '@/services/api'
import { useAuthStore } from '@/stores/auth'
import BaseSkeleton from '@/components/ui/BaseSkeleton.vue'
import BaseCard from '@/components/ui/BaseCard.vue'
import BaseModal from '@/components/ui/BaseModal.vue'

const { t } = useI18n()
const toast = useToast()
const auth = useAuthStore()
const loading = ref(true)
const categories = ref([])
const showCreateModal = ref(false)

onMounted(async () => {
  try {
    const { data } = await categoryApi.list()
    categories.value = Array.isArray(data) ? data : (data?.results ?? [])
  } catch {
    categories.value = []
  } finally {
    loading.value = false
  }
})

async function handleDelete(cat) {
  if (!confirm(t('common.confirm') + '?')) return
  try {
    await categoryApi.delete(cat.id)
    categories.value = categories.value.filter(c => c.id !== cat.id)
    toast.success(t('toast.deleteSuccess'))
  } catch {
    toast.error(t('toast.serverError'))
  }
}
</script>

<style scoped>
.empty-state-icon {
  animation: emptyIconFloat 3s ease-in-out infinite;
}

@keyframes emptyIconFloat {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-6px); }
}
</style>
