<template>
  <div class="flex justify-between items-center">
    <div
      class="bg-yellowMain w-16 h-16 flex items-center justify-center rounded-full mr-4 text-white lg:text-2xl"
    >
      {{ num }}
    </div>
    <div class="flex-1 min-w-0 text-xl break-words max-w-[80%] mr-auto">
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
