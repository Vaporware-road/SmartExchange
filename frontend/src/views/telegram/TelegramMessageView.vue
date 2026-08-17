<template>
  <div class="relative w-full min-w-0 overflow-hidden">
    <!-- Token gate: block hub until getMe succeeds (management / super_admin) -->
    <div
      v-if="requiresGate && hubLocked"
      class="fixed inset-0 z-50 flex items-center justify-center bg-black/70 backdrop-blur-sm"
    >
      <div class="card-luxury max-w-md w-[90%] px-6 py-8 text-center space-y-4">
        <template v-if="verifyLoading">
          <LoadingSpinner class="w-12 h-12 text-gold mx-auto" />
          <p class="text-[var(--text-primary)] font-medium">{{ $t('telegram.admin.gate.verifying') }}</p>
          <p class="text-sm text-[var(--text-secondary)]">{{ $t('telegram.admin.gate.verifyingHint') }}</p>
        </template>
        <template v-else>
          <p class="text-lg font-semibold text-gold">{{ $t('telegram.admin.gate.failedTitle') }}</p>
          <p class="text-sm text-[var(--text-secondary)]">{{ verifyError || $t('telegram.admin.gate.failedHint') }}</p>
          <button type="button" class="btn-luxury-gradient min-h-[44px]" @click="runVerify">
            {{ $t('telegram.admin.gate.retry') }}
          </button>
        </template>
      </div>
    </div>

    <div :class="{ 'pointer-events-none select-none opacity-40': requiresGate && hubLocked }">
      <div class="flex flex-wrap items-end justify-between gap-3 mb-6">
        <h1 class="text-2xl font-bold text-gold animate-fade-in-up">
          {{ $t('telegram.hubTitle') }}
        </h1>
        <div v-if="verifiedBot" class="flex flex-wrap items-center gap-2">
          <select
            v-if="hubBotOptions.length"
            class="input-luxury py-1.5 text-sm min-w-[10rem]"
            :aria-label="$t('telegram.channels.selectBot')"
            :value="verifiedBot.id"
            @change="onHubBotChange"
          >
            <option v-for="b in hubBotOptions" :key="b.id" :value="b.id">
              {{ botSelectLabel(b) }}
            </option>
          </select>
          <p class="text-sm text-[var(--text-secondary)]">
            {{ $t('telegram.admin.gate.scopedTo', { name: verifiedBot.username || verifiedBot.name }) }}
          </p>
        </div>
      </div>

      <div class="flex flex-col lg:flex-row gap-6 items-start min-w-0">
        <!-- Admin category nav -->
        <aside
          v-if="showAdminNav"
          class="card-luxury w-full lg:w-56 shrink-0 px-2 py-3 space-y-1 rtl:lg:order-2"
        >
          <p class="px-3 py-1 text-xs uppercase tracking-wide text-gray-500">
            {{ $t('telegram.admin.navLabel') }}
          </p>
          <button
            v-for="cat in adminCategories"
            :key="cat.id"
            type="button"
            class="w-full text-left rtl:text-right px-3 py-2 rounded-lg text-sm transition-all"
            :class="adminSection === cat.id ? 'btn-luxury' : 'hover:bg-white/5 text-[var(--text-secondary)]'"
            @click="selectAdminSection(cat.id)"
          >
            <i :class="[cat.icon, 'me-2']" />
            {{ $t(cat.labelKey) }}
          </button>
        </aside>

        <div class="flex-1 min-w-0 w-full">
          <div
            v-if="dashboardError && showAdminNav && !hubLocked"
            class="card-luxury mb-4 px-4 py-3 flex flex-wrap items-center justify-between gap-3"
          >
            <p class="text-sm text-amber-300">{{ dashboardError }}</p>
            <button type="button" class="btn-luxury-outline text-sm" @click="loadDashboard">
              {{ $t('common.refresh') }}
            </button>
          </div>
          <!-- Admin panels -->
          <TelegramHubAdminPanels
            v-if="showAdminNav && adminSection !== 'tools'"
            :section="adminSection"
            :dashboard="dashboard"
            :verified-bot="verifiedBot"
            @open-tools="openToolsTab"
            @select-section="selectAdminSection"
            @bot-updated="onBotUpdated"
            @refresh-dashboard="loadDashboard"
          />

          <template v-else>
            <!-- Tabs -->
            <div class="card-luxury mb-6 px-3 py-2 flex flex-wrap gap-2 items-center rtl:flex-row-reverse min-w-0">
              <button
                v-for="tab in tabs"
                :key="tab.id"
                type="button"
                class="inline-flex items-center gap-2 px-4 py-2 rounded-full text-sm font-medium transition-all"
                :class="activeTab === tab.id ? 'btn-luxury' : 'btn-luxury-outline bg-transparent'"
                @click="activeTab = tab.id"
              >
                <i :class="tab.icon" />
                <span>{{ $t(tab.labelKey) }}</span>
              </button>
            </div>

            <!-- Tab content -->
            <Transition name="fade-slide" mode="out-in">
              <div :key="activeTab">
        <!-- Tab 1: Messenger -->
        <div
          v-if="activeTab === 'messenger'"
          class="grid grid-cols-1 md:grid-cols-2 gap-6 items-start animate-fade-in-up rtl:md:grid-flow-dense"
        >
          <!-- Form -->
          <form @submit.prevent="handleSend" class="card-luxury space-y-4 px-4 py-3 min-w-0 w-full">
            <h2 class="text-lg font-semibold text-gold mb-2">
              {{ $t('telegram.tabs.messenger') }}
            </h2>

            <div>
              <label class="block text-sm font-medium text-gray-400 mb-2">
                {{ $t('telegram.messenger.channelLabel') }}
              </label>
              <select v-model="channelId" class="input-luxury" required>
                <option value="">{{ $t('telegram.messenger.channelPlaceholder') }}</option>
                <option
                  v-for="ch in channels"
                  :key="ch.id"
                  :value="ch.id"
                >
                  {{ ch.name }}
                </option>
              </select>
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-400 mb-2">
                {{ $t('telegram.messenger.bannerLabel') }}
              </label>
              <select v-model="bannerKey" class="input-luxury">
                <option
                  v-for="opt in bannerOptions"
                  :key="opt.value"
                  :value="opt.value"
                >
                  {{ $t(opt.labelKey) }}
                </option>
              </select>
            </div>

            <div v-if="useDoublePrice" class="grid grid-cols-1 gap-3">
              <div>
                <label class="block text-sm font-medium text-gray-400 mb-2">
                  {{ $t('telegram.messenger.cashPrice') }}
                </label>
                <input
                  v-model.number="cashPrice"
                  type="number"
                  step="0.01"
                  min="0"
                  class="input-luxury"
                />
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-400 mb-2">
                  {{ $t('telegram.messenger.accountPrice') }}
                </label>
                <input
                  v-model.number="accountPrice"
                  type="number"
                  step="0.01"
                  min="0"
                  class="input-luxury"
                />
              </div>
            </div>
            <div v-else>
              <label class="block text-sm font-medium text-gray-400 mb-2">
                {{ $t('telegram.messenger.price') }}
              </label>
              <input
                v-model.number="singlePrice"
                type="number"
                step="0.01"
                min="0"
                class="input-luxury"
              />
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-400 mb-2">
                {{ $t('telegram.messenger.messageLabel') }}
              </label>
              <textarea
                v-model="message"
                class="input-luxury"
                rows="4"
                :placeholder="$t('telegram.messenger.messagePlaceholder')"
              />
            </div>

            <div class="flex flex-wrap gap-4">
              <button type="submit" class="btn-luxury-gradient min-h-[48px]" :disabled="submitting || !channelId">
                <LoadingSpinner v-if="submitting" class="w-5 h-5" />
                <span v-else>{{ $t('telegram.messenger.send') }}</span>
              </button>
            </div>
          </form>

          <!-- Live preview -->
          <div class="card-luxury px-4 py-3 animate-fade-in-up hover-lift min-w-0">
            <h2 class="text-lg font-semibold text-gold mb-4">
              {{ $t('telegram.messenger.livePreview') }}
            </h2>
            <div class="bg-[var(--glass-bg)] border border-[var(--glass-border)] rounded-2xl p-4 space-y-3">
              <div class="flex items-center gap-3 min-w-0">
                <div class="w-10 h-10 rounded-full bg-gradient-to-br from-gold/80 to-amber-500/80 flex items-center justify-center text-xs font-bold text-black shadow-soft shrink-0">
                  {{ selectedChannelInitials }}
                </div>
                <div class="min-w-0 flex-1">
                  <p class="font-semibold text-[var(--text-primary)] truncate">
                    {{ selectedChannel?.name || $t('telegram.messenger.channelDefault') }}
                  </p>
                  <p class="text-xs text-[var(--text-secondary)]">
                    Telegram • {{ previewTimestamp }}
                  </p>
                </div>
              </div>

              <div class="mt-2 rounded-2xl bg-black/20 border border-white/5 px-4 py-3 space-y-2">
                <p v-if="selectedBannerLabel" class="text-xs font-semibold text-gold uppercase tracking-wide">
                  {{ selectedBannerLabel }}
                </p>
                <p v-if="previewPriceLine" class="text-sm text-[var(--text-primary)]">
                  {{ previewPriceLine }}
                </p>
                <p v-if="message" class="text-sm text-[var(--text-primary)] whitespace-pre-line">
                  {{ message }}
                </p>
              </div>

              <div class="flex justify-end">
                <div class="inline-flex rounded-full bg-white/5 border border-white/10 px-3 py-1.5 text-xs text-[var(--text-secondary)] gap-2">
                  <span class="inline-flex items-center gap-1">
                    <i class="fas fa-eye" />
                    0
                  </span>
                  <span class="inline-flex items-center gap-1">
                    <i class="fas fa-check-double" />
                    0
                  </span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Tab 2: Bot Setup -->
        <div
          v-else-if="activeTab === 'bot'"
          class="space-y-6 animate-fade-in-up"
        >
          <div class="flex flex-wrap items-center justify-between gap-4">
            <div>
              <h2 class="text-lg font-semibold text-gold">
                {{ $t('telegram.tabs.botSetup') }}
              </h2>
              <p class="text-sm text-[var(--text-secondary)] mt-1">
                {{ $t('telegram.botSetup.description') }}
              </p>
            </div>
            <button
              type="button"
              class="btn-luxury inline-flex items-center gap-2"
              @click="$router.push({ name: 'telegram-bot-new' })"
            >
              <i class="fas fa-plus" />
              {{ $t('telegram.botSetup.addNewBot') }}
            </button>
          </div>

          <!-- Bot list: empty state -->
          <div
            v-if="!botsList.length"
            class="card-luxury px-6 py-12 flex flex-col items-center justify-center text-center"
          >
            <div class="w-16 h-16 rounded-2xl flex items-center justify-center mb-4 bg-[var(--glass-bg)] border border-[var(--glass-border)]">
              <i class="fas fa-robot text-2xl text-gold opacity-80" />
            </div>
            <h3 class="text-lg font-semibold text-[var(--text-primary)] mb-2">
              {{ $t('telegram.botSetup.noBots') }}
            </h3>
            <p class="text-sm text-[var(--text-secondary)] mb-6 max-w-sm">
              {{ $t('telegram.botSetup.noBotsDesc') }}
            </p>
            <button type="button" class="btn-luxury" @click="$router.push({ name: 'telegram-bot-new' })">
              <i class="fas fa-plus" />
              {{ $t('telegram.botSetup.addNewBot') }}
            </button>
          </div>

          <!-- Bot list: card grid -->
          <div
            v-else
            class="grid grid-cols-1 md:grid-cols-2 gap-4"
          >
            <div
              v-for="b in botsList"
              :key="b.id"
              class="card-luxury px-4 py-4 relative min-w-0 hover-lift transition-all"
            >
              <div class="absolute top-3 right-3 flex gap-2 rtl:flex-row-reverse">
                <button
                  type="button"
                  class="btn-luxury-outline p-2 rounded-lg text-sm"
                  :title="$t('common.edit')"
                  @click="$router.push({ name: 'telegram-bot-edit', params: { id: b.id } })"
                >
                  <i class="fas fa-pencil-alt" />
                </button>
                <button
                  type="button"
                  class="p-2 rounded-lg text-sm text-red-400 hover:bg-red-500/10 border border-transparent hover:border-red-500/30 transition-colors"
                  :title="$t('common.delete')"
                  @click="openDeleteBotConfirm(b)"
                >
                  <i class="fas fa-trash" />
                </button>
              </div>
              <div class="pr-24 rtl:pr-4 rtl:pl-24">
                <h3 class="text-[var(--text-primary)] font-semibold truncate">
                  {{ b.name || `Bot #${b.id}` }}
                </h3>
                <p
                  v-if="b.display_name"
                  class="text-sm text-[var(--text-secondary)] truncate mt-0.5"
                >
                  {{ b.display_name }}
                </p>
                <p
                  v-if="b.notes"
                  class="text-sm text-[var(--text-secondary)] mt-2 line-clamp-2"
                >
                  {{ b.notes }}
                </p>
                <p class="text-xs text-[var(--text-secondary)] mt-2">
                  {{ formatBotCreatedAt(b.created_at) }}
                </p>
                <span
                  class="inline-block mt-2 text-xs px-2 py-1 rounded-full"
                  :class="b.is_active ? 'bg-emerald-500/10 text-emerald-400' : 'bg-red-500/10 text-red-400'"
                >
                  {{ b.is_active ? $t('telegram.channels.active') : $t('telegram.channels.inactive') }}
                </span>
              </div>
            </div>
          </div>

          <!-- Delete Bot Confirmation Modal -->
          <Teleport to="body">
            <Transition name="modal-fade">
              <div
                v-if="botDeleteConfirm"
                class="fixed inset-0 z-50 flex items-center justify-center"
              >
                <div
                  class="absolute inset-0 bg-black/60 backdrop-blur-sm"
                  @click="botDeleteConfirm = null"
                />
                <div
                  class="relative z-10 w-full max-w-md mx-4 rounded-2xl p-6 shadow-2xl"
                  style="background: var(--bg-card, #1e2535);"
                  role="dialog"
                  aria-modal="true"
                >
                  <h3 class="text-lg font-semibold text-[var(--text-primary)] mb-2">
                    {{ $t('common.delete') }}
                  </h3>
                  <p class="text-sm text-[var(--text-secondary)] mb-6">
                    {{ $t('telegram.botSetup.deleteBotConfirm', { name: botDeleteConfirm?.name || `Bot #${botDeleteConfirm?.id}` }) }}
                  </p>
                  <div class="flex gap-3 justify-end">
                    <button type="button" class="btn-luxury-outline" :disabled="botDeleting" @click="botDeleteConfirm = null">
                      {{ $t('common.cancel') }}
                    </button>
                    <button
                      type="button"
                      class="px-4 py-2 rounded-lg font-medium bg-red-500/20 text-red-400 border border-red-500/30 hover:bg-red-500/30 transition-colors disabled:opacity-50"
                      :disabled="botDeleting"
                      @click="confirmDeleteBot"
                    >
                      <LoadingSpinner v-if="botDeleting" class="w-5 h-5 inline" />
                      <span v-else>{{ $t('common.delete') }}</span>
                    </button>
                  </div>
                </div>
              </div>
            </Transition>
          </Teleport>
        </div>

        <!-- Tab 3: Channels -->
        <div
          v-else-if="activeTab === 'channels'"
          class="space-y-6 animate-fade-in-up"
        >
          <div class="card-luxury px-4 py-3">
            <h2 class="text-lg font-semibold text-gold mb-2">
              {{ $t('telegram.channels.title') }}
            </h2>
            <p class="text-sm text-gray-400 mb-4">
              {{ $t('telegram.channels.description') }}
            </p>

            <form @submit.prevent="addChannel" class="space-y-3">
              <h3 class="text-sm font-medium text-gold">{{ $t('telegram.channels.addChannel') }}</h3>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                <div>
                  <label class="block text-sm font-medium text-gray-400 mb-1">{{ $t('telegram.channels.channelName') }}</label>
                  <input
                    v-model="channelForm.name"
                    type="text"
                    class="input-luxury w-full"
                    :placeholder="$t('telegram.channels.channelNamePlaceholder')"
                    required
                  />
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-400 mb-1">{{ $t('telegram.channels.channelId') }}</label>
                  <input
                    v-model="channelForm.chat_id"
                    type="text"
                    class="input-luxury w-full"
                    :placeholder="$t('telegram.channels.channelIdPlaceholder')"
                    required
                  />
                </div>
              </div>
              <div class="flex flex-wrap gap-4 items-center">
                <div>
                  <label class="block text-sm font-medium text-gray-400 mb-1">{{ $t('telegram.channels.bot') }}</label>
                  <select v-model="channelForm.bot" class="input-luxury" required>
                    <option value="">{{ $t('telegram.channels.selectBot') }}</option>
                    <option v-for="b in botsList" :key="b.id" :value="b.id">{{ b.name || b.display_name || `Bot #${b.id}` }}</option>
                  </select>
                </div>
                <div class="mt-6">
                  <BaseCheckbox v-model="channelForm.is_active">{{ $t('telegram.channels.active') }}</BaseCheckbox>
                </div>
                <button type="submit" class="btn-luxury" :disabled="channelSaving">
                  <LoadingSpinner v-if="channelSaving" class="w-5 h-5" />
                  <span v-else>{{ $t('telegram.channels.add') }}</span>
                </button>
              </div>
            </form>
          </div>

          <div class="card-luxury overflow-hidden w-full min-w-0 px-4 py-3">
            <div v-if="manageChannelsLoading" class="space-y-2">
              <div v-for="i in 3" :key="i" class="h-12 rounded bg-white/5 animate-pulse" />
            </div>
            <template v-else>
              <div class="w-full overflow-x-auto max-w-full">
                <table class="w-full text-sm min-w-[500px]">
                <thead>
                  <tr class="text-[var(--text-secondary)] border-b" style="border-color: var(--glass-border);">
                    <th class="text-left py-3 px-4 font-medium">{{ $t('telegram.channels.bot') }}</th>
                    <th class="text-left py-3 px-4 font-medium">{{ $t('telegram.channels.channelName') }}</th>
                    <th class="text-left py-3 px-4 font-medium">{{ $t('telegram.channels.channelId') }}</th>
                    <th class="text-left py-3 px-4 font-medium">{{ $t('common.status') }}</th>
                    <th class="text-left py-3 px-4 font-medium">{{ $t('common.actions') }}</th>
                  </tr>
                </thead>
                <tbody>
                  <tr
                    v-for="(ch, idx) in manageChannelsList"
                    :key="ch.id"
                    class="border-b transition-colors hover:bg-white/5 animate-fade-in-up"
                    :style="{ 'animation-delay': `${idx * 0.03}s` }"
                  >
                    <td class="py-3 px-4 text-[var(--text-primary)] break-words min-w-0">{{ ch.bot_name }}</td>
                    <td class="py-3 px-4 text-[var(--text-primary)] break-words min-w-0">{{ ch.name }}</td>
                    <td class="py-3 px-4 text-[var(--text-secondary)] font-mono text-xs break-all">{{ ch.chat_id }}</td>
                    <td class="py-3 px-4">
                      <span
                        class="text-xs px-2 py-1 rounded-full"
                        :class="ch.is_active ? 'bg-emerald-500/10 text-emerald-400' : 'bg-gray-500/10 text-gray-400'"
                      >
                        {{ ch.is_active ? $t('telegram.channels.active') : $t('telegram.channels.inactive') }}
                      </span>
                    </td>
                    <td class="py-3 px-4 flex gap-2">
                      <button
                        type="button"
                        class="btn-luxury-outline text-sm py-1.5 px-2"
                        @click="openEditChannel(ch)"
                      >
                        <i class="fas fa-edit" />
                      </button>
                      <button
                        type="button"
                        class="btn-luxury-outline text-sm py-1.5 px-2 text-red-400 hover:bg-red-500/10"
                        @click="confirmDeleteChannel(ch)"
                      >
                        <i class="fas fa-trash" />
                      </button>
                    </td>
                  </tr>
                </tbody>
              </table>
              </div>
              <p v-if="!manageChannelsList.length && !manageChannelsLoading" class="text-center text-gray-500 py-6">
                {{ $t('telegram.channels.noChannels') }}
              </p>
            </template>
          </div>

          <!-- Edit channel modal -->
          <div
            v-if="editingChannel"
            class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60"
            @click.self="editingChannel = null"
          >
            <div class="card-luxury max-w-md w-full p-4 space-y-3">
              <h3 class="text-lg font-semibold text-gold">{{ $t('telegram.channels.editChannel') }}</h3>
              <div>
                <label class="block text-sm font-medium text-gray-400 mb-1">{{ $t('telegram.channels.channelName') }}</label>
                <input v-model="editChannelForm.name" type="text" class="input-luxury w-full" required />
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-400 mb-1">{{ $t('telegram.channels.channelId') }}</label>
                <input v-model="editChannelForm.chat_id" type="text" class="input-luxury w-full" required />
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-400 mb-1">{{ $t('telegram.channels.bot') }}</label>
                <select v-model="editChannelForm.bot" class="input-luxury w-full" required>
                  <option value="">{{ $t('telegram.channels.selectBot') }}</option>
                  <option v-for="b in botsList" :key="b.id" :value="b.id">{{ b.name || b.display_name || `Bot #${b.id}` }}</option>
                </select>
              </div>
              <BaseCheckbox v-model="editChannelForm.is_active">{{ $t('telegram.channels.active') }}</BaseCheckbox>
              <div class="flex gap-2 pt-2">
                <button type="button" class="btn-luxury" :disabled="channelSaving" @click="saveEditChannel">
                  <LoadingSpinner v-if="channelSaving" class="w-5 h-5" />
                  <span v-else>{{ $t('common.save') }}</span>
                </button>
                <button type="button" class="btn-luxury-outline" @click="editingChannel = null">
                  {{ $t('common.cancel') }}
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- Tab 4: Automation -->
        <div
          v-else-if="activeTab === 'automation'"
          class="space-y-6 animate-fade-in-up"
        >
          <div class="card-luxury px-4 py-3">
            <h2 class="text-lg font-semibold text-gold mb-2">
              {{ $t('telegram.tabs.automation') }}
            </h2>
            <p class="text-sm text-gray-400 mb-4">
              {{ $t('telegram.automation.description') }}
            </p>

            <div class="mb-6">
              <BaseCheckbox v-model="autoPostOnUpdate" :disabled="automationSettingsSaving" @update:model-value="saveAutoPostOnUpdate">
                {{ $t('telegram.automation.autoPostOnUpdate') }}
              </BaseCheckbox>
              <p class="text-xs text-gray-500 mt-1 ml-8">
                {{ $t('telegram.automation.autoPostOnUpdateHint') }}
              </p>
            </div>

            <form @submit.prevent="addSchedule" class="space-y-3 border-t border-[var(--glass-border)] pt-4">
              <h3 class="text-sm font-medium text-gold">{{ $t('telegram.automation.addSchedule') }}</h3>
              <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-3">
                <div>
                  <label class="block text-sm font-medium text-gray-400 mb-1">{{ $t('telegram.channels.channelName') }}</label>
                  <select v-model="scheduleForm.channel" class="input-luxury w-full" required>
                    <option value="">{{ $t('telegram.automation.selectChannel') }}</option>
                    <option v-for="c in manageChannelsList" :key="c.id" :value="c.id">{{ c.name }}</option>
                  </select>
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-400 mb-1">{{ $t('telegram.automation.target') }}</label>
                  <select v-model="scheduleTargetType" class="input-luxury w-full">
                    <option value="category">{{ $t('telegram.automation.targetCategory') }}</option>
                    <option value="special">{{ $t('telegram.automation.targetSpecial') }}</option>
                  </select>
                </div>
                <div v-if="scheduleTargetType === 'category'">
                  <label class="block text-sm font-medium text-gray-400 mb-1">{{ $t('telegram.automation.category') }}</label>
                  <select v-model="scheduleForm.category" class="input-luxury w-full" required>
                    <option value="">{{ $t('telegram.automation.selectCategory') }}</option>
                    <option v-for="cat in categoriesList" :key="cat.id" :value="cat.id">{{ cat.name }}</option>
                  </select>
                </div>
                <div v-else>
                  <label class="block text-sm font-medium text-gray-400 mb-1">{{ $t('telegram.automation.specialPrice') }}</label>
                  <select v-model="scheduleForm.special_price_type" class="input-luxury w-full" required>
                    <option value="">{{ $t('telegram.automation.selectSpecial') }}</option>
                    <option v-for="s in specialPricesList" :key="s.id" :value="s.id">{{ s.name }}</option>
                  </select>
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-400 mb-1">{{ $t('telegram.automation.time') }}</label>
                  <input
                    v-model="scheduleForm.time_of_day"
                    type="time"
                    class="input-luxury w-full"
                    required
                  />
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-400 mb-1">{{ $t('telegram.automation.timezone') }}</label>
                  <input
                    v-model="scheduleForm.timezone"
                    type="text"
                    class="input-luxury w-full"
                    placeholder="Asia/Tehran"
                  />
                </div>
                <div class="flex items-end gap-2">
                  <BaseCheckbox v-model="scheduleForm.enabled">{{ $t('telegram.automation.enabled') }}</BaseCheckbox>
                  <button type="submit" class="btn-luxury" :disabled="scheduleSaving">
                    <LoadingSpinner v-if="scheduleSaving" class="w-5 h-5" />
                    <span v-else>{{ $t('telegram.automation.add') }}</span>
                  </button>
                </div>
              </div>
            </form>
          </div>

          <div class="card-luxury overflow-hidden w-full min-w-0 px-4 py-3">
            <h3 class="text-sm font-medium text-gold mb-3">{{ $t('telegram.automation.schedules') }}</h3>
            <div v-if="schedulesLoading" class="space-y-2">
              <div v-for="i in 3" :key="i" class="h-10 rounded bg-white/5 animate-pulse" />
            </div>
            <template v-else>
              <div class="w-full overflow-x-auto max-w-full">
                <table class="w-full text-sm min-w-[500px]">
                <thead>
                  <tr class="text-[var(--text-secondary)] border-b" style="border-color: var(--glass-border);">
                    <th class="text-left py-3 px-4 font-medium">{{ $t('telegram.channels.channelName') }}</th>
                    <th class="text-left py-3 px-4 font-medium">{{ $t('telegram.automation.target') }}</th>
                    <th class="text-left py-3 px-4 font-medium">{{ $t('telegram.automation.time') }}</th>
                    <th class="text-left py-3 px-4 font-medium">{{ $t('telegram.automation.timezone') }}</th>
                    <th class="text-left py-3 px-4 font-medium">{{ $t('common.status') }}</th>
                    <th class="text-left py-3 px-4 font-medium">{{ $t('common.actions') }}</th>
                  </tr>
                </thead>
                <tbody>
                  <tr
                    v-for="(sched, idx) in schedulesList"
                    :key="sched.id"
                    class="border-b transition-colors hover:bg-white/5 animate-fade-in-up"
                    :style="{ 'animation-delay': `${idx * 0.02}s` }"
                  >
                    <td class="py-3 px-4 text-[var(--text-primary)]">{{ sched.channel_name }}</td>
                    <td class="py-3 px-4 text-[var(--text-secondary)]">{{ scheduleTargetLabel(sched) }}</td>
                    <td class="py-3 px-4 text-[var(--text-secondary)]">{{ formatTime(sched.time_of_day) }}</td>
                    <td class="py-3 px-4 text-[var(--text-secondary)]">{{ sched.timezone || '—' }}</td>
                    <td class="py-3 px-4">
                      <span
                        class="text-xs px-2 py-1 rounded-full"
                        :class="sched.enabled ? 'bg-emerald-500/10 text-emerald-400' : 'bg-gray-500/10 text-gray-400'"
                      >
                        {{ sched.enabled ? $t('telegram.channels.active') : $t('telegram.channels.inactive') }}
                      </span>
                    </td>
                    <td class="py-3 px-4 flex gap-2">
                      <button
                        type="button"
                        class="btn-luxury-outline text-sm py-1.5 px-2"
                        @click="deleteSchedule(sched)"
                      >
                        <i class="fas fa-trash" />
                      </button>
                    </td>
                  </tr>
                </tbody>
              </table>
              </div>
              <p v-if="!schedulesList.length && !schedulesLoading" class="text-center text-gray-500 py-6">
                {{ $t('telegram.automation.noSchedules') }}
              </p>
            </template>
          </div>
        </div>

        <!-- Tab 5: Customers -->
        <div
          v-else-if="activeTab === 'customers'"
          class="space-y-6 animate-fade-in-up"
        >
          <div class="card-luxury px-4 py-3">
            <h2 class="text-lg font-semibold text-gold mb-2">
              {{ $t('telegram.tabs.customers') }}
            </h2>
            <p class="text-sm text-gray-400 mb-2">
              {{ $t('telegram.customers.description') }}
            </p>
            <p class="text-xs text-amber-400/90 mb-4">
              {{ $t('telegram.customers.staffTelegramHint') }}
            </p>
            <div v-if="customersLoading" class="flex justify-center py-8">
              <LoadingSpinner class="w-8 h-8 text-gold" />
            </div>
            <div v-else class="overflow-x-auto">
              <table class="w-full text-sm">
                <thead>
                  <tr class="border-b border-[var(--glass-border)] text-[var(--text-secondary)]">
                    <th class="text-left py-3 px-2 font-medium">{{ $t('telegram.customers.telegramId') }}</th>
                    <th class="text-left py-3 px-2 font-medium">{{ $t('telegram.customers.username') }}</th>
                    <th class="text-left py-3 px-2 font-medium">{{ $t('telegram.customers.name') }}</th>
                    <th class="text-left py-3 px-2 font-medium">{{ $t('telegram.customers.tag') }}</th>
                  </tr>
                </thead>
                <tbody>
                  <tr
                    v-for="c in customersList"
                    :key="c.id"
                    class="border-b border-[var(--glass-border)]/60"
                  >
                    <td class="py-3 px-2 font-mono text-xs">{{ c.telegram_user_id }}</td>
                    <td class="py-3 px-2">{{ c.username || '—' }}</td>
                    <td class="py-3 px-2">{{ [c.first_name, c.last_name].filter(Boolean).join(' ') || '—' }}</td>
                    <td class="py-3 px-2">
                      <span v-if="c.is_admin || c.display_tag === 'admin'" class="text-sm">
                        {{ $t('telegram.customers.tags.admin') }}
                      </span>
                      <select
                        v-else
                        class="input-luxury py-1 text-sm min-w-[8rem]"
                        :value="c.tag"
                        :disabled="customerTagSavingId === c.id"
                        @change="updateCustomerTag(c, $event.target.value)"
                      >
                        <option value="global">{{ $t('telegram.customers.tags.global') }}</option>
                        <option value="vip">{{ $t('telegram.customers.tags.vip') }}</option>
                        <option value="special">{{ $t('telegram.customers.tags.special') }}</option>
                      </select>
                    </td>
                  </tr>
                </tbody>
              </table>
              <p v-if="!customersList.length" class="text-center text-gray-500 py-6">
                {{ $t('telegram.customers.empty') }}
              </p>
            </div>
          </div>
        </div>
      </div>
            </Transition>
          </template>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import { useI18n } from 'vue-i18n'
import { useToast } from 'vue-toastification'
import { telegramApi, categoryApi, specialPriceApi } from '@/services/api'
import { createAppDateTimeFormat } from '@/utils/localeFormat.js'
import LoadingSpinner from '@/components/ui/LoadingSpinner.vue'
import BaseCheckbox from '@/components/ui/BaseCheckbox.vue'
import { useAuthStore } from '@/stores/auth'
import { useTelegramHubStore } from '@/stores/telegramHub'
import TelegramHubAdminPanels from './TelegramHubAdminPanels.vue'

const { t, locale } = useI18n()
const toast = useToast()
const auth = useAuthStore()
const telegramHub = useTelegramHubStore()

const requiresGate = computed(() => auth.isSuperAdmin || auth.isManager)
const showAdminNav = computed(() => requiresGate.value)
const hubLocked = ref(requiresGate.value && !telegramHub.isSessionValid)
const verifyLoading = ref(false)
const verifyError = ref('')
const verifiedBot = ref(telegramHub.isSessionValid ? telegramHub.verifiedBot : null)
const dashboard = ref(telegramHub.isSessionValid ? telegramHub.lastDashboard : null)
const dashboardError = ref('')
const adminSection = ref(
  telegramHub.lastAdminSection === 'publish'
    ? 'customersStatus'
    : (telegramHub.lastAdminSection || 'customersStatus')
)

const DASHBOARD_REFRESH_SECTIONS = new Set([
  'customersStatus',
  'notifications',
  'exchangeRequests',
  'reports',
  'analytics',
  'customerAnalysis',
])
const DASHBOARD_REFRESH_DEBOUNCE_MS = 300
let dashboardRefreshTimer = null

const adminCategories = [
  { id: 'customersStatus', labelKey: 'telegram.admin.nav.customersStatus', icon: 'fas fa-user-tag' },
  { id: 'notifications', labelKey: 'telegram.admin.nav.notifications', icon: 'fas fa-bell' },
  { id: 'reports', labelKey: 'telegram.admin.nav.reports', icon: 'fas fa-chart-pie' },
  { id: 'analytics', labelKey: 'telegram.admin.nav.analytics', icon: 'fas fa-chart-line' },
  { id: 'exchangeRequests', labelKey: 'telegram.admin.nav.exchangeRequests', icon: 'fas fa-exchange-alt' },
  { id: 'customerAnalysis', labelKey: 'telegram.admin.nav.customerAnalysis', icon: 'fas fa-user-clock' },
  { id: 'reengage', labelKey: 'telegram.admin.nav.reengage', icon: 'fas fa-paper-plane' },
  { id: 'botSettings', labelKey: 'telegram.admin.nav.botSettings', icon: 'fas fa-sliders-h' },
  { id: 'tools', labelKey: 'telegram.admin.nav.tools', icon: 'fas fa-tools' },
]

function selectAdminSection(id) {
  adminSection.value = id
  telegramHub.setAdminSection(id)
  if (id === 'tools' && !['messenger', 'bot', 'channels', 'automation', 'customers'].includes(activeTab.value)) {
    activeTab.value = 'messenger'
  }
  if (!DASHBOARD_REFRESH_SECTIONS.has(id)) return
  if (dashboardRefreshTimer) clearTimeout(dashboardRefreshTimer)
  dashboardRefreshTimer = setTimeout(() => {
    loadDashboard()
  }, DASHBOARD_REFRESH_DEBOUNCE_MS)
}

function openToolsTab(tabId) {
  adminSection.value = 'tools'
  telegramHub.setAdminSection('tools')
  activeTab.value = tabId
  if (tabId === 'customers') loadCustomers()
}

function botSelectLabel(bot) {
  if (!bot) return ''
  const handle = bot.username ? `@${bot.username}` : ''
  return handle || bot.display_name || bot.name || `Bot #${bot.id}`
}

async function onHubBotChange(event) {
  const id = Number(event?.target?.value)
  if (!id || Number(verifiedBot.value?.id) === id) return
  const fromList = botsList.value.find((b) => Number(b.id) === id) || { id }
  telegramHub.setVerifiedBot({
    ...fromList,
    id,
    username: fromList.username || '',
  })
  verifiedBot.value = telegramHub.verifiedBot
  dashboard.value = null
  telegramHub.setDashboard(null)
  await loadDashboard()
}

function onBotUpdated(data) {
  if (!data) return
  verifiedBot.value = {
    ...(verifiedBot.value || {}),
    ...data,
    username: verifiedBot.value?.username || '',
  }
  telegramHub.setVerifiedBot(verifiedBot.value)
}

async function runVerify() {
  await unlockHub({ force: true })
}

async function unlockHub({ force = false } = {}) {
  if (!requiresGate.value) {
    hubLocked.value = false
    await loadHubToolsData()
    return
  }
  const showGate = force || !telegramHub.isSessionValid
  if (showGate) {
    verifyLoading.value = true
    verifyError.value = ''
    hubLocked.value = true
  }
  try {
    const result = await telegramHub.ensureVerified({
      force,
      botId: telegramHub.verifiedBot?.id ?? null,
      userId: auth.user?.id ?? null,
    })
    if (!result?.ok || !result?.bot) {
      throw new Error(t('telegram.admin.gate.failedHint'))
    }
    verifiedBot.value = result.bot
    hubLocked.value = false
    if (result.fromCache) {
      dashboard.value = telegramHub.lastDashboard
      loadHubToolsData()
      loadDashboard()
      return
    }
    await loadDashboard()
    await loadHubToolsData()
  } catch (err) {
    telegramHub.clearSession()
    hubLocked.value = true
    verifiedBot.value = null
    dashboard.value = null
    verifyError.value =
      err?.response?.data?.message ||
      err?.response?.data?.detail ||
      err?.message ||
      t('telegram.admin.gate.failedHint')
  } finally {
    verifyLoading.value = false
  }
}

async function loadHubToolsData() {
  try {
    const { data } = await telegramApi.channels()
    channels.value = data ?? []
  } catch {
    channels.value = []
  }
  loadBots()
  loadManageChannels()
  loadCategoriesAndSpecialPrices()
  loadSchedules()
  loadAutomationSettings()
}

async function loadDashboard() {
  if (!verifiedBot.value?.id) return
  dashboardError.value = ''
  try {
    const { data } = await telegramApi.admin.dashboard({ bot_id: verifiedBot.value.id })
    dashboard.value = data
    telegramHub.setDashboard(data)
  } catch (err) {
    dashboardError.value =
      err?.response?.data?.message ||
      err?.response?.data?.detail ||
      t('telegram.admin.gate.dashboardError')
    if (!dashboard.value) {
      telegramHub.setDashboard(null)
    }
  }
}

const tabs = computed(() => {
  const base = [
    { id: 'messenger', labelKey: 'telegram.tabs.messenger', icon: 'fas fa-paper-plane' },
    { id: 'bot', labelKey: 'telegram.tabs.botSetup', icon: 'fas fa-robot' },
    { id: 'channels', labelKey: 'telegram.tabs.channels', icon: 'fas fa-broadcast-tower' },
    { id: 'automation', labelKey: 'telegram.tabs.automation', icon: 'fas fa-clock' },
  ]
  // Customer tags API is management / super_admin only (matches backend).
  if (auth.isSuperAdmin || auth.isManager) {
    base.push({
      id: 'customers',
      labelKey: 'telegram.tabs.customers',
      icon: 'fas fa-users',
    })
  }
  return base
})

const activeTab = ref('messenger')
const route = useRoute()

watch(() => route.query.tab, (tab) => {
  if (tab === 'botSetup') {
    activeTab.value = 'bot'
    if (showAdminNav.value) {
      adminSection.value = 'tools'
      telegramHub.setAdminSection('tools')
    }
  }
}, { immediate: true })

const channels = ref([])
const channelId = ref('')
const message = ref('')
const submitting = ref(false)

const botsList = ref([])
const botDeleteConfirm = ref(null)
const botDeleting = ref(false)

const hubBotOptions = computed(() => {
  const list = Array.isArray(botsList.value) ? [...botsList.value] : []
  const current = verifiedBot.value
  if (current?.id && !list.some((b) => Number(b.id) === Number(current.id))) {
    list.unshift(current)
  }
  return list
})

const manageChannelsList = ref([])
const manageChannelsLoading = ref(false)
const channelForm = ref({
  name: '',
  chat_id: '',
  bot: '',
  is_active: true,
})
const channelSaving = ref(false)
const editingChannel = ref(null)
const editChannelForm = ref({ name: '', chat_id: '', bot: '', is_active: true })

const categoriesList = ref([])
const specialPricesList = ref([])
const schedulesList = ref([])
const schedulesLoading = ref(false)
const scheduleForm = ref({
  channel: '',
  category: '',
  special_price_type: '',
  time_of_day: '09:00',
  timezone: 'Asia/Tehran',
  enabled: true,
})
const scheduleTargetType = ref('category')
const scheduleSaving = ref(false)
const autoPostOnUpdate = ref(false)
const automationSettingsSaving = ref(false)

const customersList = ref([])
const customersLoading = ref(false)
const customerTagSavingId = ref(null)

const bannerKey = ref('none')
const cashPrice = ref('')
const accountPrice = ref('')
const singlePrice = ref('')

const bannerOptions = [
  { value: 'none', labelKey: 'telegram.messenger.bannerNone' },
  { value: 'buy_gbp_double', labelKey: 'telegram.messenger.bannerBuyDouble' },
  { value: 'sell_gbp_double', labelKey: 'telegram.messenger.bannerSellDouble' },
  { value: 'generic_single', labelKey: 'telegram.messenger.bannerGenericSingle' },
]

const useDoublePrice = computed(() =>
  bannerKey.value === 'buy_gbp_double' || bannerKey.value === 'sell_gbp_double',
)

const selectedChannel = computed(() =>
  channels.value.find((c) => String(c.id) === String(channelId.value)) || null,
)

const selectedChannelInitials = computed(() => {
  const name = selectedChannel.value?.name || 'CH'
  return name
    .split(' ')
    .filter(Boolean)
    .slice(0, 2)
    .map((part) => part[0]?.toUpperCase() ?? '')
    .join('') || 'CH'
})

const selectedBannerLabel = computed(() => {
  const found = bannerOptions.find((b) => b.value === bannerKey.value)
  return found && found.value !== 'none' ? t(found.labelKey) : ''
})

const previewPriceLine = computed(() => {
  if (useDoublePrice.value) {
    const parts = []
    if (cashPrice.value) {
      parts.push(`Cash: ${cashPrice.value}`)
    }
    if (accountPrice.value) {
      parts.push(`Account: ${accountPrice.value}`)
    }
    return parts.join(' | ')
  }
  if (singlePrice.value) {
    return `Price: ${singlePrice.value}`
  }
  return ''
})

const previewTimestamp = computed(() => {
  const now = new Date()
  const appLoc = locale.value === 'fa' ? 'fa' : 'en'
  return createAppDateTimeFormat(appLoc, { hour: '2-digit', minute: '2-digit' }).format(now)
})

onMounted(async () => {
  await unlockHub()
})

onUnmounted(() => {
  if (dashboardRefreshTimer) clearTimeout(dashboardRefreshTimer)
})

watch(activeTab, (tab) => {
  if (tab === 'customers') loadCustomers()
})

async function loadCustomers() {
  customersLoading.value = true
  try {
    const { data } = await telegramApi.customers.list({
      bot_id: verifiedBot.value?.id,
    })
    customersList.value = Array.isArray(data) ? data : (data?.results ?? [])
  } catch {
    customersList.value = []
    toast.error(t('telegram.customers.loadError'))
  } finally {
    customersLoading.value = false
  }
}

async function updateCustomerTag(customer, tag) {
  if (!customer?.id || customer.tag === tag) return
  customerTagSavingId.value = customer.id
  try {
    const { data } = await telegramApi.customers.updateTag(customer.id, { tag })
    const idx = customersList.value.findIndex((c) => c.id === customer.id)
    if (idx >= 0) customersList.value[idx] = { ...customersList.value[idx], ...data }
    toast.success(t('telegram.customers.tagUpdated'))
  } catch (err) {
    toast.error(err?.response?.data?.detail || t('telegram.customers.tagError'))
  } finally {
    customerTagSavingId.value = null
  }
}

async function loadManageChannels() {
  manageChannelsLoading.value = true
  try {
    const { data } = await telegramApi.channelsManage.list()
    manageChannelsList.value = Array.isArray(data) ? data : (data?.results ?? [])
  } catch {
    manageChannelsList.value = []
  } finally {
    manageChannelsLoading.value = false
  }
}

async function addChannel() {
  if (!channelForm.value.bot) return
  channelSaving.value = true
  try {
    await telegramApi.channelsManage.create({
      name: channelForm.value.name.trim(),
      chat_id: channelForm.value.chat_id.trim(),
      bot: Number(channelForm.value.bot),
      is_active: channelForm.value.is_active,
    })
    toast.success(t('toast.saveSuccess'))
    channelForm.value = { name: '', chat_id: '', bot: '', is_active: true }
    await loadManageChannels()
    const { data } = await telegramApi.channels().catch(() => ({ data: [] }))
    channels.value = data ?? []
  } catch (err) {
    const msg = err.response?.data?.detail || t('toast.serverError')
    toast.error(typeof msg === 'string' ? msg : t('toast.serverError'))
  } finally {
    channelSaving.value = false
  }
}

function openEditChannel(ch) {
  editingChannel.value = ch
  editChannelForm.value = {
    name: ch.name,
    chat_id: ch.chat_id,
    bot: ch.bot,
    is_active: !!ch.is_active,
  }
}

async function saveEditChannel() {
  if (!editingChannel.value || !editChannelForm.value.bot) return
  channelSaving.value = true
  try {
    await telegramApi.channelsManage.update(editingChannel.value.id, {
      name: editChannelForm.value.name.trim(),
      chat_id: editChannelForm.value.chat_id.trim(),
      bot: Number(editChannelForm.value.bot),
      is_active: editChannelForm.value.is_active,
    })
    toast.success(t('toast.saveSuccess'))
    editingChannel.value = null
    await loadManageChannels()
    const { data } = await telegramApi.channels().catch(() => ({ data: [] }))
    channels.value = data ?? []
  } catch (err) {
    const msg = err.response?.data?.detail || t('toast.serverError')
    toast.error(typeof msg === 'string' ? msg : t('toast.serverError'))
  } finally {
    channelSaving.value = false
  }
}

function confirmDeleteChannel(ch) {
  if (!window.confirm(t('telegram.channels.deleteConfirm', { name: ch.name }))) return
  deleteChannel(ch)
}

async function deleteChannel(ch) {
  try {
    await telegramApi.channelsManage.delete(ch.id)
    toast.success(t('toast.deleteSuccess'))
    await loadManageChannels()
    const { data } = await telegramApi.channels().catch(() => ({ data: [] }))
    channels.value = data ?? []
  } catch (err) {
    toast.error(t('toast.serverError'))
  }
}

async function loadCategoriesAndSpecialPrices() {
  try {
    const [cRes, sRes] = await Promise.all([categoryApi.list(), specialPriceApi.list()])
    const cData = cRes.data
    categoriesList.value = Array.isArray(cData) ? cData : (cData?.results ?? [])
    const sData = sRes.data
    specialPricesList.value = Array.isArray(sData) ? sData : (sData?.results ?? [])
  } catch {
    categoriesList.value = []
    specialPricesList.value = []
  }
}

async function loadSchedules() {
  schedulesLoading.value = true
  try {
    const { data } = await telegramApi.autoPostConfig.list()
    schedulesList.value = Array.isArray(data) ? data : (data?.results ?? [])
  } catch {
    schedulesList.value = []
  } finally {
    schedulesLoading.value = false
  }
}

async function loadAutomationSettings() {
  try {
    const { data } = await telegramApi.automationSettings.get()
    autoPostOnUpdate.value = !!data?.auto_post_on_update
    if (data?.degraded && data?.detail) {
      toast.warning(String(data.detail))
    }
  } catch {
    autoPostOnUpdate.value = false
  }
}

async function saveAutoPostOnUpdate() {
  automationSettingsSaving.value = true
  try {
    await telegramApi.automationSettings.update({ auto_post_on_update: autoPostOnUpdate.value })
    toast.success(t('toast.saveSuccess'))
  } catch (err) {
    const detail = err?.response?.data?.detail
    toast.error(detail ? String(detail) : t('toast.serverError'))
    autoPostOnUpdate.value = !autoPostOnUpdate.value
  } finally {
    automationSettingsSaving.value = false
  }
}

function scheduleTargetLabel(sched) {
  if (sched.target_type === 'category' && sched.category) {
    const cat = categoriesList.value.find((c) => Number(c.id) === Number(sched.category))
    return cat ? cat.name : t('telegram.automation.targetCategory')
  }
  if (sched.target_type === 'special' && sched.special_price_type) {
    const sp = specialPricesList.value.find((s) => Number(s.id) === Number(sched.special_price_type))
    return sp ? sp.name : t('telegram.automation.targetSpecial')
  }
  return '—'
}

function formatTime(timeVal) {
  if (!timeVal) return '—'
  if (typeof timeVal === 'string' && /^\d{2}:\d{2}/.test(timeVal)) return timeVal.slice(0, 5)
  return String(timeVal)
}

async function addSchedule() {
  const channelId = scheduleForm.value.channel
  const isCategory = scheduleTargetType.value === 'category'
  const categoryId = isCategory ? scheduleForm.value.category : null
  const specialId = !isCategory ? scheduleForm.value.special_price_type : null
  if (!channelId || (!categoryId && !specialId)) {
    toast.error(t('validation.required'))
    return
  }
  scheduleSaving.value = true
  try {
    const payload = {
      channel: Number(channelId),
      time_of_day: scheduleForm.value.time_of_day || '09:00',
      timezone: (scheduleForm.value.timezone || 'Asia/Tehran').trim(),
      enabled: scheduleForm.value.enabled,
    }
    if (isCategory) {
      payload.category = Number(categoryId)
      payload.special_price_type = null
    } else {
      payload.category = null
      payload.special_price_type = Number(specialId)
    }
    await telegramApi.autoPostConfig.create(payload)
    toast.success(t('toast.saveSuccess'))
    scheduleForm.value = { channel: '', category: '', special_price_type: '', time_of_day: '09:00', timezone: 'Asia/Tehran', enabled: true }
    await loadSchedules()
  } catch (err) {
    const msg = err.response?.data?.detail || t('toast.serverError')
    toast.error(typeof msg === 'string' ? msg : t('toast.serverError'))
  } finally {
    scheduleSaving.value = false
  }
}

async function deleteSchedule(sched) {
  if (!window.confirm(t('telegram.automation.deleteScheduleConfirm'))) return
  try {
    await telegramApi.autoPostConfig.delete(sched.id)
    toast.success(t('toast.deleteSuccess'))
    await loadSchedules()
  } catch (err) {
    toast.error(t('toast.serverError'))
  }
}

async function loadBots() {
  try {
    const { data } = await telegramApi.bots.list()
    botsList.value = Array.isArray(data) ? data : (data?.results ?? [])
  } catch {
    botsList.value = []
  }
}

function formatBotCreatedAt(dateStr) {
  if (!dateStr) return '—'
  try {
    const d = new Date(dateStr)
    if (Number.isNaN(d.getTime())) return '—'
    const appLoc = locale.value === 'fa' ? 'fa' : 'en'
    return createAppDateTimeFormat(appLoc, { year: 'numeric', month: 'short', day: 'numeric' }).format(d)
  } catch {
    return '—'
  }
}

function openDeleteBotConfirm(bot) {
  botDeleteConfirm.value = { id: bot.id, name: bot.name || bot.display_name || `Bot #${bot.id}` }
}

async function confirmDeleteBot() {
  if (!botDeleteConfirm.value) return
  await deleteBot(botDeleteConfirm.value.id)
  botDeleteConfirm.value = null
}

async function deleteBot(id) {
  botDeleting.value = true
  try {
    await telegramApi.bots.delete(id)
    toast.success(t('toast.deleteSuccess'))
    await loadBots()
  } catch (err) {
    const msg = err.response?.data?.detail || t('toast.serverError')
    toast.error(typeof msg === 'string' ? msg : t('toast.serverError'))
  } finally {
    botDeleting.value = false
  }
}

async function handleSend() {
  const ch = channels.value.find((c) => String(c.id) === String(channelId.value))
  if (!ch) return
  submitting.value = true
  try {
    const payload = {
      bot_id: ch.bot,
      channel_id: Number(channelId.value),
      message: message.value?.trim() || previewPriceLine.value || selectedBannerLabel.value || '',
    }
    if (bannerKey.value && bannerKey.value !== 'none') {
      payload.banner_key = bannerKey.value
    }
    if (useDoublePrice.value) {
      if (cashPrice.value !== '' && cashPrice.value != null && !Number.isNaN(cashPrice.value)) {
        payload.cash_price = cashPrice.value
      }
      if (accountPrice.value !== '' && accountPrice.value != null && !Number.isNaN(accountPrice.value)) {
        payload.account_price = accountPrice.value
      }
    } else {
      if (singlePrice.value !== '' && singlePrice.value != null && !Number.isNaN(singlePrice.value)) {
        payload.price = singlePrice.value
      }
    }
    await telegramApi.sendMessage(payload)
  } finally {
    submitting.value = false
  }
}
</script>

<style scoped>
.modal-fade-enter-active,
.modal-fade-leave-active {
  transition: opacity 0.2s ease;
}
.modal-fade-enter-from,
.modal-fade-leave-to {
  opacity: 0;
}
</style>
