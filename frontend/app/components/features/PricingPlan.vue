<template>
  <div
    class="w-[65%] h-[40vh] min-h-full bg-transparent border-yellow-500 border-[2px] rounded-3xl font-roboto text-center"
  >
    <h1 class="text-2xl text-center pt-2 font-[700]">{{ title }}</h1>
    <p class="text-sm font-[400] font-montserrat">${{ price }} / month</p>

    <div>
      <li class="list-none text-start p-2 items-center">
        <ul v-for="feature in features" :key="feature" class="flex flex-row items-center mx-4 mb-4">
            <Icon name="material-symbols:verified" class="mr-2 bg-gray-600"></Icon>
          {{
            feature
          }}
        </ul>

      </li>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  title: {
    type: String,
    required: true,
  },
  price: {
    type: Number,
    required: true,
  },
  features: {
    type: Array,
    required: true,
  },
});
</script>
