<template>
  <div class="mx-auto w-full max-w-4xl min-w-0">
    <!-- Page header -->
    <header class="mb-6 flex flex-wrap items-center justify-between gap-3">
      <div class="min-w-0">
        <router-link
          to="/programmer"
          class="mb-2 inline-flex items-center gap-1.5 text-sm text-[var(--text-secondary)] transition-colors hover:text-[var(--primary)]"
        >
          <i class="fas fa-arrow-left text-xs rtl:rotate-180" />
          {{ $t('onboarding.backToList') }}
        </router-link>
        <h1 class="text-2xl font-bold text-gold">{{ $t('programmerHub.register') }}</h1>
        <p class="mt-1 text-sm text-[var(--text-secondary)]">
          {{ $t('onboarding.subtitle') }}
        </p>
      </div>
      <div
        class="hidden sm:flex items-center gap-2 rounded-xl border border-[var(--border-card)] bg-[var(--bg-card)] px-3 py-2 text-xs text-[var(--text-secondary)]"
      >
        <span class="inline-flex h-2 w-2 rounded-full bg-emerald-500" />
        {{ $t('programmerHub.active') }}
      </div>
    </header>

    <form class="space-y-6" novalidate @submit.prevent="handleSubmit">
      <!-- Section 1: Basic Info -->
      <FormSection
        icon="fas fa-user"
        :title="$t('onboarding.basicInfo')"
        :description="$t('onboarding.basicInfoDesc')"
      >
        <TextField
          v-model="form.first_name"
          :label="$t('programmerHub.firstName')"
          :placeholder="$t('programmerHub.firstName')"
          :error="fieldError('first_name')"
          required
          @blur="touch('first_name')"
        />
        <TextField
          v-model="form.last_name"
          :label="$t('programmerHub.lastName')"
          :placeholder="$t('programmerHub.lastName')"
          :error="fieldError('last_name')"
          required
          @blur="touch('last_name')"
        />
        <TextField
          v-model="form.country"
          :label="$t('programmerHub.country')"
          :placeholder="$t('programmerHub.country')"
          :error="fieldError('country')"
          required
          @blur="touch('country')"
        />
        <TextField
          v-model="form.email"
          type="email"
          inputmode="email"
          autocomplete="email"
          :label="$t('programmerHub.email')"
          :placeholder="$t('programmerHub.email')"
          :error="fieldError('email')"
          required
          @blur="touch('email')"
        />
        <TextField
          v-model="form.phone"
          type="tel"
          inputmode="tel"
          autocomplete="tel"
          :label="$t('programmerHub.phone')"
          :placeholder="$t('programmerHub.phone')"
          :error="fieldError('phone')"
          required
          @blur="touch('phone')"
        />
      </FormSection>

      <!-- Section 2: Business Details -->
      <FormSection
        icon="fas fa-briefcase"
        :title="$t('onboarding.businessDetails')"
        :description="$t('onboarding.businessDetailsDesc')"
      >
        <TextField
          v-model="form.exchange_name"
          :label="$t('programmerHub.exchangeName')"
          :placeholder="$t('programmerHub.exchangeName')"
          :error="fieldError('exchange_name')"
          required
          @blur="touch('exchange_name')"
        />
        <TextField
          v-model="form.website"
          type="url"
          inputmode="url"
          autocomplete="url"
          :label="$t('programmerHub.website')"
          :placeholder="'https://example.com'"
          :hint="$t('programmerHub.websiteHint')"
          :error="fieldError('website')"
          @blur="touch('website')"
        />
        <SelectField
          v-model="form.collaboration_type"
          :label="$t('collaboration.title')"
          :placeholder="$t('collaboration.placeholder')"
          :hint="$t('collaboration.hint')"
          :options="collaborationOptions"
          :error="fieldError('collaboration_type')"
          @blur="touch('collaboration_type')"
        />
      </FormSection>

      <!-- Section 3: System Access -->
      <FormSection
        icon="fas fa-key"
        :title="$t('onboarding.systemAccess')"
        :description="$t('onboarding.systemAccessDesc')"
      >
        <TextField
          v-model="form.telegram_id"
          :label="$t('programmerHub.telegramId')"
          :placeholder="$t('programmerHub.telegramId')"
          :hint="$t('programmerHub.telegramIdHint')"
          :error="fieldError('telegram_id')"
          @blur="touch('telegram_id')"
        />
        <SelectField
          v-model="form.plan"
          :label="$t('programmerHub.plan')"
          :options="planOptions"
          required
        />
        <TextField
          v-if="isDelegated"
          v-model="form.telegram_username"
          :label="$t('programmerHub.telegramUsername')"
          :placeholder="$t('programmerHub.telegramUsername')"
          :error="fieldError('telegram_username')"
          @blur="touch('telegram_username')"
        />
        <TextField
          v-if="!isDelegated"
          v-model="form.telegram_bot_token"
          type="password"
          autocomplete="new-password"
          :label="$t('programmerHub.botToken')"
          :placeholder="$t('telegram.botSetup.tokenPlaceholder')"
          :error="fieldError('telegram_bot_token')"
          required
          @blur="touch('telegram_bot_token')"
        />
        <div v-else class="text-xs text-[var(--text-secondary)]">
          <i class="fas fa-info-circle me-1" />
          {{ $t('programmerHub.delegatedNoBotHint') }}
        </div>
      </FormSection>

      <!-- Section 4: Delegated Operator -->
      <FormSection
        icon="fas fa-user-cog"
        :title="$t('programmerHub.delegationTitle')"
        :description="$t('programmerHub.delegationDesc')"
      >
        <SelectField
          v-model="form.sub_role"
          :label="$t('programmerHub.subRole')"
          :hint="$t('programmerHub.subRoleHint')"
          :options="subRoleOptions"
        />
        <TextField
          v-if="isDelegated"
          v-model="form.owner_username"
          :label="$t('programmerHub.ownerUsername')"
          :placeholder="$t('programmerHub.ownerUsername')"
          :hint="$t('programmerHub.ownerUsernameHint')"
          :error="fieldError('owner_username')"
          required
          @blur="touch('owner_username')"
        />
        <!-- Audit trail: auto-filled, read-only -->
        <div class="min-w-0 w-full">
          <span class="mb-1.5 block text-sm font-medium text-[var(--text-primary)]">
            {{ $t('onboarding.registeredBy') }}
          </span>
          <div
            class="flex items-center gap-2.5 rounded-xl border border-[var(--border-card)] bg-[var(--bg-input)]/70 px-4 py-3"
          >
            <span class="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-primary-muted text-sm text-[var(--primary)]">
              <i class="fas fa-user-shield" />
            </span>
            <div class="min-w-0">
              <p class="truncate text-sm font-medium text-[var(--text-primary)]">
                {{ registeredByName }}
              </p>
              <p class="text-xs text-[var(--text-secondary)]">
                {{ $t('onboarding.registeredByHint') }}
              </p>
            </div>
          </div>
        </div>
      </FormSection>

      <!-- Form actions -->
      <div class="flex flex-col-reverse gap-3 sm:flex-row sm:items-center sm:justify-between">
        <p
          v-if="generatedPassword"
          class="flex items-center gap-2 rounded-xl border border-[var(--border-card)] bg-primary-muted px-4 py-3 text-sm font-medium text-[var(--primary)] min-w-0"
        >
          <i class="fas fa-key shrink-0" />
          <span class="min-w-0 break-words">
            {{ $t('programmerHub.generatedPassword') }}:
            <code class="font-mono font-bold">{{ generatedPassword }}</code>
          </span>
        </p>
        <p v-else class="hidden text-sm text-[var(--text-secondary)] sm:block">
          <span class="text-red-500">*</span>
          {{ $t('validation.requiredMarkHint') }}
        </p>
        <button
          type="submit"
          class="btn-luxury inline-flex min-h-[48px] w-full items-center justify-center gap-2 sm:w-auto sm:px-8"
          :disabled="saving"
        >
          <LoadingSpinner v-if="saving" class="w-5 h-5" />
          <i v-else class="fas fa-user-plus" />
          {{ saving ? $t('programmerHub.saving') : $t('common.create') }}
        </button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { reactive, ref, computed, watch } from 'vue'
import { useI18n } from 'vue-i18n'
import { useRouter } from 'vue-router'
import { useToast } from 'vue-toastification'
import { authApi, getApiErrorDetails } from '@/services/api'
import { useAuthStore } from '@/stores/auth'
import FormSection from '@/components/forms/FormSection.vue'
import TextField from '@/components/forms/TextField.vue'
import SelectField from '@/components/forms/SelectField.vue'
import LoadingSpinner from '@/components/ui/LoadingSpinner.vue'
import { createRegisterSchema, collectFieldErrors } from '@/utils/registerClientSchema'

const COLLABORATION_TYPES = ['reseller', 'white_label', 'agency', 'direct']
const PLANS = ['bronze', 'silver', 'gold']
const SUB_ROLES = ['admin', 'operator', 'head_operator']

const { t, locale } = useI18n()
const router = useRouter()
const toast = useToast()
const auth = useAuthStore()

const saving = ref(false)
const generatedPassword = ref('')
const touched = reactive({})

const form = reactive({
  first_name: '',
  last_name: '',
  exchange_name: '',
  country: '',
  email: '',
  phone: '',
  website: '',
  collaboration_type: '',
  telegram_id: '',
  telegram_username: '',
  telegram_bot_token: '',
  plan: 'bronze',
  sub_role: 'admin',
  owner_username: '',
})

const schema = computed(() => createRegisterSchema(t))

const isDelegated = computed(
  () => form.sub_role === 'operator' || form.sub_role === 'head_operator'
)

const collaborationOptions = computed(() =>
  COLLABORATION_TYPES.map((key) => ({ value: key, label: t(`collaboration.${key}`) }))
)

const subRoleOptions = computed(() =>
  SUB_ROLES.map((key) => ({ value: key, label: t(`programmerHub.${key}`) }))
)

const planOptions = computed(() =>
  PLANS.map((key) => ({ value: key, label: t(`programmerHub.plans.${key}`) }))
)

const registeredByName = computed(
  () => auth.user?.full_name || auth.user?.username || '—'
)

const fieldErrors = ref({})

function touch(field) {
  touched[field] = true
  validate()
}

function fieldError(field) {
  return fieldErrors.value[field] || ''
}

function validate() {
  fieldErrors.value = collectFieldErrors(schema.value, form, touched)
  return Object.keys(fieldErrors.value).length === 0
}

// Re-validate after locale switch so messages stay translated
watch(locale, () => {
  if (Object.keys(touched).length) validate()
})

async function handleSubmit() {
  // Mark everything touched so full errors show on submit
  for (const key of Object.keys(form)) touched[key] = true
  if (!validate()) {
    toast.error(t('toast.validationError'))
    return
  }
  saving.value = true
  generatedPassword.value = ''
  try {
    const payload = {
      ...form,
      website: form.website?.trim() || '',
      collaboration_type: form.collaboration_type || '',
      // Never send the bot token for delegated operators (backend ignores it anyway).
      telegram_bot_token: isDelegated.value ? '' : form.telegram_bot_token,
    }
    const { data } = await authApi.programmer.register(payload)
    generatedPassword.value = data.generated_password || ''
    toast.success(t('programmerHub.created'))
    router.push('/programmer')
  } catch (error) {
    toast.error(getApiErrorDetails(error).message)
  } finally {
    saving.value = false
  }
}
</script>
