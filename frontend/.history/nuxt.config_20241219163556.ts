export default defineNuxtConfig({
  future: {
    compatibilityVersion: 4,
  },

  modules: ["@nuxtjs/tailwindcss"],
  srcDir: ".",

  dir: {
    app: "app",
  },
  compatibilityDate: "2024-12-19",
});
