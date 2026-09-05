<template>
  <div class="trial-banner" role="status">
    <i class="fas fa-lock trial-banner__icon" aria-hidden="true" />
    <div class="trial-banner__text">
      <strong>{{ t('trial.expiredTitle') }}</strong>
      <span class="trial-banner__hint">{{ t('trial.expiredText') }}</span>
    </div>
    <button type="button" class="trial-banner__btn" @click="open = !open">
      <i class="fas fa-headset" aria-hidden="true" />
      <span>{{ t('trial.talkToUs') }}</span>
    </button>
  </div>
  <div v-if="open" class="trial-banner__channels">
    <SupportChannelList inline />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'
import SupportChannelList from '@/components/support/SupportChannelList.vue'

const { t } = useI18n()
const open = ref(false)
</script>

<style scoped>
/*
  Not dismissible, like the verification banner: the panel still reads, so
  without a standing reminder an expired customer just sees writes fail.
*/
.trial-banner {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  flex-wrap: wrap;
  padding: 0.5rem 0.9rem;
  border-bottom: 1px solid var(--glass-border);
  background: color-mix(in srgb, #f59e0b 16%, transparent);
  font-size: 0.8125rem;
}

.trial-banner__icon {
  color: #f59e0b;
}

.trial-banner__text {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 0.5rem;
  min-width: 0;
  flex: 1;
}

.trial-banner__hint {
  color: var(--text-secondary);
}

.trial-banner__btn {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.3rem 0.7rem;
  border-radius: 0.6rem;
  border: 1px solid var(--border-card);
  font-weight: 600;
  transition: all 0.25s ease;
}

.trial-banner__btn:hover {
  border-color: var(--primary);
  color: var(--primary);
}

.trial-banner__channels {
  padding: 0.6rem 0.9rem;
  border-bottom: 1px solid var(--glass-border);
  background: color-mix(in srgb, #f59e0b 8%, transparent);
}
</style>
