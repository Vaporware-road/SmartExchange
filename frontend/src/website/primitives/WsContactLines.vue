<template>
  <ul class="ws-contact-lines">
    <li v-for="line in lines" :key="line.key">
      <i :class="line.icon" aria-hidden="true" />
      <a v-if="line.href" :href="line.href" :dir="line.ltr ? 'ltr' : null">{{ line.value }}</a>
      <span v-else :class="{ 'ws-contact-lines__block': line.multiline }">{{ line.value }}</span>
    </li>
  </ul>
</template>

<script setup>
import { computed } from 'vue'

/** The desk's real contact details, in the order a customer needs them. */
const props = defineProps({
  contact: { type: Object, default: () => ({}) },
  address: { type: String, default: '' },
  hours: { type: String, default: '' },
})

const lines = computed(() => {
  const contact = props.contact || {}
  const rows = []
  const phones = [contact.phone, contact.phone_2, contact.phone_3].filter(Boolean)
  phones.forEach((phone, index) => {
    rows.push({
      key: `phone-${index}`,
      icon: 'fas fa-phone',
      value: phone,
      href: `tel:${phone.replace(/\s+/g, '')}`,
      ltr: true,
    })
  })
  if (contact.email) {
    rows.push({ key: 'email', icon: 'fas fa-envelope', value: contact.email, href: `mailto:${contact.email}`, ltr: true })
  }
  const address = props.address || contact.address
  if (address) {
    rows.push({
      key: 'address',
      icon: 'fas fa-location-dot',
      value: address,
      href: contact.map_url || null,
      multiline: true,
    })
  }
  const hours = props.hours || contact.hours
  if (hours) {
    rows.push({ key: 'hours', icon: 'fas fa-clock', value: hours, multiline: true })
  }
  return rows
})
</script>

<style scoped>
.ws-contact-lines {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.ws-contact-lines li {
  display: flex;
  align-items: flex-start;
  gap: 0.85em;
  color: var(--ws-text-muted);
}

.ws-contact-lines i {
  color: var(--ws-primary);
  margin-top: 0.3em;
  width: 1.1em;
  text-align: center;
  flex: none;
}

.ws-contact-lines a:hover {
  color: var(--ws-primary);
}

.ws-contact-lines__block {
  white-space: pre-line;
}
</style>
