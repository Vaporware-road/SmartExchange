<template>
  <label class="inline-flex w-full items-center justify-between gap-3" :class="{ 'cursor-not-allowed opacity-60': disabled }">
    <span v-if="label || $slots.default" class="text-sm text-[var(--text-primary)]">
      <slot>{{ label }}</slot>
    </span>
    <button
      type="button"
      role="switch"
      class="control-switch"
      :data-on="isOn ? 'true' : 'false'"
      :data-size="size"
      :aria-checked="isOn ? 'true' : 'false'"
      :aria-label="ariaLabel || label || undefined"
      :disabled="disabled"
      @click="toggle"
    >
      <span class="control-switch-thumb" />
    </button>
  </label>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  modelValue: {
    type: Boolean,
    default: false,
  },
  disabled: {
    type: Boolean,
    default: false,
  },
  label: {
    type: String,
    default: '',
  },
  ariaLabel: {
    type: String,
    default: '',
  },
  size: {
    type: String,
    default: 'md',
    validator: (v) => ['sm', 'md'].includes(v),
  },
})

const emit = defineEmits(['update:modelValue'])

const isOn = computed(() => Boolean(props.modelValue))

function toggle() {
  if (props.disabled) return
  emit('update:modelValue', !isOn.value)
}
</script>
