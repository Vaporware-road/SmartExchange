<template>
  <div>
    <h1 class="text-2xl font-bold text-gold mb-6">Settings</h1>
    <div class="space-y-6">
      <div class="card-luxury">
        <h2 class="text-lg font-semibold text-gold mb-4">Site Settings</h2>
        <p class="text-gray-400 mb-4">Configure branding and contact information from the Django admin or API.</p>
        <router-link to="/settings/logs" class="btn-luxury-outline">
          <i class="fas fa-list"></i> View Logs
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
</script>
