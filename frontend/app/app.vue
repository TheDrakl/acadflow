<template>
  <div class="overflow-hidden">
    <NuxtLayout>
      <NuxtLoadingIndicator />
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>


<style>
html,
body {
  @apply bg-white;
  @apply dark:bg-darkGrayBg;
}
</style>

<script setup>
import { useAuth } from './composables/useAuth'; // or wherever your useAuth function is

const { isAuthenticated, isAccessTokenExpired, refreshToken } = useAuth();

onMounted(() => {
  if (isAuthenticated() && isAccessTokenExpired()) {
    console.log("Token expired, refreshing...");
    refreshToken();
  } else {
    console.log("Token is not expired");
  }
});
</script>
