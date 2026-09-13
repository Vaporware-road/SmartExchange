<template>
  <nav class="wb-rail" :aria-label="$t('website.builder.steps')">
    <button
      v-for="step in steps"
      :key="step.key"
      type="button"
      class="wb-rail__item"
      :class="{ 'is-active': step.key === modelValue }"
      @click="$emit('update:modelValue', step.key)"
    >
      <span class="wb-rail__icon"><i :class="step.icon" /></span>
      <span class="wb-rail__text">
        <span class="wb-rail__label">{{ $t(`website.builder.step.${step.key}`) }}</span>
        <span class="wb-rail__hint">{{ $t(`website.builder.hint.${step.key}`) }}</span>
      </span>
    </button>
  </nav>
</template>

<script setup>
defineProps({
  modelValue: { type: String, required: true },
  steps: { type: Array, required: true },
})
defineEmits(['update:modelValue'])
</script>

<style scoped>
.wb-rail {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.wb-rail__item {
  display: flex;
  align-items: center;
  gap: 12px;
  width: 100%;
  padding: 11px 12px;
  border: 1px solid transparent;
  border-radius: 12px;
  background: transparent;
  color: var(--text-secondary);
  text-align: start;
  font: inherit;
  cursor: pointer;
  transition: background 0.18s ease, color 0.18s ease, border-color 0.18s ease;
}

.wb-rail__item:hover {
  background: var(--bg-hover);
  color: var(--text-primary);
}

.wb-rail__item.is-active {
  background: var(--bg-card);
  border-color: var(--border-card);
  color: var(--text-primary);
}

.wb-rail__icon {
  width: 34px;
  height: 34px;
  flex: none;
  display: grid;
  place-items: center;
  border-radius: 9px;
  background: var(--bg-input);
  color: var(--primary);
}

.wb-rail__item.is-active .wb-rail__icon {
  background: var(--primary);
  color: var(--text-on-primary, #fff);
}

.wb-rail__text {
  display: flex;
  flex-direction: column;
  min-width: 0;
}

.wb-rail__label {
  font-weight: 600;
  font-size: 0.92rem;
}

.wb-rail__hint {
  font-size: 0.76rem;
  color: var(--text-secondary);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

@media (max-width: 1100px) {
  .wb-rail {
    flex-direction: row;
    overflow-x: auto;
    gap: 8px;
  }

  .wb-rail__hint {
    display: none;
  }

  .wb-rail__item {
    width: auto;
    white-space: nowrap;
  }
}
</style>
