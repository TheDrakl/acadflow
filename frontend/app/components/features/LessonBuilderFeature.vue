<template>
    <div class="flex flex-col lg:flex-row items-center gap-8">
      <!-- Image Section -->
      <div class="flex-shrink-0">
        <img :src="img" alt="Feature Image" class="w-64 lg:w-72 mx-auto lg:mx-0" draggable="false" loading="lazy">
      </div>
  
      <!-- Text Section -->
      <div class="flex-1 text-center lg:text-left">
        <h2 class="text-4xl font-[500] mb-4">{{ title }}</h2>
        <p class="text-lg leading-relaxed">
          <slot></slot>
        </p>
      </div>
    </div>
  </template>
  
  <script setup>
  const props = defineProps({
    title: String,
    img: String,
  });
  </script>