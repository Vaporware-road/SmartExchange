<template>
  <div>
    <h1 class="text-2xl font-bold text-gold mb-6">{{ $t('programmerHub.title') }}</h1>

    <div v-if="loading" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      <BaseSkeleton v-for="i in 6" :key="i" variant="card" class="!h-40" />
    </div>
    <div v-else-if="!users.length" class="card-luxury p-8 text-center text-[var(--text-secondary)]">
      {{ $t('programmerHub.empty') }}
    </div>
    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      <BaseCard
        v-for="u in users"
        :key="u.id"
        variant="glass"
        padding="sm"
        class="border border-[var(--glass-border)]"
      >
        <button type="button" class="w-full text-start" @click="openUser(u)">
          <div class="flex items-start gap-3">
            <div
              class="w-12 h-12 rounded-xl flex items-center justify-center shrink-0"
              :class="planBadgeClass(u.plan)"
            >
              <i :class="planIcon(u.plan)" />
            </div>
            <div class="min-w-0 flex-1">
              <p class="font-semibold text-[var(--text-primary)] truncate">
                {{ displayName(u) }}
                <span
                  v-if="isDelegated(u)"
                  class="ms-1 inline-block rounded px-1.5 py-0.5 align-middle text-[10px] font-medium border border-[var(--border-card)] text-[var(--text-secondary)]"
                >
                  <i class="fas fa-user-cog me-1" />{{ $t(`programmerHub.${u.sub_role}`) }}
                </span>
              </p>
              <p class="text-sm text-[var(--text-secondary)] truncate">
                {{ u.exchange_name || u.username }}
              </p>
              <p class="text-xs text-[var(--text-secondary)] mt-1 truncate">
                {{ u.country }} · {{ u.email }}
              </p>
              <p
                v-if="isDelegated(u)"
                class="text-xs text-[var(--text-secondary)] mt-1 truncate"
              >
                <i class="fas fa-user-tie me-1" />{{ $t('programmerHub.ownerUsername') }}: {{ u.owner_username }}
              </p>
            </div>
          </div>
        </button>
        <div class="mt-3 flex flex-wrap gap-1">
          <button
            v-for="p in plans"
            :key="p"
            type="button"
            class="px-2 py-1 rounded-lg text-xs font-medium border"
            :class="u.plan === p ? planBadgeClass(p) : 'border-[var(--border-card)] text-[var(--text-secondary)]'"
            @click.stop="setPlan(u, p)"
          >
            <i :class="planIcon(p)" class="me-1" />
            {{ $t(`programmerHub.plans.${p}`) }}
          </button>
        </div>
      </BaseCard>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useToast } from 'vue-toastification'
import { authApi, getApiErrorDetails } from '@/services/api'
import BaseCard from '@/components/ui/BaseCard.vue'
import BaseSkeleton from '@/components/ui/BaseSkeleton.vue'

const plans = ['bronze', 'silver', 'gold']
const router = useRouter()
const toast = useToast()
const loading = ref(true)
const users = ref([])

function displayName(u) {
  return `${u.first_name || ''} ${u.last_name || ''}`.trim() || u.full_name || u.username
}

function isDelegated(u) {
  return u.sub_role === 'operator' || u.sub_role === 'head_operator'
}

function planIcon(plan) {
  if (plan === 'gold') return 'fas fa-crown'
  return 'fas fa-medal'
}

function planBadgeClass(plan) {
  if (plan === 'gold') return 'bg-amber-500/20 text-amber-400 border-amber-500/40'
  if (plan === 'silver') return 'bg-slate-400/20 text-slate-200 border-slate-400/40'
  return 'bg-orange-800/30 text-orange-300 border-orange-700/40'
}

async function loadUsers() {
  loading.value = true
  try {
    const { data } = await authApi.users.list()
    users.value = Array.isArray(data) ? data : (data?.results ?? [])
  } catch (error) {
    toast.error(getApiErrorDetails(error).message)
  } finally {
    loading.value = false
  }
}

async function openUser(user) {
  router.push({ name: 'programmer-user', params: { id: user.id } })
}

async function setPlan(user, plan) {
  try {
    const { data } = await authApi.programmer.update(user.id, { plan })
    users.value = users.value.map((row) => (row.id === user.id ? { ...row, ...data } : row))
  } catch (error) {
    toast.error(getApiErrorDetails(error).message)
  }
}

onMounted(loadUsers)
</script>
