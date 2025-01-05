export function $api<T>(
    request: Parameters<typeof $fetch<T>>[0],
    opts?: Parameters<typeof $fetch<T>>[1],
  ) {
    const auth = useAuth()
  
    return $fetch<T>(request, {
      ...opts,
      headers: {
        Authorization: auth.logged ? `Bearer ${auth.accessToken.value}` : '',
        ...opts?.headers,
      },
    })
  }