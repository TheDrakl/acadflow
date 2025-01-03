<template>
  <section
    class="min-h-[120vh] lg:min-h-[90vh] bg-yellowMain dark:bg-yellowMainBg"
    id="register"
  >
    <h1
      class="font-[500] text-4xl lg:text-4xl text lg:leading-[1] pt-12 font-montserrat text-center"
      data-aos="fade-center"
      data-aos-offset="400"
      data-aos-easing="ease-in-sine"
    >
      To begin, please register <br />on our platform
    </h1>
    <div class="container mx-auto py-6 grid grid-cols-1 lg:grid-cols-2 gap-6">
      <!-- Left Side -->
      <div
        class="left flex flex-col items-center mt-20 order-2 lg:order-1"
        data-aos="fade-right"
        data-aos-offset="300"
        data-aos-easing="ease-in-sine"
      >
        <h3 class="text-3xl">Sign up</h3>
        <div
          class="flex flex-col w-full max-w-[80%] mt-6 space-y-4 items-center"
        >
          <!-- Email Input -->
          <div class="w-full max-w-[70%]">
            <label for="email" class="sr-only">Email</label>
            <div
              class="h-12 border border-lightGray rounded-2xl focus-within:border-primary"
            >
              <input
                id="email"
                type="email"
                v-model="form.email.value"
                class="w-full h-full px-4 bg-transparent outline-none rounded-2xl placeholder-gray-700 text-base"
                placeholder="Enter your email"
                autocomplete="email"
              />
            </div>
            <p v-if="form.email.error" class="text-red-500 text-sm">{{ form.email.error }}</p>
          </div>

          <!-- Password Input -->
          <div class="w-full max-w-[70%]">
            <label for="password" class="sr-only">Password</label>
            <div
              class="h-12 border border-lightGray rounded-2xl focus-within:border-primary"
            >
              <input
                id="password"
                type="text"
                v-model="form.password.value"
                class="w-full h-full px-4 bg-transparent outline-none rounded-2xl placeholder-gray-700 text-base"
                placeholder="Enter your password"
                autocomplete="new-password"
              />
            </div>
            <p v-if="form.password.error" class="text-red-500 text-sm">{{ form.password.error }}</p>
          </div>

          <!-- Confirm Password Input -->
          <div class="w-full max-w-[70%]">
            <label for="confirm-password" class="sr-only">Confirm Password</label>
            <div
              class="h-12 border border-lightGray rounded-2xl focus-within:border-primary"
            >
              <input
                id="confirm-password"
                type="text"
                v-model="form.password2.value"
                class="w-full h-full px-4 bg-transparent outline-none rounded-2xl placeholder-gray-700 text-base"
                placeholder="Confirm your password"
                autocomplete="new-password"
              />
            </div>
            <p v-if="form.password2.error" class="text-red-500 text-sm">{{ form.password2.error }}</p>
          </div>
        </div>

        <p class="text-white dark:text-gray-100 ml-44 text-sm mt-2">
          Already have an account?
          <span class="cursor-pointer hover:underline" @click="openLogin"
            >Log in</span
          >
        </p>
        <FirstButton
          class="mt-[24px] text-white border-solid border-[2px] border-yellow-500 bg-buttonColor py-[0.7rem] w-[40%] shadow-lg"
          @click="handleRegister"
        >Register</FirstButton>
      </div>

      <!-- Right Side -->
      <div
        class="right flex justify-center lg:justify-end items-center order-1 lg:order-2"
      >
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
  <Teleport to="body" v-if="isOpenLogin">
    <div>
      <LoginForm @close="closeLogin" @toggle="toggle" />
    </div>
  </Teleport>
  <Teleport to="body" v-if="isOpenRegister">
    <div>
      <RegisterForm @close="closeRegister" @toggle="toggle" />
    </div>
  </Teleport>
</template>


<script setup>
import { ref, reactive } from 'vue';

const isOpenLogin = ref(false);
const isOpenRegister = ref(false);

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

const handleRegister = () => {
  if (validateForm(form)) {
    // Proceed with registration
    console.log("Form is valid, proceed with registration.");
  } else {
    console.log("Form is invalid.");
  }
};

const toggle = (val) => {
  if (val == "login") {
    isOpenLogin.value = false;
    isOpenRegister.value = true;
  } else if (val == "register") {
    isOpenLogin.value = true;
    isOpenRegister.value = false;
  }
};

const openLogin = () => {
  isOpenLogin.value = true;
};

const closeLogin = () => {
  isOpenLogin.value = false;
};

const closeRegister = () => {
  isOpenRegister.value = false;
};
</script>