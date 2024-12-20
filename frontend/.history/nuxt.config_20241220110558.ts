export default defineNuxtConfig({
  future: {
    compatibilityVersion: 4,
  },

  modules: ["@nuxtjs/tailwindcss", '@nuxtjs/google-fonts'],
  googleFonts: {
    families: {
      Roboto: [300, 400, 500, 700],
    },
  },
  srcDir: "./app/",

  dir: {
    app: "app",
  },
  compatibilityDate: "2024-12-19",
});
