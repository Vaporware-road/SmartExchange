<template>
  <div class="flex flex-col items-center py-12">
    <LoadingSpinner class="w-10 h-10 text-gold" />
    <p class="mt-4 text-sm text-[var(--text-secondary)]">{{ $t('common.loading') }}</p>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import LoadingSpinner from '@/components/ui/LoadingSpinner.vue'

const route = useRoute()
const router = useRouter()

onMounted(() => {
  const id = route.params.id
  router.replace({
    path: '/finalize',
    query: { category: String(id), details: '1' },
  })
})
</script>
