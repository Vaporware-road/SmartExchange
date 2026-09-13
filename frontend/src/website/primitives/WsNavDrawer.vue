<template>
  <Transition name="ws-drawer">
    <div v-if="modelValue" class="ws-drawer">
      <nav>
        <a v-for="(link, i) in links" :key="i" :href="link.href" @click="close">{{ t(link.label) }}</a>
      </nav>
      <WsButton v-if="cta" :href="ctaHref" @click="close">{{ cta }}</WsButton>
      <WsLanguage />
    </div>
  </Transition>
</template>

<script setup>
import WsButton from './WsButton.vue'
import WsLanguage from './WsLanguage.vue'
import { useSiteContext } from '../composables/useSiteContext.js'

defineProps({
  modelValue: { type: Boolean, default: false },
  links: { type: Array, default: () => [] },
  cta: { type: String, default: '' },
  ctaHref: { type: String, default: '' },
})
const emit = defineEmits(['update:modelValue'])
const { t } = useSiteContext()

function close() {
  emit('update:modelValue', false)
}
</script>

<style scoped>
.ws-drawer {
  display: none;
  flex-direction: column;
  gap: 18px;
  padding: 20px 24px 28px;
  border-top: 1px solid var(--ws-border);
  background: var(--ws-surface);
}

.ws-drawer nav {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.ws-drawer nav a {
  color: var(--ws-text);
  font-weight: 500;
}

@container ws (max-width: 860px) {
  .ws-drawer {
    display: flex;
  }
}

.ws-drawer-enter-active,
.ws-drawer-leave-active {
  transition: opacity 0.2s ease, transform 0.2s ease;
}

.ws-drawer-enter-from,
.ws-drawer-leave-to {
  opacity: 0;
  transform: translateY(-8px);
}
</style>
