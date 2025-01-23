<template>
  <div class="profile-page" v-if="auth.isAuthenticated.value">
    <h1 class="text-xl font-bold mb-4">Profile Page</h1>
    <div v-if="user">
      <p><strong>Name:</strong> {{ user.name || "" }}</p>
      <p><strong>Email:</strong> {{ user.email }}</p>
    </div>
    <div v-else>
      <p>Loading user data...</p>
    </div>
    s
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

const user = ref(null)
const error = ref(null)
const auth = useAuth()

definePageMeta({
  middleware: ['auth-user']
})


onMounted(async () => {
  try {
    const response = await $fetch('http://127.0.0.1:8000/users/profile/', {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('access_token')}`
      }
    })
    user.value = response
  } catch (err) {
    error.value = err
    console.error('Error fetching user data:', err)
  }
})
</script>
