<template>
  <div class="space-y-4 min-w-0">
    <!-- Customers Status -->
    <div v-if="section === 'customersStatus'" class="card-luxury px-4 py-4 space-y-4">
      <h2 class="text-lg font-semibold text-gold">{{ $t('telegram.admin.customersStatus.title') }}</h2>
      <p class="text-sm text-[var(--text-secondary)]">{{ $t('telegram.admin.customersStatus.hint') }}</p>
      <div class="grid grid-cols-2 md:grid-cols-4 gap-3">
        <div v-for="card in tagCards" :key="card.key" class="rounded-xl bg-white/5 border border-white/10 px-3 py-3">
          <p class="text-xs text-gray-400">{{ card.label }}</p>
          <p class="text-2xl font-semibold text-[var(--text-primary)] mt-1">{{ card.value }}</p>
        </div>
      </div>
      <button type="button" class="btn-luxury-outline text-sm" @click="$emit('select-section', 'customerAnalysis')">
        {{ $t('telegram.admin.customersStatus.manageTags') }}
      </button>
    </div>

    <!-- Notifications -->
    <div v-else-if="section === 'notifications'" class="card-luxury px-4 py-4 space-y-4">
      <h2 class="text-lg font-semibold text-gold">{{ $t('telegram.admin.notifications.title') }}</h2>
      <div class="flex flex-wrap gap-4 text-sm">
        <span>{{ $t('telegram.admin.notifications.total', { n: dashboard?.notifications?.total ?? 0 }) }}</span>
        <span>{{ $t('telegram.admin.notifications.active', { n: dashboard?.notifications?.active ?? 0 }) }}</span>
      </div>
      <div class="overflow-x-auto">
        <table class="w-full text-sm">
          <thead>
            <tr class="text-left text-gray-400 border-b border-white/10">
              <th class="py-2 pr-3">{{ $t('telegram.admin.notifications.customer') }}</th>
              <th class="py-2 pr-3">{{ $t('telegram.admin.notifications.pair') }}</th>
              <th class="py-2 pr-3">{{ $t('telegram.admin.notifications.direction') }}</th>
              <th class="py-2">{{ $t('common.status') }}</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="alert in (dashboard?.notifications?.items || [])"
              :key="alert.id"
              class="border-b border-white/5"
            >
              <td class="py-2 pr-3">{{ alert.customer_telegram_user_id || alert.customer }}</td>
              <td class="py-2 pr-3">{{ alert.source_currency }}/{{ alert.target_currency }}</td>
              <td class="py-2 pr-3">{{ alert.direction }}</td>
              <td class="py-2">{{ alert.is_active ? $t('telegram.channels.active') : $t('telegram.channels.inactive') }}</td>
            </tr>
          </tbody>
        </table>
        <p v-if="!(dashboard?.notifications?.items || []).length" class="text-center text-gray-500 py-6">
          {{ $t('common.noData') }}
        </p>
      </div>
    </div>

    <!-- Reports -->
    <div v-else-if="section === 'reports'" class="card-luxury px-4 py-4 space-y-4">
      <h2 class="text-lg font-semibold text-gold">{{ $t('telegram.admin.reports.title') }}</h2>
      <p class="text-sm text-[var(--text-secondary)]">{{ $t('telegram.admin.reports.hint') }}</p>
      <div class="grid grid-cols-2 md:grid-cols-3 gap-3">
        <div v-for="card in reportCards" :key="card.key" class="rounded-xl bg-white/5 border border-white/10 px-3 py-3">
          <p class="text-xs text-gray-400">{{ card.label }}</p>
          <p class="text-2xl font-semibold text-[var(--text-primary)] mt-1">{{ card.value }}</p>
        </div>
      </div>
    </div>

    <!-- Analytics -->
    <div v-else-if="section === 'analytics'" class="card-luxury px-4 py-4 space-y-4">
      <h2 class="text-lg font-semibold text-gold">{{ $t('telegram.admin.analytics.title') }}</h2>
      <div class="rounded-xl bg-white/5 border border-white/10 px-3 py-3">
        <p class="text-sm font-medium">{{ $t('telegram.admin.analytics.dailyUsage') }}</p>
        <div class="mt-3 space-y-1 max-h-64 overflow-y-auto text-sm">
          <div
            v-for="row in (dashboard?.analytics?.daily_usage || [])"
            :key="row.date"
            class="flex justify-between gap-4 border-b border-white/5 py-1"
          >
            <span class="text-gray-400">{{ row.date }}</span>
            <span>{{ row.users }}</span>
          </div>
          <p v-if="!(dashboard?.analytics?.daily_usage || []).length" class="text-gray-500 py-2">
            {{ $t('common.noData') }}
          </p>
        </div>
      </div>
      <div class="rounded-xl bg-white/5 border border-white/10 px-3 py-3">
        <p class="text-sm font-medium">{{ $t('telegram.admin.analytics.channelMembers') }}</p>
        <ul class="mt-2 space-y-1 text-sm">
          <li
            v-for="ch in (dashboard?.analytics?.channel_members || [])"
            :key="ch.channel_id"
            class="flex justify-between gap-2 border-b border-white/5 py-1"
          >
            <span>{{ ch.name }}</span>
            <span class="text-gray-400 text-right">
              {{ ch.member_count ?? '—' }}
              <span v-if="ch.publish_activity_total != null" class="block text-xs">
                {{ $t('telegram.admin.analytics.publishActivity', { n: ch.publish_activity_total }) }}
              </span>
              <span v-if="!ch.bot_admin_verified" class="text-amber-400/80"> (no admin)</span>
            </span>
          </li>
          <li v-if="!(dashboard?.analytics?.channel_members || []).length" class="text-gray-500 py-2">
            {{ $t('common.noData') }}
          </li>
        </ul>
      </div>
      <div class="rounded-xl bg-white/5 border border-dashed border-white/20 px-3 py-3 opacity-80">
        <p class="text-sm font-medium">{{ $t('telegram.admin.analytics.channelViews') }}</p>
        <p class="text-sm text-gray-400 mt-1">{{ $t('telegram.admin.analytics.channelViewsStub') }}</p>
      </div>
    </div>

    <!-- Exchange requests -->
    <div v-else-if="section === 'exchangeRequests'" class="card-luxury px-4 py-4 space-y-4">
      <div class="flex flex-wrap items-center justify-between gap-3">
        <h2 class="text-lg font-semibold text-gold">{{ $t('telegram.admin.exchangeRequests.title') }}</h2>
        <button
          type="button"
          class="btn-luxury-outline text-sm inline-flex items-center gap-2"
          :disabled="exchangeListLoading"
          @click="refreshExchangeSection"
        >
          <LoadingSpinner v-if="exchangeListLoading" class="w-4 h-4" />
          <i v-else class="fas fa-sync-alt" />
          {{ $t('common.refresh') }}
        </button>
      </div>
      <p class="text-sm text-[var(--text-secondary)]">{{ $t('telegram.admin.exchangeRequests.hint') }}</p>
      <div class="flex flex-wrap gap-2">
        <button
          type="button"
          class="text-sm"
          :class="exchangeFilter === 'all' ? 'btn-luxury' : 'btn-luxury-outline'"
          @click="exchangeFilter = 'all'"
        >
          {{ $t('common.all') }}
        </button>
        <button
          type="button"
          class="text-sm"
          :class="exchangeFilter === 'new' ? 'btn-luxury' : 'btn-luxury-outline'"
          @click="exchangeFilter = 'new'"
        >
          {{ $t('telegram.admin.exchangeRequests.new') }}
        </button>
        <button
          type="button"
          class="text-sm"
          :class="exchangeFilter === 'cancelled' ? 'btn-luxury' : 'btn-luxury-outline'"
          @click="exchangeFilter = 'cancelled'"
        >
          {{ $t('telegram.admin.exchangeRequests.canceled') }}
        </button>
        <button
          type="button"
          class="text-sm"
          :class="exchangeFilter === 'successful' ? 'btn-luxury' : 'btn-luxury-outline'"
          @click="exchangeFilter = 'successful'"
        >
          {{ $t('telegram.admin.exchangeRequests.successful') }}
        </button>
      </div>
      <div class="grid grid-cols-2 md:grid-cols-4 gap-3">
        <div v-for="(detail, months) in (dashboard?.exchange_requests?.new_members_detail || {})" :key="months" class="rounded-xl bg-white/5 border border-white/10 px-3 py-3">
          <p class="text-xs text-gray-400">{{ detail.label || $t('telegram.admin.exchangeRequests.newMembers', { months }) }}</p>
          <p class="text-lg font-semibold mt-1">+{{ (detail.channel_growth || 0) + (detail.bot_dm_growth || 0) }}</p>
          <p class="text-xs text-gray-500 mt-1">
            ch {{ detail.channel_growth || 0 }} · bot {{ detail.bot_dm_growth || 0 }}
          </p>
        </div>
      </div>
      <div>
        <h3 class="text-sm font-medium text-gold mb-2">{{ $t('telegram.admin.exchangeRequests.mostRequested') }}</h3>
        <ul class="text-sm space-y-1">
          <li v-for="row in (dashboard?.exchange_requests?.most_requested_currencies || [])" :key="row.currency">
            {{ row.currency }} — {{ row.count }}
          </li>
          <li v-if="!(dashboard?.exchange_requests?.most_requested_currencies || []).length" class="text-gray-500">
            {{ $t('common.noData') }}
          </li>
        </ul>
      </div>
      <div class="overflow-x-auto">
        <table class="w-full text-sm">
          <thead>
            <tr class="text-left text-gray-400 border-b border-white/10">
              <th class="py-2 pr-3">{{ $t('telegram.admin.exchangeRequests.customer') }}</th>
              <th class="py-2 pr-3">{{ $t('telegram.admin.exchangeRequests.pair') }}</th>
              <th class="py-2 pr-3">{{ $t('telegram.admin.exchangeRequests.amount') }}</th>
              <th class="py-2 pr-3">{{ $t('telegram.admin.exchangeRequests.ttl') }}</th>
              <th class="py-2">{{ $t('common.status') }}</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="er in filteredExchangeItems"
              :key="er.id"
              class="border-b border-white/5 cursor-pointer"
              :class="selectedExchangeId === er.id ? 'bg-white/10' : 'hover:bg-white/5'"
              @click="selectExchange(er)"
            >
              <td class="py-2 pr-3 font-mono text-xs">
                {{ er.customer_telegram_user_id }}
                <span class="block text-gray-400">{{ er.customer_name || '—' }}</span>
              </td>
              <td class="py-2 pr-3">{{ er.source_currency }}→{{ er.target_currency }}</td>
              <td class="py-2 pr-3">{{ er.amount }}</td>
              <td class="py-2 pr-3">{{ er.ttl_minutes }}</td>
              <td class="py-2">{{ statusLabel(er.status) }}</td>
            </tr>
          </tbody>
        </table>
        <p v-if="!filteredExchangeItems.length && !exchangeListLoading" class="text-center text-gray-500 py-6">
          {{ $t('common.noData') }}
        </p>
      </div>
      <div v-if="selectedExchange" class="rounded-xl bg-white/5 border border-white/10 px-3 py-3 space-y-3">
        <p class="text-sm">
          #{{ selectedExchange.id }} · {{ statusLabel(selectedExchange.status) }} · TTL {{ selectedExchange.ttl_minutes }}
        </p>
        <div v-if="changeStateOpen" class="flex flex-wrap gap-2">
          <button type="button" class="btn-luxury-outline text-sm" @click="setExchangeStatus('new')">
            {{ $t('telegram.admin.exchangeRequests.new') }}
          </button>
          <button type="button" class="btn-luxury-outline text-sm" @click="setExchangeStatus('cancelled')">
            {{ $t('telegram.admin.exchangeRequests.canceled') }}
          </button>
          <button type="button" class="btn-luxury-outline text-sm" @click="setExchangeStatus('successful')">
            {{ $t('telegram.admin.exchangeRequests.successful') }}
          </button>
          <button type="button" class="btn-luxury-outline text-sm" @click="changeStateOpen = false">
            {{ $t('common.back') }}
          </button>
        </div>
        <div v-else class="flex flex-wrap gap-2">
          <button type="button" class="btn-luxury text-sm" @click="changeStateOpen = true">
            {{ $t('telegram.admin.exchangeRequests.changeState') }}
          </button>
          <button type="button" class="btn-luxury-outline text-sm" :disabled="holding" @click="holdExchange">
            {{ $t('telegram.admin.exchangeRequests.hold') }}
          </button>
        </div>
      </div>
    </div>

    <!-- Customer analysis -->
    <div v-else-if="section === 'customerAnalysis'" class="card-luxury px-4 py-4 space-y-4">
      <h2 class="text-lg font-semibold text-gold">{{ $t('telegram.admin.customerAnalysis.title') }}</h2>
      <p class="text-sm text-[var(--text-secondary)]">{{ $t('telegram.admin.customerAnalysis.hint') }}</p>
      <div class="grid grid-cols-2 md:grid-cols-4 gap-3">
        <div class="rounded-xl bg-white/5 border border-white/10 px-3 py-3">
          <p class="text-xs text-gray-400">{{ $t('telegram.admin.customerAnalysis.returned') }}</p>
          <p class="text-2xl font-semibold mt-1">{{ dashboard?.customer_analysis?.returned ?? 0 }}</p>
        </div>
        <div class="rounded-xl bg-white/5 border border-white/10 px-3 py-3">
          <p class="text-xs text-gray-400">{{ $t('telegram.admin.customerAnalysis.inactive') }}</p>
          <p class="text-2xl font-semibold mt-1">{{ dashboard?.customer_analysis?.inactive ?? 0 }}</p>
        </div>
        <div class="rounded-xl bg-white/5 border border-white/10 px-3 py-3">
          <p class="text-xs text-gray-400">{{ $t('telegram.admin.customerAnalysis.vipRatio') }}</p>
          <p class="text-2xl font-semibold mt-1">{{ ratioLabel }}</p>
        </div>
      </div>
      <div>
        <h3 class="text-sm font-medium text-gold mb-2">{{ $t('telegram.admin.customerAnalysis.peakHours') }}</h3>
        <div class="flex items-end gap-1 h-24">
          <div
            v-for="row in (dashboard?.customer_analysis?.peak_hours || [])"
            :key="row.hour"
            class="flex-1 bg-gold/40 rounded-t min-w-0"
            :style="{ height: peakBarHeight(row.count) }"
            :title="`${row.hour}:00 — ${row.count}`"
          />
        </div>
      </div>
      <div class="space-y-3 pt-2 border-t border-white/10">
        <h3 class="text-sm font-medium text-gold">{{ $t('telegram.admin.customerAnalysis.setTag') }}</h3>
        <p class="text-sm text-[var(--text-secondary)]">{{ $t('telegram.admin.customerAnalysis.prompt') }}</p>
        <input
          v-model="tagUserQuery"
          class="input-luxury"
          :placeholder="$t('telegram.admin.customerAnalysis.userid')"
        />
        <div v-if="tagCustomersLoading" class="flex justify-center py-4">
          <LoadingSpinner class="w-6 h-6 text-gold" />
        </div>
        <div v-else class="overflow-x-auto">
          <table class="w-full text-sm">
            <thead>
              <tr class="text-left text-gray-400 border-b border-white/10">
                <th class="py-2 pr-3">{{ $t('telegram.customers.telegramId') }}</th>
                <th class="py-2 pr-3">{{ $t('telegram.customers.name') }}</th>
                <th class="py-2 pr-3">{{ $t('telegram.admin.customerAnalysis.requests') }}</th>
                <th class="py-2">{{ $t('telegram.customers.tag') }}</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="c in filteredTagCustomers"
                :key="c.id"
                class="border-b border-white/5"
              >
                <td class="py-2 pr-3 font-mono text-xs">{{ c.telegram_user_id }}</td>
                <td class="py-2 pr-3">{{ c.display_name || c.username || '—' }}</td>
                <td class="py-2 pr-3">{{ c.request_count ?? 0 }}</td>
                <td class="py-2">
                  <span v-if="c.is_admin || c.display_tag === 'admin'">
                    {{ $t('telegram.customers.tags.admin') }}
                  </span>
                  <select
                    v-else
                    class="input-luxury py-1 text-sm min-w-[8rem]"
                    :value="c.tag"
                    :disabled="customerTagSavingId === c.id"
                    @change="updateAnalysisTag(c, $event.target.value)"
                  >
                    <option value="global">{{ $t('telegram.customers.tags.global') }}</option>
                    <option value="vip">{{ $t('telegram.customers.tags.vip') }}</option>
                    <option value="special">{{ $t('telegram.customers.tags.special') }}</option>
                  </select>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <div v-else-if="section === 'reengage'" class="space-y-4">
      <div class="card-luxury px-4 py-4 space-y-4">
        <h2 class="text-lg font-semibold text-gold">{{ $t('telegram.admin.reengage.title') }}</h2>
        <p class="text-sm text-[var(--text-secondary)]">{{ $t('telegram.admin.reengage.hint') }}</p>
        <div>
          <label class="block text-sm font-medium text-gray-400 mb-2">{{ $t('telegram.admin.reengage.audience') }}</label>
          <select v-model="audience" class="input-luxury">
            <option value="global">{{ $t('telegram.customers.tags.global') }}</option>
            <option value="vip">{{ $t('telegram.customers.tags.vip') }}</option>
            <option value="special">{{ $t('telegram.customers.tags.special') }}</option>
            <option value="inactive">{{ $t('telegram.admin.reengage.inactive') }}</option>
          </select>
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-400 mb-2">{{ $t('telegram.admin.reengage.message') }}</label>
          <textarea v-model="message" class="input-luxury" rows="4" />
        </div>
        <button
          type="button"
          class="btn-luxury-gradient min-h-[44px]"
          :disabled="sending || !message.trim()"
          @click="sendReengage"
        >
          <LoadingSpinner v-if="sending" class="w-5 h-5" />
          <span v-else>{{ $t('telegram.admin.reengage.send') }}</span>
        </button>
        <p v-if="lastResult" class="text-sm text-[var(--text-secondary)]">
          {{ $t('telegram.admin.reengage.result', lastResult) }}
        </p>
      </div>

      <div class="card-luxury px-4 py-4 space-y-4">
        <h3 class="text-sm font-semibold text-gold">{{ $t('telegram.admin.stubs.periodicTitle') }}</h3>
        <div>
          <label class="block text-sm font-medium text-gray-400 mb-2">{{ $t('telegram.admin.reengage.audience') }}</label>
          <select v-model="campaignAudience" class="input-luxury">
            <option value="global">{{ $t('telegram.customers.tags.global') }}</option>
            <option value="vip">{{ $t('telegram.customers.tags.vip') }}</option>
            <option value="special">{{ $t('telegram.customers.tags.special') }}</option>
            <option value="inactive">{{ $t('telegram.admin.reengage.inactive') }}</option>
          </select>
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-400 mb-2">{{ $t('telegram.admin.stubs.schedulePlaceholder') }}</label>
          <select v-model="campaignSchedule" class="input-luxury">
            <option value="daily">{{ $t('telegram.admin.campaigns.daily') }}</option>
            <option value="weekly">{{ $t('telegram.admin.campaigns.weekly') }}</option>
            <option value="monthly">{{ $t('telegram.admin.campaigns.monthly') }}</option>
          </select>
        </div>
        <textarea v-model="campaignMessage" class="input-luxury" rows="3" :placeholder="$t('telegram.admin.stubs.messagePlaceholder')" />
        <button
          type="button"
          class="btn-luxury-outline text-sm min-h-[44px]"
          :disabled="savingCampaign || !campaignMessage.trim()"
          @click="saveCampaign"
        >
          {{ $t('telegram.admin.campaigns.save') }}
        </button>
        <ul v-if="campaigns.length" class="text-sm space-y-2 mt-2">
          <li v-for="c in campaigns" :key="c.id" class="flex justify-between gap-2 border-b border-white/5 py-1">
            <span>{{ c.audience }} · {{ c.schedule }}</span>
            <button type="button" class="text-rose-400 text-xs" @click="deleteCampaign(c.id)">
              {{ $t('common.delete') }}
            </button>
          </li>
        </ul>
      </div>

      <div class="card-luxury px-4 py-4 space-y-4">
        <h3 class="text-sm font-semibold text-gold">{{ $t('telegram.admin.stubs.offerTitle') }}</h3>
        <input v-model="offerTitle" class="input-luxury" :placeholder="$t('telegram.admin.stubs.offerPlaceholder')" />
        <textarea v-model="offerBody" class="input-luxury" rows="3" :placeholder="$t('telegram.admin.reengage.message')" />
        <select v-model="offerAudience" class="input-luxury">
          <option value="global">{{ $t('telegram.customers.tags.global') }}</option>
          <option value="vip">{{ $t('telegram.customers.tags.vip') }}</option>
          <option value="special">{{ $t('telegram.customers.tags.special') }}</option>
          <option value="inactive">{{ $t('telegram.admin.reengage.inactive') }}</option>
        </select>
        <input
          v-model="offerValidUntil"
          type="datetime-local"
          class="input-luxury"
          :placeholder="$t('telegram.admin.offers.validUntil')"
        />
        <div class="flex flex-wrap gap-2">
          <button
            type="button"
            class="btn-luxury-outline text-sm"
            :disabled="savingOffer || !offerTitle.trim() || !offerBody.trim()"
            @click="saveOffer(false)"
          >
            {{ $t('common.save') }}
          </button>
          <button
            type="button"
            class="btn-luxury text-sm"
            :disabled="savingOffer || !offerTitle.trim() || !offerBody.trim()"
            @click="saveOffer(true)"
          >
            {{ $t('telegram.admin.offers.saveAndSend') }}
          </button>
        </div>
        <ul v-if="offers.length" class="text-sm space-y-2 mt-2">
          <li v-for="o in offers" :key="o.id" class="flex justify-between gap-2 border-b border-white/5 py-1">
            <span>{{ o.title }} ({{ o.audience }})</span>
            <button type="button" class="text-gold text-xs" @click="sendOfferNow(o.id)">
              {{ $t('telegram.admin.reengage.send') }}
            </button>
          </li>
        </ul>
      </div>
    </div>

    <!-- Bot settings (TTL / flags) -->
    <div v-else-if="section === 'botSettings'" class="card-luxury px-4 py-4 space-y-4">
      <h2 class="text-lg font-semibold text-gold">{{ $t('telegram.admin.botSettings.title') }}</h2>
      <p class="text-sm text-[var(--text-secondary)]">{{ $t('telegram.admin.botSettings.hint') }}</p>
      <div>
        <label class="block text-sm font-medium text-gray-400 mb-2">
          {{ $t('telegram.botSetup.defaultExchangeTtl') }}
        </label>
        <input v-model.number="ttlMinutes" type="number" min="1" class="input-luxury" />
      </div>
      <label class="inline-flex items-center gap-2 text-sm">
        <input v-model="botActive" type="checkbox" class="rounded" />
        {{ $t('telegram.botSetup.isActive') }}
      </label>
      <button type="button" class="btn-luxury min-h-[44px]" :disabled="savingBot" @click="saveBotSettings">
        <LoadingSpinner v-if="savingBot" class="w-5 h-5" />
        <span v-else>{{ $t('common.save') }}</span>
      </button>
    </div>
  </div>
</template>

<script setup>
import { computed, ref, watch } from 'vue'
import { useI18n } from 'vue-i18n'
import { useToast } from 'vue-toastification'
import { telegramApi } from '@/services/api'
import LoadingSpinner from '@/components/ui/LoadingSpinner.vue'

const props = defineProps({
  section: { type: String, required: true },
  dashboard: { type: Object, default: null },
  verifiedBot: { type: Object, default: null },
})

const emit = defineEmits(['open-tools', 'select-section', 'bot-updated', 'refresh-dashboard'])

const { t } = useI18n()
const toast = useToast()

const audience = ref('global')
const message = ref('')
const sending = ref(false)
const lastResult = ref(null)
const ttlMinutes = ref(5)
const botActive = ref(true)
const savingBot = ref(false)
const exchangeFilter = ref('all')
const campaignAudience = ref('global')
const campaignSchedule = ref('weekly')
const campaignMessage = ref('')
const campaigns = ref([])
const savingCampaign = ref(false)
const offerTitle = ref('')
const offerBody = ref('')
const offerAudience = ref('global')
const offerValidUntil = ref('')
const offers = ref([])
const savingOffer = ref(false)
const liveExchangeItems = ref(null)
const exchangeListLoading = ref(false)
const selectedExchangeId = ref(null)
const changeStateOpen = ref(false)
const holding = ref(false)
const tagCustomers = ref([])
const tagCustomersLoading = ref(false)
const tagUserQuery = ref('')
const customerTagSavingId = ref(null)

watch(
  () => props.verifiedBot,
  (bot) => {
    if (!bot) return
    ttlMinutes.value = bot.default_exchange_ttl_minutes ?? 5
    botActive.value = !!bot.is_active
    loadCampaignsAndOffers()
  },
  { immediate: true },
)

watch(
  () => [props.section, props.verifiedBot?.id],
  ([section, botId]) => {
    if (section === 'reengage' && botId) {
      loadCampaignsAndOffers()
    }
    if (section === 'exchangeRequests' && botId) {
      loadExchangeRequests()
    }
    if (section === 'customerAnalysis' && botId) {
      loadTagCustomers()
    }
  },
  { immediate: true },
)

async function loadCampaignsAndOffers() {
  if (!props.verifiedBot?.id) return
  try {
    const [cRes, oRes] = await Promise.all([
      telegramApi.admin.campaigns.list({ bot_id: props.verifiedBot.id }),
      telegramApi.admin.offers.list({ bot_id: props.verifiedBot.id }),
    ])
    campaigns.value = cRes.data || []
    offers.value = oRes.data || []
  } catch {
    campaigns.value = []
    offers.value = []
  }
}

function unwrapList(data) {
  if (Array.isArray(data)) return data
  return data?.results ?? []
}

async function loadExchangeRequests() {
  if (!props.verifiedBot?.id) return
  const botId = props.verifiedBot.id
  if (
    liveExchangeItems.value != null
    && liveExchangeItems.value.some((row) => row.bot != null && Number(row.bot) !== Number(botId))
  ) {
    liveExchangeItems.value = null
  }
  exchangeListLoading.value = true
  try {
    const { data } = await telegramApi.exchangeRequests.list({
      bot_id: botId,
    })
    liveExchangeItems.value = unwrapList(data)
  } catch {
    liveExchangeItems.value = null
    toast.error(t('telegram.admin.exchangeRequests.loadError'))
  } finally {
    exchangeListLoading.value = false
  }
}

function refreshExchangeSection() {
  emit('refresh-dashboard')
  loadExchangeRequests()
}

const filteredExchangeItems = computed(() => {
  const items = liveExchangeItems.value ?? props.dashboard?.exchange_requests?.items ?? []
  if (exchangeFilter.value === 'successful') {
    return items.filter((er) => er.status === 'successful')
  }
  if (exchangeFilter.value === 'new' || exchangeFilter.value === 'pending') {
    return items.filter((er) => er.status === 'new')
  }
  if (exchangeFilter.value === 'cancelled') {
    return items.filter((er) => er.status === 'cancelled')
  }
  return items
})

const selectedExchange = computed(() => {
  const items = liveExchangeItems.value ?? props.dashboard?.exchange_requests?.items ?? []
  return items.find((er) => er.id === selectedExchangeId.value) || null
})

const filteredTagCustomers = computed(() => {
  const q = tagUserQuery.value.trim()
  if (!q) return tagCustomers.value
  return tagCustomers.value.filter((c) => String(c.telegram_user_id).includes(q))
})

const tagCards = computed(() => {
  const by = props.dashboard?.customers_status?.by_tag || {}
  return [
    { key: 'total', label: t('telegram.admin.customersStatus.total'), value: by.total ?? 0 },
    { key: 'global', label: t('telegram.customers.tags.global'), value: by.global ?? 0 },
    { key: 'vip', label: t('telegram.customers.tags.vip'), value: by.vip ?? 0 },
    { key: 'special', label: t('telegram.customers.tags.special'), value: by.special ?? 0 },
  ]
})

const reportCards = computed(() => {
  const r = props.dashboard?.reports || {}
  return [
    { key: 'running', label: t('telegram.admin.reports.running'), value: r.running ?? 0 },
    { key: 'new', label: t('telegram.admin.reports.new'), value: r.new ?? r.pending ?? 0 },
    { key: 'successful', label: t('telegram.admin.reports.successful'), value: r.successful ?? 0 },
    { key: 'cancelled', label: t('telegram.admin.reports.cancelled'), value: r.cancelled ?? 0 },
  ]
})

const ratioLabel = computed(() => {
  const ratio = props.dashboard?.customer_analysis?.vip_vs_ordinary_request_ratio
  if (ratio == null) return '—'
  return String(ratio)
})

const peakMax = computed(() => {
  const rows = props.dashboard?.customer_analysis?.peak_hours || []
  return Math.max(1, ...rows.map((r) => r.count || 0))
})

function peakBarHeight(count) {
  const pct = roundPct(count)
  return `${Math.max(4, pct)}%`
}

function roundPct(count) {
  return Math.round(((count || 0) / peakMax.value) * 100)
}

function statusLabel(status) {
  if (status === 'new') return t('telegram.admin.exchangeRequests.new')
  if (status === 'cancelled') return t('telegram.admin.exchangeRequests.canceled')
  if (status === 'successful') return t('telegram.admin.exchangeRequests.successful')
  return status || '—'
}

function selectExchange(er) {
  selectedExchangeId.value = er.id
  changeStateOpen.value = false
}

function upsertExchange(row) {
  if (!row?.id) return
  const items = [...(liveExchangeItems.value || [])]
  const idx = items.findIndex((er) => er.id === row.id)
  if (idx >= 0) items[idx] = { ...items[idx], ...row }
  else items.unshift(row)
  liveExchangeItems.value = items
}

async function setExchangeStatus(status) {
  if (!selectedExchange.value?.id) return
  try {
    const { data } = await telegramApi.exchangeRequests.patch(selectedExchange.value.id, { status })
    upsertExchange(data)
    changeStateOpen.value = false
    toast.success(t('telegram.admin.exchangeRequests.stateUpdated'))
  } catch (err) {
    toast.error(err?.response?.data?.status?.[0] || err?.response?.data?.detail || t('toast.serverError'))
  }
}

async function holdExchange() {
  if (!selectedExchange.value?.id) return
  holding.value = true
  try {
    const { data } = await telegramApi.exchangeRequests.hold(selectedExchange.value.id)
    upsertExchange(data)
    toast.success(t('telegram.admin.exchangeRequests.holdOk', { ttl: data.ttl_minutes }))
  } catch (err) {
    toast.error(err?.response?.data?.detail || t('toast.serverError'))
  } finally {
    holding.value = false
  }
}

async function loadTagCustomers() {
  if (!props.verifiedBot?.id) return
  tagCustomersLoading.value = true
  try {
    const { data } = await telegramApi.customers.list({ bot_id: props.verifiedBot.id })
    tagCustomers.value = unwrapList(data)
  } catch {
    tagCustomers.value = []
    toast.error(t('telegram.customers.loadError'))
  } finally {
    tagCustomersLoading.value = false
  }
}

async function updateAnalysisTag(customer, tag) {
  if (!customer?.id || customer.tag === tag) return
  customerTagSavingId.value = customer.id
  try {
    const { data } = await telegramApi.customers.updateTag(customer.id, { tag })
    const idx = tagCustomers.value.findIndex((c) => c.id === customer.id)
    if (idx >= 0) tagCustomers.value[idx] = { ...tagCustomers.value[idx], ...data }
    toast.success(t('telegram.customers.tagUpdated'))
  } catch (err) {
    toast.error(err?.response?.data?.tag?.[0] || err?.response?.data?.detail || t('telegram.customers.tagError'))
  } finally {
    customerTagSavingId.value = null
  }
}

async function sendReengage() {
  if (!message.value.trim() || !props.verifiedBot?.id) return
  sending.value = true
  lastResult.value = null
  try {
    const { data } = await telegramApi.admin.reengage({
      bot_id: props.verifiedBot.id,
      audience: audience.value,
      message: message.value.trim(),
    })
    lastResult.value = {
      sent: data.sent ?? 0,
      failed: data.failed ?? 0,
      skipped: data.skipped ?? 0,
    }
    toast.success(t('telegram.admin.reengage.sentOk'))
  } catch (err) {
    toast.error(err?.response?.data?.message || err?.response?.data?.detail || t('toast.serverError'))
  } finally {
    sending.value = false
  }
}

async function saveBotSettings() {
  if (!props.verifiedBot?.id) return
  savingBot.value = true
  try {
    const { data } = await telegramApi.bots.patch(props.verifiedBot.id, {
      default_exchange_ttl_minutes: Number(ttlMinutes.value) || 5,
      is_active: !!botActive.value,
    })
    toast.success(t('toast.saveSuccess'))
    emit('bot-updated', data)
  } catch (err) {
    toast.error(err?.response?.data?.detail || t('toast.serverError'))
  } finally {
    savingBot.value = false
  }
}

async function saveCampaign() {
  if (!props.verifiedBot?.id || !campaignMessage.value.trim()) return
  savingCampaign.value = true
  try {
    await telegramApi.admin.campaigns.create({
      bot_id: props.verifiedBot.id,
      audience: campaignAudience.value,
      schedule: campaignSchedule.value,
      message: campaignMessage.value.trim(),
      is_active: true,
    })
    campaignMessage.value = ''
    toast.success(t('toast.saveSuccess'))
    await loadCampaignsAndOffers()
  } catch (err) {
    toast.error(err?.response?.data?.message || t('toast.serverError'))
  } finally {
    savingCampaign.value = false
  }
}

async function deleteCampaign(id) {
  try {
    await telegramApi.admin.campaigns.delete(id)
    await loadCampaignsAndOffers()
  } catch (err) {
    toast.error(err?.response?.data?.message || t('toast.serverError'))
  }
}

async function saveOffer(sendNow) {
  if (!props.verifiedBot?.id || !offerTitle.value.trim() || !offerBody.value.trim()) return
  savingOffer.value = true
  try {
    await telegramApi.admin.offers.create({
      bot_id: props.verifiedBot.id,
      title: offerTitle.value.trim(),
      body: offerBody.value.trim(),
      audience: offerAudience.value,
      valid_until: offerValidUntil.value ? new Date(offerValidUntil.value).toISOString() : null,
      is_active: true,
      send_now: sendNow,
    })
    offerTitle.value = ''
    offerBody.value = ''
    offerValidUntil.value = ''
    toast.success(sendNow ? t('telegram.admin.reengage.sentOk') : t('toast.saveSuccess'))
    await loadCampaignsAndOffers()
  } catch (err) {
    toast.error(err?.response?.data?.message || t('toast.serverError'))
  } finally {
    savingOffer.value = false
  }
}

async function sendOfferNow(id) {
  try {
    await telegramApi.admin.offers.send(id)
    toast.success(t('telegram.admin.reengage.sentOk'))
  } catch (err) {
    toast.error(err?.response?.data?.message || t('toast.serverError'))
  }
}
</script>
