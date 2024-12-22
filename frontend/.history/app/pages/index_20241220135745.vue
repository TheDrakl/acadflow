<template>
  <div>
    <section class="bg-yellowMain min-h-screen">
      <div class="lg:mt-10 flex flex-col lg:flex-row justify-between items-center pt-20 mx-6 lg:mx-0">
        <div class="left flex flex-col flex-1">
          <img
            src="public/images/hero-img.png"
            alt="Illustration"
            class="h-[240px] w-[360px] lg:h-[580px] lg:w-[780px]"
            draggable="false"
          />
        </div>
        <div class="right flex flex-1 flex-col text-white items-center mr-0 lg:mr-16">
          <h1 class="font-[300] text-6xl lg:text-[5.5rem] lg:leading-[1] text-right mr-auto">
            Transform Learning <br />with AcadFlow
          </h1>
          <p class="mt-[24px] font-[300] text-[20px] leading-6 text-center">
            Build schools, create courses,<br />
            and manage students and teachers<br />
            with scalable, flexible features
          </p>
          <FirstButton
            class="mt-[24px] text-white border-solid border-[2px] border-yellow-600 bg-buttonColor py-[0.7rem] px-14"
            >REGISTER NOW</FirstButton
          >

        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import FirstButton from "~/components/buttons/FirstButton.vue";
</script>

<style scoped>
body {
  @apply font-roboto;
}
</style>
