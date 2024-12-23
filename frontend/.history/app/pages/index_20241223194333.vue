<template>
  <div>
    <!-- Hero Section -->
    <HeroSection />

    <!-- Learning Program Section -->
    <LearningProgramSection />

    <!-- Lesson Builder Blocks -->
    <section class="mt-12 min-h-[120vh] lg:min-h-[90vh] bg-yellowMain">
      <div class="container mx-auto py-12">
        <h1
          class="font-[500] text-5xl lg:text-6xl text lg:leading-[1] pt-4 font-montserrat text-center"
          data-aos="fade-center"
          data-aos-offset="400"
          data-aos-easing="ease-in-sine"
        >
          Lesson Builder <br />
          Interactive Blocks
        </h1>
        <!-- Grid for Features -->
        <div
          class="grid grid-cols-1 lg:grid-cols-2 gap-y-16 gap-x-8 mt-16 place-items-center"
        >
          <LessonBuilderFeature
            title="Interactive Exercises"
            data-aos="fade-right"
            data-aos-offset="200"
            data-aos-easing="ease-in-sine"
            >Design dynamic lessons with various interactive exercises, such as
            fill-in-the-blanks, multiple-choice questions, reorder elements,
            True/False, match pairs, and open-ended responses. These exercises
            foster engagement and cater to different learning
            styles.</LessonBuilderFeature
          >
          <LessonBuilderFeature
            title="Multimedia blocks"
            data-aos="fade-left"
            data-aos-offset="200"
            data-aos-easing="ease-in-sine"
            >Enhance your lessons with multimedia content including audio,
            video, images, and galleries. These elements create an immersive
            learning experience and make the lessons more engaging for
            students.</LessonBuilderFeature
          >
          <LessonBuilderFeature
            title="Integration blocks"
            data-aos="fade-right"
            data-aos-offset="200"
            data-aos-easing="ease-in-sine"
            >Easily integrate content from popular platforms like YouTube,
            WordWall, and Quizlet. Add videos, quizzes, and other resources
            seamlessly to enrich your lessons with external
            content.</LessonBuilderFeature
          >
          <LessonBuilderFeature
            title="Additional Tools"
            data-aos="fade-left"
            data-aos-offset="200"
            data-aos-easing="ease-in-sine"
            >Customize lessons with helpful elements such as titles, text
            blocks, file download buttons, external links, and Teacher’s notes.
            These tools provide clarity and offer additional resources to guide
            students through their learning.</LessonBuilderFeature
          >
        </div>
      </div>
    </section>
    <!-- Pricing Plans -->
    <section class="mt-12 min-h-[120vh] lg:min-h-[90vh] bg-milkWhite"></section>

    <!-- Registration Form -->
    <section class="mt-12 min-h-[120vh] lg:min-h-[90vh] bg-yellowMain">
      <h1
        class="font-[500] text-4xl lg:text-4xl text lg:leading-[1] pt-12 font-montserrat text-center"
        data-aos="fade-center"
        data-aos-offset="400"
        data-aos-easing="ease-in-sine"
      >
        To begin, please register <br>on our platform
      </h1>
      <div class="container mx-auto py-6 grid grid-cols-1 lg:grid-cols-2 gap-6">
        <!-- Left Side -->
        <div class="left flex flex-col items-center mt-20 order-2 lg:order-1"
        data-aos="fade-right"
        data-aos-offset="300"
        data-aos-easing="ease-in-sine">
          <h3 class="text-3xl">Sign up</h3>
          <div class="flex flex-col w-full max-w-[80%] mt-6 space-y-4 items-center">
            <SignUpInput :text="'Enter your name'" ></SignUpInput>
            <SignUpInput :text="'Enter your email address'"></SignUpInput>
            <SignUpInput :text="'Enter your password'"></SignUpInput>
            <SignUpInput :text="'Enter your password again'"></SignUpInput>
          </div>
          <p class="text-white ml-44 text-sm mt-2">Already have an account? <span class="cursor-pointer hover:underline">Log in</span></p>
          <FirstButton class="mt-[24px] text-white border-solid border-[2px] border-yellow-500 bg-buttonColor py-[0.7rem] w-[40%] shadow-lg">Register</FirstButton>
        </div>

        <!-- Right Side -->
        <div class="right flex justify-center lg:justify-end items-center order-1 lg:order-2">
          <img
            src="/images/register-form.png"
            alt="Illustration"
            class="h-[380px] w-[420px] lg:h-[600px] lg:w-[660px]"
            draggable="false"
            loading="lazy"
            data-aos="fade-left"
            data-aos-offset="340"
            data-aos-easing="ease-in-sine"
          />
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">

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
