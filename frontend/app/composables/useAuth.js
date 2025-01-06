import { ref } from "vue";
import { jwtDecode } from "jwt-decode"; // Ensure jwtDecode is imported correctly

export function useAuth() {
  const logged = ref(false);
  const accessToken = ref("");

  // Ensure checkToken is called when initializing useAuth

  const isAuthenticated = () => {
    return logged.value && !!accessToken.value;
  };

  const login = (token) => {
    localStorage.setItem("access_token", token);
    logged.value = true;
    accessToken.value = token;
  };

  const logout = () => {
    localStorage.removeItem("access_token");
    logged.value = false;
    accessToken.value = "";
  };

  const isAccessTokenExpired = () => {
    if (!accessToken.value) return true;

    try {
      const decoded = jwtDecode(accessToken.value);
      const isExpired = decoded.exp * 1000 < Date.now();
      console.log('isExpired', isExpired);
      return isExpired;
    } catch (error) {
      console.error("Error decoding token:", error);
      return true;
    }
  };

  // Ensure this function checks the token in localStorage first
  const checkToken = () => {
    if (process.client) {
      const token = localStorage.getItem("access_token");
      if (token) {
        logged.value = true;
        accessToken.value = token;
      } else {
        accessToken.value = "";
      }
    }
  };
  checkToken()

  const refreshToken = async () => {
    if (!isAuthenticated()) {
      console.log(
        "User is not authenticated or token is valid, skipping refresh."
      );
      return;
    }

    try {
      const response = await $fetch(
        "http://127.0.0.1:8000/users/token/refresh/",
        {
          method: "POST",
          credentials: "include",
        }
      );
      if (response && response.access) {
        console.log("Token refreshed:", response.access);
        console.log("Logging in using refreshed token");
        login(response.access);
      }
    } catch (error) {
      console.error("Error refreshing token:", error);
      logout();
    }
  };

  return {
    logged,
    accessToken,
    login,
    logout,
    isAuthenticated,
    isAccessTokenExpired,
    refreshToken,
    checkToken,
  };
}