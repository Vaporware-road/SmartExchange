<template>
  <footer class="ws-footer">
    <div class="ws-container ws-footer__simple">
      <WsLogo with-name />
      <WsSocials v-if="content.show_socials !== false" />
      <p class="ws-footer__copy">{{ copyright }}</p>
    </div>
    <p v-if="disclaimer" class="ws-container ws-footer__disclaimer">{{ disclaimer }}</p>
  </footer>
</template>

<script setup>
import WsLogo from '../../primitives/WsLogo.vue'
import WsSocials from '../../primitives/WsSocials.vue'
import { useFooter } from './_footer.js'

const props = defineProps({ content: { type: Object, default: () => ({}) } })
const { copyright, disclaimer } = useFooter(props)
</script>

<style scoped>
.ws-footer__simple {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 20px;
  padding-block: 34px;
}

.ws-footer__copy {
  margin: 0;
  color: var(--ws-text-muted);
  font-size: 0.85rem;
}
</style>
