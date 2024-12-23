<template>
  <div class="w-full max-w-[60%]">
    <label for="textInput" class="sr-only">Enter Text</label>
    <div
      class="h-12 border border-lightGray rounded-2xl focus-within:border-primary"
    >
      <input
        id="textInput"
        type="text"
        class="w-full h-full px-4 bg-transparent outline-none rounded-2xl text-black"
        :placeholder="text"
      />
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
    text: {}
})
</script>

<style scoped>
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
</style>
