<template>
  <div class="flex flex-col items-center justify-center py-20">
    <LoadingSpinner class="w-10 h-10 text-[var(--primary)] mb-4" />
    <p class="text-[var(--text-secondary)]">{{ $t('common.loading') }}</p>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { specialPriceApi, templateEditorApi } from '@/services/api'
import LoadingSpinner from '@/components/ui/LoadingSpinner.vue'

const route = useRoute()
const router = useRouter()
const id = route.params.id

onMounted(async () => {
  const specialPriceTypeId = Number(id)
  if (!Number.isFinite(specialPriceTypeId)) {
    router.replace({ path: '/templates' })
    return
  }

  try {
    const { data: listRes } = await templateEditorApi.list()
    const list = Array.isArray(listRes) ? listRes : listRes?.results ?? []
    const existing = list.find(
      (t) =>
        t.special_price_type === specialPriceTypeId ||
        t.special_price_type_id === specialPriceTypeId
    )
    if (existing?.id) {
      router.replace({ path: `/templates/${existing.id}/editor` })
      return
    }

    const { data: spt } = await specialPriceApi.get(specialPriceTypeId)
    const name = String(spt?.name ?? '').trim()
    if (!name) {
      router.replace({ path: '/templates/new', query: { specialPriceTypeId: id } })
      return
    }

    const { data: created } = await templateEditorApi.create({
      name,
      special_price_type: specialPriceTypeId,
    })
    if (created?.id) {
      router.replace({ path: `/templates/${created.id}/editor` })
      return
    }

    router.replace({ path: '/templates/new', query: { specialPriceTypeId: id } })
  } catch {
    router.replace({ path: '/templates', query: { specialPriceTypeId: id } })
  }
})
</script>
