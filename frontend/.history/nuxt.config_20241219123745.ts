export default defineNuxtConfig({
  compatibilityDate: "2024-12-18",
  modules: ["@nuxt/ui", "@nuxtjs/supabase"],
  future: {
    compatibilityVersion: 4,
  },
  dir: {
    app: 'app',  // Custom directory for app (default is 'app')
  },
  experimental: {
    scanPageMeta: 'after-resolve',
  },
  supabase: {
    redirect: false
  }
});
