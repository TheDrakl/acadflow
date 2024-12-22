export default defineNuxtConfig({
  future: {
    compatibilityVersion: 4,
  },
    ssr: true,

  modules: ["@nuxt/ui", "@nuxtjs/tailwindcss", '@nuxtjs/google-fonts', '@nuxt/icon', '@nuxtjs/color-mode'],
  colorMode: {
    preference: 'light', // Always use light mode
    fallback: 'light',  // Fallback to light mode if no stored preference is found
    classSuffix: '', // Optional: Remove any suffix for dark mode classes (if you use Tailwind CSS)
  },
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