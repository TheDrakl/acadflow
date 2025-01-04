<template>
  <div
    class="fixed inset-0 bg-gray-800 bg-opacity-75 flex justify-center items-center z-50"
    @keydown="handleButton"
    tabindex="-1"
    @click.self="closeModal"
    v-if="!success"
  >
    <form
      @submit.prevent="handleSubmit"
      class="flex justify-center items-center w-full h-full"
    >
      <div
        class="p-6 rounded-lg shadow-lg max-w-md w-full items-center justify-center flex flex-col relative"
        :class="{
          'bg-gray-100': isLoading,
          'bg-white': !isLoading,
          'opacity-50 pointer-events-none': isLoading,
        }"
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
        <div
          v-if="isLoading"
          class="absolute inset-0 flex justify-center items-center bg-opacity-50 bg-gray-800 z-20"
        >
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
        <div
          class="w-full flex flex-col space-y-4 justify-center items-center text-center"
        >
          <!-- Email Field -->
          <div class="w-full">
            <label for="registerEmail" class="sr-only">Email Address</label>
            <input
              id="registerEmail"
              type="email"
              name="email"
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
            <label for="registerPassword" class="sr-only">Password</label>
            <input
              id="registerPassword"
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
            <label for="registerPassword2" class="sr-only"
              >Confirm Password</label
            >
            <input
              id="registerPassword2"
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
  <div
    v-if="success"
    class="fixed bottom-0 inset-0 flex justify-center items-end z-50"
  >
    <h2 class="p-4 bg-green-400 text-center font-roboto w-full">
      You successfully registered an account, now you can login
    </h2>
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

const success = ref(false);

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

const handleSubmit = async () => {
  const isValid = validateForm(form);

  if (isValid) {
    isLoading.value = true;
    try {
      await registerUser(); // Wait for the registration to complete
      success.value = true;
      setTimeout(() => {
        success.value = false;
        closeModal();
      }, 3000);
    } catch (error) {
      console.error("Error during registration:", error);
    } finally {
      isLoading.value = false; // Ensure this runs after the process completes
    }
  }
};

const registerUser = async () => {
  try {
    const response = await $fetch("http://127.0.0.1:8000/users/register/", {
      method: "POST", // Ensure method is uppercase
      body: {
        email: form.email.value, // Access the correct property
        name: "",
        password: form.password.value, // Ensure you provide the correct value
        confirm_password: form.password2.value, // Match the field name in your backend
      },
      headers: {
        "Content-Type": "application/json", // Ensure proper content type
      },
    });

    console.log("Registration successful:");
    console.log(response);
  } catch (err) {
    console.error("An unexpected error occurred:", err);
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
  } else if (event.key === "Enter") {
    handleSubmit();
  }
};

const handleFocus = (field) => {
  form[field].error = "";
};

onMounted(() => {
  if (typeof window !== "undefined") {
    document.body.style.overflow = "hidden";
    window.addEventListener("keydown", handleButton);
  }
});

onBeforeUnmount(() => {
  if (typeof window !== "undefined") {
    document.body.style.overflow = "auto";
    window.removeEventListener("keydown", handleButton);
  }
});
</script>
