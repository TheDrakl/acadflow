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
          <li>
            <a href="#" class="group transition-all duration-300 ease-in-out">CONTACT</a>
            <span
              class="bg-left-bottom bg-gradient-to-r from-pink-500 to-pink-500 bg-[length:0%_2px] bg-no-repeat group-hover:bg-[length:100%_2px] transition-all duration-500 ease-out
            ></span>
          </li>
          <a
            class="group text-pink-500 transition-all duration-300 ease-in-out"
            href="#"
          >
            <span
              class="bg-left-bottom bg-gradient-to-r from-pink-500 to-pink-500 bg-[length:0%_2px] bg-no-repeat group-hover:bg-[length:100%_2px] transition-all duration-500 ease-out"
            >
              This text gets 'underlined' on hover
            </span>
          </a>
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
