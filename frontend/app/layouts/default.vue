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
          <NuxtLink to="/profile">
            <div
              class="bg-[url('/images/user-image.png')] bg-cover bg-center w-[2.5rem] h-[2.2rem] lg:w-[2.8rem] lg:h-[2.8rem] rounded-full border-[1px] border-solid border-gray-400 shadow-sm cursor-pointer"
            ></div>
          </NuxtLink>
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
      <LoginForm @close="closeLogin" @toggle="toggle" />
    </div>
  </Teleport>
  <Teleport to="body" v-if="isOpenRegister">
    <div>
      <RegisterForm @close="closeRegister" @toggle="toggle" />
    </div>
  </Teleport>
  <main class="">
    <NuxtPage />
  </main>

  <footer class="bg-deepYellow min-h-[50vh]"></footer>
</template>
<script setup>
const isOpenLogin = ref(false);
const isOpenRegister = ref(false);
const colorMode = useColorMode();
const iconName = ref("material-symbols:light-mode");
const auth = useAuth();

const isLoggedIn = ref(false);

// Move the async function inside onMounted to avoid the warning

// Check if the user is logged in
const isLoggedInFn = () => {
  try {
    const authenticated = auth.isAuthenticated();
    isLoggedIn.value = authenticated;
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
    const csrfToken = getCsrfToken();
    auth.logout()
    const response = await $fetch("http://127.0.0.1:8000/users/logout/", {
      method: "POST",
      headers: {
        "X-CSRFToken": csrfToken,
      },
      credentials: "include",
    });

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
