import { ref } from 'vue';
import {jwtDecode} from 'jwt-decode'; // Ensure jwtDecode is imported correctly

export function useAuth() {
  // Reactive state for managing login status and access token
  const logged = ref(false);
  const accessToken = ref('');

  // Check if a token exists in localStorage on initial load
  if (process.client) {
    const token = localStorage.getItem('access_token');
    if (token) {
      logged.value = true;
      accessToken.value = token;
    }
  }

  // Method to log in and store the token
  const login = (token) => {
    localStorage.setItem('access_token', token);
    logged.value = true;
    accessToken.value = token;
  };

  // Method to log out and clear the token
  const logout = () => {
    localStorage.removeItem('access_token');
    logged.value = false;
    accessToken.value = '';
  };

  // Method to check if the user is authenticated (token is valid)
  const isAuthenticated = () => {
    return logged.value && !!accessToken.value;
  };

  // Method to check if access token is expired
  const isAccessTokenExpired = () => {
    if (!accessToken.value) return true; // If no access token, consider expired
    try {
      const decoded = jwtDecode(accessToken.value);
      console.log("Token is not expired");
      console.log(decoded.exp * 1000, Date.now());
      return decoded.exp * 1000 < Date.now(); // Check expiration
    } catch (error) {
      console.error("Error decoding token:", error);
      return true; // If decoding fails, treat as expired
    }
  };

  const refreshToken = async () => {
    try {
      const response = await $fetch('http://127.0.0.1:8000/users/token/refresh/', {
        method: 'POST',
        credentials: 'include',
      });
      console.log(response)
  
      if (response && response.access) {
        console.log('Token refreshed:', response.access);
        login(response.access); // Store the new access token
      } else {
        console.error('Token refresh failed:', response);
        logout(); // Token refresh failed, log out
      }
    } catch (error) {
      console.error('Error refreshing token:', error);
      logout(); // In case of an error, log out
    }
  };

  onMounted(() => {
    if (isAuthenticated() && isAccessTokenExpired()) {
      console.log("Token expired, refreshing...");
      refreshToken();
    }
    else {
      console.log("Token is not expired");
    }
  })

  return {
    logged,
    accessToken,
    login,
    logout,
    isAuthenticated,
    isAccessTokenExpired,
    refreshToken,
  };
}