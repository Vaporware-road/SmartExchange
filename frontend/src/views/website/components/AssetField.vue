<template>
  <div class="wb-asset">
    <button type="button" class="wb-asset__preview" @click="open = true">
      <img v-if="modelValue" :src="modelValue" alt="" />
      <span v-else><i class="fas fa-image" /> {{ $t('website.builder.chooseImage') }}</span>
    </button>
    <button v-if="modelValue" type="button" class="wb-asset__clear" @click="$emit('update:modelValue', '')">
      <i class="fas fa-xmark" />
    </button>

    <BaseModal v-model="open" :title="$t('website.builder.imageLibrary')">
      <div class="wb-asset__upload">
        <label class="btn-luxury">
          <i class="fas fa-upload" /> {{ $t('website.builder.upload') }}
          <input type="file" accept="image/*" hidden @change="upload" />
        </label>
        <span v-if="uploading" class="wb-asset__busy"><i class="fas fa-circle-notch fa-spin" /></span>
        <p v-if="uploadError" class="wb-asset__error">{{ uploadError }}</p>
      </div>

      <div v-if="store.assets.length" class="wb-asset__grid">
        <button
          v-for="asset in store.assets"
          :key="asset.id"
          type="button"
          class="wb-asset__tile"
          :class="{ 'is-active': asset.url === modelValue }"
          @click="pick(asset)"
        >
          <img :src="asset.url" alt="" />
          <span class="wb-asset__remove" @click.stop="remove(asset)"><i class="fas fa-trash" /></span>
        </button>
      </div>
      <EmptyState v-else title-key="website.builder.noImages" icon="fas fa-image" />
    </BaseModal>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useI18n } from 'vue-i18n'
import BaseModal from '@/components/ui/BaseModal.vue'
import EmptyState from '@/components/ui/EmptyState.vue'
import { useWebsiteStore } from '@/stores/website'

/** Picks an image the owner already uploaded, or uploads a new one. */
defineProps({ modelValue: { type: String, default: '' } })
const emit = defineEmits(['update:modelValue'])

const { t } = useI18n()
const store = useWebsiteStore()
const open = ref(false)
const uploading = ref(false)
const uploadError = ref('')

onMounted(() => {
  if (!store.assets.length) store.loadAssets().catch(() => {})
})

function pick(asset) {
  emit('update:modelValue', asset.url)
  open.value = false
}

async function upload(event) {
  const file = event.target.files?.[0]
  event.target.value = ''
  if (!file) return
  uploading.value = true
  uploadError.value = ''
  try {
    const asset = await store.uploadAsset(file)
    pick(asset)
  } catch (err) {
    uploadError.value = err?.message || t('website.builder.uploadFailed')
  } finally {
    uploading.value = false
  }
}

async function remove(asset) {
  await store.deleteAsset(asset.id)
}
</script>

<style scoped>
.wb-asset {
  display: flex;
  align-items: center;
  gap: 8px;
}

.wb-asset__preview {
  flex: 1;
  min-height: 64px;
  border: 1px dashed var(--border-card);
  border-radius: 10px;
  background: var(--bg-input);
  color: var(--text-secondary);
  cursor: pointer;
  overflow: hidden;
  padding: 0;
  display: grid;
  place-items: center;
  font-size: 0.85rem;
}

.wb-asset__preview img {
  width: 100%;
  max-height: 130px;
  object-fit: contain;
}

.wb-asset__clear {
  border: 1px solid var(--border-card);
  background: transparent;
  color: var(--text-secondary);
  border-radius: 8px;
  width: 32px;
  height: 32px;
  cursor: pointer;
}

.wb-asset__upload {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 16px;
}

.wb-asset__upload label {
  cursor: pointer;
}

.wb-asset__error {
  color: var(--color-sell, #f43f5e);
  font-size: 0.82rem;
  margin: 0;
}

.wb-asset__grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(112px, 1fr));
  gap: 10px;
  max-height: 46vh;
  overflow-y: auto;
}

.wb-asset__tile {
  position: relative;
  aspect-ratio: 1;
  border: 2px solid transparent;
  border-radius: 10px;
  overflow: hidden;
  background: var(--bg-input);
  cursor: pointer;
  padding: 0;
}

.wb-asset__tile.is-active {
  border-color: var(--primary);
}

.wb-asset__tile img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.wb-asset__remove {
  position: absolute;
  top: 5px;
  inset-inline-end: 5px;
  width: 26px;
  height: 26px;
  display: grid;
  place-items: center;
  border-radius: 7px;
  background: rgba(0, 0, 0, 0.55);
  color: #fff;
  font-size: 0.72rem;
  opacity: 0;
  transition: opacity 0.15s ease;
}

.wb-asset__tile:hover .wb-asset__remove {
  opacity: 1;
}
</style>
