<template>
  <div class="bg-black text-white py-2 font-roboto font-[300]">
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
          <li><a href="#" class="hover:text-gray-300">HOME</a></li>
          <li><a href="#" class="hover:text-gray-300">ABOUT</a></li>
          <li><a href="#" class="hover:text-gray-300">DASHBOARD</a></li>
          <li class="relative">
            <a href="#" class="group transition duration-300">CONTACT</a>
            <span
              class="block max-w-0 group-hover:max-w-full transition-all duration-500 h-0.5 bg-yellow-300"
            ></span>
          </li>
          <li>
            <a href="#" class="group transition duration-300">
              CONTACT
              <span
                class="block max-w-0 group-hover:max-w-full transition-all duration-500 h-0.5 bg-yellow-700"
              ></span>
            </a>
          </li>
        </ul>
        <!-- Button -->
        <button
          class="bg-gray-300 text-black py-2 px-4 rounded hover:bg-gray-400"
        >
          Sign Up
        </button>
      </nav>
    </div>
  </div>
</template>

<style>
/* Add styles here if needed */
</style>
