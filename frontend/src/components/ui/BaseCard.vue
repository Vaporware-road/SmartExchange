<template>
  <div
    class="base-card rounded-2xl transition-all duration-300 ease-in-out"
    :class="[
      paddingClasses[padding],
      variantClasses[variant],
      { 'hover:shadow-glow hover:border-[rgba(255,215,0,0.4)]': hover && variant === 'default' },
      { 'hover:scale-[1.01] hover:shadow-lg': hover && variant === 'elevated' },
    ]"
  >
    <slot />
  </div>
</template>

<script setup>
defineProps({
  padding: {
    type: String,
    default: 'default',
    validator: (v) => ['none', 'sm', 'default', 'lg'].includes(v),
  },
  hover: {
    type: Boolean,
    default: true,
  },
  variant: {
    type: String,
    default: 'default',
    validator: (v) => ['default', 'glass', 'elevated'].includes(v),
  },
})

const paddingClasses = {
  none: 'p-0',
  sm: 'p-4',
  default: 'p-6',
  lg: 'p-8',
}

const variantClasses = {
  default: 'bg-[var(--bg-card)] border border-[var(--border-card)] shadow-soft',
  glass: 'glass',
  elevated: 'bg-[var(--bg-elevated)] border border-[var(--border-card)] shadow-card',
}
</script>
