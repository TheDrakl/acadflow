<template>
  <div class="font-roboto w-[60%]">
    <!-- SKELETON -->
    <div v-if="loading" class="animate-pulse">
      <div class="flex justify-between mb-4">
        <div class="bg-gray-300 rounded-full w-16 h-16"></div>
        <div class="bg-gray-300 rounded-md w-28 h-6"></div>
      </div>
      <div class="bg-gray-300 h-8 w-48 rounded-md mb-4"></div>
      <div class="flex flex-row mt-6 items-center">
        <div class="bg-gray-300 h-8 w-32 rounded-md mr-4"></div>
        <div class="bg-gray-300 h-6 w-24 rounded-md"></div>
      </div>
      <div class="bg-gray-300 h-4 w-36 rounded-md mt-4"></div>
      <div class="bg-gray-300 h-10 w-full rounded-md mt-6"></div>
      <div>
        <div class="bg-gray-300 h-6 w-64 rounded-md mt-8"></div>
        <ul class="list-none mt-2">
          <li v-for="i in 3" :key="i" class="flex items-center mb-2">
            <div class="bg-gray-300 h-4 w-4 rounded-full mr-2"></div>
            <div class="bg-gray-300 h-4 w-48 rounded-md"></div>
          </li>
        </ul>
      </div>
    </div>

    <div v-else>
      <div class="flex flex-col">
        <div class="flex justify-between">
          <Icon name="bxs:cube" size="4rem" class="text-yellowMain -ml-1" />
          <div v-if="mostSold">
            <h3
              class="border-[1px] bg-milkWhite border-yellowMain py-1 px-2 rounded-lg shadow-md font-[300] font-inter"
            >
              Best seller
            </h3>
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
            <li v-for="feature in features" :key="feature">
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
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

const props = defineProps({
  title: String,
  price: String,
  discount: String,
  description: String,
  features: Array,
  time: String,
  mostSold: Boolean,
});

const loading = ref(true);

onMounted(() => {
  setTimeout(() => {
    loading.value = false;
  }, 2000); // Simulate data fetching delay
});
</script>
