export default defineNuxtRouteMiddleware((to, from) => {
  if (to.path === "/profile") {
    try {
      const token = localStorage.getItem("token");
      if (token) {
        return true;
      } else {
        return navigateTo("/login");
      }
    } catch (e) {
      console.log(e);
      return abortNavigation(); // This should stop the navigation to /about
    }
  }
});
