export default defineNuxtConfig({
  future: {
    compatibilityVersion: 4,
  },
    ssr: true,

  modules: ["@nuxtjs/tailwindcss", '@nuxtjs/google-fonts', '@nuxt/icon', '@nuxtjs/seo' ],
  
  
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

  seo: {
    title: 'My Nuxt Site',
    description: 'This is a description of my awesome Nuxt site.',
    url: 'https://www.yoursite.com',
    image: '/images/og-image.png',
    twitter: {
      card: 'summary_large_image',
      site: '@yoursite',
      creator: '@creator',
    },
    og: {
      type: 'website',
      locale: 'en_US',
      image: '/images/og-image.png',
    },
    robots: {
      index: true,
      follow: true,
    },
    additionalMetaTags: [
      { name: 'author', content: 'Your Name' },
      { name: 'keywords', content: 'nuxt, vue, seo, web development' },
    ],
  },
});