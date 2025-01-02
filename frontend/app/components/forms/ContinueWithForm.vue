<template>
  <div
    class="flex flex-row items-center mx-12 border-[1.5px] border-solid border-black w-4/5 justify-center rounded-lg font-roboto font-[500] text-lg cursor-pointer"
  >
    <div>
      <img
        :src="path"
        alt="google-logo"
        :width="imgWidth"
        :height="imgHeight"
        class="select-none object-contain"
        draggable="false"
      />
    </div>
    <div>
      <h3 class="ml-4">Continue with {{ name }}</h3>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
    name: {
        type: String,
    },
    path: {
        type: String,
        default: '/icons/google-logo.svg'
    },
    imgHeight: {
        type: String,
        default: '36px'
    },
    imgWidth: {
        type: String,
        default: '36px'
    }
})

</script>
