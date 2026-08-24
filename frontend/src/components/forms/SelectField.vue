<template>
  <div class="min-w-0 w-full">
    <label
      v-if="label"
      :for="id"
      class="mb-1.5 block text-sm font-medium text-[var(--text-primary)]"
    >
      {{ label }}
      <span v-if="required" class="text-red-500">*</span>
    </label>
    <div class="relative">
      <select
        :id="id"
        :value="modelValue"
        :disabled="disabled"
        :required="required"
        class="input-luxury w-full appearance-none pe-10 disabled:opacity-60 disabled:cursor-not-allowed"
        :class="{ '!border-red-500 focus:!ring-red-500/20': error }"
        @change="emit('update:modelValue', $event.target.value)"
        @blur="emit('blur')"
      >
        <option v-if="placeholder" value="">{{ placeholder }}</option>
        <option
          v-for="opt in options"
          :key="opt.value"
          :value="opt.value"
          :disabled="opt.disabled"
        >
          {{ opt.label }}
        </option>
      </select>
      <i class="fas fa-chevron-down pointer-events-none absolute end-3 top-1/2 -translate-y-1/2 text-sm text-[var(--text-secondary)]" />
    </div>
    <p
      v-if="error"
      class="mt-1.5 flex items-start gap-1.5 text-sm text-red-500"
      role="alert"
    >
      <i class="fas fa-exclamation-circle mt-0.5 text-xs" />
      <span class="min-w-0 break-words">{{ error }}</span>
    </p>
    <p v-else-if="hint" class="mt-1.5 text-xs text-[var(--text-secondary)]">
      {{ hint }}
    </p>
  </div>
</template>

<script setup>
import { useId } from 'vue'

const props = defineProps({
  modelValue: { type: [String, Number], default: '' },
  label: { type: String, default: '' },
  placeholder: { type: String, default: '' },
  hint: { type: String, default: '' },
  error: { type: String, default: '' },
  required: { type: Boolean, default: false },
  disabled: { type: Boolean, default: false },
  options: {
    type: Array,
    default: () => [],
  },
})

const emit = defineEmits(['update:modelValue', 'blur'])

const id = props.label ? useId() : undefined
</script>
