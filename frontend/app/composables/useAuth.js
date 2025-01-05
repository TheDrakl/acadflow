export function useAuth() {
  // Reactive state for managing login status and access token
  const logged = ref(false);
  const accessToken = ref('');

  // Check if a token exists in localStorage on initial load
  const token = localStorage.getItem('access_token');
  if (token) {
    logged.value = true;
    accessToken.value = token;
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

  return {
    logged,
    accessToken,
    login,
    logout,
    isAuthenticated,
  };
}