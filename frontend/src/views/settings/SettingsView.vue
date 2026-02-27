<template>
  <div>
    <h1 class="text-2xl font-bold text-gold mb-6">{{ $t('settings.title') }}</h1>
    <div class="space-y-6">
      <div class="card-luxury">
        <h2 class="text-lg font-semibold text-gold mb-4">{{ $t('settings.siteSettings') }}</h2>
        <p class="text-[var(--text-secondary)] mb-4">{{ $t('settings.siteSettingsDesc') }}</p>
        <router-link to="/settings/logs" class="btn-luxury-outline">
          <i class="fas fa-list"></i> {{ $t('settings.viewLogs') }}
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
</script>
