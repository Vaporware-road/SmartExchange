import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import Layout from '@/layouts/AppLayout.vue'

const routes = [
  {
    path: '/login',
    name: 'login',
    component: () => import('@/views/auth/LoginView.vue'),
    meta: { public: true },
  },
  {
    path: '/landing',
    name: 'landing',
    component: () => import('@/views/auth/LandingView.vue'),
    meta: { public: true },
  },
  {
    path: '/',
    component: Layout,
    meta: { requiresAuth: true, titleKey: 'breadcrumb.home' },
    children: [
      {
        path: '',
        name: 'dashboard',
        component: () => import('@/views/dashboard/DashboardView.vue'),
        meta: { titleKey: 'routes.dashboard' },
      },
      {
        path: 'prices',
        name: 'prices',
        component: () => import('@/views/prices/PricesView.vue'),
        meta: { titleKey: 'routes.prices' },
      },
      {
        path: 'prices/:id/update',
        name: 'update-price',
        component: () => import('@/views/prices/UpdatePriceView.vue'),
        meta: { titleKey: 'routes.updatePrice' },
      },
      {
        path: 'prices/category/:id/update',
        name: 'bulk-update',
        component: () => import('@/views/prices/BulkUpdateView.vue'),
        meta: { titleKey: 'routes.bulkUpdate' },
      },
      {
        path: 'prices/:id/history',
        name: 'price-history',
        component: () => import('@/views/prices/PriceHistoryView.vue'),
        meta: { titleKey: 'routes.priceHistory' },
      },
      {
        path: 'special-prices',
        name: 'special-prices',
        component: () => import('@/views/special-prices/SpecialPricesView.vue'),
        meta: { titleKey: 'routes.specialPrices' },
      },
      {
        path: 'special-prices/:id/update',
        name: 'update-special-price',
        component: () => import('@/views/special-prices/UpdateSpecialPriceView.vue'),
        meta: { titleKey: 'routes.updateSpecialPrice' },
      },
      {
        path: 'special-prices/:id/history',
        name: 'special-price-history',
        component: () => import('@/views/special-prices/SpecialPriceHistoryView.vue'),
        meta: { titleKey: 'routes.specialPriceHistory' },
      },
      {
        path: 'finalize',
        name: 'finalize',
        component: () => import('@/views/finalize/FinalizeDashboardView.vue'),
        meta: { titleKey: 'routes.finalize' },
      },
      {
        path: 'finalize/category/:id',
        name: 'finalize-category',
        component: () => import('@/views/finalize/FinalizeCategoryView.vue'),
        meta: { titleKey: 'routes.finalizeCategory' },
      },
      {
        path: 'finalize/special-price/:id',
        name: 'finalize-special-price',
        component: () => import('@/views/finalize/FinalizeSpecialPriceView.vue'),
        meta: { titleKey: 'routes.finalizeSpecialPrice' },
      },
      {
        path: 'categories',
        name: 'categories',
        component: () => import('@/views/categories/CategoriesView.vue'),
        meta: { titleKey: 'routes.categories' },
      },
      {
        path: 'categories/new',
        name: 'category-new',
        component: () => import('@/views/categories/CategoryFormView.vue'),
        meta: { titleKey: 'routes.categoryNew' },
      },
      {
        path: 'categories/create',
        redirect: { name: 'category-new' },
      },
      {
        path: 'categories/:id/edit',
        name: 'category-edit',
        component: () => import('@/views/categories/CategoryFormView.vue'),
        meta: { titleKey: 'routes.categoryEdit' },
      },
      {
        path: 'categories/:id/price-types/new',
        name: 'price-type-new',
        component: () => import('@/views/categories/PriceTypeFormView.vue'),
        meta: { titleKey: 'routes.priceTypeNew' },
      },
      {
        path: 'settings',
        name: 'settings',
        component: () => import('@/views/settings/SettingsView.vue'),
        meta: { titleKey: 'routes.settings' },
      },
      {
        path: 'settings/logs',
        name: 'logs',
        component: () => import('@/views/settings/LogsView.vue'),
        meta: { titleKey: 'routes.logs' },
      },
      {
        path: 'analysis',
        name: 'analysis',
        component: () => import('@/views/analysis/AnalyticsView.vue'),
        meta: { titleKey: 'routes.analysis' },
      },
      {
        path: 'telegram/send',
        name: 'telegram-send',
        component: () => import('@/views/telegram/TelegramMessageView.vue'),
        meta: { titleKey: 'routes.telegramSend' },
      },
      {
        path: 'telegram/settings',
        name: 'telegram-settings',
        component: () => import('@/views/telegram/TelegramSettingsView.vue'),
        meta: { titleKey: 'routes.telegramSettings' },
      },
      {
        path: 'templates',
        name: 'templates',
        component: () => import('@/views/templates/TemplatesDashboardView.vue'),
        meta: { titleKey: 'routes.templates' },
      },
      {
        path: 'templates/new',
        name: 'template-new',
        component: () => import('@/views/templates/TemplateFormView.vue'),
        meta: { titleKey: 'routes.templateNew' },
      },
      {
        path: 'templates/:id/editor',
        name: 'template-editor',
        component: () => import('@/views/templates/TemplateEditorView.vue'),
        meta: { titleKey: 'routes.templateEditor' },
      },
    ],
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach(async (to, from, next) => {
  const auth = useAuthStore()
  await auth.ensureInitialized()

  if (to.meta.public) {
    if (auth.isAuthenticated && to.name === 'login') {
      next({ name: 'dashboard' })
    } else {
      next()
    }
  } else if (to.meta.requiresAuth && !auth.isAuthenticated) {
    next({ name: 'login', query: { redirect: to.fullPath } })
  } else {
    next()
  }
})

export default router
