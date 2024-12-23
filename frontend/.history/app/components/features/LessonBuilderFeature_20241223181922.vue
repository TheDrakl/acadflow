<template>
    <div class="w-[70%] h-40 rounded-2xl border-[3px] border-white shadow-lg">
        <h1>{{ title }}</h1>
        <p class="p-2">
            <slot></slot>
        </p>
    </div>
</template>

<script setup>
const props = defineProps({
    title: String,
})

</script>