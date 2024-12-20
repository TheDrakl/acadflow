<template>
    <div class="container max-w-4xl">
      <main class="my-10">
        <NuxtPage></NuxtPage>
      </main>
    </div>
  </template>
  
  <script setup>
  // Link to Google Fonts
  useHead({
    link: [
      {
        rel: 'preconnect',
        href: 'https://fonts.googleapis.com'
      },
      {
        rel: 'stylesheet',
        href: 'https://fonts.googleapis.com/css2?family=Inter&display=swap',
        crossorigin: ''
      }
    ]
  })
  </script>
  
  <style>
  /* Set the font family for the entire site */
  body {
    font-family: 'Inter';
  }
  /* Set the background color for the entire site */
  body {
    @apply bg-white, text-black
  }
  </style>