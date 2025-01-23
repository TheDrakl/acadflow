import { useAuth } from "@/composables/useAuth";

export default defineNuxtRouteMiddleware((to) => {
  const auth = useAuth();

  // Ensure the code runs only on the client
  if (process.client) {
    auth.checkToken(); // Synchronize auth state with localStorage
    if (to.path === "/profile" && !auth.isAuthenticated.value) {
      console.log("User is not authenticated. Redirecting to login...");
      window.location.href = "/login"; // Hard redirect
    }
  }
});
