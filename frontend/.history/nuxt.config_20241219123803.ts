export default defineNuxtConfig({
  compatibilityDate: "2024-12-18",
  future: {
    compatibilityVersion: 4,
  },
  dir: {
    app: 'app',  // Custom directory for app (default is 'app')
  },
  experimental: {
    scanPageMeta: 'after-resolve',
  },
});
