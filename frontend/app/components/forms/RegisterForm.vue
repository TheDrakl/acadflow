<template>
  <div
    class="fixed inset-0 bg-gray-800 bg-opacity-75 flex justify-center items-center z-50"
    @keydown="handleButton"
    tabindex="-1"
    @click.self="closeModal"
  >
    <form
      @submit.prevent="handleSubmit"
      class="flex justify-center items-center w-full h-full"
    >
      <div
        class="p-6 rounded-lg shadow-lg max-w-md w-full items-center justify-center flex flex-col relative"
        :class="{ 'bg-gray-100': isLoading, 'bg-white': !isLoading, 'opacity-50 pointer-events-none': isLoading }"
        @click.stop
      >
        <!-- Close Icon -->
        <Icon
          name="material-symbols:close"
          class="absolute top-4 right-4 z-10 cursor-pointer"
          size="1.8rem"
          @click="closeModal"
        />

        <!-- Loading Spinner -->
        <div v-if="isLoading" class="absolute inset-0 flex justify-center items-center bg-opacity-50 bg-gray-800 z-20">
          <Spinning />
        </div>

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
        <div class="w-full flex flex-col space-y-4 justify-center items-center text-center">
          <!-- Email Field -->
          <div class="w-full">
            <label for="email" class="sr-only">Email Address</label>
            <input
              id="email"
              type="text"
              class="w-3/4 h-[2.5rem] px-4 border font-roboto border-gray-900 rounded-lg focus:outline-none focus:ring-1 focus:ring-gray-500 focus:border-gray-500 transition duration-300"
              :class="{ 'border-[2px] border-red-500': form.email.error }"
              placeholder="Enter your email"
              v-model="form.email.value"
              @focus="handleFocus('email')"
              autocomplete="email"
            />
            <p
              v-if="form.email.error"
              class="text-red-500 flex float-right mx-14"
            >
              {{ form.email.error }}
            </p>
          </div>
          <!-- Password Field -->
          <div class="w-full">
            <label for="password" class="sr-only">Password</label>
            <input
              id="password"
              type="text"
              class="w-3/4 h-[2.5rem] px-4 border font-roboto border-gray-900 rounded-lg focus:outline-none focus:ring-1 focus:ring-gray-500 focus:border-gray-500 transition duration-300"
              :class="{ 'border-[2px] border-red-500': form.password.error }"
              placeholder="Enter your password"
              v-model="form.password.value"
              @focus="handleFocus('password')"
              autocomplete="new-password"
            />
            <p
              v-if="form.password.error"
              class="text-red-500 flex float-right mx-14"
            >
              {{ form.password.error }}
            </p>
          </div>
          <!-- Confirm Password Field -->
          <div class="w-full">
            <label for="password2" class="sr-only">Confirm Password</label>
            <input
              id="password2"
              type="text"
              class="w-3/4 h-[2.5rem] px-4 border font-roboto border-gray-900 rounded-lg focus:outline-none focus:ring-1 focus:ring-gray-500 focus:border-gray-500 transition duration-300"
              :class="{ 'border-[2px] border-red-500': form.password2.error }"
              placeholder="Confirm your password"
              v-model="form.password2.value"
              @focus="handleFocus('password2')"
              autocomplete="new-password"
            />
            <p
              v-if="form.password2.error"
              class="text-red-500 flex float-right mx-14"
            >
              {{ form.password2.error }}
            </p>
          </div>
        </div>
        <!-- Submit Button -->
        <div class="w-full flex justify-center">
          <FirstButton
            class="mt-6 text-white dark:text-white bg-buttonColor py-[0.7rem] px-8 lg:px-12 w-3/4 shadow-lg"
            >Register</FirstButton
          >
        </div>
        <!-- Footer Links -->
        <div class="flex justify-center text-center flex-col space-y-2 mt-4">
          <p class="font-roboto">
            <span class="text-black">Already have an account? </span>
            <span
              class="text-blue-400 hover:text-blue-500 underline cursor-pointer"
              @click="openLogin"
              >Log In</span
            >
          </p>
        </div>
      </div>
    </form>
  </div>
</template>

<script setup>
const emit = defineEmits(["close", "toggle"]);

const form = reactive({
  email: { value: "", error: "" },
  password: { value: "", error: "" },
  password2: { value: "", error: "" },
});

const isLoading = ref(false);

const validateForm = (form) => {
  let isValid = true;

  // Email validation regex
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  // Validate fields
  Object.keys(form).forEach((key) => {
    if (!form[key].value.trim()) {
      form[key].error = "This field is required";
      isValid = false;
    } else if (key === "email" && !emailRegex.test(form[key].value)) {
      form[key].error = "Please enter a valid email address";
      isValid = false;
    } else if (key === "password2" && form[key].value !== form.password.value) {
      form[key].error = "Passwords do not match";
      isValid = false;
    } else {
      form[key].error = "";
    }
  });

  return isValid;
};

const handleSubmit = () => {
  console.log("Form submitted");
  const isValid = validateForm(form);

  if (isValid) {
    console.log("Form is valid:", form);
    isLoading.value = true;
    setTimeout(() => {
      isLoading.value = false;
    }, 3000);
  } else {
    console.log("Form is invalid:", form);
  }
};

const openLogin = () => {
  emit("toggle", "register");
};

const closeModal = () => {
  emit("close");
};

const handleButton = (event) => {
  if (event.key === "Escape") {
    closeModal();
  } else if (event.key === 'Enter') {
    handleSubmit()
  }
};

const handleFocus = (field) => {
  form[field].error = "";
};

onMounted(() => {
  document.body.style.overflow = "hidden"; // Disable scrolling
  window.addEventListener("keydown", handleButton);
});

onBeforeUnmount(() => {
  document.body.style.overflow = "auto"; // Re-enable scrolling
  window.removeEventListener("keydown", handleButton);
});
</script>