<template>
  <section
    class="min-h-[120vh] lg:min-h-[90vh] bg-milkWhite dark:bg-darkGrayBg dark:text-gray-300"
    id="pricing"
  >
    <div class="container mx-auto py-6">
      <!-- Title Section -->
      <div class="flex flex-col items-center" data-aos="fade-center" data-aos-offset="500" data-aos-easing="ease-in-sine">
        <h1 class="font-[500] text-5xl lg:text-5xl lg:leading-[1] pt-4 font-montserrat text-center">
          Pricing Plans
        </h1>

        <!-- Toggle Section -->
        <div class="bg-gray-200 rounded-md h-[2.2rem] mt-12 text-blue-500 flex flex-row justify-center items-center p-[2px] font-inter">
          <div class="rounded-md px-6 py-1 cursor-pointer hover:text-white hover:bg-blue-500 dark:hover:bg-gray-600" :class="{ 'bg-gray-100': activeAnnual }" @click="toggleAnnual('annual')">
            <h4>
              Annual
              <span class="text-black bg-blue-200 rounded-lg py-[1px] px-[4px]">
                -15%
              </span>
            </h4>
          </div>
          <div class="rounded-md px-6 py-1 cursor-pointer hover:text-white hover:bg-blue-500 dark:hover:bg-gray-600" :class="{ 'bg-gray-100': !activeAnnual }" @click="toggleAnnual('monthly')">
            <h4>Monthly</h4>
          </div>
        </div>
      </div>

      <!-- Pricing Cards -->
      <div class="grid grid-cols-1 sm:grid-cols-1 lg:grid-cols-3 gap-20 mt-[4%] place-items-center mx-4 lg:mx-10">
        <PricingPlan
          v-for="plan in formattedPlans"
          :key="plan.id" 
          :title="plan.name"
          :price="plan.price"
          :discount="plan.discount"
          :description="plan.description"
          :features="plan.features"
          :mostSold="plan.mostSold"
          :time="time"
          :loading="isLoading"
          class="pricing-card bg-white dark:bg-[#333333]"
          data-aos="fade-up"
          data-aos-duration="1000"
          data-aos-offset="300"
        />
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';

const isLoading = ref(false);
const plans = ref([]);

const fetchPricePlans = async () => {
  isLoading.value = true;
  try {
    const data = await $fetch("http://127.0.0.1:8000/api/pricing/");
    plans.value = data; // Set plans value when data is received
  } catch (error) {
    console.error("Error fetching price plans:", error);
    // Handle error if needed (e.g., show a message to the user)
  } finally {
    isLoading.value = false; // Set isLoading to false after the fetch attempt
  }
};

const activeAnnual = ref(true);

const toggleAnnual = (type) => {
  if (type === "annual") {
    activeAnnual.value = true;
  } else {
    activeAnnual.value = false;
  }
};

const time = computed(() => (activeAnnual.value ? "year" : "month"));

onMounted(() => {
  fetchPricePlans();
});

// Format plans before passing them down to PricingPlan
const formattedPlans = computed(() => {
  return plans.value.map(plan => {
    return {
      ...plan,
      price: parseFloat(plan.price).toFixed(0), 
      discount: parseFloat(plan.discount).toFixed(0)
    };
  });
});
</script>

<style scoped>
/* Responsive container size for small screens */
.container {
  max-width: 1200px;
}

/* Pricing card hover adjustments */
.pricing-card {
  width: 100%;
  max-width: 350px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  border-radius: 0.5rem;
  padding: 1.5rem;
  transition: transform 150ms ease, box-shadow 150ms ease;
}

.pricing-card:hover {
  transform: scale(1.04);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
}
</style>