<template>
  <button
    :class="[
      'bg-transparent border-solid border-[2px] text-md font-roboto font-[400] py-2 px-8 rounded-xl hover:bg-gray-400',
      `text-${color}-600`, // Dynamically apply text color
      `border-${color}-600`, // Dynamically apply border color
      hoverClass // Hover background color
    ]"
  >
    <slot></slot>
  </button>
</template>

<script setup>
const props = defineProps({
  color: String,
})

// Dynamically compute the hover class for the button
const hoverClass = computed(() => {
  return `hover:bg-${props.color}-400`
});
</script>