import { computed } from 'vue'
import { useSiteContext } from '../../composables/useSiteContext.js'

/**
 * Contact details, preferring what the owner typed into the website and
 * falling back to the panel's own settings — so a desk that already filled in
 * Settings does not have to type its phone number a second time.
 */
export function useContact(props) {
  const { t, branding } = useSiteContext()
  const content = computed(() => props.content || {})
  const panel = computed(() => branding.value.contact || {})
  const inherit = computed(() => content.value.inherit_panel_contact !== false)

  function pick(own, fallbackKey) {
    return own || (inherit.value ? panel.value[fallbackKey] || '' : '')
  }

  return {
    t,
    title: computed(() => t(content.value.title)),
    subtitle: computed(() => t(content.value.subtitle)),
    address: computed(() => pick(t(content.value.address), 'address')),
    hours: computed(() => pick(t(content.value.hours), 'hours')),
    mapUrl: computed(() => pick(content.value.map_embed_url, 'map_url')),
    showForm: computed(() => {
      if (content.value.show_form === false) return false
      // Nothing to send to means no form: an empty card is worse than no card.
      const socials = branding.value.socials || {}
      return Boolean(
        socials.telegram ||
          content.value.phone ||
          content.value.email ||
          (inherit.value && (panel.value.phone || panel.value.email)),
      )
    }),
    contact: computed(() => ({
      phone: pick(content.value.phone, 'phone'),
      phone_2: pick(content.value.phone_2, 'phone_2'),
      phone_3: inherit.value ? panel.value.phone_3 || '' : '',
      email: pick(content.value.email, 'email'),
      map_url: pick(content.value.map_embed_url, 'map_url'),
    })),
  }
}
