export default defineNuxtConfig({
  future: {
    compatibilityVersion: 4,
  },

  modules: ["@nuxt/ui", "@nuxtjs/tailwindcss", '@nuxtjs/google-fonts'],
  ui: {
      // Disable Nuxt UI's automatic theme injection
    primary: 'green',
    gray: 'cool'
  },
  googleFonts: {
    families: {
      Roboto: [300, 400, 500, 700],
      Montserrat: [300, 400, 500],
    },
  },
  srcDir: "./app/",

  dir: {
    app: "app",
  },
  compatibilityDate: "2024-12-19",
});