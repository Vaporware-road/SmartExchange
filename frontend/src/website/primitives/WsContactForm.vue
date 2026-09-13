<template>
  <form v-if="target" class="ws-form" @submit.prevent="send">
    <label>
      <span>{{ $t('website.contact.yourName') }}</span>
      <input v-model.trim="name" type="text" required :placeholder="$t('website.contact.namePlaceholder')" />
    </label>
    <label>
      <span>{{ $t('website.contact.message') }}</span>
      <textarea v-model.trim="message" rows="4" required :placeholder="$t('website.contact.messagePlaceholder')" />
    </label>
    <WsButton>
      <i :class="target.icon" aria-hidden="true" />
      {{ $t(target.labelKey) }}
    </WsButton>
    <p class="ws-form__hint ws-muted">{{ $t('website.contact.formHint') }}</p>
  </form>

  <!-- Guidance for the owner, never for a visitor: a live page must not tell
       the public that its own contact details are missing. -->
  <p v-else-if="isEditing" class="ws-muted">{{ $t('website.contact.noChannel') }}</p>
</template>

<script setup>
import { computed, ref } from 'vue'
import WsButton from './WsButton.vue'
import { useSiteContext } from '../composables/useSiteContext.js'

/**
 * A contact form that never stores anything.
 *
 * A desk's enquiries belong in the channel it already answers — Telegram,
 * WhatsApp or email — so this composes the visitor's message and hands it over.
 * Nothing is posted to the panel, which means no lead table to secure, no spam
 * endpoint to rate-limit, and no message sitting unread in a database.
 */
const props = defineProps({
  contact: { type: Object, default: () => ({}) },
  socials: { type: Object, default: () => ({}) },
})

const { branding, isEditing, t: localized } = useSiteContext()
const name = ref('')
const message = ref('')

const target = computed(() => {
  const socials = props.socials || branding.value.socials || {}
  const contact = props.contact || branding.value.contact || {}
  if (socials.telegram) {
    return { kind: 'telegram', href: socials.telegram, icon: 'fab fa-telegram', labelKey: 'website.contact.sendTelegram' }
  }
  if (contact.phone) {
    return { kind: 'whatsapp', href: contact.phone, icon: 'fab fa-whatsapp', labelKey: 'website.contact.sendWhatsapp' }
  }
  if (contact.email) {
    return { kind: 'email', href: contact.email, icon: 'fas fa-envelope', labelKey: 'website.contact.sendEmail' }
  }
  return null
})

function send() {
  const current = target.value
  if (!current) return
  const business = localized(branding.value.business_name) || ''
  const body = `${name.value}\n\n${message.value}`

  if (current.kind === 'email') {
    const subject = encodeURIComponent(`${business} — ${name.value}`.trim())
    window.location.href = `mailto:${current.href}?subject=${subject}&body=${encodeURIComponent(body)}`
    return
  }
  if (current.kind === 'whatsapp') {
    const number = current.href.replace(/[^\d]/g, '')
    window.open(`https://wa.me/${number}?text=${encodeURIComponent(body)}`, '_blank', 'noopener')
    return
  }
  // Telegram deep links carry no message body, so the text goes to the
  // clipboard and the visitor pastes it into the chat that just opened.
  navigator.clipboard?.writeText(body).catch(() => {})
  window.open(current.href, '_blank', 'noopener')
}
</script>

<style scoped>
.ws-form {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

label {
  display: flex;
  flex-direction: column;
  gap: 7px;
  font-size: 0.88rem;
  color: var(--ws-text-muted);
}

input,
textarea {
  font: inherit;
  font-size: 0.95rem;
  color: var(--ws-text);
  background: var(--ws-surface);
  border: 1px solid var(--ws-border);
  border-radius: var(--ws-radius-sm);
  padding: 0.8em 1em;
  resize: vertical;
}

input:focus,
textarea:focus {
  outline: none;
  border-color: var(--ws-primary);
  box-shadow: var(--ws-glow);
}

.ws-form__hint {
  margin: 0;
  font-size: 0.78rem;
}

.ws-form :deep(.ws-btn) {
  align-self: flex-start;
}
</style>
