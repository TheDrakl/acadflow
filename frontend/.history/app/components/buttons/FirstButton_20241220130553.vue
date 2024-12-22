<template>
  <button
    :class="[`bg-transparent border-solid border-[2px] border-yellow-600 text-yellow-600 text-md font-roboto font-[400] py-2 px-8 rounded-xl hover:bg-gray-400 text-${color}-400`

    ]"
  >
    <slot></slot>
  </button>
</template>

<script setup>

const props = defineProps({
  color: String,
})

</script>
