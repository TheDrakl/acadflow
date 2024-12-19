// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  future: {
    compatibilityVersion: 4,
  },
  dir: {
    app: 'app',  // Custom directory for app (default is 'app')
  },
  experimental: {
    scanPageMeta: 'after-resolve',
  },
  devtools: { enabled: true }
})
