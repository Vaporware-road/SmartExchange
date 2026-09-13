<template>
  <footer class="ws-footer ws-footer--rich">
    <div class="ws-container">
      <div class="ws-footer__lead">
        <WsLogo with-name />
        <p v-if="about" class="ws-lead">{{ about }}</p>
      </div>

      <hr class="ws-divider" />

      <div class="ws-footer__grid">
        <nav v-for="(column, i) in columns" :key="i" class="ws-footer__col">
          <h3>{{ t(column.title) }}</h3>
          <a v-for="(link, j) in column.links || []" :key="j" :href="link.href">{{ t(link.label) }}</a>
        </nav>
        <div class="ws-footer__contact">
          <WsContactLines :contact="branding.contact || {}" />
          <WsSocials v-if="content.show_socials !== false" />
        </div>
      </div>

      <div class="ws-footer__bar">
        <p>{{ copyright }}</p>
        <p v-if="disclaimer" class="ws-footer__disclaimer">{{ disclaimer }}</p>
      </div>
    </div>
  </footer>
</template>

<script setup>
import WsLogo from '../../primitives/WsLogo.vue'
import WsSocials from '../../primitives/WsSocials.vue'
import WsContactLines from '../../primitives/WsContactLines.vue'
import { useSiteContext } from '../../composables/useSiteContext.js'
import { useFooter } from './_footer.js'

const props = defineProps({ content: { type: Object, default: () => ({}) } })
const { branding } = useSiteContext()
const { t, about, columns, copyright, disclaimer } = useFooter(props)
</script>

<style scoped>
.ws-footer__lead {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 26px;
  padding-block: calc(var(--ws-section-gap) * 0.5) 28px;
}

.ws-footer__lead :deep(.ws-logo) {
  font-size: 1.35rem;
}

.ws-footer__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
  gap: calc(var(--ws-block-gap) * 1.3);
  padding-block: 34px;
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
}

.ws-footer__col a {
  color: var(--ws-text-muted);
  font-size: 0.92rem;
}

.ws-footer__col a:hover {
  color: var(--ws-primary);
}

.ws-footer__contact {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.ws-footer__bar {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
  padding-block: 22px;
  border-top: 1px solid var(--ws-border);
  color: var(--ws-text-muted);
  font-size: 0.82rem;
}

.ws-footer__bar p {
  margin: 0;
}
</style>
