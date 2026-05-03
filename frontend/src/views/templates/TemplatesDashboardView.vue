<template>
  <div>
    <div class="mb-6 flex flex-col gap-3 md:flex-row md:items-center md:justify-between">
      <h1 class="min-w-0 text-2xl font-bold text-gold">{{ $t('routes.templates') }}</h1>
      <div class="flex w-full shrink-0 flex-col gap-2 sm:flex-row sm:justify-end md:w-auto">
        <router-link
          to="/templates/media"
          class="btn-luxury-outline inline-flex w-full items-center justify-center gap-2 sm:w-auto"
        >
          <i class="fas fa-images"></i>
          {{ $t('routes.templateMediaLibrary') }}
        </router-link>
        <router-link
          to="/templates/new"
          class="btn-luxury inline-flex w-full items-center justify-center gap-2 sm:w-auto"
        >
          <i class="fas fa-plus"></i> Add Template
        </router-link>
      </div>
    </div>

    <!-- Loading: vertical card skeletons -->
    <div v-if="loading" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
      <div
        v-for="i in 8"
        :key="i"
        class="rounded-2xl overflow-hidden border border-[var(--border-card)] bg-[var(--bg-card)]"
      >
        <BaseSkeleton variant="card" class="!h-40 !rounded-none" />
        <div class="p-4 space-y-2">
          <BaseSkeleton variant="text" class="!max-w-[80%] !h-5" />
          <BaseSkeleton variant="text" class="!max-w-[120px] !h-8" />
        </div>
      </div>
    </div>

    <!-- Empty state -->
    <div
      v-else-if="!templates || !templates.length"
      class="card-luxury p-12 text-center"
    >
      <p class="text-[var(--text-secondary)] mb-4">{{ $t('emptyState.noTemplates') || 'No templates yet.' }}</p>
      <router-link to="/templates/new" class="btn-luxury">
        <i class="fas fa-plus"></i> Add Template
      </router-link>
    </div>

    <!-- Template cards: vertical layout with preview + details -->
    <div
      v-else
      class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4"
    >
      <div
        v-for="(t, index) in templates"
        :key="t.id"
        class="template-card group rounded-2xl overflow-hidden border border-[var(--border-card)] bg-[var(--bg-card)] shadow-[var(--shadow-card)] transition-all duration-300 hover:border-[var(--border-card-hover)] hover:shadow-glow"
        :style="{ animationDelay: `${index * 0.04}s` }"
      >
        <!-- Preview: Telegram bubble + frosted glass + blurred lines + gold vars -->
        <div class="template-card-preview relative h-40 overflow-hidden bg-[var(--bg-base)]">
          <div
            class="absolute inset-2 flex items-center justify-center rounded-2xl transition-transform duration-300 group-hover:scale-[1.02]"
            :class="telegramBubbleClass"
          >
            <div
              class="absolute inset-0 rounded-2xl template-preview-glass flex flex-col justify-center px-3 py-2"
            >
              <!-- Blurred placeholder lines -->
              <div
                v-for="j in 4"
                :key="'line-' + j"
                class="h-2.5 rounded w-full mb-1.5 opacity-60"
                style="background: var(--text-secondary); filter: blur(2px);"
              />
              <!-- Gold variable keys from config -->
              <div class="flex flex-wrap gap-1.5 mt-1">
                <span
                  v-for="key in getPreviewVariableKeys(t)"
                  :key="key"
                  class="text-xs font-medium text-gold"
                >
                  {{ key }}
                </span>
              </div>
            </div>
            <!-- Badge: category / special_price_type / Default -->
            <span
              class="absolute top-2 end-2 px-2 py-0.5 rounded-lg text-xs font-medium border backdrop-blur-sm template-badge"
            >
              {{ getTemplateBadgeLabel(t) }}
            </span>
          </div>
        </div>

        <!-- Details: name, platform icon, actions -->
        <div class="template-card-details p-4 flex flex-col gap-3">
          <div class="flex items-center gap-2 min-w-0">
            <i class="fab fa-telegram text-lg text-[var(--primary)] shrink-0" />
            <span class="font-semibold text-gold truncate" :title="t.name">
              {{ t.name ?? `Template ${t.id}` }}
            </span>
          </div>
          <router-link
            :to="`/templates/${t.id}/editor`"
            class="btn-luxury-outline text-sm py-2 w-full sm:w-auto"
          >
            <i class="fas fa-edit"></i> Editor
          </router-link>
          <button
            type="button"
            class="btn-luxury-outline text-sm py-2 w-full sm:w-auto !border-rose-500/50 !text-rose-400 hover:!bg-rose-500/10"
            :disabled="deletingId === t.id"
            @click="deleteTemplate(t)"
          >
            <i class="fas fa-trash"></i>
            {{ deletingId === t.id ? 'Deleting...' : 'Delete' }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useToast } from 'vue-toastification'
import { getApiErrorDetails, templateEditorApi } from '@/services/api'
import BaseSkeleton from '@/components/ui/BaseSkeleton.vue'

const loading = ref(true)
const templates = ref([])
const deletingId = ref(null)
const toast = useToast()

/** Extract up to 5 variable_key values from config (themes or legacy fields) for preview. */
function getPreviewVariableKeys(template) {
  const cj = template?.config_json
  if (cj && typeof cj === 'object' && Array.isArray(cj.widgets) && cj.widgets.length) {
    return cj.widgets
      .slice(0, 5)
      .map((w) => w?.name || w?.type)
      .filter(Boolean)
  }
  const config = template?.config
  if (!config) return ['$PRICE']
  const themes = config.themes
  if (themes && typeof themes === 'object') {
    const firstThemeName = Object.keys(themes)[0]
    const theme = firstThemeName ? themes[firstThemeName] : null
    const layers = theme?.layers
    if (Array.isArray(layers) && layers.length) {
      return layers
        .slice(0, 5)
        .map((l) => l?.variable_key)
        .filter(Boolean)
    }
  }
  const fields = config.fields
  if (fields && typeof fields === 'object') {
    return Object.keys(fields).slice(0, 5)
  }
  return ['$PRICE']
}

/** Badge label: category_name or fallback id label. */
function getTemplateBadgeLabel(template) {
  if (template?.category_name) return template.category_name
  if (template?.category) return `Category #${template.category}`
  return 'Unassigned'
}

/** Telegram bubble background: subtle green/blue tint (sent message style). */
const telegramBubbleClass =
  'bg-[#2AABEE]/20 dark:bg-[#229ED9]/25 border border-[var(--glass-border)]'

async function deleteTemplate(template) {
  if (!template?.id || deletingId.value != null) return
  const name = String(template?.name ?? '').trim() || `Template #${template.id}`
  const confirmed = window.confirm(
    `Are you sure you want to delete "${name}"?\nThis action cannot be undone.`
  )
  if (!confirmed) return

  deletingId.value = template.id
  try {
    await templateEditorApi.delete(template.id)
    templates.value = templates.value.filter((t) => t.id !== template.id)
    toast.success('Template deleted successfully.')
  } catch (error) {
    toast.error(getApiErrorDetails(error).message)
  } finally {
    deletingId.value = null
  }
}

onMounted(async () => {
  try {
    const { data } = await templateEditorApi.list()
    templates.value = Array.isArray(data) ? data : (data?.results ?? data ?? [])
  } catch {
    templates.value = []
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
.template-preview-glass {
  background: var(--glass-bg);
  backdrop-filter: blur(16px) saturate(180%);
  -webkit-backdrop-filter: blur(16px) saturate(180%);
  border: 1px solid var(--glass-border);
}

.template-badge {
  background: rgba(255, 255, 255, 0.2);
  border-color: var(--border-card-hover);
  color: var(--primary);
}

.dark .template-badge {
  background: rgba(0, 0, 0, 0.3);
  border-color: var(--border-card-hover);
}
</style>
