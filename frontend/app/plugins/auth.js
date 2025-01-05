// plugins/auth.js
export default defineNuxtPlugin(nuxtApp => {
    nuxtApp.hook('app:created', () => {
      const originalFetch = nuxtApp.$fetch;
  
      // Override the global $fetch method
      nuxtApp.$fetch = async (url, options = {}) => {
        const token = localStorage.getItem('access_token');
  
        // If the token exists, add it to the Authorization header
        if (token) {
          if (!options.headers) options.headers = {};
          options.headers['Authorization'] = `Bearer ${token}`;
        }
  
        const response = await originalFetch(url, options);
  
        // Handle token expiry (e.g., refresh the token, logout user)
        if (response.status === 401) {
          // Implement token refresh logic here or force the user to login again
        }
  
        return response;
      };
    });
  });