<template>
  <div>
    <div
      class="container mx-auto px-0 lg:px-4 lg:bg-gray-50 text-black mt-2 lg:pt-4 lg:pb-4 font-roboto font-[300] rounded-2xl bg-gradient-to-r from-transparent via-yellow-50 to-transparent"
    >
      <nav class="hidden md:flex justify-between items-center h-8">
        <!-- Logo -->
        <div class="logo">
          <img
            src="public/images/acadflow-logo.png"
            alt="logo"
            class="w-48 h-auto"
          />
        </div>
        <!-- Navigation -->
        <ul
          class="flex space-x-8 lg:space-x-16 xl:space-x-28 text-[1rem] lg:text-[1.1rem]"
        >
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
        <FirstButton
          class="self-center text-yellow-600 border-solid border-[2px] border-yellow-600 bg-transparent hover:bg-yellow-600 hover:text-white py-2 px-8"
          >Sign Up</FirstButton
        >
      </nav>
      <nav class="flex md:hidden float-right ml-auto">
        <Icon name="pajamas:hamburger" style="color: black" size="2rem" class="absolute right-4 top-4"/>
      </nav>
    </div>
  </div>
  <main class="">
    <NuxtPage />    
  </main>

</template>

<script setup>
import FirstButton from "~/components/buttons/FirstButton.vue";
</script>
