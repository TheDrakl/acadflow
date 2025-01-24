<template>
  <div class="lg:pb-6 dark:bg-darkGrayBg2 bg-white">
    <div
      class="container mx-auto px-0 py-0 md:py-4 lg:px-4 text-black lg:pt-4 lg:pb-4 font-roboto font-[300] rounded-2xl bg-gradient-to-r dark:bg-transparent dark:from-transparent dark:to-transparent from-transparent via-gray-100 to-transparent"
    >
      <nav class="hidden md:flex justify-between items-center h-auto mt-2">
        <!-- Logo -->
        <div class="logo">
          <NuxtLink
            to="/"
            class="group transition duration-300 relative hover:text-black dark:hover:text-white"
          >
            <img
              src="public/images/acadflow-logo.png"
              alt="logo"
              class="w-36 lg:w-48 h-auto cursor-pointer"
            />
          </NuxtLink>
        </div>
        <!-- Navigation -->
        <ul
          class="flex space-x-4 lg:space-x-16 xl:space-x-28 text-[1rem] lg:text-[1.15rem] text-darkGray dark:text-white"
        >
          <li>
            <NuxtLink
              to="/"
              class="group transition duration-300 relative hover:text-black dark:hover:text-white"
            >
              HOME
              <span
                class="block max-w-0 group-hover:max-w-full transition-all duration-500 h-0.5 bg-yellow-500"
              ></span>
            </NuxtLink>
          </li>
          <li>
            <NuxtLink
              to="/about"
              class="group transition duration-300 relative hover:text-black dark:hover:text-white"
            >
              ABOUT US
              <span
                class="block max-w-0 group-hover:max-w-full transition-all duration-500 h-0.5 bg-yellow-500"
              ></span>
            </NuxtLink>
          </li>
          <li>
            <NuxtLink
              to="/dashboard"
              class="group transition duration-300 relative hover:text-black dark:hover:text-white"
            >
              DASHBOARD
              <span
                class="block max-w-0 group-hover:max-w-full transition-all duration-500 h-0.5 bg-yellow-500"
              ></span>
            </NuxtLink>
          </li>
          <li>
            <NuxtLink
              to="/contact"
              class="group transition duration-300 relative hover:text-black dark:hover:text-white"
            >
              CONTACT
              <span
                class="block max-w-0 group-hover:max-w-full transition-all duration-500 h-0.5 bg-yellow-500"
              ></span>
            </NuxtLink>
          </li>
        </ul>
        <div class="flex flex-row justify-between space-x-20 items-center">
          <FirstButton
            v-if="!isLoggedIn"
            class="self-center text-yellow-600 border-solid border-[2px] border-yellow-600 bg-transparent hover:bg-yellow-600 dark:hover:border-yellow-700 hover:text-white py-2 px-8"
            @click="openLogin"
            >Sign In</FirstButton
          >
          <FirstButton
            v-if="isLoggedIn"
            class="self-center text-yellow-600 border-solid border-[2px] border-yellow-600 bg-transparent hover:bg-yellow-600 dark:hover:border-yellow-700 hover:text-white py-2 px-8"
            @click="logout()"
            >Log Out</FirstButton
          >
          <Icon
            :name="iconName"
            size="1.5rem"
            @click="toggleColorMode"
            class="cursor-pointer hidden lg:flex lg:absolute top-[1.75rem] right-16 bg-black dark:bg-[#FFEB3B]"
          />
          <div
            class="bg-[url('/images/user-image.png')] bg-cover bg-center w-[2.5rem] h-[2.2rem] lg:w-[2.8rem] lg:h-[2.8rem] rounded-full border-[1px] border-solid border-gray-400 shadow-sm cursor-pointer"
            @click="handleProfile()"
          ></div>
        </div>
      </nav>
      <nav class="flex md:hidden float-right ml-auto">
        <Icon
          name="pajamas:hamburger"
          size="2rem"
          class="absolute right-4 top-4 bg-black dark:bg-[#FFEB3B]"
        />
      </nav>
    </div>
  </div>
  <!-- Modals for registration / login -->
  <Teleport to="body" v-if="isOpenLogin">
    <div>
      <LoginForm
        @close="closeLogin"
        @toggle="toggle"
        @success="loggedInFn($event)"
      />
    </div>
  </Teleport>
  <Teleport to="body" v-if="isOpenRegister">
    <div>
      <RegisterForm
        @close="closeRegister"
        @toggle="toggle"
        @success="loggedInFn($event)"
      />
    </div>
  </Teleport>
  <div
    v-if="isLoading"
    class="absolute inset-0 flex justify-center items-center bg-opacity-50 bg-gray-800 z-20"
  >
    <Spinning />
  </div>
  <div
    v-if="successLogin"
    class="fixed bottom-0 inset-0 flex justify-center items-end z-50"
    data-aos="fade-top"
    data-aos-offset="200"
    data-aos-easing="ease-in-sine"
  >
    <h2 class="p-4 bg-green-300 text-center font-roboto w-full">
      You successfully logged in account.
    </h2>
  </div>
  <div
    v-if="successRegister"
    class="fixed bottom-0 inset-0 flex justify-center items-end z-50"
  >
    <h2 class="p-4 bg-green-300 text-center font-roboto w-full">
      You successfully registered an account, now you can login
    </h2>
  </div>
  <main class="">
    <NuxtPage />
  </main>
  <footer>
    <div
      class="bg-[#333333] text-white p-8 md:pt-16 md:px-16 md:pb-4 font-roboto"
    >
      <section
        class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-[1fr,1.5fr,1.5fr,1fr] gap-12 md:gap-16 text-center md:text-start"
      >
        <!-- Gym info -->
        <div class="flex flex-col items-center">
          <h2 class="text-4xl font-bold mb-4 text-lightGray"></h2>
          <img
            src="public/images/acadflow-logo.png"
            alt=""
            class="w-full max-w-[13rem]"
          />
        </div>

        <!-- Links -->
        <div class="lg:flex-col items-center hidden lg:flex">
          <h2 class="text-xl font-inter mb-4 text-lightGray">Services</h2>
          <ul class="space-y-2 text-md text-milkBlue font-montserrat text-center">
            <li><a href="#" class="hover-underline-animation">Home</a></li>
            <li><a href="#" class="hover-underline-animation">About</a></li>
            <li><a href="#" class="hover-underline-animation">Dashboard</a></li>
            <li><a href="#" class="hover-underline-animation">Contact</a></li>
            <li><a href="#" class="hover-underline-animation">Privacy Policy</a></li>
          </ul>
        </div>

        <!-- Contact Info -->
        <div class="flex flex-col items-center text-center">
          <h2 class="text-xl font-inter mb-4 text-lightGray">Contact Us</h2>
          <ul class="space-y-4 text-md text-milkBlue font-montserrat">
            <li class="flex items-center justify-center">
              <font-awesome-icon
                :icon="['fa', 'phone']"
                class="text-milkBlue"
              />
              <span class="ml-3">+123 456 7890</span>
            </li>
            <li class="flex items-center justify-center">
              <font-awesome-icon
                :icon="['fa', 'envelope']"
                class="text-milkBlue"
              />
              <span class="ml-3">info@email.com</span>
            </li>
            <li class="flex items-center justify-center">
              <font-awesome-icon :icon="['fa', 'map']" class="text-milkBlue" />
              <span class="ml-3">Address 2, A1</span>
            </li>
          </ul>
        </div>

        <!-- Social Media Links -->
        <div class="flex flex-col items-center">
          <div class="space-between space-x-8 text-3xl ">
            <Icon
              name="mdi:instagram"
              style="color: white"
              size="2rem"
              class="text-milkBlue cursor-pointer"
            ></Icon>
            <Icon
              name="uil:youtube"
              style="color: white"
              size="2rem"
              class="text-milkBlue cursor-pointer"
            ></Icon>
            <Icon
              name="mdi:twitter"
              style="color: white"
              size="2rem"
              class="text-milkBlue cursor-pointer"
            ></Icon>
            <Icon
              name="ic:baseline-facebook"
              style="color: white"
              size="2rem"
              class="text-milkBlue cursor-pointer"
            ></Icon>
          </div>
          <!-- Newsletter -->
          <div class="flex flex-col items-center mt-8">
            <h2 class="text-xl font-inter mb-4 text-gray-200 text-center">
              Newsletter
            </h2>
            <form class="flex flex-col space-y-4">
              <input
                type="email"
                placeholder="Your email"
                class="p-2 w-[25vh] rounded bg-black text-white border border-lightGray placeholder-lightGray focus:outline-none focus:ring-1 focus:ring-orange-900"
              />
              <button
                class="p-2 rounded-md bg-buttonColor hover:bg-[#001F4D] text-milkWhite font-montserrat"
              >
                Subscribe
              </button>
            </form>
          </div>
        </div>
      </section>

      <!-- All rights reserved by -->
      <div class="border-t-[1px] border-colorLine mt-16"></div>
      <div class="mt-8 mb-4 text-center">
        <p class="text-sm font-montserrat text-milkBlue tracking-wide">
          &copy; 2025 AcadFlow. All rights reserved. Created by
          <span class="text-yellowMain hover:underline"
            ><a href="https://github.com/TheDrakl">TheDrakl</a></span
          >
        </p>
      </div>
    </div>
  </footer>
</template>
<script setup>
const isOpenLogin = ref(false);
const isOpenRegister = ref(false);
const colorMode = useColorMode();
const iconName = ref("material-symbols:light-mode");
const auth = useAuth();
const isLoading = ref(false);
const success = ref(false);
const successLogin = ref(false);
const successRegister = ref(false);

const isLoggedIn = ref(false);

const router = useRouter();
// Move the async function inside onMounted to avoid the warning

const loggedInFn = (component) => {
  if (component === "login") {
    successLogin.value = true;
    success.value = true;
    setTimeout(() => {
      successLogin.value = false;
    }, 1500);
    return (isLoggedIn.value = true);
  }

  if (component === "register") {
    successRegister.value = true;
    success.value = true;
    setTimeout(() => {
      successRegister.value = false;
    }, 1500);
  }
};

// Check if the user is logged in

const handleProfile = () => {
  if (!isLoggedIn.value) {
    isOpenLogin.value = true;
    console.log(isLoggedIn.value);
  } else if (isLoggedIn.value) {
    router.push("/profile");
    console.log(isLoggedIn.value);
  }
};

const isLoggedInFn = async () => {
  try {
    const authenticated = await auth.isAuthenticated.value;
    return (isLoggedIn.value = authenticated);
  } catch (error) {
    console.error("Error checking authentication:", error);
    isLoggedIn.value = false; // Ensure it's set to false in case of error
  }
};

// Toggle login / register components
const toggle = (val) => {
  if (val == "login") {
    isOpenLogin.value = false;
    isOpenRegister.value = true;
  } else if (val == "register") {
    isOpenLogin.value = true;
    isOpenRegister.value = false;
  }
};

const getCsrfToken = () => {
  const name = "csrftoken=";
  const cookies = document.cookie.split(";");

  for (let i = 0; i < cookies.length; i++) {
    let cookie = cookies[i].trim();
    if (cookie.indexOf(name) === 0) {
      return cookie.substring(name.length, cookie.length);
    }
  }
  return null;
};
const logout = async () => {
  try {
    isLoading.value = true;
    const csrfToken = getCsrfToken();
    auth.logout();
    const response = await $fetch("http://127.0.0.1:8000/users/logout/", {
      method: "POST",
      headers: {
        "X-CSRFToken": csrfToken,
      },
      credentials: "include",
    });
    router.push("/");
    isLoading.value = false;

    if (response.status === 403) {
      console.log(
        "Forbidden: You do not have permission to perform this action."
      );
      try {
        auth.logout();
      } catch (error) {
        console.log("Error:", error);
      }
    } else {
      auth.logout();
      console.log(response.value);

      isLoggedIn.value = false;
    }
  } catch (error) {
    if (error.response) {
      const { status } = error.response;
      if (status === 403) {
        console.log(
          "Forbidden: You do not have permission to perform this action."
        );
        try {
          auth.logout();
        } catch (error) {
          console.log("Error:", error);
        }
      } else {
        console.error("Unexpected error:", error);
      }
    } else {
      console.error("Logout error:", error);
    }
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

// Color mode toggle
const toggleColorMode = () => {
  colorMode.preference = colorMode.value === "light" ? "dark" : "light";
};

onMounted(async () => {
  // First, check authentication
  await isLoggedInFn();

  // Now, update the icon for color mode
  iconName.value =
    colorMode.value === "light"
      ? "material-symbols:nightlight"
      : "material-symbols:light-mode";
});
</script>
