<template>
  <div>
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-2xl font-bold text-gold">Price Templates</h1>
      <router-link to="/templates/new" class="btn-luxury">
        <i class="fas fa-plus"></i> Add Template
      </router-link>
    </div>
    <div v-if="loading" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      <BaseSkeleton v-for="i in 6" :key="i" variant="card" class="!h-20" />
    </div>
    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      <div
        v-for="t in templates"
        :key="t.id"
        class="card-luxury p-4 flex items-center justify-between"
      >
        <span>{{ t.name ?? `Template ${t.id}` }}</span>
        <router-link :to="`/templates/${t.id}/editor`" class="btn-luxury-outline text-sm py-2">
          <i class="fas fa-edit"></i> Editor
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { templateApi } from '@/services/api'
import BaseSkeleton from '@/components/ui/BaseSkeleton.vue'

const loading = ref(true)
const templates = ref([])

onMounted(async () => {
  try {
    const { data } = await templateApi.list()
    templates.value = Array.isArray(data) ? data : []
  } catch {
    templates.value = []
  } finally {
    loading.value = false
  }
})
</script>
