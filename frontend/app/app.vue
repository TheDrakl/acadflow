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

const { isAuthenticated, isAccessTokenExpired, refreshToken } = useAuth();

onMounted(() => {
  // checkToken()
  if (isAuthenticated && isAccessTokenExpired() ) {
    console.log("Token expired, refreshing...");
    refreshToken();
  }
});

</script>