<template>
  <div>
    <section class="bg-yellowMain min-h-screen">
      <div class="mt-10 flex justify-between items-center ">
        <div class="left flex flex-1 mt-28">
          <img src="public/images/hero-img.png" alt="Illustration" class="h-[480px] w-[720px]" />
        </div>
        <div class="right flex flex-1 flex-col">
          <h1>Transform Learning with AcadFlow</h1>
          <p>
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