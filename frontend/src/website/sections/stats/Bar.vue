<template>
  <section class="ws-section ws-section--tight ws-stats-bar">
    <div class="ws-container">
      <h2 v-if="title" class="ws-h2 ws-stats-bar__title">{{ title }}</h2>
      <dl class="ws-stats-bar__row">
        <div v-for="(item, i) in items" :key="i">
          <dt class="ws-num">{{ item.value }}<span v-if="item.suffix">{{ item.suffix }}</span></dt>
          <dd>{{ t(item.label) }}</dd>
        </div>
      </dl>
    </div>
  </section>
</template>

<script setup>
import { computed } from 'vue'
import { useSiteContext } from '../../composables/useSiteContext.js'

const props = defineProps({ content: { type: Object, default: () => ({}) } })
const { t } = useSiteContext()
const title = computed(() => t(props.content.title))
const items = computed(() => props.content.items || [])
</script>

<style scoped>
.ws-stats-bar__title {
  text-align: center;
  margin-bottom: 30px;
}

.ws-stats-bar__row {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  gap: 32px;
  margin: 0;
  padding: 30px 0;
  border-block: 1px solid var(--ws-border);
}

.ws-stats-bar__row > div {
  text-align: center;
}

dt {
  font-family: var(--ws-font-heading);
  font-weight: var(--ws-heading-weight);
  color: var(--ws-primary);
  font-size: clamp(1.8rem, 1.3rem + 2cqi, 3rem);
  line-height: 1.1;
}

dd {
  margin: 6px 0 0;
  color: var(--ws-text-muted);
  font-size: 0.92rem;
}
</style>
