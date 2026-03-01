<template>
  <div>
    <nav class="mb-6">
      <router-link
        :to="'/categories'"
        class="inline-flex items-center gap-2 text-[var(--text-secondary)] hover:text-gold transition-colors font-medium"
      >
        <i class="fas" :class="isRtl ? 'fa-arrow-right' : 'fa-arrow-left'" />
        <span>{{ $t('telegramStudio.backToCategories') || 'Back to Categories' }}</span>
      </router-link>
    </nav>

    <div v-if="loading" class="card-luxury p-8 flex items-center justify-center min-h-[200px]">
      <LoadingSpinner class="w-10 h-10 text-gold" />
    </div>

    <template v-else-if="category">
      <h1 class="text-2xl font-bold text-gold mb-2 animate-fade-in-up">
        {{ $t('telegramStudio.title') || 'Telegram Message Studio' }}
      </h1>
      <p class="text-[var(--text-secondary)] mb-6">
        {{ category.name }}
      </p>

      <!-- Incomplete message warning -->
      <div
        v-if="isIncomplete"
        class="mb-6 rounded-xl border px-4 py-3 text-sm flex items-center gap-2 border-[var(--border-card-hover)] bg-primary-muted text-[var(--text-primary)]"
      >
        <i class="fas fa-exclamation-triangle shrink-0 text-gold" />
        <span>{{ $t('telegramStudio.incompleteMessage') || 'Media or message description is not set. The Telegram message may appear incomplete.' }}</span>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 md:gap-8 items-start">
        <!-- Left: Form sections (first on mobile) -->
        <div class="space-y-6 animate-fade-in-up order-1 lg:order-1">
          <!-- Section 1: Media -->
          <section class="card-luxury overflow-hidden">
            <div
              class="flex items-center gap-3 pb-4 mb-4 border-b"
              style="border-color: var(--border-card);"
            >
              <span
                class="flex items-center justify-center w-10 h-10 rounded-xl shrink-0 bg-primary-muted text-[var(--primary)]"
              >
                <i class="fas fa-image" />
              </span>
              <h2 class="text-lg font-semibold text-gold m-0">
                {{ $t('telegramStudio.media') || 'Media' }}
              </h2>
            </div>
            <div class="flex flex-col sm:flex-row gap-4 items-start">
              <div
                class="w-full sm:w-40 h-32 rounded-xl border-2 border-dashed flex items-center justify-center overflow-hidden cursor-pointer transition-colors hover:border-gold/50"
                style="border-color: var(--border-card); background: var(--bg-input);"
                @click="fileInput?.click()"
              >
                <img
                  v-if="form.telegram_media_url"
                  :src="form.telegram_media_url"
                  alt=""
                  class="w-full h-full object-cover"
                />
                <span v-else class="text-sm text-[var(--text-secondary)] px-2 text-center">
                  {{ $t('telegramStudio.uploadImage') || 'Click to upload' }}
                </span>
              </div>
              <div class="flex-1 min-w-0">
                <p class="text-sm text-[var(--text-secondary)] mb-2">
                  {{ $t('telegramStudio.mediaHint') || 'Image for the Telegram message.' }}
                </p>
                <button
                  type="button"
                  class="btn-luxury-outline text-sm py-2"
                  :disabled="uploadingMedia"
                  @click="fileInput?.click()"
                >
                  <LoadingSpinner v-if="uploadingMedia" class="w-4 h-4 inline-block me-2" />
                  {{ uploadingMedia ? ($t('telegramStudio.uploading') || 'Uploading…') : ($t('telegramStudio.changeImage') || 'Change image') }}
                </button>
              </div>
            </div>
            <input
              ref="fileInput"
              type="file"
              accept="image/*"
              class="hidden"
              @change="onFileSelect"
            />
          </section>

          <!-- Section 2: Description -->
          <section class="card-luxury overflow-hidden">
            <div
              class="flex items-center justify-between gap-2 flex-wrap pb-4 mb-4 border-b"
              style="border-color: var(--border-card);"
            >
              <div class="flex items-center gap-3">
                <span
                  class="flex items-center justify-center w-10 h-10 rounded-xl shrink-0 bg-primary-muted text-[var(--primary)]"
                >
                  <i class="fas fa-align-left" />
                </span>
                <h2 class="text-lg font-semibold text-gold m-0">
                  {{ $t('telegramStudio.description') || 'Description' }}
                </h2>
              </div>
              <div class="relative">
                <button
                  type="button"
                  class="btn-luxury-outline text-sm py-1.5 px-3 gap-1"
                  :title="$t('telegramStudio.insertVariable') || 'Insert variable'"
                  @click="showVariableMenu = !showVariableMenu"
                >
                  <i class="fas fa-braces" />
                  <span class="hidden sm:inline">{{ $t('telegramStudio.insertVariable') || 'Insert variable' }}</span>
                </button>
                <div
                  v-if="showVariableMenu"
                  class="absolute top-full end-0 mt-1 z-20 min-w-[200px] rounded-xl border shadow-lg py-2 max-h-60 overflow-y-auto"
                  style="border-color: var(--border-card); background: var(--bg-card);"
                >
                  <p class="px-3 py-1 text-xs text-[var(--text-secondary)]">
                    {{ $t('telegramStudio.priceTypes') || 'Price types' }}
                  </p>
                  <button
                    v-for="pt in (category.price_types || [])"
                    :key="pt.id"
                    type="button"
                    class="w-full text-start px-3 py-2 text-sm transition-colors hover:bg-[var(--bg-hover)]"
                    style="color: var(--text-primary);"
                    @click="insertVariable(pt.slug || pt.name)"
                  >
                    {{ pt.name }} — <code class="text-gold">{{ variableCode(pt) }}</code>
                  </button>
                  <p v-if="!(category.price_types || []).length" class="px-3 py-2 text-sm text-[var(--text-secondary)]">
                    {{ $t('telegramStudio.noPriceTypes') || 'No price types in this category.' }}
                  </p>
                </div>
              </div>
            </div>
            <textarea
              ref="descriptionTextarea"
              v-model="form.telegram_message_description"
              class="input-luxury min-h-[120px] resize-y"
              :placeholder="$t('telegramStudio.descriptionPlaceholder') || 'Message text under the image…'"
            />
          </section>

          <!-- Section 3: Inline Buttons -->
          <section class="card-luxury overflow-hidden">
            <div
              class="flex items-center gap-3 pb-4 mb-4 border-b"
              style="border-color: var(--border-card);"
            >
              <span
                class="flex items-center justify-center w-10 h-10 rounded-xl shrink-0 bg-primary-muted text-[var(--primary)]"
              >
                <i class="fas fa-th-large" />
              </span>
              <h2 class="text-lg font-semibold text-gold m-0">
                {{ $t('telegramStudio.inlineButtons') || 'Inline buttons' }}
              </h2>
            </div>
            <div class="space-y-2">
              <div
                v-for="(btn, idx) in form.inline_buttons"
                :key="idx"
                class="flex flex-wrap gap-2 items-center p-3 rounded-xl"
                style="background: var(--bg-input); border: 1px solid var(--border-card);"
              >
                <input
                  v-model="btn.label"
                  type="text"
                  class="input-luxury flex-1 min-w-[100px] py-2"
                  :placeholder="$t('telegramStudio.buttonLabel') || 'Label'"
                />
                <input
                  v-model="btn.url"
                  type="url"
                  class="input-luxury flex-1 min-w-[120px] py-2"
                  :placeholder="$t('telegramStudio.buttonUrl') || 'URL'"
                />
                <button
                  type="button"
                  class="btn-luxury-outline p-2 border-red-500/50 text-red-400 hover:bg-red-500/10 shrink-0"
                  :aria-label="$t('common.delete')"
                  @click="removeButton(idx)"
                >
                  <i class="fas fa-trash" />
                </button>
              </div>
            </div>
            <button
              type="button"
              class="btn-luxury-outline text-sm py-2 w-full mt-3"
              @click="addButton"
            >
              <i class="fas fa-plus me-2" />
              {{ $t('telegramStudio.addButton') || 'Add button' }}
            </button>
          </section>

          <!-- Save -->
          <div class="flex justify-end pt-2">
            <button
              type="button"
              class="btn-luxury px-8 py-3 text-lg gap-2"
              :class="{ 'opacity-80 pointer-events-none': saving }"
              :disabled="saving"
              @click="save"
            >
              <LoadingSpinner v-if="saving" class="w-5 h-5" />
              <i v-else class="fas fa-check-double" />
              <span>{{ saving ? ($t('telegramStudio.saving') || 'Saving…') : ($t('telegramStudio.saveSync') || 'Save & Sync') }}</span>
            </button>
          </div>
        </div>

        <!-- Right: Live Preview (below form on mobile) -->
        <div class="lg:sticky lg:top-6 order-2 lg:order-2">
          <div
            class="card-luxury p-5 border-2 border-[var(--border-card-hover)] shadow-glow"
          >
            <div
              class="flex items-center gap-2 mb-4 pb-3 border-b"
              style="border-color: var(--border-card);"
            >
              <i class="fas fa-mobile-alt text-gold" />
              <h2 class="text-lg font-semibold text-gold m-0">
                {{ $t('telegramStudio.livePreview') || 'Live preview' }}
              </h2>
            </div>
            <TelegramMockup
              :image-url="form.telegram_media_url"
              :description="form.telegram_message_description"
              :buttons="validButtons"
              :variable-values="variableValues"
            />
          </div>
        </div>
      </div>
    </template>

    <div v-else class="card-luxury p-8 text-center text-[var(--text-secondary)]">
      {{ $t('telegramStudio.categoryNotFound') || 'Category not found.' }}
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, nextTick } from 'vue'
import { useRoute } from 'vue-router'
import { useToast } from 'vue-toastification'
import { useI18n } from 'vue-i18n'
import { categoryApi } from '@/services/api'
import LoadingSpinner from '@/components/ui/LoadingSpinner.vue'
import TelegramMockup from '@/components/telegram/TelegramMockup.vue'

const route = useRoute()
const toast = useToast()
const { t } = useI18n()

const categoryId = computed(() => route.params.id)
const isRtl = computed(() => document.documentElement.dir === 'rtl')
const loading = ref(true)
const category = ref(null)
const form = ref({
  telegram_message_description: '',
  telegram_media_url: '',
  inline_buttons: [],
})
const showVariableMenu = ref(false)
const fileInput = ref(null)
const descriptionTextarea = ref(null)
const uploadingMedia = ref(false)
const saving = ref(false)

const validButtons = computed(() =>
  (form.value.inline_buttons || []).filter((b) => b && (b.label || b.url)).map((b) => ({ label: b.label || '', url: b.url || '' }))
)

const isIncomplete = computed(() => {
  const hasMedia = !!form.value.telegram_media_url?.trim()
  const hasDescription = !!form.value.telegram_message_description?.trim()
  return !hasMedia || !hasDescription
})

const variableValues = computed(() => {
  const out = {}
  const pts = category.value?.price_types || []
  pts.forEach((pt) => {
    const key = pt.slug || pt.name
    if (key) out[key] = pt.latest_price != null ? String(pt.latest_price) : '—'
  })
  return out
})

onMounted(async () => {
  await loadCategory()
})

async function loadCategory() {
  loading.value = true
  try {
    const { data } = await categoryApi.get(categoryId.value)
    category.value = data
    form.value = {
      telegram_message_description: data.telegram_message_description ?? '',
      telegram_media_url: data.telegram_media_url ?? '',
      inline_buttons: Array.isArray(data.inline_buttons)
        ? data.inline_buttons.map((b) => ({ label: b?.label ?? '', url: b?.url ?? '' }))
        : [],
    }
  } catch {
    category.value = null
  } finally {
    loading.value = false
  }
}

function insertVariable(slugOrName) {
  const code = `{{${slugOrName}}}`
  const ta = descriptionTextarea.value
  if (ta) {
    const start = ta.selectionStart
    const end = ta.selectionEnd
    const text = form.value.telegram_message_description
    form.value.telegram_message_description = text.slice(0, start) + code + text.slice(end)
    nextTick(() => {
      ta.focus()
      ta.setSelectionRange(start + code.length, start + code.length)
    })
  } else {
    form.value.telegram_message_description = (form.value.telegram_message_description || '') + code
  }
  showVariableMenu.value = false
}

function variableCode(pt) {
  return `{{${pt.slug || pt.name}}}`
}

function addButton() {
  if (!form.value.inline_buttons) form.value.inline_buttons = []
  form.value.inline_buttons.push({ label: '', url: '' })
}

function removeButton(idx) {
  form.value.inline_buttons.splice(idx, 1)
}

async function onFileSelect(e) {
  const file = e.target?.files?.[0]
  if (!file || !categoryId.value) return
  uploadingMedia.value = true
  try {
    const fd = new FormData()
    fd.append('file', file)
    const { data } = await categoryApi.uploadTelegramMedia(categoryId.value, fd)
    if (data?.url) {
      form.value.telegram_media_url = data.url
      toast.success(t('toast.saveSuccess'))
    }
  } catch (err) {
    toast.error(err.response?.data?.detail || t('toast.serverError'))
  } finally {
    uploadingMedia.value = false
    e.target.value = ''
  }
}

async function save() {
  saving.value = true
  try {
    await categoryApi.patch(categoryId.value, {
      telegram_message_description: form.value.telegram_message_description || null,
      telegram_media_url: form.value.telegram_media_url || '',
      inline_buttons: form.value.inline_buttons.filter((b) => b && (b.label || b.url)),
    })
    toast.success(t('toast.saveSuccess'))
  } catch (err) {
    toast.error(err.response?.data?.detail || t('toast.serverError'))
  } finally {
    saving.value = false
  }
}
</script>
