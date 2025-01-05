export default defineNuxtRouteMiddleware(async (to, from) => {
  if (to.path === "/profile") {
    // Handle client-side logic (access localStorage)
    if (process.client) {
      const token = localStorage.getItem("access_token");

      if (token) {
        // If the token exists, validate it
        return navigateTo("/login");
      }
    }

    // Handle server-side logic (assume no token)
    if (process.server) {
      // Token validation would typically be done via cookies or headers for SSR
      return navigateTo("/login"); // Redirect to login if the request is server-side
    }
  }
});
