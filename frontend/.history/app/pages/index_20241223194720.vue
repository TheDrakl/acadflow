<template>
  <div>
    <HeroSection />

    <LearningProgramSection />

    <LessonBuilderSection />
    <PricingPlansSection />
    
    <RegistrationFormSection />
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
