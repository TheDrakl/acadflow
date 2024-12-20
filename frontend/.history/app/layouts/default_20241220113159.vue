<template>
  <div class="bg-black text-white">
    <div class="container mx-auto px-4 my-4">
      <nav class="flex justify-between items-center h-16">
        <!-- Logo Section -->
        <div class="logo">
          <img
            src="public/images/acadflow-logo.png"
            alt="logo"
            class="w-48 h-auto cursor-pointer"
          />
        </div>
        <!-- Navigation Links -->
        <div class="flex">
          <ul class="flex space-x-40 text-[1.1rem]">
            <li><a href="#">HOME</a></li>
            <li><a href="#">ABOUT</a></li>
            <li><a href="#">DASHBOARD</a></li>
            <li><a href="#">CONTACT</a></li>
          </ul>
        </div>
        <!-- Sign Up Button -->
        <button
          class="bg-gray-300 py-2 px-4 rounded hover:bg-gray-400 transition"
        >
          Sign Up
        </button>
      </nav>
      <NuxtPage></NuxtPage>
    </div>
  </div>
</template>
