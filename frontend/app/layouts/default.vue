<template>
  <div class="lg:pb-6 dark:bg-darkGrayBg2 bg-white">
    <div
      class="container mx-auto px-0 lg:px-4 text-black lg:pt-4 lg:pb-4 font-roboto font-[300] rounded-2xl bg-gradient-to-r dark:bg-transparent dark:from-transparent dark:to-transparent from-transparent via-gray-100 to-transparent"
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
              class="w-48 h-auto cursor-pointer"
            />
          </NuxtLink>
        </div>
        <!-- Navigation -->
        <ul
          class="flex space-x-8 lg:space-x-16 xl:space-x-28 text-[1rem] lg:text-[1.15rem] text-darkGray dark:text-white"
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
            class="self-center text-yellow-600 border-solid border-[2px] border-yellow-600 bg-transparent hover:bg-yellow-600 dark:hover:border-yellow-700 hover:text-white py-2 px-8"
            @click="openLogin"
            >Sign In</FirstButton
          >
          <Icon
            :name="iconName"
            size="1.5rem"
            @click="toggleColorMode"
            class="cursor-pointer hidden lg:flex lg:absolute top-[1.75rem] right-16 bg-black dark:bg-[#FFEB3B]"
          />
          <div
            class="bg-[url('/images/user-image.png')] bg-cover bg-center w-[2.8rem] h-[2.8rem] rounded-full border-[1px] border-solid border-gray-400 shadow-sm cursor-pointer"
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
const iconName = ref('material-symbols:light-mode')

// Toggle login / register components
const toggle = (val) => {
  if (val == "login") {
    isOpenLogin.value = false;
    isOpenRegister.value = true;
    console.log(process.server)
    console.log(process.client)
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


// Color mode
const toggleColorMode = () => {
  if (colorMode.value === 'light') {
    colorMode.preference = 'dark';
  } else {
    colorMode.preference = 'light';
  }
};

onMounted(() => {
  // Now we safely set the icon based on the color mode after the component has mounted
  iconName.value = colorMode.value === 'light' ? 'material-symbols:nightlight' : 'material-symbols:light-mode';
});

</script>
