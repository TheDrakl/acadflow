export default defineNuxtConfig({
  future: {
    compatibilityVersion: 4,
  },
  ssr: true,

  modules: [
    "@nuxtjs/color-mode",
    "nuxt3-notifications",
    "@nuxtjs/tailwindcss",
    "@nuxtjs/google-fonts",
    "@nuxt/icon",
    "nuxt-icons",
    "nuxt-aos",
  ],
  googleFonts: {
    families: {
      Roboto: [300, 400, 500, 700],
      Montserrat: [300, 400, 500],
      Inter: [300, 400, 500],
    },
  },
  srcDir: "./app/",

  dir: {
    app: "app",
  },
  compatibilityDate: "2024-12-19",

  components: [
    {
      path: "~/components", // will get any components nested in let's say /components/test too
      pathPrefix: false,
    },
  ],
  plugins: ["~/plugins/directives.js", '~/plugins/auth.js'],
});
