<template>
  <button
    :class="buttonClasses"
    :style="buttonStyle"
    @click="handleClick"
  >
    <slot></slot>
  </button>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue'

// Define props to make the button customizable
const props = defineProps({
  // Color options for the button
  bgColor: {
    type: String,
    default: 'transparent',
  },
  textColor: {
    type: String,
    default: 'yellow-600',
  },
  borderColor: {
    type: String,
    default: 'yellow-600',
  },
  textSize: {
    type: String,
    default: 'md',
  },
  font: {
    type: String,
    default: 'Roboto',
  },
  padding: {
    type: String,
    default: 'py-2 px-8',
  },
  rounded: {
    type: String,
    default: 'xl',
  },
  hoverColor: {
    type: String,
    default: 'gray-400',
  },
  customClasses: {
    type: String,
    default: '',
  },
  styleOverride: {
    type: Object,
    default: () => {},
  },
  onClick: {
    type: Function,
    default: () => {},
  },
})

// Computed class for dynamic styling
const buttonClasses = computed(() => [
  `bg-${props.bgColor}`,
  `border-solid border-[2px] border-${props.borderColor}`,
  `text-${props.textColor}`,
  `text-${props.textSize}`,
  `font-${props.font}`,
  `font-[400]`,
  props.padding,
  `rounded-${props.rounded}`,
  `hover:bg-${props.hoverColor}`,
  props.customClasses, // Allow additional custom classes to be passed in
])

// Button click handler (fires on click)
const handleClick = () => {
  if (props.onClick) {
    props.onClick()
  }
}
</script>

<style scoped>
/* Add any scoped styles here if needed */
</style>