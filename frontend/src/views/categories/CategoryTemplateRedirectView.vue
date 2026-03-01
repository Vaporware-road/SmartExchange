<template>
  <div class="flex flex-col items-center justify-center py-20">
    <LoadingSpinner class="w-10 h-10 text-[var(--primary)] mb-4" />
    <p class="text-[var(--text-secondary)]">{{ $t('common.loading') }}</p>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { templateEditorApi } from '@/services/api'
import LoadingSpinner from '@/components/ui/LoadingSpinner.vue'

const route = useRoute()
const router = useRouter()
const id = route.params.id

onMounted(async () => {
  try {
    const { data } = await templateEditorApi.list()
    const list = Array.isArray(data) ? data : data?.results ?? []
    const categoryId = Number(id)
    const template = list.find(
      (t) => t.category === categoryId || t.category_id === categoryId
    )
    if (template?.id) {
      router.replace({ path: `/templates/${template.id}/editor` })
    } else {
      router.replace({ path: '/templates/new', query: { category_id: id } })
    }
  } catch {
    router.replace({ path: '/templates', query: { category_id: id } })
  }
})
</script>
