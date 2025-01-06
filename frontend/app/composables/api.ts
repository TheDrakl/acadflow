export function $api<T>(
  request: Parameters<typeof $fetch<T>>[0],
  opts?: Parameters<typeof $fetch<T>>[1],
): Promise<T> {
  const auth = useAuth();

  // Ensure token is valid or refreshed before making the request
  if (auth.logged && auth.isAccessTokenExpired()) {
    console.log('Access token expired. Attempting to refresh...');
    return auth.refreshToken().then(() => {
      // After refreshing, make the API request with the latest token
      return $fetch<T>(request, {
        ...opts,
        headers: {
          Authorization: auth.logged ? `Bearer ${auth.accessToken.value}` : '',
          ...opts?.headers,
        },
      });
    }).catch((error) => {
      console.error('Token refresh failed:', error);
      auth.logout(); // Logout if refresh fails
      throw new Error('Authentication failed');
    });
  }

  // If the token is valid, directly make the API request
  return $fetch<T>(request, {
    ...opts,
    headers: {
      Authorization: auth.logged ? `Bearer ${auth.accessToken.value}` : '',
      ...opts?.headers,
    },
  });
}