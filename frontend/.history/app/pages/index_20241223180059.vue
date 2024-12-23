<template>
  <div>

    <!-- Hero Section -->
    <section class="bg-yellowMain min-h-[110vh] lg:min-h-[90vh] font-roboto">
      <div
        class="lg:mt-10 flex flex-col lg:flex-row justify-between items-center pt-20 mx-6 lg:mx-0"
      >
        <div class="left flex flex-col flex-1">
          <img
            src="/images/hero-img.png"
            alt="Illustration"
            class="h-[240px] w-[360px] lg:h-[580px] lg:w-[780px]"
            draggable="false"
            loading="lazy"
          />
        </div>
        <div
          class="right flex flex-1 flex-col text-white items-center mr-0 lg:mr-16 mt-[5%]"
        >
          <h1
            class="font-[300] text-6xl lg:text-[5.3rem] lg:leading-[1] text-center md:text-right mr-auto font-montserrat"
          >
            Transform Learning <br />with AcadFlow
          </h1>
          <p class="mt-[14px] font-[300] text-[16px] leading-6 text-center">
            Create courses and manage schools with flexible tools
          </p>

          <div class="flex flex-col lg:flex-row gap-4 mt-6" >
            <div class="w-full lg:w-auto">
              <FirstButton
                class="mt-[24px] text-white border-solid border-[2px] border-yellow-500 bg-buttonColor py-[0.7rem] px-8 lg:px-12 w-full"
              >
                Register Now
              </FirstButton>
            </div>
            <div class="w-full lg:w-auto">
              <FirstButton
                class="mt-4 lg:mt-[24px] text-white border-solid border-yellow-600 border-[2px] hover:bg-yellow-600 bg-transparent py-[0.7rem] px-8 lg:px-8 w-full"
              >
                <div class="items-center flex flex-row space-x-2">
                  <Icon
                    name="material-symbols:chat-info"
                    style="color: white"
                    size="1rem"
                  ></Icon>
                  <span>Learn more about our platform</span>
                </div>
              </FirstButton>
            </div>
          </div>

          <!-- Icons -->
          <div
            class="flex flex-col text-sm xl:-ml-[60%] mt-[10%] space-y-2 text-buttonColor"
          >
            <div class="flex flex-row items-center space-x-2">
              <Icon
                name="material-symbols:globe-uk"
                style="color: black"
                size="1.2rem"
              ></Icon>
              <p>
                Empowering education globally — connecting learners and
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
      <!-- Stars -->
      <div
        class="absolute -bottom-20 lg:bottom-2 left-1/2 transform -translate-x-1/2 text-center"
      >
        <div class="flex -space-x-3 justify-center">
          <Icon
            v-for="star in 4"
            :key="star"
            name="material-symbols:star"
            style="color: black"
            size="1.8rem"
          />
          <Icon
            name="material-symbols:star-half"
            style="color: black"
            size="1.8rem"
          />
        </div>
        <p class="font-[300] mt-2">
          Trusted by <span class="font-[400]">1.493 users</span>
        </p>
      </div>
    </section>

    <section class="mt-12 min-h-[120vh] lg:min-h-[90vh] bg-milkWhite">
      <div
        class="flex flex-col lg:flex-row justify-center lg:justify-between items-center mx-4"
      >
        <div class="flex-shrink-0 w-full lg:w-[54%] mt-16 flex justify-center">
          <img
            src="/images/learning.png"
            alt="Illustration"
            class="h-[220px] w-[360px] lg:h-[600px] lg:w-[660px]"
            draggable="false"
            loading="lazy"
            data-aos="fade-right"
            data-aos-offset="200"
            data-aos-easing="ease-in-sine"
          />
        </div>
        <div class="flex flex-col items-center w-full mt-6">
          <div
            data-aos="fade-left"
            data-aos-offset="180"
            data-aos-easing="ease-in-sine"
          >
            <h1
              class="font-[500] text-6xl lg:text-6xl text lg:leading-[1] mt-12 font-montserrat text-center lg:mr-[15%]"
            >
              Engaging Courses
            </h1>
            <p class="text-center lg:mr-[18%] mt-[20px] font-roboto-[300]">
              Perfect for self-paced learning, interactive lessons, or
              feedback-driven programs that students<br />
              can purchase and complete on their schedule.
            </p>
          </div>
          <div class="space-y-12 mt-8">
            <LearningProgramFeatures
              :num="1"
              data-aos="fade-left"
              data-aos-offset="150"
              data-aos-easing="ease-in-sine"
            >
              Set up a course or workshop effortlessly—add a title, an image,
              and get started in minutes!</LearningProgramFeatures
            >
            <LearningProgramFeatures
              :num="2"
              data-aos="fade-left"
              data-aos-offset="150"
              data-aos-easing="ease-in-sine"
            >
              Enrich your course with interactive content using 20+ customizable
              lesson blocks designed to engage
              learners.</LearningProgramFeatures
            >
            <LearningProgramFeatures
              :num="3"
              data-aos="fade-left"
              data-aos-offset="130"
              data-aos-easing="ease-in-sine"
              >Easily enroll students by sharing their email addresses—we’ll
              handle the rest to provide a seamless
              experience.</LearningProgramFeatures
            >
            <LearningProgramFeatures
              :num="4"
              data-aos="fade-left"
              data-aos-offset="120"
              data-aos-easing="ease-in-sine"
              >Monitor student progress and provide tailored feedback on
              assignments to help them succeed.</LearningProgramFeatures
            >
          </div>
        </div>
      </div>
    </section>

    <section>


    </section>
  </div>
</template>

<script setup lang="ts">
import FirstButton from "~/components/buttons/FirstButton.vue";
import LearningProgramFeatures from "~/components/features/LearningProgramFeatures.vue";

useHead({
  title: "AcadFlow | Transform Learning with AcadFlow",
  meta: [
    {
      hid: "description",
      name: "description",
      content:
        "AcadFlow allows you to create flexible courses, manage schools, and empower education globally. Perfect for students and educators alike.",
    },
    {
      hid: "og:title",
      property: "og:title",
      content: "Transform Learning with AcadFlow",
    },
    {
      hid: "og:description",
      property: "og:description",
      content:
        "Join thousands of schools transforming education with AcadFlow. Create and manage interactive courses effortlessly.",
    },
    {
      hid: "og:image",
      property: "og:image",
      content: "/images/og-image.png", // Use your image URL
    },
    {
      hid: "og:url",
      property: "og:url",
      content: "https://www.acadflow.com", // Change this to your website URL
    },
    {
      hid: "twitter:title",
      name: "twitter:title",
      content: "Transform Learning with AcadFlow",
    },
    {
      hid: "twitter:description",
      name: "twitter:description",
      content:
        "Create courses and manage schools with flexible tools. AcadFlow empowers educators and students worldwide.",
    },
    {
      hid: "twitter:image",
      name: "twitter:image",
      content: "/images/og-image.png", // Use your image URL
    },
    {
      hid: "robots",
      name: "robots",
      content: "index, follow",
    },
  ],
});
</script>

<style scoped>
body {
  @apply font-roboto;
}
</style>
