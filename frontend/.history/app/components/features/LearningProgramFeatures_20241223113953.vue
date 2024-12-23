<template>
  <div class="flex justify-between items-center font-roboto">
    <div
      class="bg-yellowMain w-12 h-12 lg:w-16 lg:h-16 flex items-center justify-center rounded-full mr-4 text-white text-xl lg:text-2xl"
    >
      {{ num }}
    </div>
    <div class="flex-1 min-w-0 text-base lg:text-xl break-words max-w-[80%] mr-auto">
      <slot></slot>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  num: Number,
});
</script>

<style scoped>
h1 {
  color: #333;
}

p {
  color: #666;
}
</style>
