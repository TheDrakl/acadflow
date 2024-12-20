<template>
  <div>
    <section class="bg-yellowMain min-h-screen">
      <div class="mt flex justify-between items-center ">
        <div class="left flex-1">
          <img src="public/images/hero-img.png" alt="Illustration" />
        </div>
        <div class="right">
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