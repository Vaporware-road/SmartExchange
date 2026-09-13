<template>
  <WsSection anchor="contact" :title="title" :subtitle="subtitle">
    <div class="ws-split">
      <div class="ws-stack">
        <WsContactLines :contact="contact" :address="address" :hours="hours" />
        <WsSocials />
        <WsContactForm v-if="showForm" :contact="contact" />
      </div>
      <div v-if="mapUrl" class="ws-media ws-contact-map">
        <iframe
          :src="mapUrl"
          loading="lazy"
          referrerpolicy="no-referrer-when-downgrade"
          :title="title || 'Map'"
          allowfullscreen
        />
      </div>
    </div>
  </WsSection>
</template>

<script setup>
import WsSection from '../../primitives/WsSection.vue'
import WsContactLines from '../../primitives/WsContactLines.vue'
import WsContactForm from '../../primitives/WsContactForm.vue'
import WsSocials from '../../primitives/WsSocials.vue'
import { useContact } from './_contact.js'

const props = defineProps({ content: { type: Object, default: () => ({}) } })
const { title, subtitle, address, hours, mapUrl, contact, showForm } = useContact(props)
</script>

<style scoped>
.ws-contact-map {
  min-height: 380px;
  height: 100%;
}

.ws-contact-map iframe {
  width: 100%;
  height: 100%;
  min-height: 380px;
  border: 0;
  display: block;
}
</style>
