<template>
  <div class="w-full max-w-[70%]">
    <label :for="inputId" class="sr-only">Enter Text</label>
    <div
      class="h-12 border border-lightGray rounded-2xl focus-within:border-primary"
    >
      <input
        :id="inputId"
        type="text"
        class="w-full h-full px-4 bg-transparent outline-none rounded-2xl placeholder-gray-700 text-base"
        :placeholder="text"
        :autocomplete="inputAutoComplete"
      />
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
    text: {
        type: String,
        default: "Enter Text",
    },
    inputId: {
        type: String,
        default: "textInput",
    },
    inputAutoComplete: {
        type: String,
        default: "off",
    },
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
