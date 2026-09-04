<template>
  <div class="verify-banner" role="status">
    <i class="fas fa-envelope-circle-check verify-banner__icon" aria-hidden="true" />
    <p class="verify-banner__text">
      <strong>{{ t('auth.verifyBanner.title') }}</strong>
      <span class="verify-banner__hint">{{ t('auth.verifyBanner.text', { email: auth.user?.email }) }}</span>
    </p>
    <button type="button" class="verify-banner__btn" :disabled="sending" @click="resend">
      <i class="fas fa-paper-plane" aria-hidden="true" />
      <span>{{ sending ? t('common.loading') : t('auth.verifyBanner.resend') }}</span>
    </button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'
import { useToast } from 'vue-toastification'
import { useAuthStore } from '@/stores/auth'
import { getApiErrorDetails } from '@/services/api'

const { t } = useI18n()
const toast = useToast()
const auth = useAuthStore()

const sending = ref(false)

async function resend() {
  sending.value = true
  try {
    const result = await auth.resendVerification()
    // A mail server that is down reports sent:false rather than throwing, so
    // the customer is told the truth instead of being sent to wait for nothing.
    toast[result?.sent ? 'success' : 'error'](
      result?.sent ? t('auth.verifyBanner.sent') : t('auth.verifyBanner.sendFailed'),
    )
  } catch (err) {
    toast.error(getApiErrorDetails(err).message)
  } finally {
    sending.value = false
  }
}
</script>

<style scoped>
/*
  Same slim single row as the demo banner, and equally not dismissible: the
  account works without verification, but an unreachable address is how a
  customer loses their panel, so the ask stays visible until it is done.
*/
.verify-banner {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  flex-wrap: wrap;
  padding: 0.5rem 0.9rem;
  border-bottom: 1px solid var(--glass-border);
  background: color-mix(in srgb, var(--primary) 10%, transparent);
  font-size: 0.8125rem;
}

.verify-banner__icon {
  color: var(--primary);
}

.verify-banner__text {
  margin: 0;
  min-width: 0;
  flex: 1 1 16rem;
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
}

.verify-banner__hint {
  color: var(--text-secondary);
}

.verify-banner__btn {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.3rem 0.7rem;
  border: 1px solid var(--glass-border);
  border-radius: 0.6rem;
  color: var(--text-primary);
  transition: background-color 0.2s;
}

.verify-banner__btn:hover:not(:disabled) {
  background: var(--bg-hover);
}

.verify-banner__btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
</style>
