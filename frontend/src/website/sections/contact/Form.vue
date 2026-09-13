<template>
  <WsSection anchor="contact" :title="title" :subtitle="subtitle">
    <div class="ws-contact-form" :class="{ 'ws-contact-form--single': !showForm }">
      <div v-if="showForm" class="ws-card ws-contact-form__panel">
        <WsContactForm :contact="contact" />
      </div>
      <aside class="ws-stack">
        <WsContactLines :contact="contact" :address="address" :hours="hours" />
        <WsSocials />
      </aside>
    </div>
  </WsSection>
</template>

<script setup>
import WsSection from '../../primitives/WsSection.vue'
import WsContactForm from '../../primitives/WsContactForm.vue'
import WsContactLines from '../../primitives/WsContactLines.vue'
import WsSocials from '../../primitives/WsSocials.vue'
import { useContact } from './_contact.js'

const props = defineProps({ content: { type: Object, default: () => ({}) } })
const { title, subtitle, address, hours, contact, showForm } = useContact(props)
</script>

<style scoped>
.ws-contact-form {
  display: grid;
  grid-template-columns: minmax(0, 1.25fr) minmax(0, 1fr);
  gap: calc(var(--ws-block-gap) * 1.5);
  align-items: start;
}

.ws-contact-form__panel {
  padding: calc(var(--ws-block-gap) * 1.2);
}

/* With no form there is only the details column, so it should not sit in a
   half-width cell with a hole beside it. */
.ws-contact-form--single {
  grid-template-columns: minmax(0, 1fr);
}

@container ws (max-width: 860px) {
  .ws-contact-form {
    grid-template-columns: minmax(0, 1fr);
  }
}
</style>
