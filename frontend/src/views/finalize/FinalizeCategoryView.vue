<template>
  <div>
    <nav class="mb-6">
      <router-link to="/finalize" class="text-gray-400 hover:text-gold transition-colors">
        <i class="fas" :class="isRtl ? 'fa-arrow-right' : 'fa-arrow-left'" />
        <span class="ms-2">{{ $t('finalize.backToList') }}</span>
      </router-link>
    </nav>

    <h1 class="text-2xl font-bold text-gold mb-6">{{ $t('finalize.title') }}</h1>

    <div v-if="loading" class="card-luxury max-w-lg p-6 space-y-4">
      <BaseSkeleton variant="text" class="!max-w-full !h-4" />
      <BaseSkeleton variant="text" class="!max-w-full !h-12" />
      <BaseSkeleton variant="text" class="!max-w-full !h-12" />
    </div>

    <template v-else>
      <!-- Configuration form (pre-finalization) -->
      <form v-if="phase === 'config'" @submit.prevent="startFinalize" class="card-luxury max-w-lg space-y-4">
        <p class="text-[var(--text-secondary)] mb-4">
          {{ $t('finalize.pendingCount', { count: pendingCount }) }}
        </p>

        <div>
          <label class="block text-sm font-medium text-[var(--text-secondary)] mb-2">
            {{ $t('finalize.channel') }}
          </label>
          <select v-model="channelId" class="input-luxury" required>
            <option value="">{{ $t('finalize.selectChannel') }}</option>
            <option v-for="ch in channels" :key="ch.id" :value="ch.id">{{ ch.name }}</option>
          </select>
        </div>

        <FloatingInput
          v-model="notes"
          :label="$t('finalize.notes')"
        />

        <div class="flex gap-4">
          <button type="submit" class="btn-luxury" :disabled="!channelId">
            <i class="fas fa-play" />
            {{ $t('finalize.startFinalize') }}
          </button>
          <router-link to="/finalize" class="btn-luxury-outline">
            {{ $t('common.cancel') }}
          </router-link>
        </div>
      </form>

      <!-- Step-by-step progress -->
      <div v-else class="card-luxury max-w-lg space-y-6">
        <div class="space-y-3">
          <div
            v-for="(step, idx) in steps"
            :key="step.key"
            class="flex items-center gap-4 p-4 rounded-xl border transition-all duration-300"
            :style="stepStyle(step)"
          >
            <div class="flex-shrink-0 w-10 h-10 rounded-full flex items-center justify-center transition-all duration-300"
              :class="stepIconBg(step)"
            >
              <i v-if="step.status === 'success'" class="fas fa-check text-white" />
              <i v-else-if="step.status === 'failed'" class="fas fa-times text-white" />
              <span v-else-if="step.status === 'inProgress'"
                class="inline-block w-5 h-5 border-2 border-gold border-t-transparent rounded-full animate-spin"
              />
              <span v-else class="text-sm font-bold text-[var(--text-secondary)]">{{ idx + 1 }}</span>
            </div>

            <div class="flex-1 min-w-0">
              <p class="font-medium" :class="step.status === 'success' ? 'text-success' : step.status === 'failed' ? 'text-danger' : step.status === 'inProgress' ? 'text-gold' : 'text-[var(--text-secondary)]'">
                {{ $t(`finalize.step.${step.key}`) }}
              </p>
              <p v-if="step.detail" class="text-xs text-[var(--text-secondary)] mt-0.5 truncate">{{ step.detail }}</p>
            </div>

            <div class="flex-shrink-0">
              <span class="text-xs font-medium px-2 py-1 rounded-lg"
                :class="statusBadge(step.status)"
              >
                {{ $t(`finalize.status.${step.status}`) }}
              </span>
            </div>
          </div>
        </div>

        <!-- Overall progress bar -->
        <div class="relative h-2 bg-[var(--bg-input)] rounded-full overflow-hidden">
          <div
            class="absolute inset-y-0 start-0 rounded-full transition-all duration-500 ease-out"
            :class="overallFailed ? 'bg-danger' : 'bg-gradient-to-r from-gold to-success'"
            :style="{ width: progressPercent + '%' }"
          />
        </div>

        <!-- Completion message -->
        <div v-if="phase === 'done'" class="text-center py-4">
          <i class="fas fa-check-circle text-4xl text-success mb-3" />
          <p class="text-lg font-bold text-success">{{ $t('finalize.completed') }}</p>
        </div>
        <div v-else-if="phase === 'error'" class="text-center py-4">
          <i class="fas fa-exclamation-triangle text-4xl text-danger mb-3" />
          <p class="text-lg font-bold text-danger">{{ $t('finalize.failed') }}</p>
        </div>

        <div class="flex gap-4 pt-2">
          <router-link v-if="phase === 'done' || phase === 'error'" to="/finalize" class="btn-luxury">
            <i class="fas fa-arrow-left" />
            {{ $t('common.back') }}
          </router-link>
          <button v-if="phase === 'error'" class="btn-luxury-outline" @click="retryFinalize">
            <i class="fas fa-redo" />
            {{ $t('common.submit') }}
          </button>
        </div>
      </div>
    </template>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
import { useToast } from 'vue-toastification'
import { finalizeApi, telegramApi } from '@/services/api'
import BaseSkeleton from '@/components/ui/BaseSkeleton.vue'
import FloatingInput from '@/components/ui/FloatingInput.vue'

const { t } = useI18n()
const toast = useToast()
const route = useRoute()
const router = useRouter()
const categoryId = computed(() => route.params.id)
const isRtl = computed(() => document.documentElement.dir === 'rtl')

const loading = ref(true)
const channels = ref([])
const pendingCount = ref(0)
const channelId = ref('')
const notes = ref('')
const phase = ref('config')

const STEP_KEYS = ['validate', 'render', 'send', 'confirm']

const steps = reactive(
  STEP_KEYS.map(key => ({ key, status: 'pending', detail: '' }))
)

const completedSteps = computed(() => steps.filter(s => s.status === 'success').length)
const overallFailed = computed(() => steps.some(s => s.status === 'failed'))
const progressPercent = computed(() => Math.round((completedSteps.value / steps.length) * 100))

function stepStyle(step) {
  if (step.status === 'success') return { borderColor: 'rgba(16, 185, 129, 0.3)', background: 'rgba(16, 185, 129, 0.05)' }
  if (step.status === 'failed') return { borderColor: 'rgba(239, 68, 68, 0.3)', background: 'rgba(239, 68, 68, 0.05)' }
  if (step.status === 'inProgress') return { borderColor: 'rgba(255, 215, 0, 0.4)', background: 'rgba(255, 215, 0, 0.05)' }
  return { borderColor: 'var(--border-card)', background: 'transparent' }
}

function stepIconBg(step) {
  if (step.status === 'success') return 'bg-success'
  if (step.status === 'failed') return 'bg-danger'
  if (step.status === 'inProgress') return 'bg-transparent'
  return 'bg-[var(--bg-input)]'
}

function statusBadge(status) {
  if (status === 'success') return 'bg-success/10 text-success'
  if (status === 'failed') return 'bg-danger/10 text-danger'
  if (status === 'inProgress') return 'bg-gold/10 text-gold'
  return 'bg-gray-500/10 text-gray-400'
}

onMounted(async () => {
  try {
    const [dashRes, chRes] = await Promise.all([
      finalizeApi.dashboard(),
      telegramApi.channels(),
    ])
    const cat = dashRes.data?.pending_by_category?.find(
      c => String(c.category_id) === String(categoryId.value)
    )
    pendingCount.value = cat?.pending_prices?.length ?? 0
    channels.value = chRes.data ?? []
  } catch {
    channels.value = []
  } finally {
    loading.value = false
  }
})

async function runStep(idx, fn) {
  steps[idx].status = 'inProgress'
  try {
    const result = await fn()
    steps[idx].status = 'success'
    steps[idx].detail = result ?? ''
    return true
  } catch (err) {
    steps[idx].status = 'failed'
    steps[idx].detail = err?.response?.data?.detail ?? err.message ?? ''
    return false
  }
}

async function startFinalize() {
  phase.value = 'progress'
  steps.forEach(s => { s.status = 'pending'; s.detail = '' })

  const ok1 = await runStep(0, async () => {
    await new Promise(r => setTimeout(r, 400))
    return t('finalize.status.success')
  })
  if (!ok1) { phase.value = 'error'; return }

  const ok2 = await runStep(1, async () => {
    await new Promise(r => setTimeout(r, 600))
    return t('finalize.status.success')
  })
  if (!ok2) { phase.value = 'error'; return }

  const ok3 = await runStep(2, async () => {
    await finalizeApi.finalizeCategory(categoryId.value, {
      channel_id: Number(channelId.value),
      notes: notes.value,
    })
    return t('finalize.status.success')
  })
  if (!ok3) { phase.value = 'error'; return }

  const ok4 = await runStep(3, async () => {
    await new Promise(r => setTimeout(r, 300))
    return t('finalize.status.success')
  })
  if (!ok4) { phase.value = 'error'; return }

  phase.value = 'done'
  toast.success(t('toast.finalizeSuccess'))
}

function retryFinalize() {
  startFinalize()
}
</script>
