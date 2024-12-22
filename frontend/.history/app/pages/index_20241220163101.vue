<div
  class="right flex flex-1 flex-col text-white items-center mr-0 lg:mr-16"
>
  <h1
    class="font-[300] text-6xl lg:text-[5.5rem] lg:leading-[1] text-center"
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
    <span>Learn more about our platform</span>
  </p>
  <!-- Icons Section -->
  <div class="icons mt-8 flex flex-col text-sm items-start lg:ml-[-16px]">
    <div class="flex flex-row items-center space-x-2">
      <Icon
        name="material-symbols:globe-uk"
        style="color: black"
        size="1.2rem"
      ></Icon>
      <p>Empowering education globally—connecting learners and educators.</p>
    </div>
    <div class="flex flex-row items-center space-x-2">
      <Icon
        name="ri:school-line"
        style="color: black"
        size="1.2rem"
      ></Icon>
      <p>Join over 500 schools transforming their teaching experience with our platform.</p>
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
<script setup>
import FirstButton from "~/components/buttons/FirstButton.vue";
</script>

<style scoped>
body {
  @apply font-roboto;
}
</style>
