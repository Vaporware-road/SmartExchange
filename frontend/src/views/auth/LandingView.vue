<template>
  <div class="min-h-screen relative overflow-hidden" style="background: var(--bg-base)">
    <!-- Theme toggle -->
    <div class="absolute top-4 right-4 z-50">
      <ThemeToggle />
    </div>

    <!-- ═══════════════════════════════════════════════ HERO ═══════════════════════════════════════════════ -->
    <section class="relative min-h-screen flex items-center justify-center px-4">
      <!-- Animated gradient orbs -->
      <div class="hero-orb hero-orb--gold" />
      <div class="hero-orb hero-orb--blue" />
      <div class="hero-orb hero-orb--purple" />

      <!-- Grid pattern overlay -->
      <div class="absolute inset-0 opacity-[0.03]" style="background-image: radial-gradient(var(--text-primary) 1px, transparent 1px); background-size: 32px 32px" />

      <div class="relative z-10 max-w-5xl mx-auto text-center">
        <!-- Logo -->
        <div class="animate-fade-in-up mb-8">
          <div class="mx-auto w-fit">
            <AppBrandLogo size="xl" rounded="xl" />
          </div>
        </div>

        <!-- Badge -->
        <div class="animate-fade-in-up mb-6" style="animation-delay: 0.1s">
          <span class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full text-xs font-medium border"
                style="background: var(--bg-card); border-color: var(--border-color); color: var(--text-secondary)">
            <span class="w-2 h-2 rounded-full bg-success animate-pulse" />
            {{ $t('landing.trialBadge') }}
          </span>
        </div>

        <!-- Heading -->
        <h1 class="animate-fade-in-up text-4xl sm:text-5xl md:text-6xl lg:text-7xl font-bold leading-tight mb-6"
            style="animation-delay: 0.2s; color: var(--text-primary)">
          {{ siteName }}
        </h1>

        <!-- Tagline -->
        <p class="animate-fade-in-up text-lg sm:text-xl md:text-2xl max-w-3xl mx-auto mb-10 leading-relaxed"
           style="animation-delay: 0.3s; color: var(--text-secondary)">
          {{ tagline }}
        </p>

        <!-- CTA Buttons -->
        <div class="animate-fade-in-up flex flex-wrap items-center justify-center gap-4 mb-16"
             style="animation-delay: 0.4s">
          <router-link :to="auth.isAuthenticated ? '/panel' : '/login'" class="btn-luxury inline-flex items-center gap-2 text-base px-8 py-3">
            <i class="fas fa-sign-in-alt" />
            <span>{{ auth.isAuthenticated ? $t('common.panel') : $t('common.accessPanel') }}</span>
          </router-link>
          <button
            type="button"
            class="btn-luxury-outline inline-flex items-center gap-2 text-base px-8 py-3"
            :disabled="demoLoading"
            @click="startDemo"
          >
            <LoadingSpinner v-if="demoLoading" class="w-5 h-5" />
            <i v-else class="fas fa-play-circle" />
            <span>{{ demoLoading ? $t('auth.signingIn') : $t('auth.exploreDemo') }}</span>
          </button>
        </div>

        <!-- Scroll indicator -->
        <div class="animate-fade-in-up" style="animation-delay: 0.6s">
          <button
            type="button"
            class="mx-auto flex flex-col items-center gap-2 opacity-40 hover:opacity-70 transition-opacity"
            @click="scrollToSection('features')"
          >
            <span class="text-xs" style="color: var(--text-secondary)">{{ $t('landing.learnMore') }}</span>
            <i class="fas fa-chevron-down animate-bounce" style="color: var(--text-secondary)" />
          </button>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════ FEATURES ═══════════════════════════════════════════ -->
    <section id="features" class="relative py-24 px-4">
      <div class="max-w-6xl mx-auto">
        <div class="text-center mb-16">
          <h2 class="animate-fade-in-up text-3xl sm:text-4xl font-bold mb-4"
              style="color: var(--text-primary)">
            {{ $t('landing.featuresTitle') }}
          </h2>
          <p class="animate-fade-in-up text-lg max-w-2xl mx-auto"
             style="animation-delay: 0.1s; color: var(--text-secondary)">
            {{ $t('landing.featuresSubtitle') }}
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <div
            v-for="(feature, i) in features"
            :key="feature.key"
            class="card-luxury p-6 group hover:shadow-glow transition-all duration-300 animate-fade-in-up"
            :style="{ animationDelay: `${0.1 + i * 0.08}s` }"
          >
            <div class="w-12 h-12 rounded-xl flex items-center justify-center mb-4 transition-transform group-hover:scale-110"
                 :style="{ background: feature.iconBg }">
              <i :class="feature.icon" class="text-xl" :style="{ color: feature.iconColor }" />
            </div>
            <h3 class="text-lg font-semibold mb-2" style="color: var(--text-primary)">
              {{ $t(`landing.features.${feature.key}.title`) }}
            </h3>
            <p class="text-sm leading-relaxed" style="color: var(--text-secondary)">
              {{ $t(`landing.features.${feature.key}.desc`) }}
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════ HOW IT WORKS ═══════════════════════════════════════════ -->
    <section class="relative py-24 px-4">
      <div class="max-w-5xl mx-auto">
        <div class="text-center mb-16">
          <h2 class="text-3xl sm:text-4xl font-bold mb-4"
              style="color: var(--text-primary)">
            {{ $t('landing.howItWorksTitle') }}
          </h2>
          <p class="text-lg max-w-2xl mx-auto"
             style="color: var(--text-secondary)">
            {{ $t('landing.howItWorksSubtitle') }}
          </p>
        </div>

        <div class="relative">
          <!-- Connector line -->
          <div class="hidden lg:block absolute top-12 left-[12.5%] right-[12.5%] h-0.5"
               style="background: var(--border-color)" />

          <div class="grid grid-cols-1 lg:grid-cols-4 gap-8">
            <div
              v-for="(step, i) in steps"
              :key="step.key"
              class="relative text-center"
            >
              <div class="relative z-10 w-12 h-12 rounded-full mx-auto mb-4 flex items-center justify-center text-sm font-bold border-2 transition-colors"
                   :style="{
                     borderColor: 'var(--primary)',
                     background: 'var(--bg-card)',
                     color: 'var(--primary)'
                   }">
                {{ i + 1 }}
              </div>
              <h3 class="text-base font-semibold mb-2" style="color: var(--text-primary)">
                {{ $t(`landing.steps.${step.key}.title`) }}
              </h3>
              <p class="text-sm" style="color: var(--text-secondary)">
                {{ $t(`landing.steps.${step.key}.desc`) }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════ STATS ═══════════════════════════════════════════ -->
    <section class="relative py-20 px-4">
      <div class="max-w-5xl mx-auto">
        <div class="card-luxury p-8 sm:p-12"
             style="background: linear-gradient(135deg, var(--bg-card), var(--bg-elevated))">
          <div class="grid grid-cols-2 md:grid-cols-4 gap-8">
            <div
              v-for="stat in stats"
              :key="stat.key"
              class="text-center"
            >
              <div class="text-3xl sm:text-4xl font-bold mb-1" style="color: var(--primary)">
                {{ stat.value }}
              </div>
              <div class="text-xs sm:text-sm" style="color: var(--text-secondary)">
                {{ $t(`landing.stats.${stat.key}`) }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════ CTA ═══════════════════════════════════════════ -->
    <section class="relative py-24 px-4">
      <div class="max-w-3xl mx-auto text-center">
        <h2 class="text-3xl sm:text-4xl font-bold mb-4"
            style="color: var(--text-primary)">
          {{ $t('landing.ctaTitle') }}
        </h2>
        <p class="text-lg mb-8 max-w-xl mx-auto"
           style="color: var(--text-secondary)">
          {{ $t('landing.ctaSubtitle') }}
        </p>
        <div class="flex flex-wrap items-center justify-center gap-4">
          <router-link :to="auth.isAuthenticated ? '/panel' : '/login'" class="btn-luxury inline-flex items-center gap-2 text-base px-8 py-3">
            <i class="fas fa-rocket" />
            <span>{{ $t('landing.ctaButton') }}</span>
          </router-link>
          <button
            type="button"
            class="btn-luxury-outline inline-flex items-center gap-2 text-base px-8 py-3"
            :disabled="demoLoading"
            @click="startDemo"
          >
            <i class="fas fa-play-circle" />
            <span>{{ $t('landing.freeTrialButton') }}</span>
          </button>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════ FOOTER ═══════════════════════════════════════════ -->
    <footer class="py-8 px-4 border-t" style="border-color: var(--border-color)">
      <div class="max-w-6xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
        <div class="flex items-center gap-2">
          <AppBrandLogo size="sm" rounded="md" />
          <span class="text-sm font-medium" style="color: var(--text-primary)">{{ siteName }}</span>
        </div>
        <p class="text-xs" style="color: var(--text-secondary)">
          {{ $t('footer.copyright', { year: currentYear, name: siteName }) }}
        </p>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { computed, ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useSiteSettingsStore } from '@/stores/siteSettings'
import { useAuthStore } from '@/stores/auth'
import { getApiErrorDetails } from '@/services/api'
import LoadingSpinner from '@/components/ui/LoadingSpinner.vue'
import ThemeToggle from '@/components/ui/ThemeToggle.vue'
import AppBrandLogo from '@/components/layout/AppBrandLogo.vue'

const router = useRouter()
const siteSettings = useSiteSettingsStore()
const auth = useAuthStore()
const demoLoading = ref(false)

const siteName = computed(() => siteSettings.siteName)
const tagline = computed(() => siteSettings.tagline)
const currentYear = new Date().getFullYear()

const features = [
  { key: 'priceHub', icon: 'fas fa-chart-line', iconBg: 'rgba(16, 185, 129, 0.12)', iconColor: '#10B981' },
  { key: 'telegram', icon: 'fab fa-telegram-plane', iconBg: 'rgba(59, 130, 246, 0.12)', iconColor: '#3B82F6' },
  { key: 'finalize', icon: 'fas fa-paper-plane', iconBg: 'rgba(255, 215, 0, 0.12)', iconColor: '#FFD700' },
  { key: 'templates', icon: 'fas fa-palette', iconBg: 'rgba(139, 92, 246, 0.12)', iconColor: '#8B5CF6' },
  { key: 'analytics', icon: 'fas fa-chart-bar', iconBg: 'rgba(244, 63, 94, 0.12)', iconColor: '#F43F5E' },
  { key: 'multiUser', icon: 'fas fa-users-cog', iconBg: 'rgba(20, 184, 166, 0.12)', iconColor: '#14B8A6' },
]

const steps = [
  { key: 'setup' },
  { key: 'update' },
  { key: 'design' },
  { key: 'publish' },
]

const stats = [
  { key: 'currencies', value: '15+' },
  { key: 'channels', value: '∞' },
  { key: 'uptime', value: '99.9%' },
  { key: 'support', value: '24/7' },
]

onMounted(() => siteSettings.fetch())

async function startDemo() {
  if (auth.isAuthenticated) {
    router.push('/panel')
    return
  }
  demoLoading.value = true
  try {
    await auth.demoLogin()
    router.push('/panel')
  } catch (err) {
    const { message } = getApiErrorDetails(err)
    alert(message)
  } finally {
    demoLoading.value = false
  }
}

function scrollToSection(id) {
  document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' })
}
</script>

<style scoped>
/* ── Hero animated orbs ── */
.hero-orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(100px);
  opacity: 0.15;
  animation: orbFloat 20s ease-in-out infinite;
}
.hero-orb--gold {
  width: 500px;
  height: 500px;
  background: var(--primary, #FFD700);
  top: -10%;
  right: -10%;
  animation-delay: 0s;
}
.hero-orb--blue {
  width: 400px;
  height: 400px;
  background: #3B82F6;
  bottom: -5%;
  left: -5%;
  animation-delay: -7s;
}
.hero-orb--purple {
  width: 350px;
  height: 350px;
  background: #8B5CF6;
  top: 30%;
  left: 50%;
  animation-delay: -14s;
}

@keyframes orbFloat {
  0%, 100% { transform: translate(0, 0) scale(1); }
  25% { transform: translate(30px, -20px) scale(1.05); }
  50% { transform: translate(-20px, 30px) scale(0.95); }
  75% { transform: translate(20px, 20px) scale(1.02); }
}

/* ── Reusable animations ── */
.animate-fade-in-up {
  opacity: 0;
  transform: translateY(20px);
  animation: fadeInUp 0.6s ease forwards;
}

@keyframes fadeInUp {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* ── Button variants ── */
.btn-luxury-outline {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 2rem;
  border-radius: 0.75rem;
  font-weight: 600;
  border: 1.5px solid var(--border-color, rgba(255, 215, 0, 0.3));
  background: transparent;
  color: var(--text-primary, #fff);
  transition: all 0.25s ease;
  cursor: pointer;
}
.btn-luxury-outline:hover:not(:disabled) {
  border-color: var(--primary, #FFD700);
  background: rgba(255, 215, 0, 0.06);
  box-shadow: 0 0 20px rgba(255, 215, 0, 0.1);
}
.btn-luxury-outline:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
</style>
