<template>
  <div class="font-roboto w-[60%]">
    <div class="flex flex-col">
      
      <div class="flex justify-between">
        <Icon name="bxs:cube" size="4rem" class="text-yellowMain -ml-1" />
        <div v-if="mostSold">
          <h3 class="border-[1px] bg-milkWhite border-yellowMain py-1 px-2 rounded-lg shadow-md font-[300] font-inter">Best seller</h3>
        </div>
      </div>
      <h2 class="font-[500] text-3xl mt-2">Plus</h2>
      <div class="flex flex-row mt-6 items-center">
        <h3 class="font-[700] text-4xl flex items-center space-x-2">
          <span>£{{ price }}</span>
          <span
            class="p-1 px-3 bg-blue-100 rounded-lg font-[300] text-base font-inter"
            >-{{ discount }}% Discount</span
          >
        </h3>
      </div>
      <p class="font-montserrat">per user/{{ time }}, billed annually</p>
      <div class="mt-2">
        <FirstButton
          class="mt-4 lg:mt-[20px] text-white bg-buttonColor py-[0.7rem] px-8 lg:px-8 w-full shadow-lg"
          >Upgrade To {{ title }}</FirstButton
        >
      </div>
      <div>
        <h3 class="mt-8 text-xl font-[500]">{{ description }}</h3>
        <ul class="list-none text-base mt-1 text-start text-gray-700">
          <li v-for="feature in features">
            <span
              ><Icon
                name="gridicons:checkmark"
                size="1rem"
                class="text-gray-600"
            /></span>
            <span>{{ feature }}</span>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  title: String,
  price: String,
  discount: String,
  description: String,
  features: Array,
  time: String,
  mostSold: Boolean,
});
</script>
