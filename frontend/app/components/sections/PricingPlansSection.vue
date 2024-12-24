<template>
  <section class="mt-12 min-h-[120vh] lg:min-h-[90vh] bg-milkWhite">
    <div class="container mx-auto py-6">
      <h1
        class="font-[500] text-5xl lg:text-5xl text lg:leading-[1] pt-4 font-montserrat text-center"
        data-aos="fade-center"
        data-aos-offset="200"
        data-aos-easing="ease-in-sine"
      >
        Pricing Plans
      </h1>
      <div class="grid grid-cols-4 mt-12 place-items-center">
        <PricingPlan :title="'Basic Plan'" :price="20" :features="['feature1', 'feature2', 'feature2', 'feature2', 'feature2']"></PricingPlan>
        <PricingPlan :title="'Basic Plan'" :price="20" :features="['feature1', 'feature2', 'feature2', 'feature2', 'feature2']"></PricingPlan>
        <PricingPlan :title="'Basic Plan'" :price="20" :features="['feature1', 'feature2', 'feature2', 'feature2', 'feature2']"></PricingPlan>
        <PricingPlan :title="'Basic Plan'" :price="20" :features="['feature1', 'feature2', 'feature2', 'feature2', 'feature2']"></PricingPlan>
      </div>
    </div>
  </section>
</template>
