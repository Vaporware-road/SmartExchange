<template>
  <div>
    <div class="flex flex-wrap items-center justify-between gap-4 mb-6">
      <h1 class="text-2xl font-bold text-gold">{{ $t('programmerHub.templatesTitle') }}</h1>
      <router-link to="/programmer" class="btn-luxury-outline">{{ $t('common.back') }}</router-link>
    </div>
    <p class="text-sm text-[var(--text-secondary)] mb-4">{{ $t('programmerHub.templatesHint') }}</p>

    <div v-if="loading" class="grid grid-cols-2 md:grid-cols-4 gap-4">
      <BaseSkeleton v-for="i in 8" :key="i" variant="card" class="!h-48" />
    </div>
    <div v-else class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
      <BaseCard
        v-for="item in items"
        :key="item.kind + item.id"
        variant="glass"
        padding="none"
        class="overflow-hidden border border-[var(--glass-border)]"
      >
        <div class="h-32 bg-[var(--bg-hover)]">
          <img
            v-if="item.image"
            :src="item.image"
            alt=""
            class="w-full h-full object-cover"
          />
        </div>
        <div class="p-3 space-y-2">
          <p class="text-sm font-semibold truncate text-[var(--text-primary)]">{{ item.name }}</p>
          <div class="flex flex-wrap gap-1">
            <button
              v-for="p in plans"
              :key="p"
              type="button"
              class="px-2 py-1 rounded-lg text-xs border"
              :class="item.plan === p ? planBadgeClass(p) : 'border-[var(--border-card)] text-[var(--text-secondary)]'"
              @click="setPlan(item, p)"
            >
              <i :class="p === 'gold' ? 'fas fa-crown' : 'fas fa-medal'" class="me-1" />
              {{ $t(`programmerHub.plans.${p}`) }}
            </button>
          </div>
        </div>
      </BaseCard>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue'
import { useToast } from 'vue-toastification'
import { authApi, getApiErrorDetails } from '@/services/api'
import BaseCard from '@/components/ui/BaseCard.vue'
import BaseSkeleton from '@/components/ui/BaseSkeleton.vue'

const plans = ['bronze', 'silver', 'gold']
const toast = useToast()
const loading = ref(true)
const priceTemplates = ref([])
const editorTemplates = ref([])

const items = computed(() => {
  const price = priceTemplates.value.map((row) => ({
    kind: 'price',
    id: row.id,
    name: row.name,
    plan: row.plan || 'bronze',
    image: row.background_image,
  }))
  const editor = editorTemplates.value.map((row) => ({
    kind: 'editor',
    id: row.id,
    name: row.name,
    plan: row.plan || 'bronze',
    image: row.image,
  }))
  return [...price, ...editor]
})

function planBadgeClass(plan) {
  if (plan === 'gold') return 'bg-amber-500/20 text-amber-400 border-amber-500/40'
  if (plan === 'silver') return 'bg-slate-400/20 text-slate-200 border-slate-400/40'
  return 'bg-orange-800/30 text-orange-300 border-orange-700/40'
}

async function load() {
  loading.value = true
  try {
    const { data } = await authApi.programmer.templates()
    priceTemplates.value = data.price_templates || []
    editorTemplates.value = data.editor_templates || []
  } catch (error) {
    toast.error(getApiErrorDetails(error).message)
  } finally {
    loading.value = false
  }
}

async function setPlan(item, plan) {
  try {
    await authApi.programmer.setTemplatePlan({ kind: item.kind, id: item.id, plan })
    if (item.kind === 'price') {
      priceTemplates.value = priceTemplates.value.map((row) =>
        row.id === item.id ? { ...row, plan } : row,
      )
    } else {
      editorTemplates.value = editorTemplates.value.map((row) =>
        row.id === item.id ? { ...row, plan } : row,
      )
    }
  } catch (error) {
    toast.error(getApiErrorDetails(error).message)
  }
}

onMounted(load)
</script>
