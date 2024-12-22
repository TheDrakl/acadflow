export default defineNuxtConfig({
  future: {
    compatibilityVersion: 4,
  },
  export default {
    ssr: true,
    target: 'server',
  };

  modules: ["@nuxtjs/tailwindcss", '@nuxtjs/google-fonts', '@nuxt/icon'],
  googleFonts: {
    families: {
      Roboto: [300, 400, 500, 700],
      Montserrat: [300, 400, 500],
      Inter: [300, 400, 500]
    },
  },
  srcDir: "./app/",

  dir: {
    app: "app",
  },
  compatibilityDate: "2024-12-19",
});