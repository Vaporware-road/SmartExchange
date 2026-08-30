<template>
  <div class="demo-banner" role="status">
    <span class="demo-banner__tag">{{ t('demo.badge') }}</span>

    <p class="demo-banner__text">
      <strong>{{ t('demo.banner.title') }}</strong>
      <span class="demo-banner__hint">{{ t('demo.banner.text') }}</span>
    </p>

    <div class="demo-banner__actions">
      <button type="button" class="demo-banner__btn demo-banner__btn--primary" @click="$emit('open-tour')">
        <i class="fas fa-compass" aria-hidden="true" />
        <span>{{ t('demo.banner.tour') }}</span>
      </button>
      <RouterLink to="/contact" class="demo-banner__btn">
        <i class="fas fa-comments" aria-hidden="true" />
        <span>{{ t('demo.banner.talk') }}</span>
      </RouterLink>
      <RouterLink to="/" class="demo-banner__btn demo-banner__btn--quiet">
        <i class="fas fa-arrow-left" aria-hidden="true" />
        <span>{{ t('demo.banner.site') }}</span>
      </RouterLink>
    </div>
  </div>
</template>

<script setup>
import { useI18n } from 'vue-i18n'
import { RouterLink } from 'vue-router'

defineEmits(['open-tour'])

const { t } = useI18n()
</script>

<style scoped>
/*
  Deliberately not dismissible: a visitor must never mistake sample data for
  their own. It stays a single slim row so it costs the panel no real estate.
*/
.demo-banner {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.5rem 0.85rem;
  padding: 0.5rem 0.9rem;
  font-size: 0.8rem;
  color: var(--text-primary);
  background:
    linear-gradient(90deg, color-mix(in srgb, var(--primary) 16%, transparent), transparent 65%),
    var(--bg-navbar);
  border-bottom: 1px solid color-mix(in srgb, var(--primary) 35%, var(--border-card));
}

.demo-banner__tag {
  flex-shrink: 0;
  padding: 0.15rem 0.55rem;
  font-size: 0.62rem;
  font-weight: 800;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  border-radius: 999px;
  color: var(--text-on-primary);
  background: var(--primary);
}

.demo-banner__text {
  min-width: 0;
  flex: 1 1 16rem;
  line-height: 1.5;
}

.demo-banner__hint {
  color: var(--text-secondary);
}

.demo-banner__hint::before {
  content: '—';
  margin: 0 0.35rem;
  opacity: 0.5;
}

.demo-banner__actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  margin-inline-start: auto;
}

.demo-banner__btn {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.3rem 0.7rem;
  font-size: 0.74rem;
  font-weight: 600;
  white-space: nowrap;
  border-radius: 999px;
  border: 1px solid var(--border-card);
  background: var(--bg-card);
  color: var(--text-primary);
  transition: all 0.25s ease;
}

.demo-banner__btn:hover {
  border-color: var(--primary);
  color: var(--primary);
}

.demo-banner__btn--primary {
  border-color: transparent;
  background: var(--primary);
  color: var(--text-on-primary);
}

.demo-banner__btn--primary:hover {
  color: var(--text-on-primary);
  filter: brightness(1.06);
}

.demo-banner__btn--quiet {
  background: transparent;
  color: var(--text-secondary);
}

/* The back arrow points the way out of the panel, so it follows the writing direction. */
[dir='rtl'] .demo-banner__btn--quiet .fa-arrow-left {
  transform: scaleX(-1);
}

@media (max-width: 640px) {
  .demo-banner__hint {
    display: none;
  }
}
</style>
