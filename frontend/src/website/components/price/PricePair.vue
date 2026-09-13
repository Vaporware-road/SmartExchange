<template>
  <span class="ws-pair">
    <img v-if="icon" class="ws-pair__icon" :src="icon" :alt="row.from || row.name" />
    <span class="ws-pair__text">
      <span class="ws-pair__name">{{ label }}</span>
      <span v-if="row.from && row.to" class="ws-pair__codes ws-num">{{ row.from }} → {{ row.to }}</span>
    </span>
  </span>
</template>

<script setup>
import { computed } from 'vue'
import { getCurrencyIconByCode } from '@/utils/categoryIcons.js'

const props = defineProps({
  row: { type: Object, required: true },
  showIcon: { type: Boolean, default: true },
})

const icon = computed(() => (props.showIcon ? getCurrencyIconByCode(props.row.from) : null))
const label = computed(() => props.row.name || `${props.row.from}/${props.row.to}`)
</script>

<style scoped>
.ws-pair {
  display: inline-flex;
  align-items: center;
  gap: 0.7em;
  min-width: 0;
}

.ws-pair__icon {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  flex: none;
}

.ws-pair__text {
  display: flex;
  flex-direction: column;
  min-width: 0;
}

.ws-pair__name {
  font-weight: 600;
  color: var(--ws-heading);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.ws-pair__codes {
  font-size: 0.76em;
  color: var(--ws-text-muted);
  letter-spacing: 0.04em;
}
</style>
