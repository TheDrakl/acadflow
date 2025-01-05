export function $api<T>(
  request: Parameters<typeof $fetch<T>>[0],
  opts?: Parameters<typeof $fetch<T>>[1],
): Promise<T> {
  const auth = useAuth();

  const executeRequest = async () => {
    // Ensure token refresh before making the request
    if (auth.logged && auth.isAccessTokenExpired()) {
      console.log('Access token expired. Attempting to refresh...');
      try {
        await auth.refreshToken(); // Refresh token before proceeding
      } catch (error) {
        console.error('Token refresh failed:', error);
        auth.logout(); // Logout if refresh fails
        throw new Error('Authentication failed');
      }
    }

    // Make the API request with the latest token
    return $fetch<T>(request, {
      ...opts,
      headers: {
        Authorization: auth.logged ? `Bearer ${auth.accessToken.value}` : '',
        ...opts?.headers,
      },
    });
  };

  // Handle request errors globally (optional)
  return executeRequest().catch((error) => {
    console.error('API request error:', error);

    // Handle specific errors (e.g., 401 Unauthorized)
    if (error.response?.status === 401) {
      console.log('Unauthorized. Logging out.');
      // auth.logout();
    }

    throw error; // Re-throw the error to handle it in the calling function
  });
}
