<template>
  <div class="template-editor template-editor-dark min-h-screen bg-[#0f172a] text-[var(--text-primary)]">
    <!-- Action Bar -->
    <header class="sticky top-0 z-40 border-b border-[var(--glass-border)] glass px-4 py-3 flex flex-wrap items-center justify-between gap-4">
      <router-link
        to="/templates"
        class="inline-flex items-center gap-2 text-[var(--text-secondary)] hover:text-[var(--primary)] transition-colors"
      >
        <i class="fas fa-arrow-left"></i>
        <span>{{ $t('templateEditor.backToTemplates') }}</span>
      </router-link>
      <div class="flex flex-wrap items-center gap-2">
        <span class="text-sm text-[var(--text-secondary)]">{{ $t('templateEditor.theme') }}:</span>
        <button
          v-for="name in themeNames"
          :key="name"
          type="button"
          :class="currentThemeName === name ? 'btn-luxury' : 'btn-luxury-outline'"
          class="text-sm py-1.5 px-3"
          @click="currentThemeName = name"
        >
          {{ name }}
        </button>
        <button type="button" class="btn-luxury-outline text-sm py-1.5 px-3" @click="cloneTheme">
          {{ $t('templateEditor.cloneTheme') }}
        </button>
        <button type="button" class="btn-luxury text-sm py-1.5 px-3" @click="saveConfig">
          {{ $t('templateEditor.saveConfig') }}
        </button>
        <button
          type="button"
          class="btn-luxury-outline text-sm py-1.5 px-3"
          :disabled="previewCooldown > 0"
          @click="renderRealPreview"
        >
          {{ $t('templateEditor.renderRealPreview') }}
          <span v-if="previewCooldown > 0">({{ previewCooldown }}s)</span>
        </button>
      </div>
    </header>

    <div v-if="loading" class="flex items-center justify-center p-12">
      <p class="text-[var(--text-secondary)]">{{ $t('templateEditor.loading') }}</p>
    </div>
    <div v-else-if="!template" class="flex items-center justify-center p-12">
      <p class="text-[var(--text-secondary)]">{{ $t('templateEditor.noTemplate') }}</p>
    </div>
    <div v-else class="relative min-h-[70vh]">
      <div class="template-editor-grid blur-md select-none pointer-events-none">
      <!-- Left Panel: Library Explorer (Accordion) -->
      <aside class="template-editor-left glass rounded-r-2xl border border-[var(--glass-border)] border-l-0 p-3 overflow-y-auto">
        <h2 class="text-xs font-semibold text-[var(--text-secondary)] uppercase tracking-wider mb-3 px-1">
          {{ $t('templateEditor.libraryExplorer') }}
        </h2>

        <!-- 1. Temporal Library -->
        <div class="library-accordion-section mb-2">
          <button
            type="button"
            class="library-accordion-header w-full flex items-center justify-between gap-2 px-3 py-2 rounded-xl text-left border border-[var(--glass-border)] bg-white/5 hover:bg-white/10 transition-colors"
            @click="accordionTemporal = !accordionTemporal"
          >
            <span class="flex items-center gap-2 text-sm font-medium text-[var(--primary)]">
              <i class="fas fa-clock"></i>
              {{ $t('templateEditor.libraryTemporal') }}
            </span>
            <i class="fas text-[var(--text-secondary)] text-xs transition-transform" :class="accordionTemporal ? 'fa-chevron-up' : 'fa-chevron-down'"></i>
          </button>
          <div v-show="accordionTemporal" class="library-accordion-content mt-1 pl-1 space-y-1">
            <p class="text-xs font-medium text-[var(--text-secondary)] px-2 py-0.5">{{ $t('templateEditor.temporalFarsi') }}</p>
            <div
              v-for="v in temporalFarsi"
              :key="v.key"
              draggable="true"
              class="variable-chip flex items-center gap-2 px-3 py-2 rounded-xl cursor-grab active:cursor-grabbing border border-[var(--glass-border)] bg-white/5 hover:bg-white/10 transition-colors"
              @dragstart="onVariableDragStart($event, v.key)"
            >
              <i class="fas fa-calendar-alt text-[var(--primary)] shrink-0"></i>
              <span class="text-sm truncate">{{ v.description || v.key }}</span>
            </div>
            <p class="text-xs font-medium text-[var(--text-secondary)] px-2 py-0.5 mt-2">{{ $t('templateEditor.temporalEnglish') }}</p>
            <div
              v-for="v in temporalEnglish"
              :key="v.key"
              draggable="true"
              class="variable-chip flex items-center gap-2 px-3 py-2 rounded-xl cursor-grab active:cursor-grabbing border border-[var(--glass-border)] bg-white/5 hover:bg-white/10 transition-colors"
              @dragstart="onVariableDragStart($event, v.key)"
            >
              <i class="fas fa-clock text-[var(--primary)] shrink-0"></i>
              <span class="text-sm truncate">{{ v.description || v.key }}</span>
            </div>
          </div>
        </div>

        <!-- 2. Branding Library -->
        <div class="library-accordion-section mb-2">
          <button
            type="button"
            class="library-accordion-header w-full flex items-center justify-between gap-2 px-3 py-2 rounded-xl text-left border border-[var(--glass-border)] bg-white/5 hover:bg-white/10 transition-colors"
            @click="accordionBranding = !accordionBranding"
          >
            <span class="flex items-center gap-2 text-sm font-medium text-[var(--primary)]">
              <i class="fas fa-shield-alt"></i>
              {{ $t('templateEditor.libraryBranding') }}
            </span>
            <i class="fas text-[var(--text-secondary)] text-xs transition-transform" :class="accordionBranding ? 'fa-chevron-up' : 'fa-chevron-down'"></i>
          </button>
          <div v-show="accordionBranding" class="library-accordion-content mt-1 pl-1 space-y-1">
            <p class="text-xs font-medium text-[var(--text-secondary)] px-2 py-0.5">{{ $t('templateEditor.brandingLogos') }}</p>
            <div
              draggable="true"
              class="variable-chip flex items-center gap-2 px-3 py-2 rounded-xl cursor-grab active:cursor-grabbing border border-[var(--glass-border)] bg-white/5 hover:bg-white/10 transition-colors"
              @dragstart="onVariableDragStart($event, 'logo')"
            >
              <i class="fas fa-image text-[var(--primary)] shrink-0"></i>
              <span class="text-sm truncate">{{ $t('templateEditor.brandingLogoMain') }}</span>
            </div>
            <p class="text-xs font-medium text-[var(--text-secondary)] px-2 py-0.5 mt-2">{{ $t('templateEditor.brandingIcons') }}</p>
            <div
              draggable="true"
              class="variable-chip flex items-center gap-2 px-3 py-2 rounded-xl cursor-grab active:cursor-grabbing border border-[var(--glass-border)] bg-white/5 hover:bg-white/10 transition-colors opacity-75"
              @dragstart="onVariableDragStart($event, 'pair_name')"
            >
              <i class="fas fa-coins text-[var(--primary)] shrink-0"></i>
              <span class="text-sm truncate">{{ $t('templateEditor.brandingIconFinance') }}</span>
            </div>
            <p class="text-xs font-medium text-[var(--text-secondary)] px-2 py-0.5 mt-2">{{ $t('templateEditor.brandingBadges') }}</p>
            <div
              v-for="badge in brandingBadges"
              :key="badge.id"
              draggable="true"
              class="variable-chip flex items-center gap-2 px-3 py-2 rounded-xl cursor-grab active:cursor-grabbing border border-[var(--glass-border)] bg-white/5 hover:bg-white/10 transition-colors"
              @dragstart="onBadgeDragStart($event, badge)"
            >
              <i class="fas fa-certificate text-[var(--primary)] shrink-0"></i>
              <span class="text-sm truncate">{{ badge.label }}</span>
            </div>
            <p class="text-xs text-[var(--text-secondary)] px-2 py-1 mt-1">{{ $t('templateEditor.libraryBrandingHint') }}</p>
            <p class="text-xs font-medium text-[var(--text-secondary)] px-2 py-0.5 mt-2">{{ $t('templateEditor.brandingOther') }}</p>
            <div
              v-for="v in brandingVariablesWithoutLogo"
              :key="v.key"
              draggable="true"
              class="variable-chip flex items-center gap-2 px-3 py-2 rounded-xl cursor-grab active:cursor-grabbing border border-[var(--glass-border)] bg-white/5 hover:bg-white/10 transition-colors"
              @dragstart="onVariableDragStart($event, v.key)"
            >
              <i class="fas fa-tag text-[var(--primary)] shrink-0"></i>
              <span class="text-sm truncate">{{ v.description || v.key }}</span>
            </div>
          </div>
        </div>

        <!-- 3. Category Libraries (dynamic tabs) -->
        <div class="library-accordion-section mb-2">
          <button
            type="button"
            class="library-accordion-header w-full flex items-center justify-between gap-2 px-3 py-2 rounded-xl text-left border border-[var(--glass-border)] bg-white/5 hover:bg-white/10 transition-colors"
            @click="accordionCategory = !accordionCategory"
          >
            <span class="flex items-center gap-2 text-sm font-medium text-[var(--primary)]">
              <i class="fas fa-coins"></i>
              {{ $t('templateEditor.libraryCategory') }}
            </span>
            <i class="fas text-[var(--text-secondary)] text-xs transition-transform" :class="accordionCategory ? 'fa-chevron-up' : 'fa-chevron-down'"></i>
          </button>
          <div v-show="accordionCategory" class="library-accordion-content mt-1 pl-1">
            <div class="flex gap-1 mb-2 border-b border-[var(--glass-border)] pb-1">
              <button
                v-for="tab in categoryLibraryTabs"
                :key="tab.id"
                type="button"
                class="px-2 py-1 rounded-lg text-xs font-medium transition-colors"
                :class="selectedCategoryTab === tab.id ? 'bg-[var(--primary)]/20 text-[var(--primary)]' : 'text-[var(--text-secondary)] hover:bg-white/5'"
                @click="selectedCategoryTab = tab.id"
              >
                {{ tab.label }}
              </button>
            </div>
            <template v-if="priceLabelChipsForCategory.length">
              <p class="text-xs font-medium text-[var(--text-secondary)] px-2 py-0.5">{{ $t('templateEditor.priceLabels') }}</p>
              <div class="space-y-1 mb-2">
                <div
                  v-for="pl in priceLabelChipsForCategory"
                  :key="pl.variable_key"
                  draggable="true"
                  class="variable-chip flex items-center gap-2 px-3 py-2 rounded-xl cursor-grab active:cursor-grabbing border border-[var(--glass-border)] bg-white/5 hover:bg-white/10 transition-colors"
                  @dragstart="onPriceLabelDragStart($event, pl)"
                >
                  <i class="fas fa-tag text-[var(--primary)] shrink-0"></i>
                  <span class="text-sm truncate">{{ pl.label }}</span>
                </div>
              </div>
            </template>
            <p class="text-xs font-medium text-[var(--text-secondary)] px-2 py-0.5">{{ $t('templateEditor.priceValues') }}</p>
            <div class="space-y-1">
              <div
                v-for="v in currentCategoryVariables"
                :key="v.key"
                draggable="true"
                class="variable-chip flex items-center gap-2 px-3 py-2 rounded-xl cursor-grab active:cursor-grabbing border border-[var(--glass-border)] bg-white/5 hover:bg-white/10 transition-colors"
                @dragstart="onVariableDragStart($event, v.key)"
              >
                <i class="fas fa-coins text-[var(--primary)] shrink-0"></i>
                <span class="text-sm truncate">{{ v.description || v.key }}</span>
              </div>
            </div>
          </div>
        </div>
      </aside>

      <!-- Center: Telegram Mockup + Canvas -->
      <main class="template-editor-center flex flex-col items-center p-4 overflow-auto">
        <!-- Background toggle -->
        <div class="flex flex-wrap items-center gap-2 mb-3 w-full max-w-2xl">
          <span class="text-sm text-[var(--text-secondary)]">{{ $t('templateEditor.background') }}:</span>
          <button
            type="button"
            :class="canvasBackgroundType === 'transparent' ? 'btn-luxury' : 'btn-luxury-outline'"
            class="text-sm py-1.5 px-3"
            @click="canvasBackgroundType = 'transparent'"
          >
            {{ $t('templateEditor.backgroundTransparent') }}
          </button>
          <button
            type="button"
            :class="canvasBackgroundType === 'solid' ? 'btn-luxury' : 'btn-luxury-outline'"
            class="text-sm py-1.5 px-3"
            @click="canvasBackgroundType = 'solid'"
          >
            {{ $t('templateEditor.backgroundSolid') }}
          </button>
          <button
            type="button"
            :class="canvasBackgroundType === 'image' ? 'btn-luxury' : 'btn-luxury-outline'"
            class="text-sm py-1.5 px-3"
            :disabled="!imageUrl"
            @click="canvasBackgroundType = 'image'"
          >
            {{ $t('templateEditor.backgroundImage') }}
          </button>
          <template v-if="canvasBackgroundType === 'solid'">
            <input
              v-model="config.canvas_background_color"
              type="color"
              class="w-10 h-8 rounded cursor-pointer border border-[var(--glass-border)] bg-transparent"
            />
            <input
              v-model="config.canvas_background_color"
              type="text"
              class="input-luxury w-24 py-1 text-sm"
              placeholder="#1a1a2e"
            />
          </template>
          <label class="flex items-center gap-2 ml-2 text-sm text-[var(--text-secondary)]">
            <input v-model="snapToGridEnabled" type="checkbox" class="rounded accent-[var(--primary)]" />
            {{ $t('templateEditor.snapToGrid') }}
          </label>
        </div>

        <!-- Telegram mockup frame (bubble) -->
        <div
          ref="canvasWrap"
          class="telegram-mockup rounded-3xl p-4 overflow-auto flex justify-center"
          style="max-height: calc(100vh - 180px);"
          @dragover.prevent
          @drop.prevent="onCanvasDrop"
        >
          <div
            ref="canvasInner"
            class="relative rounded-2xl overflow-hidden shadow-lg"
            :style="[canvasStyle, canvasBackgroundStyle]"
          >
            <!-- Background layer -->
            <div
              v-if="canvasBackgroundType === 'transparent'"
              class="absolute inset-0 canvas-checkerboard"
            />
            <div
              v-else-if="canvasBackgroundType === 'solid'"
              class="absolute inset-0"
              :style="{ backgroundColor: config.canvas_background_color || '#1a1a2e' }"
            />
            <div
              v-else-if="canvasBackgroundType === 'image' && imageUrl"
              class="absolute inset-0 bg-cover bg-center bg-no-repeat"
              :style="{ backgroundImage: `url(${imageUrl})` }"
            />
            <!-- Layers -->
            <div
              v-for="(layer, idx) in visibleLayers"
              :key="idx"
              class="absolute border-2 min-w-[2rem] min-h-[1rem]"
              :class="[
                selectedLayerIndex === idx ? 'border-[var(--primary)]' : 'border-transparent hover:border-[var(--text-secondary)]',
                (layer.locked && selectedLayerIndex === idx) ? 'cursor-default' : 'cursor-move',
              ]"
              :style="layerStyle(layer)"
              @mousedown.stop="startLayerDrag($event, layerIndexByVisible(idx))"
            >
              <span
                class="px-1 block"
                :style="layerTextStyle(layer)"
              >{{ layerSampleText(layer) }}</span>
            </div>
            <!-- Alignment guides (during drag) -->
            <template v-if="alignmentGuides.vertical.length || alignmentGuides.horizontal.length">
              <div
                v-for="x in alignmentGuides.vertical"
                :key="'v-' + x"
                class="absolute top-0 bottom-0 w-0.5 pointer-events-none z-10"
                :style="{ left: x + 'px', background: 'rgba(255,215,0,0.8)' }"
              />
              <div
                v-for="y in alignmentGuides.horizontal"
                :key="'h-' + y"
                class="absolute left-0 right-0 h-0.5 pointer-events-none z-10"
                :style="{ top: y + 'px', background: 'rgba(255,215,0,0.8)' }"
              />
            </template>
          </div>
        </div>
      </main>

      <!-- Right Panel: Layers + Inspector -->
      <aside class="template-editor-right glass rounded-l-2xl border border-[var(--glass-border)] border-r-0 p-4 overflow-y-auto flex flex-col gap-4">
        <!-- Layer list -->
        <section>
          <h3 class="text-sm font-semibold text-[var(--primary)] mb-2">{{ $t('templateEditor.layers') }}</h3>
          <div class="space-y-1">
            <div
              v-for="(layer, idx) in currentLayers"
              :key="idx"
              draggable="true"
              class="layer-row flex items-center gap-2 px-2 py-1.5 rounded-lg border transition-colors"
              :class="selectedLayerIndex === idx ? 'border-[var(--primary)] bg-[var(--primary)]/10' : 'border-transparent hover:bg-white/5'"
              @click="selectedLayerIndex = idx"
              @dragstart="onLayerListDragStart($event, idx)"
              @dragover.prevent="onLayerListDragOver($event, idx)"
              @drop.prevent="onLayerListDrop($event, idx)"
            >
              <i class="fas fa-grip-vertical text-[var(--text-secondary)] cursor-grab shrink-0"></i>
              <span class="flex-1 truncate text-sm">{{ layer.static_text || layer.variable_key || 'Layer' }}</span>
              <button
                type="button"
                class="p-1 rounded hover:bg-white/10"
                :title="layer.locked ? $t('templateEditor.unlockLayer') : $t('templateEditor.lockLayer')"
                @click.stop="layer.locked = !layer.locked"
              >
                <i class="fas text-sm" :class="layer.locked ? 'fa-lock text-[var(--primary)]' : 'fa-lock-open text-[var(--text-secondary)]'"></i>
              </button>
              <button
                type="button"
                class="p-1 rounded hover:bg-white/10"
                :title="layer.visible === false ? $t('templateEditor.showLayer') : $t('templateEditor.hideLayer')"
                @click.stop="layer.visible = layer.visible === false"
              >
                <i class="fas text-sm" :class="layer.visible !== false ? 'fa-eye text-[var(--text-secondary)]' : 'fa-eye-slash text-[var(--text-secondary)] opacity-60'"></i>
              </button>
            </div>
            <p v-if="!currentLayers.length" class="text-xs text-[var(--text-secondary)] py-2">{{ $t('templateEditor.noLayers') }}</p>
          </div>
        </section>

        <!-- Inspector (selected layer) - Precision panels -->
        <section v-if="selectedLayer" class="border-t border-[var(--glass-border)] pt-4 space-y-4">
          <h3 class="text-sm font-semibold text-[var(--primary)]">{{ $t('templateEditor.selectedLayer') }}</h3>

          <div>
            <label class="block text-[var(--text-secondary)] mb-1 text-xs">{{ $t('templateEditor.variableKey') }}</label>
            <select
              v-model="selectedLayer.variable_key"
              class="input-luxury w-full py-2 text-sm"
            >
              <option v-for="v in variables" :key="v.key" :value="v.key">{{ v.key }}</option>
            </select>
          </div>

          <!-- Typography -->
          <div class="inspector-block">
            <h4 class="text-xs font-semibold text-[var(--primary)] mb-2 uppercase tracking-wider">{{ $t('templateEditor.inspectorTypography') }}</h4>
            <div class="space-y-3 text-sm">
              <div>
                <label class="block text-[var(--text-secondary)] mb-1">{{ $t('templateEditor.font') }}</label>
                <select v-model="selectedLayer.font" class="input-luxury w-full py-2 text-sm">
                  <option value="">—</option>
                  <option v-for="f in fonts" :key="f.filename" :value="f.filename">{{ f.display_name }}</option>
                </select>
              </div>
              <div>
                <label class="block text-[var(--text-secondary)] mb-1">{{ $t('templateEditor.size') }} ({{ selectedLayer.size || 24 }})</label>
                <input
                  v-model.number="selectedLayer.size"
                  type="range"
                  min="8"
                  max="120"
                  class="w-full h-2 rounded-lg appearance-none bg-[var(--bg-input)] accent-[var(--primary)]"
                />
              </div>
              <div>
                <label class="block text-[var(--text-secondary)] mb-1">{{ $t('templateEditor.fontWeight') }}</label>
                <select v-model="selectedLayer.font_weight" class="input-luxury w-full py-2 text-sm">
                  <option value="normal">Normal</option>
                  <option value="bold">Bold</option>
                </select>
              </div>
              <div>
                <label class="block text-[var(--text-secondary)] mb-1">{{ $t('templateEditor.tracking') }} ({{ selectedLayer.letter_spacing ?? 0 }})</label>
                <input
                  v-model.number="selectedLayer.letter_spacing"
                  type="range"
                  min="-2"
                  max="8"
                  step="0.5"
                  class="w-full h-2 rounded-lg appearance-none bg-[var(--bg-input)] accent-[var(--primary)]"
                />
              </div>
              <div>
                <label class="block text-[var(--text-secondary)] mb-1">{{ $t('templateEditor.align') }}</label>
                <select v-model="selectedLayer.align" class="input-luxury w-full py-2 text-sm">
                  <option value="left">left</option>
                  <option value="center">center</option>
                  <option value="right">right</option>
                </select>
              </div>
              <div>
                <label class="block text-[var(--text-secondary)] mb-1">{{ $t('templateEditor.maxWidth') }}</label>
                <input
                  v-model.number="selectedLayer.max_width"
                  type="number"
                  min="0"
                  class="input-luxury w-full py-2 text-sm"
                  placeholder="—"
                />
              </div>
            </div>
          </div>

          <!-- Appearance -->
          <div class="inspector-block">
            <h4 class="text-xs font-semibold text-[var(--primary)] mb-2 uppercase tracking-wider">{{ $t('templateEditor.inspectorAppearance') }}</h4>
            <div class="space-y-3 text-sm">
              <div>
                <label class="block text-[var(--text-secondary)] mb-1">{{ $t('templateEditor.color') }}</label>
                <div class="flex gap-2 items-center">
                  <input
                    v-model="selectedLayer.color"
                    type="color"
                    class="w-10 h-8 rounded cursor-pointer border border-[var(--glass-border)] bg-transparent shrink-0"
                  />
                  <input
                    v-model="selectedLayer.color"
                    type="text"
                    class="input-luxury flex-1 py-2 text-sm"
                    placeholder="#ffffff"
                  />
                </div>
              </div>
              <div>
                <label class="block text-[var(--text-secondary)] mb-1">{{ $t('templateEditor.colorPresets') }}</label>
                <div class="flex flex-wrap gap-1.5">
                  <button type="button" class="w-8 h-8 rounded-lg border-2 border-[var(--glass-border)] hover:border-[var(--primary)] transition-colors" style="background:#D4AF37" title="Gold" @click="selectedLayer.color = '#D4AF37'" />
                  <button type="button" class="w-8 h-8 rounded-lg border-2 border-[var(--glass-border)] hover:border-[var(--primary)] transition-colors bg-white" title="White" @click="selectedLayer.color = '#ffffff'" />
                  <button type="button" class="w-8 h-8 rounded-lg border-2 border-[var(--glass-border)] hover:border-[var(--primary)] transition-colors" style="background:#10B981" title="Emerald" @click="selectedLayer.color = '#10B981'" />
                  <button type="button" class="w-8 h-8 rounded-lg border-2 border-[var(--glass-border)] hover:border-[var(--primary)] transition-colors" style="background:#F43F5E" title="Rose" @click="selectedLayer.color = '#F43F5E'" />
                </div>
              </div>
              <div>
                <label class="block text-[var(--text-secondary)] mb-1">{{ $t('templateEditor.stylePreset') }}</label>
                <div class="flex flex-wrap gap-2">
                  <button type="button" class="btn-luxury-outline text-xs py-1.5 px-2" @click="applyPreset('title')">{{ $t('templateEditor.presetTitle') }}</button>
                  <button type="button" class="btn-luxury-outline text-xs py-1.5 px-2" @click="applyPreset('price')">{{ $t('templateEditor.presetPrice') }}</button>
                  <button type="button" class="btn-luxury-outline text-xs py-1.5 px-2" @click="applyPreset('date')">{{ $t('templateEditor.presetDate') }}</button>
                </div>
              </div>
            </div>
          </div>

          <!-- Position -->
          <div class="inspector-block">
            <h4 class="text-xs font-semibold text-[var(--primary)] mb-2 uppercase tracking-wider">{{ $t('templateEditor.inspectorPosition') }}</h4>
            <div class="space-y-3 text-sm">
              <div class="grid grid-cols-2 gap-2">
                <div>
                  <label class="block text-[var(--text-secondary)] mb-0.5">X</label>
                  <input v-model.number="selectedLayer.x" type="number" min="0" class="input-luxury w-full py-1.5 text-sm" />
                </div>
                <div>
                  <label class="block text-[var(--text-secondary)] mb-0.5">Y</label>
                  <input v-model.number="selectedLayer.y" type="number" min="0" class="input-luxury w-full py-1.5 text-sm" />
                </div>
              </div>
              <div class="grid grid-cols-2 gap-2">
                <button type="button" class="btn-luxury-outline text-xs py-1.5" @click="nudgeLayer(-1, 0)">←</button>
                <button type="button" class="btn-luxury-outline text-xs py-1.5" @click="nudgeLayer(1, 0)">→</button>
                <button type="button" class="btn-luxury-outline text-xs py-1.5" @click="nudgeLayer(0, -1)">↑</button>
                <button type="button" class="btn-luxury-outline text-xs py-1.5" @click="nudgeLayer(0, 1)">↓</button>
              </div>
              <div>
                <label class="block text-[var(--text-secondary)] mb-1">{{ $t('templateEditor.rotate') }} ({{ selectedLayer.rotation ?? 0 }}°)</label>
                <input
                  v-model.number="selectedLayer.rotation"
                  type="range"
                  min="0"
                  max="360"
                  class="w-full h-2 rounded-lg appearance-none bg-[var(--bg-input)] accent-[var(--primary)]"
                />
              </div>
              <div>
                <label class="block text-[var(--text-secondary)] mb-1">{{ $t('templateEditor.scale') }} ({{ ((selectedLayer.scale ?? 1) * 100).toFixed(0) }}%)</label>
                <input
                  v-model.number="selectedLayer.scale"
                  type="range"
                  min="0.5"
                  max="2"
                  step="0.05"
                  class="w-full h-2 rounded-lg appearance-none bg-[var(--bg-input)] accent-[var(--primary)]"
                />
              </div>
              <div>
                <label class="block text-[var(--text-secondary)] mb-1">{{ $t('templateEditor.opacity') }} ({{ ((selectedLayer.opacity ?? 1) * 100).toFixed(0) }}%)</label>
                <input
                  :value="(selectedLayer.opacity ?? 1) * 100"
                  type="range"
                  min="0"
                  max="100"
                  class="w-full h-2 rounded-lg appearance-none bg-[var(--bg-input)] accent-[var(--primary)]"
                  @input="selectedLayer.opacity = Number($event.target.value) / 100"
                />
              </div>
              <div class="flex gap-2 pt-1">
                <button type="button" class="btn-luxury-outline text-xs py-1.5 flex-1" @click="moveLayerUp">{{ $t('templateEditor.moveUp') }}</button>
                <button type="button" class="btn-luxury-outline text-xs py-1.5 flex-1" @click="moveLayerDown">{{ $t('templateEditor.moveDown') }}</button>
              </div>
              <button type="button" class="btn-luxury-outline text-sm w-full text-red-400 hover:bg-red-500/10" @click="deleteLayer">
                {{ $t('common.delete') }} {{ $t('templateEditor.layer') }}
              </button>
            </div>
          </div>
        </section>
      </aside>
    </div>
    <div class="absolute inset-0 flex items-center justify-center bg-[#0f172a]/50 backdrop-blur-sm z-10">
      <p class="text-2xl font-semibold text-[var(--primary)] border border-gold/50 rounded-2xl px-8 py-5 bg-black/50 shadow-xl">
        هنوز کامل نشده
      </p>
    </div>
    </div>

    <!-- Real preview modal -->
    <div
      v-if="realPreviewUrl"
      class="fixed inset-0 z-50 flex items-center justify-center bg-black/70"
      @click.self="realPreviewUrl = null"
    >
      <div class="max-w-[90vw] max-h-[90vh] overflow-auto rounded-2xl glass p-4">
        <img :src="realPreviewUrl" alt="Preview" class="max-w-full max-h-[85vh] object-contain rounded-xl" />
        <button type="button" class="btn-luxury mt-3 w-full" @click="realPreviewUrl = null">
          {{ $t('common.close') }}
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useToast } from 'vue-toastification'
import { templateEditorApi, categoryApi } from '@/services/api'
import i18n from '@/i18n'

const route = useRoute()
const toast = useToast()
const templateId = computed(() => route.params.id)

const loading = ref(true)
const template = ref(null)
const variables = ref([])
const fonts = ref([])
const config = ref({
  base_width: 1080,
  base_height: 1080,
  themes: {},
  usage_theme_map: {},
  canvas_background_type: 'image',
  canvas_background_color: '#1a1a2e',
})
const currentThemeName = ref('default')
const selectedLayerIndex = ref(null)
const previewCooldown = ref(0)
const realPreviewUrl = ref(null)
const canvasWrap = ref(null)
const canvasInner = ref(null)
const accordionTemporal = ref(true)
const accordionBranding = ref(true)
const accordionCategory = ref(true)
const selectedCategoryTab = ref('gbp')
const categoriesFromApi = ref([])
const snapToGridEnabled = ref(true)
const GRID_SIZE = 8
const alignmentGuides = ref({ vertical: [], horizontal: [] })
const ALIGNMENT_THRESHOLD = 6

const BASE = 1080

const imageUrl = computed(() => {
  if (!template.value?.image) return ''
  const img = template.value.image
  if (typeof img === 'string' && (img.startsWith('http') || img.startsWith('/'))) return img
  if (img?.url) return img.url
  return `/media/${img}`
})

const baseWidth = computed(() => config.value.base_width || BASE)
const baseHeight = computed(() => config.value.base_height || BASE)

const canvasStyle = computed(() => ({
  width: baseWidth.value + 'px',
  height: baseHeight.value + 'px',
}))

const canvasBackgroundType = computed({
  get: () => config.value.canvas_background_type || 'image',
  set: (v) => { config.value.canvas_background_type = v },
})

const canvasBackgroundStyle = computed(() => {
  if (canvasBackgroundType.value === 'solid') {
    return { backgroundColor: config.value.canvas_background_color || '#1a1a2e' }
  }
  return {}
})

const themeNames = computed(() => {
  const t = config.value.themes || {}
  const names = Object.keys(t)
  return names.length ? names : ['default']
})

const currentLayers = computed(() => {
  const themes = config.value.themes || {}
  let theme = themes[currentThemeName.value]
  if (!theme) {
    if (themeNames.value[0]) currentThemeName.value = themeNames.value[0]
    theme = themes[currentThemeName.value]
    if (!theme) return []
  }
  return theme.layers || []
})

const visibleLayers = computed(() => {
  const layers = currentLayers.value
  return layers.map((l, i) => ({ ...l, _index: i })).filter((l) => l.visible !== false)
})

function layerIndexByVisible(visibleIdx) {
  const layers = currentLayers.value
  let j = 0
  for (let i = 0; i < layers.length; i++) {
    if (layers[i].visible !== false) {
      if (j === visibleIdx) return i
      j++
    }
  }
  return 0
}

const selectedLayer = computed(() => {
  const idx = selectedLayerIndex.value
  const layers = currentLayers.value
  if (idx == null || idx < 0 || idx >= layers.length) return null
  return layers[idx]
})

const temporalVariables = computed(() =>
  variables.value.filter((v) => v.group === 'dates')
)
const TEMPORAL_FARSI_KEYS = ['date_fa', 'farsi_date', 'farsi_weekday', 'time']
const temporalFarsi = computed(() =>
  temporalVariables.value.filter((v) => TEMPORAL_FARSI_KEYS.includes(v.key))
)
const temporalEnglish = computed(() =>
  temporalVariables.value.filter((v) => !TEMPORAL_FARSI_KEYS.includes(v.key))
)
const brandingVariables = computed(() =>
  variables.value.filter((v) => v.group === 'branding')
)
const brandingBadges = [
  { id: 'official', label: 'قیمت رسمی' },
  { id: 'verified', label: 'تایید شده' },
]
const brandingVariablesWithoutLogo = computed(() =>
  brandingVariables.value.filter((v) => v.key !== 'logo')
)
const categoryLibraryTabs = computed(() => {
  const cats = categoriesFromApi.value
  if (cats && cats.length) {
    const fromApi = cats.map((c) => ({ id: c.slug || String(c.id), label: c.name, slug: c.slug || '' }))
    return [...fromApi, { id: 'special', label: 'Special', slug: 'special' }]
  }
  return [
    { id: 'gbp', label: 'GBP / Category', slug: 'gbp' },
    { id: 'tether', label: 'Tether', slug: 'tether' },
    { id: 'special', label: 'Special', slug: 'special' },
  ]
})
const currentCategoryVariables = computed(() => {
  const tab = selectedCategoryTab.value
  const priceVars = variables.value.filter((v) => v.group === 'prices')
  if (tab === 'special') return priceVars.filter((v) => v.key === 'price' || v.key.startsWith('special_'))
  if (tab === 'tether') return priceVars.filter((v) => v.key.startsWith('tether_'))
  return priceVars.filter((v) => !v.key.startsWith('tether_') && v.key !== 'price' && !v.key.startsWith('special_'))
})
const priceLabelChipsForCategory = computed(() => {
  const tab = selectedCategoryTab.value
  if (tab === 'tether') {
    return [
      { label: 'خرید تتر به تومن', variable_key: 'tether_buy_irr' },
      { label: 'فروش تتر به تومن', variable_key: 'tether_sell_irr' },
      { label: 'خرید تتر پوند', variable_key: 'tether_buy_gbp' },
      { label: 'فروش تتر پوند', variable_key: 'tether_sell_gbp' },
    ]
  }
  if (tab === 'special') return []
  return [
    { label: 'خرید نقدی', variable_key: 'price_cash_buy' },
    { label: 'فروش نقدی', variable_key: 'price_cash_sell' },
    { label: 'خرید از حساب', variable_key: 'price_account_buy' },
    { label: 'فروش از حساب', variable_key: 'price_account_sell' },
  ]
})
function onPriceLabelDragStart(e, pl) {
  e.dataTransfer.setData('application/json', JSON.stringify({ price_label: pl }))
  e.dataTransfer.effectAllowed = 'copy'
}

function snapToGrid(val) {
  if (!snapToGridEnabled.value) return val
  return Math.round(val / GRID_SIZE) * GRID_SIZE
}

function ensureThemes() {
  if (!config.value.themes || !Object.keys(config.value.themes).length) {
    config.value.themes = { default: { layers: [] } }
    currentThemeName.value = 'default'
  }
  if (!config.value.themes[currentThemeName.value]) {
    currentThemeName.value = Object.keys(config.value.themes)[0] || 'default'
  }
}

function layerStyle(layer) {
  const x = layer.x ?? 0
  const y = layer.y ?? 0
  const rot = layer.rotation ?? 0
  const scale = layer.scale ?? 1
  return {
    left: x + 'px',
    top: y + 'px',
    transform: `rotate(${rot}deg) scale(${scale})`,
    transformOrigin: 'top left',
    color: layer.color || '#ffffff',
    fontSize: (layer.size || 24) + 'px',
    textAlign: layer.align || 'left',
    maxWidth: layer.max_width ? layer.max_width + 'px' : 'none',
    opacity: layer.opacity != null ? layer.opacity : 1,
  }
}

function layerTextStyle(layer) {
  const style = {
    color: layer.color || '#ffffff',
    fontSize: (layer.size || 24) + 'px',
    textAlign: layer.align || 'left',
    fontWeight: layer.font_weight || 'normal',
    letterSpacing: (layer.letter_spacing ?? 0) + 'px',
    textShadow: '0 0 2px rgba(0,0,0,0.8), 0 1px 2px rgba(0,0,0,0.8)',
  }
  if (layer.opacity != null) style.opacity = layer.opacity
  return style
}

const DUMMY_NUMBER = '65,400'
function layerSampleText(layer) {
  if (layer.static_text) return layer.static_text
  const key = layer.variable_key || layer.key || ''
  const v = variables.value.find((x) => x.key === key)
  if (v?.type === 'number') return DUMMY_NUMBER
  return key ? key.replace(/_/g, ' ').replace(/\b\w/g, (c) => c.toUpperCase()) : 'Sample'
}

function onBadgeDragStart(e, badge) {
  e.dataTransfer.setData('application/json', JSON.stringify({ static_text: badge.label }))
  e.dataTransfer.effectAllowed = 'copy'
}

function onVariableDragStart(e, key) {
  e.dataTransfer.setData('application/json', JSON.stringify({ variable_key: key }))
  e.dataTransfer.effectAllowed = 'copy'
}

function onCanvasDrop(e) {
  try {
    const raw = e.dataTransfer.getData('application/json')
    if (!raw) return
    const payload = JSON.parse(raw)
    const variable_key = payload.variable_key
    const static_text = payload.static_text
    const price_label = payload.price_label
    const el = canvasInner.value || canvasWrap.value
    const rect = el?.getBoundingClientRect()
    if (!rect) return
    let x = snapToGrid(Math.max(0, ((e.clientX - rect.left) / rect.width) * baseWidth.value - 20))
    let y = snapToGrid(Math.max(0, ((e.clientY - rect.top) / rect.height) * baseHeight.value - 10))
    ensureThemes()
    const themes = config.value.themes
    if (!themes[currentThemeName.value]) themes[currentThemeName.value] = { layers: [] }
    const layers = themes[currentThemeName.value].layers
    const baseLayer = {
      x,
      y,
      size: 32,
      color: '#D4AF37',
      align: 'left',
      z_index: layers.length,
      visible: true,
      locked: false,
      rotation: 0,
      scale: 1,
      opacity: 1,
    }
    if (price_label) {
      const { label, variable_key: vk } = price_label
      layers.push({
        ...baseLayer,
        variable_key: 'pair_name',
        static_text: label,
      })
      layers.push({
        ...baseLayer,
        x: x + 20,
        variable_key: vk,
      })
      selectedLayerIndex.value = layers.length - 1
      return
    }
    if (static_text) {
      layers.push({
        ...baseLayer,
        variable_key: 'pair_name',
        static_text,
      })
      selectedLayerIndex.value = layers.length - 1
      return
    }
    if (!variable_key) return
    layers.push({
      ...baseLayer,
      variable_key,
    })
    selectedLayerIndex.value = layers.length - 1
  } catch (_) {}
}

let dragLayerIndex = null
let dragStartX = 0
let dragStartY = 0
let dragStartLeft = 0
let dragStartTop = 0
let dragScaleX = 1
let dragScaleY = 1

function startLayerDrag(e, idx) {
  const layer = currentLayers.value[idx]
  if (layer?.locked) return
  selectedLayerIndex.value = idx
  if (!layer) return
  const el = canvasInner.value || canvasWrap.value
  const rect = el?.getBoundingClientRect()
  if (rect) {
    dragScaleX = baseWidth.value / rect.width
    dragScaleY = baseHeight.value / rect.height
  } else {
    dragScaleX = 1
    dragScaleY = 1
  }
  dragLayerIndex = idx
  dragStartX = e.clientX
  dragStartY = e.clientY
  dragStartLeft = layer.x ?? 0
  dragStartTop = layer.y ?? 0
  window.addEventListener('mousemove', onLayerDragMove)
  window.addEventListener('mouseup', onLayerDragEnd)
}

function onLayerDragMove(e) {
  if (dragLayerIndex == null) return
  const layer = currentLayers.value[dragLayerIndex]
  if (!layer) return
  const dx = (e.clientX - dragStartX) * dragScaleX
  const dy = (e.clientY - dragStartY) * dragScaleY
  let newX = Math.max(0, dragStartLeft + dx)
  let newY = Math.max(0, dragStartTop + dy)
  const W = baseWidth.value
  const H = baseHeight.value
  const layers = currentLayers.value
  const verticalGuides = []
  const horizontalGuides = []
  function snapTo(val, targets) {
    for (const t of targets) {
      if (Math.abs(val - t) <= ALIGNMENT_THRESHOLD) return t
    }
    return null
  }
  const canvasXTargets = [0, W / 2, W]
  const canvasYTargets = [0, H / 2, H]
  for (let i = 0; i < layers.length; i++) {
    if (i === dragLayerIndex) continue
    const l = layers[i]
    canvasXTargets.push(l.x ?? 0)
    canvasYTargets.push(l.y ?? 0)
  }
  const snappedX = snapTo(newX, canvasXTargets)
  const snappedY = snapTo(newY, canvasYTargets)
  if (snappedX != null) {
    newX = snappedX
    verticalGuides.push(snappedX)
  }
  if (snappedY != null) {
    newY = snappedY
    horizontalGuides.push(snappedY)
  }
  alignmentGuides.value = { vertical: verticalGuides, horizontal: horizontalGuides }
  const finalX = snapToGridEnabled.value && snappedX == null ? snapToGrid(newX) : newX
  const finalY = snapToGridEnabled.value && snappedY == null ? snapToGrid(newY) : newY
  layer.x = finalX
  layer.y = finalY
}

function onLayerDragEnd() {
  dragLayerIndex = null
  alignmentGuides.value = { vertical: [], horizontal: [] }
  window.removeEventListener('mousemove', onLayerDragMove)
  window.removeEventListener('mouseup', onLayerDragEnd)
}

let layerListDragFrom = null
function onLayerListDragStart(e, idx) {
  layerListDragFrom = idx
  e.dataTransfer.setData('text/plain', String(idx))
  e.dataTransfer.effectAllowed = 'move'
}
function onLayerListDragOver(e, idx) {
  e.preventDefault()
}
function onLayerListDrop(e, toIdx) {
  e.preventDefault()
  const from = layerListDragFrom
  if (from == null || from === toIdx) return
  const theme = config.value.themes[currentThemeName.value]
  if (!theme?.layers) return
  const arr = theme.layers
  const item = arr[from]
  arr.splice(from, 1)
  const newIdx = from < toIdx ? toIdx - 1 : toIdx
  arr.splice(newIdx, 0, item)
  selectedLayerIndex.value = newIdx
  layerListDragFrom = null
}

function nudgeLayer(dx, dy) {
  const layer = selectedLayer.value
  if (!layer) return
  layer.x = Math.max(0, snapToGrid((layer.x || 0) + dx))
  layer.y = Math.max(0, snapToGrid((layer.y || 0) + dy))
}

function moveLayerUp() {
  const idx = selectedLayerIndex.value
  if (idx == null || idx <= 0) return
  const theme = config.value.themes[currentThemeName.value]
  if (!theme?.layers) return
  const arr = theme.layers
  ;[arr[idx - 1], arr[idx]] = [arr[idx], arr[idx - 1]]
  selectedLayerIndex.value = idx - 1
}

function moveLayerDown() {
  const idx = selectedLayerIndex.value
  if (idx == null || idx >= currentLayers.value.length - 1) return
  const theme = config.value.themes[currentThemeName.value]
  if (!theme?.layers) return
  const arr = theme.layers
  ;[arr[idx], arr[idx + 1]] = [arr[idx + 1], arr[idx]]
  selectedLayerIndex.value = idx + 1
}

function deleteLayer() {
  const idx = selectedLayerIndex.value
  const theme = config.value.themes[currentThemeName.value]
  if (theme?.layers && idx != null) {
    theme.layers.splice(idx, 1)
    selectedLayerIndex.value = null
  }
}

const PRESETS = {
  title: { size: 48, font_weight: 'bold', color: '#ffffff' },
  price: { size: 36, font_weight: 'normal', color: '#FFD700' },
  date: { size: 18, font_weight: 'normal', color: '#9CA3AF' },
}
function applyPreset(name) {
  const layer = selectedLayer.value
  if (!layer) return
  const p = PRESETS[name]
  if (!p) return
  Object.assign(layer, p)
}

function cloneTheme() {
  const name = currentThemeName.value + '_copy'
  const themes = config.value.themes || {}
  const src = themes[currentThemeName.value]
  if (!src) return
  themes[name] = { layers: JSON.parse(JSON.stringify(src.layers || [])) }
  config.value.themes = themes
  currentThemeName.value = name
  toast.success(i18n.global.t('toast.saveSuccess'))
}

async function saveConfig() {
  try {
    await templateEditorApi.updateConfig(templateId.value, config.value)
    toast.success(i18n.global.t('toast.saveSuccess'))
  } catch (err) {
    toast.error(err?.response?.data?.detail || i18n.global.t('errors.unknown'))
  }
}

const PREVIEW_COOLDOWN_SEC = 3
async function renderRealPreview() {
  if (previewCooldown.value > 0) return
  try {
    const { data } = await templateEditorApi.preview(templateId.value, config.value, currentThemeName.value)
    const url = URL.createObjectURL(data)
    if (realPreviewUrl.value) URL.revokeObjectURL(realPreviewUrl.value)
    realPreviewUrl.value = url
    previewCooldown.value = PREVIEW_COOLDOWN_SEC
    const iv = setInterval(() => {
      previewCooldown.value--
      if (previewCooldown.value <= 0) clearInterval(iv)
    }, 1000)
  } catch (err) {
    toast.error(err?.response?.data?.error || i18n.global.t('templateEditor.previewThrottle'))
  }
}

watch(currentThemeName, (name) => {
  if (!config.value.themes?.[name]) {
    const first = Object.keys(config.value.themes || {})[0]
    if (first) currentThemeName.value = first
  }
})

onMounted(async () => {
  loading.value = true
  try {
    const [tRes, vRes, fRes, cRes] = await Promise.all([
      templateEditorApi.get(templateId.value),
      templateEditorApi.variables(),
      templateEditorApi.fonts().catch(() => ({ data: [] })),
      categoryApi.list().catch(() => ({ data: [] })),
    ])
    template.value = tRes.data
    const raw = template.value.config || {}
    config.value = {
      base_width: raw.base_width || BASE,
      base_height: raw.base_height || BASE,
      usage_theme_map: raw.usage_theme_map || {},
      themes: raw.themes || { default: { layers: [] } },
      variables: raw.variables,
      fields: raw.fields,
      canvas_background_type: raw.canvas_background_type || (template.value.image ? 'image' : 'solid'),
      canvas_background_color: raw.canvas_background_color || '#1a1a2e',
    }
    ensureThemes()
    variables.value = Array.isArray(vRes.data) ? vRes.data : []
    categoriesFromApi.value = Array.isArray(cRes?.data) ? cRes.data : []
    if (categoryLibraryTabs.value.length && !categoryLibraryTabs.value.some((t) => t.id === selectedCategoryTab.value)) {
      selectedCategoryTab.value = categoryLibraryTabs.value[0].id
    }
    fonts.value = Array.isArray(fRes.data) ? fRes.data : []
    if (currentLayers.value.length) {
      currentLayers.value.forEach((l) => {
        if (l.locked === undefined) l.locked = false
        if (l.visible === undefined) l.visible = true
      })
    }
  } catch {
    template.value = null
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
.template-editor-dark {
  --bg-base: #0f172a;
}
.template-editor-grid {
  display: grid;
  grid-template-columns: 260px 1fr 300px;
  min-height: calc(100vh - 56px);
}
@media (max-width: 1200px) {
  .template-editor-grid {
    grid-template-columns: 1fr;
    grid-template-rows: auto 1fr auto;
  }
  .template-editor-left { border-radius: 0.5rem; border: 1px solid var(--glass-border); }
  .template-editor-right { border-radius: 0.5rem; border: 1px solid var(--glass-border); }
}
.telegram-mockup {
  background: linear-gradient(180deg, rgba(42, 171, 238, 0.12) 0%, rgba(34, 158, 217, 0.08) 100%);
  border: 1px solid var(--glass-border);
}
.canvas-checkerboard {
  background-image:
    linear-gradient(45deg, #1e293b 25%, transparent 25%),
    linear-gradient(-45deg, #1e293b 25%, transparent 25%),
    linear-gradient(45deg, transparent 75%, #1e293b 75%),
    linear-gradient(-45deg, transparent 75%, #1e293b 75%);
  background-size: 16px 16px;
  background-position: 0 0, 0 8px, 8px -8px, -8px 0px;
  background-color: #0f172a;
}
.variable-chip:focus {
  outline: none;
}
.inspector-block {
  padding: 0.5rem 0;
  border-bottom: 1px solid var(--glass-border);
}
.inspector-block:last-child {
  border-bottom: none;
}
</style>
