<template>
  <div class="wb-upload">
    <label class="wb-upload__drop">
      <img v-if="url" :src="url" alt="" />
      <span v-else><i class="fas fa-cloud-arrow-up" /> {{ $t('website.builder.upload') }}</span>
      <input type="file" accept="image/*" hidden :disabled="busy" @change="pick" />
    </label>
    <button v-if="url" type="button" class="wb-upload__clear" @click="clear">
      <i class="fas fa-xmark" /> {{ $t('common.remove') }}
    </button>
    <p v-if="error" class="wb-upload__error">{{ error }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { websiteApi } from '@/services/api'

/**
 * Branding files go straight onto the site row (multipart PATCH) rather than
 * into the image library: there is exactly one logo and one favicon, and
 * putting them in the gallery would invite an owner to "delete" the logo their
 * live site is using.
 */
const props = defineProps({
  url: { type: String, default: '' },
  field: { type: String, required: true },
})
const emit = defineEmits(['uploaded'])

const busy = ref(false)
const error = ref('')

async function pick(event) {
  const file = event.target.files?.[0]
  event.target.value = ''
  if (!file) return
  busy.value = true
  error.value = ''
  try {
    const form = new FormData()
    form.append(props.field, file)
    await websiteApi.updateSite(form)
    emit('uploaded')
  } catch (err) {
    error.value = err?.message || 'upload failed'
  } finally {
    busy.value = false
  }
}

async function clear() {
  const form = new FormData()
  form.append(props.field, '')
  await websiteApi.updateSite(form)
  emit('uploaded')
}
</script>

<style scoped>
.wb-upload {
  display: flex;
  flex-direction: column;
  gap: 7px;
}

.wb-upload__drop {
  display: grid;
  place-items: center;
  min-height: 92px;
  border: 1px dashed var(--border-card);
  border-radius: 11px;
  background: var(--bg-input);
  color: var(--text-secondary);
  font-size: 0.83rem;
  cursor: pointer;
  overflow: hidden;
  padding: 8px;
}

.wb-upload__drop img {
  max-height: 76px;
  max-width: 100%;
  object-fit: contain;
}

.wb-upload__clear {
  align-self: flex-start;
  border: 0;
  background: transparent;
  color: var(--text-secondary);
  font: inherit;
  font-size: 0.78rem;
  cursor: pointer;
  padding: 0;
}

.wb-upload__error {
  margin: 0;
  font-size: 0.78rem;
  color: var(--color-sell, #f43f5e);
}
</style>
