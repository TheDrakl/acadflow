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
import { onMounted } from "vue";
import { useAuth } from "@/composables/useAuth"; // Adjust the import path accordingly

const { isAuthenticated, isAccessTokenExpired, refreshToken } = useAuth();

onMounted(() => {
  if (isAuthenticated() && isAccessTokenExpired()) {
    console.log("Token expired, refreshing...");
    refreshToken();
  }
});
</script>
