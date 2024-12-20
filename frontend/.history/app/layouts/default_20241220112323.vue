<template>
  <div class="container mx-auto">
    <main class="my-4 mx-2">
      <nav class="flex justify-between items-center h-16">
        <!-- Logo Section -->
        <div class="logo">
          <img
            src="public/images/acadflow-logo.png"
            alt="logo"
            class="w-48 h-auto"
          />
        </div>
        <!-- Navigation Links -->
        <div class="flex">
          <ul class="flex space-x-12 text-[1rem]">
            <li><a href="#">HOME</a></li>
            <li><a href="#">ABOUT</a></li>
            <li><a href="#">DASHBOARD</a></li>
            <li><a href="#">CONTACT</a></li>
          </ul>
        </div>
        <!-- Sign Up Button -->
        <button class="bg-gray-300 py-2 px-4 rounded hover:bg-gray-400 transition">
          Sign Up
        </button>
      </nav>
      <NuxtPage></NuxtPage>
    </main>
  </div>
</template>