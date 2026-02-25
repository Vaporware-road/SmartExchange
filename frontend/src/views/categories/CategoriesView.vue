<template>
  <div>
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-2xl font-bold text-gold">{{ $t('sidebar.categories') }}</h1>
      <router-link to="/categories/new" class="btn-luxury">
        <i class="fas fa-plus"></i> {{ $t('common.create') }}
      </router-link>
    </div>
    <div v-if="loading" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      <BaseSkeleton v-for="i in 6" :key="i" variant="card" class="!h-24" />
    </div>
    <div v-else-if="categories.length" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      <div
        v-for="cat in categories"
        :key="cat.id"
        class="card-luxury p-4 flex items-center justify-between"
      >
        <div>
          <h3 class="font-semibold text-gold">{{ cat.name }}</h3>
          <p class="text-sm text-gray-400">{{ cat.price_type_count ?? cat.price_types?.length ?? 0 }} {{ $t('analysis.priceType') }}</p>
        </div>
        <div class="flex gap-2">
          <router-link :to="`/categories/${cat.id}/edit`" class="btn-luxury-outline text-sm py-1.5">
            {{ $t('common.edit') }}
          </router-link>
          <router-link :to="`/categories/${cat.id}/price-types/new`" class="btn-luxury-outline text-sm py-1.5">
            <i class="fas fa-plus" />
          </router-link>
          <button
            v-if="auth.canDeleteItems"
            class="btn-luxury-outline text-sm py-1.5 !border-red-500/50 !text-red-400 hover:!bg-red-500/10"
            @click="handleDelete(cat)"
          >
            <i class="fas fa-trash" />
          </button>
        </div>
      </div>
    </div>
    <EmptyState
      v-else
      icon="fas fa-tags"
      title-key="emptyState.noCategories"
      description-key="emptyState.noCategoriesDesc"
      action-label="emptyState.createCategory"
      action-to="/categories/new"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useI18n } from 'vue-i18n'
import { useToast } from 'vue-toastification'
import { categoryApi } from '@/services/api'
import { useAuthStore } from '@/stores/auth'
import BaseSkeleton from '@/components/ui/BaseSkeleton.vue'
import EmptyState from '@/components/ui/EmptyState.vue'

const { t } = useI18n()
const toast = useToast()
const auth = useAuthStore()
const loading = ref(true)
const categories = ref([])

onMounted(async () => {
  try {
    const { data } = await categoryApi.list()
    categories.value = data ?? []
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
