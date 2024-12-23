export default defineNuxtConfig({
  future: {
    compatibilityVersion: 4,
  },
    ssr: true,

  modules: ["@nuxtjs/tailwindcss", '@nuxtjs/google-fonts', '@nuxt/icon', '@nuxtjs/seo' ],

  seo: {
    siteName: 'Your Site Name',
    twitterCard: 'summary_large_image', /
    twitterSite: '@yourtwitterhandle',
    ogHost: 'https://www.yoursite.com',
  }
  
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