<template>
  <div>
    <section class="bg-yellowMain min-h-screen">
      <div class="mt-10 flex justify-between items-center pt-16">
        <div class="left flex flex-col flex-1">
          <img src="public/images/hero-img.png" alt="Illustration" class="h-[480px] w-[720px]" />
        </div>
        <div class="right flex flex-1 flex-col text-white">
          <h1 class="font-[300] text-6xl text-right mr-auto">Transform Learning <br>with AcadFlow</h1>
          <p class="mt-[24px] font-[300]">
            Build schools, create courses, and manage students and teachers with
            scalable, flexible features
          </p>
          <FirstButton>REGISTER NOW</FirstButton>
        </div>
      </div>
    </section>
  </div>
</template>


<script setup>
import FirstButton from '~/components/buttons/FirstButton.vue';
</script>

<style scoped>
body {
  @apply font-roboto
}
</style>