<template>
  <div class="flex flex-col items-center justify-center py-16 px-4 text-center">
    <div
      class="w-20 h-20 rounded-2xl flex items-center justify-center mb-6"
      style="background: rgba(255, 215, 0, 0.1); border: 1px solid var(--border-color);"
    >
      <i :class="icon" class="text-3xl text-[var(--primary)] opacity-70" />
    </div>
    <h3 class="text-lg font-bold text-[var(--text-primary)] mb-2">
      {{ $t(titleKey) }}
    </h3>
    <p class="text-sm text-[var(--text-secondary)] mb-8 max-w-sm">
      {{ $t(descriptionKey) }}
    </p>
    <router-link v-if="actionTo" :to="actionTo">
      <button class="btn-luxury">
        <i v-if="actionIcon" :class="actionIcon" />
        {{ $t(actionLabel) }}
      </button>
    </router-link>
  </div>
</template>

<script setup>
defineProps({
  icon: {
    type: String,
    default: 'fas fa-inbox',
  },
  titleKey: {
    type: String,
    required: true,
  },
  descriptionKey: {
    type: String,
    required: true,
  },
  actionLabel: {
    type: String,
    default: '',
  },
  actionTo: {
    type: String,
    default: '',
  },
  actionIcon: {
    type: String,
    default: 'fas fa-plus',
  },
})
</script>
