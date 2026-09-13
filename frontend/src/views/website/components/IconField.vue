<template>
  <div class="wb-icon">
    <span class="wb-icon__preview"><i :class="resolved" /></span>
    <input
      class="input-luxury"
      type="text"
      dir="ltr"
      list="ws-icon-suggestions"
      :value="modelValue"
      :placeholder="$t('website.builder.iconPlaceholder')"
      @input="$emit('update:modelValue', $event.target.value)"
    />
    <datalist id="ws-icon-suggestions">
      <option v-for="name in SUGGESTIONS" :key="name" :value="name" />
    </datalist>
  </div>
</template>

<script setup>
import { computed } from 'vue'

/**
 * A plain Font Awesome name with a live preview, rather than a picker grid:
 * the shell already loads the whole icon set, and a datalist of the icons an
 * exchange actually uses covers the common cases without a modal.
 */
const props = defineProps({ modelValue: { type: String, default: '' } })
defineEmits(['update:modelValue'])

const SUGGESTIONS = [
  'money-bill-transfer', 'coins', 'sack-dollar', 'building-columns', 'shield-halved',
  'bolt', 'clock', 'globe', 'handshake', 'chart-line', 'lock', 'headset',
  'location-dot', 'plane', 'credit-card', 'receipt', 'user-tie', 'star',
]

const resolved = computed(() => {
  const name = (props.modelValue || '').trim()
  if (!name) return 'fas fa-circle-question'
  return name.includes('fa-') ? name : `fas fa-${name}`
})
</script>

<style scoped>
.wb-icon {
  display: flex;
  align-items: center;
  gap: 8px;
}

.wb-icon__preview {
  width: 40px;
  height: 40px;
  flex: none;
  display: grid;
  place-items: center;
  border-radius: 9px;
  background: var(--bg-input);
  border: 1px solid var(--border-card);
  color: var(--primary);
}

.wb-icon input {
  flex: 1;
  min-width: 0;
}
</style>
