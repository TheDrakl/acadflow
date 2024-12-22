<template>
  <div>
    <section class="bg-yellowMain min-h-screen">
      <div class="mt-10 flex justify-between items-center pt-16">
        <div class="left flex flex-col flex-1">
          <img
            src="public/images/hero-img.png"
            alt="Illustration"
            class="h-[580px] w-[780px]"
            draggable="false"
          />
        </div>
        <div class="right flex flex-1 flex-col text-white items-center mr-16">
          <h1 class="font-[300] text-[5.5rem] leading-[1] text-right mr-auto">
            Transform Learning <br />with AcadFlow
          </h1>
          <p class="mt-[24px] font-[300] text-[20px] leading-6 text-center">
            Build schools, create courses,<br />
            and manage students and teachers<br />
            with scalable, flexible features
          </p>
          <FirstButton
            class="mt-[24px] text-white border-solid border-[2px] border-yellow-600 bg-buttonColor py-[0.7rem] px-14 hover:py-1"
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
