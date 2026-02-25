<template>
  <div>
    <nav class="mb-6">
      <router-link to="/templates" class="text-gray-400 hover:text-gold transition-colors">
        <i class="fas fa-arrow-left mr-2"></i>Back to Templates
      </router-link>
    </nav>
    <h1 class="text-2xl font-bold text-gold mb-6">Template Editor</h1>
    <div class="card-luxury p-8 text-center">
      <p class="text-gray-400 mb-4">Template ID: {{ templateId }}</p>
      <p class="text-gray-400">The template editor with drag-and-drop requires integration with the existing Django template editor. For now, use the legacy URL:</p>
      <a
        :href="`/template-editor/`"
        target="_blank"
        rel="noopener"
        class="btn-luxury-outline mt-4 inline-flex"
      >
        Open Legacy Editor
      </a>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const templateId = computed(() => route.params.id)
</script>
