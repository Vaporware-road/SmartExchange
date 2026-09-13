<template>
  <WsSection anchor="contact" :title="title" :subtitle="subtitle" center alt>
    <div class="ws-grid ws-contact-cards" :style="{ '--ws-cols': cols }">
      <article v-for="card in cards" :key="card.key" class="ws-card ws-contact-card">
        <WsIcon :name="card.icon" />
        <h3 class="ws-h3">{{ $t(card.titleKey) }}</h3>
        <a v-if="card.href" :href="card.href" dir="ltr">{{ card.value }}</a>
        <p v-else class="ws-body">{{ card.value }}</p>
      </article>
    </div>
    <div class="ws-contact-card__socials">
      <WsSocials />
    </div>
  </WsSection>
</template>

<script setup>
import { computed } from 'vue'
import WsSection from '../../primitives/WsSection.vue'
import WsIcon from '../../primitives/WsIcon.vue'
import WsSocials from '../../primitives/WsSocials.vue'
import { useContact } from './_contact.js'

const props = defineProps({ content: { type: Object, default: () => ({}) } })
const { title, subtitle, address, hours, contact } = useContact(props)

const cards = computed(() => {
  const rows = []
  if (contact.value.phone) {
    rows.push({
      key: 'phone',
      icon: 'phone',
      titleKey: 'website.contact.callUs',
      value: contact.value.phone,
      href: `tel:${contact.value.phone.replace(/\s+/g, '')}`,
    })
  }
  if (address.value) {
    rows.push({
      key: 'address',
      icon: 'location-dot',
      titleKey: 'website.contact.visitUs',
      value: address.value,
      href: contact.value.map_url || null,
    })
  }
  if (hours.value) {
    rows.push({ key: 'hours', icon: 'clock', titleKey: 'website.contact.openHours', value: hours.value })
  }
  if (!rows.length && contact.value.email) {
    rows.push({
      key: 'email',
      icon: 'envelope',
      titleKey: 'website.contact.emailUs',
      value: contact.value.email,
      href: `mailto:${contact.value.email}`,
    })
  }
  return rows
})

/* A desk with only opening hours to show should not get one card stranded on
   the left of a three-column grid. */
const cols = computed(() => Math.min(cards.value.length || 1, 3))
</script>

<style scoped>
.ws-contact-cards {
  /* Narrow rows stay centred instead of hugging the start edge. */
  max-width: calc(var(--ws-cols, 3) * 320px);
  margin-inline: auto;
}

.ws-contact-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 12px;
}

.ws-contact-card p {
  white-space: pre-line;
}

.ws-contact-card a:hover {
  color: var(--ws-primary);
}

.ws-contact-card__socials {
  display: flex;
  justify-content: center;
  margin-top: calc(var(--ws-block-gap) * 1.2);
}
</style>
