export default defineNuxtConfig({
  future: {
    compatibilityVersion: 4,
  },

  modules: ["@nuxt/ui", "@nuxtjs/tailwindcss", '@nuxtjs/google-fonts'],
  ui: {
    config: {
      // Disable Nuxt UI's automatic theme injection
      theme: 'none',  // or use a custom theme
      default: 'none', // This prevents automatic style application
    }
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