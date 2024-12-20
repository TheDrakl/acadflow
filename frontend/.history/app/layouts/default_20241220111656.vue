<template>
  <div class="container">
    <main class="my-4 mx-4">
      <nav class="flex justify-between text-center items-center">
        <div class="logo">
          <img
            src="public/images/acadflow-logo.png"
            alt="logo"
            class="w-48 h-auto"
          />
        </div>
        <div>
          <ul class="flex justify-between space-x-20 text-lg">
            <li><a href="#">HOME</a></li>
            <li><a href="#">ABOUT</a></li>
            <li><a href="#">DASHBOARD</a></li>
            <li><a href="#">CONTACT</a></li>
          </ul>
        </div>
        <div>
          <button>Sign Up</button>
        </div>
      </nav>
      <NuxtPage></NuxtPage>
    </main>
  </div>
</template>

<script setup>
// Link to Google Fonts
useHead({
  link: [
    {
      rel: "preconnect",
      href: "https://fonts.googleapis.com",
    },
    {
      rel: "stylesheet",
      href: "https://fonts.googleapis.com/css2?family=Inter&display=swap",
      crossorigin: "",
    },
  ],
});
</script>

<style>
/* Set the font family for the entire site */
body {
  font-family: "Inter";
}
/* Set the background color for the entire site */
body {
  @apply bg-white;
  @apply text-black;
}
</style>
