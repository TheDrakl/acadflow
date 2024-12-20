<template>
  <div class="bg-white text-black py-2 font-roboto font-[300]">
    <div class="container mx-auto px-4">
      <nav class="flex justify-between items-center h-16">
        <!-- Logo -->
        <div class="logo">
          <img
            src="public/images/acadflow-logo.png"
            alt="logo"
            class="w-48 h-auto"
          />
        </div>
        <!-- Navigation -->
        <ul class="flex space-x-28 text-[1.1rem]">
          <li>
            <a href="#" class="group transition duration-300">
              HOME
              <span
                class="block max-w-0 group-hover:max-w-full transition-all duration-500 h-0.5 bg-yellow-500"
              ></span>
            </a>
          </li>
          <li>
            <a href="#" class="group transition duration-300">
              ABOUT US
              <span
                class="block max-w-0 group-hover:max-w-full transition-all duration-500 h-0.5 bg-yellow-500"
              ></span>
            </a>
          </li>
          <li>
            <a href="#" class="group transition duration-300">
              DASHBOARD
              <span
                class="block max-w-0 group-hover:max-w-full transition-all duration-500 h-0.5 bg-yellow-500"
              ></span>
            </a>
          </li>
          <li>
            <a href="#" class="group transition duration-300">
              CONTACT
              <span
                class="block max-w-0 group-hover:max-w-full transition-all duration-500 h-0.5 bg-yellow-500"
              ></span>
            </a>
          </li>
        </ul>
        <!-- Button -->
        <!-- <button
          class="bg-gray-300 text-black py-2 px-4 rounded hover:bg-gray-400"
        >
          Sign Up
        </button> -->
        <FirstButton class="self-center">Sign Up</FirstButton>
      </nav>
    </div>
    <NuxtPage />
  </div>
</template>

<script setup>
import FirstButton from '~/components/buttons/FirstButton.vue'
</script>