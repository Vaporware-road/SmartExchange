<template>
  <footer class="ws-footer">
    <div class="ws-container ws-footer__grid">
      <div class="ws-stack ws-footer__brand">
        <WsLogo with-name />
        <p v-if="about" class="ws-body">{{ about }}</p>
        <WsSocials v-if="content.show_socials !== false" />
      </div>
      <nav v-for="(column, i) in columns" :key="i" class="ws-footer__col">
        <h3>{{ t(column.title) }}</h3>
        <a v-for="(link, j) in column.links || []" :key="j" :href="link.href">{{ t(link.label) }}</a>
      </nav>
    </div>
    <div class="ws-container ws-footer__bar">
      <p>{{ copyright }}</p>
      <p v-if="disclaimer" class="ws-footer__disclaimer">{{ disclaimer }}</p>
    </div>
  </footer>
</template>

<script setup>
import WsLogo from '../../primitives/WsLogo.vue'
import WsSocials from '../../primitives/WsSocials.vue'
import { useFooter } from './_footer.js'

const props = defineProps({ content: { type: Object, default: () => ({}) } })
const { t, about, columns, copyright, disclaimer } = useFooter(props)
</script>

<style scoped>
.ws-footer__grid {
  display: grid;
  grid-template-columns: minmax(0, 1.5fr) repeat(auto-fit, minmax(140px, 1fr));
  gap: calc(var(--ws-block-gap) * 1.4);
  padding-block: calc(var(--ws-section-gap) * 0.55) 34px;
}

.ws-footer__brand .ws-body {
  max-width: 42ch;
}

.ws-footer__col {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.ws-footer__col h3 {
  font-size: 0.78rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--ws-text-muted);
  margin-bottom: 4px;
}

.ws-footer__col a {
  color: var(--ws-text-muted);
  font-size: 0.92rem;
}

.ws-footer__col a:hover {
  color: var(--ws-primary);
}

.ws-footer__bar {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
  padding-block: 20px;
  border-top: 1px solid var(--ws-border);
  color: var(--ws-text-muted);
  font-size: 0.82rem;
}

.ws-footer__bar p {
  margin: 0;
}
</style>
