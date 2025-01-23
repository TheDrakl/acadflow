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
          <div class="w-full">
            <label for="loginEmail" class="sr-only">Email</label>
            <input
              type="text"
              id="loginEmail"
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
          <div class="w-full">
            <label for="loginPassword" class="sr-only">Password</label>
            <input
              type="password"
              id="loginPassword"
              name="password"
              class="w-3/4 h-[2.5rem] px-4 border font-roboto border-gray-900 rounded-lg focus:outline-none focus:ring-1 focus:ring-gray-500 focus:border-gray-500 transition duration-300"
              :class="{ 'border-[2px] border-red-500': form.password.error }"
              placeholder="Enter your password"
              v-model="form.password.value"
              @focus="handleFocus('password')"
              autocomplete="current-password"
            />
            <p
              v-if="form.password.error"
              class="text-red-500 flex float-right mx-14"
            >
              {{ form.password.error }}
            </p>
          </div>
        </div>
        <div v-if="errors && errors.length" class="text-red-400 font-inter mt-1 flex ml-auto mr-[12%]">
          <p>{{ errors }}</p>
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
    </form>
  </div>
</template>
<script setup>
const form = reactive({
  email: { value: "", error: "" },
  password: { value: "", error: "" },
});

const success = ref(false);
const errors = ref([]);

const isLoading = ref(false);
const token = ref("");

const auth = useAuth();

const emit = defineEmits(["close", "toggle", "success"]);

const openRegister = () => {
  emit("toggle", "login");
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
  errors.value = []
};

const validateForm = (form) => {
  let isValid = true;

  // Email validation regex
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  Object.keys(form).forEach((key) => {
    if (!form[key].value.trim()) {
      form[key].error = "This field is required";
      isValid = false;
    } else if (key === "email" && !emailRegex.test(form[key].value)) {
      form[key].error = "Please enter a valid email address";
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
      const isLoggedIn = await loginUser();
      console.log(isLoggedIn);
      if (isLoggedIn) {
        success.value = true;
        emit("success", "login");

        setTimeout(() => {
          success.value = false;
          closeModal();
        }, 1000);
      } else {
        console.error("Login failed: Invalid credentials or API error.");
        errors.value = "Invalid email or password!";
      }
    } catch (error) {
      console.error("Error during login:", error);
    } finally {
      isLoading.value = false;
    }
  }
};

const loginUser = async () => {
  try {
    const response = await $fetch("http://127.0.0.1:8000/users/login/", {
      method: "POST",
      body: {
        email: form.email.value,
        password: form.password.value,
      },
      headers: {
        "Content-Type": "application/json",
      },
      credentials: "include",

      onResponse({ response }) {
        if (response.status !== 200) {
          throw new Error(`Unexpected response status: ${response.status}`);
        }
      },
    });

    console.log("Login successful:", response);
    token.value = response.tokens.access;
    auth.login(token.value);
    console.log(token.value);
    return true;
  } catch (err) {
    if (err.data) {
      console.error("Validation errors:", err.data);
      errors.value = err.data;
    } else {
      console.error("Unexpected error:", err);
    }
  }
};

onMounted(() => {
  if ((typeof window !== "undefined") & !success) {
    document.body.style.overflow = "hidden";
    window.addEventListener("keydown", handleButton);
  }
});

onBeforeUnmount(() => {
  if ((typeof window !== "undefined") & !success) {
    document.body.style.overflow = "auto";
    window.removeEventListener("keydown", handleButton);
  }
});
</script>
