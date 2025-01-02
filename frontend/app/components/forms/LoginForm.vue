<template>
  <div
    class="fixed inset-0 bg-gray-200 bg-opacity-50 flex justify-center items-center z-50"
    @keydown="handleEscape"
    tabindex="-1"
    @click.self="closeModal"
  >
    <div
      class="bg-white p-6 rounded-lg shadow-lg max-w-md w-full items-center justify-center flex flex-col relative"
      @click.stop
    >
      <Icon
        name="material-symbols:close"
        class="absolute top-4 right-4 z-10 cursor-pointer"
        size="1.8rem"
        @click="closeModal"
      />
      <div class="flex flex-col space-y-4 items-center justify-center mt-8">
        <ContinueWithForm
          name="Google"
          path="/icons/google-logo.svg"
        ></ContinueWithForm>
        <ContinueWithForm
          name="GitHub"
          path="/icons/github-logo.svg"
        ></ContinueWithForm>
      </div>
      <p class="font-roboto font-[500] text-md my-2">Or</p>
      <div
        class="w-full flex flex-col space-y-4 justify-center items-center text-center"
      >
        <input
          type="text"
          class="w-3/4 h-[2.5rem] px-4 border font-roboto border-gray-900 rounded-lg focus:outline-none focus:ring-2 focus:ring-gray-500 focus:border-gray-500 transition duration-300"
          placeholder="Enter your email"
        />
        <input
          type="text"
          class="w-3/4 h-[2.5rem] px-4 border font-roboto border-gray-900 rounded-lg focus:outline-none focus:ring-2 focus:ring-gray-500 focus:border-gray-500 transition duration-300"
          placeholder="Enter your password"
        />
      </div>
      <div class="w-full flex justify-center">
        <FirstButton
          class="mt-6 text-white dark:text-white bg-buttonColor py-[0.7rem] px-8 lg:px-12 w-3/4 shadow-lg"
          >Log In</FirstButton
        >
      </div>
      <div class="flex justify-center text-center flex-col space-y-2 mt-4">
        <p
          class="text-blue-400 hover:text-blue-500 underline font-roboto cursor-pointer"
        >
          Reset password
        </p>
        <p class="font-roboto">
          <span class="text-black">Don't have an account? </span>
          <span
            class="text-blue-400 hover:text-blue-500 underline cursor-pointer"
            @click="openRegister"
            >Register</span
          >
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
const emit = defineEmits(["close", "toggle"]);

const openRegister = () => {
  emit("toggle", "login");
};

const closeModal = () => {
  emit("close");
};

const handleEscape = (event) => {
  if (event.key === "Escape") {
    closeModal();
  }
};

onMounted(() => {
  window.addEventListener("keydown", handleEscape); // Add global event listener for Escape key
});

onBeforeUnmount(() => {
  window.removeEventListener("keydown", handleEscape); // Remove event listener on cleanup
});
</script>
