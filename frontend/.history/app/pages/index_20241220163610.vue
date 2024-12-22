<template>
  <div>
    <section class="bg-yellowMain min-h-screen">
      <div
        class="lg:mt-10 flex flex-col lg:flex-row justify-between items-center pt-20 mx-6 lg:mx-0"
      >
        <div class="left flex flex-col flex-1">
          <img
            src="public/images/hero-img.png"
            alt="Illustration"
            class="h-[240px] w-[360px] lg:h-[580px] lg:w-[780px]"
            draggable="false"
          />
        </div>
        <div
          class="right flex flex-1 flex-col text-white items-center mr-0 lg:mr-16"
        >
          <h1
            class="font-[300] text-6xl lg:text-[5.5rem] lg:leading-[1] text-right mr-auto mt-12"
          >
            Transform Learning <br />with AcadFlow
          </h1>
          <p class="mt-[24px] font-[300] text-[20px] leading-6 text-center">
            Build schools, create courses,<br />
            and manage students and teachers<br />
            with scalable, flexible features
          </p>
          <FirstButton
            class="mt-[18px] text-white border-solid border-[2px] border-yellow-500 bg-buttonColor py-[0.7rem] px-24"
            >Register Now</FirstButton
          >
          <p
            class="mt-[6px] items-center flex justify-between space-x-1 cursor-pointer text-sm hover:underline"
          >
            <Icon
              name="material-symbols:chat-info"
              style="color: white"
              size="1rem"
            ></Icon>
            <span>Learn more about out platform</span>
          </p>
          <!-- Icons -->
          <div
            class="flex flex-col text-sm xl:-ml-[40%] mt-16 space-y-2 text-buttonColor"
          >
            <div class="flex flex-row items-center space-x-2">
              <Icon
                name="material-symbols:globe-uk"
                style="color: black"
                size="1.2rem"
              ></Icon>
              <p>
                Empowering education globally—connecting learners and
                educators.”
              </p>
            </div>
            <div class="flex flex-row items-center space-x-2">
              <Icon
                name="ri:school-line"
                style="color: black"
                size="1.2rem"
              ></Icon>
              <p>
                Join over 500 schools transforming their teaching experience
                with our platform.
              </p>
            </div>
            <div class="flex flex-row items-center space-x-2">
              <Icon
                name="mdi:account-school"
                style="color: black"
                size="1.2rem"
              ></Icon>
              <p>Join 500+ schools transforming education.</p>
            </div>
          </div>
        </div>
      </div>
      <div class="-space-x-2">
        <Icon v-for="star in 4"
          name="material-symbols:star"
          style="color: black"
          size="1.2rem"
        />
        <Icon
          name="material-symbols:star-half"
          style="color: black"
          size="1.2rem"
        />
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
