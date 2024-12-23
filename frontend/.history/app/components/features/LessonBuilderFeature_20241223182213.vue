<template>
    <div class="w-[80%] h-56 rounded-3xl border-[3px] border-white shadow-lg">
        <h1 class="mt-2 text-center font-roboto text-2xl font-[500]">{{ title }}</h1>
        <p class="p-2 mt-2 font-montserrat font-[00]">
            <slot></slot>
        </p>
    </div>
</template>

<script setup>
const props = defineProps({
    title: String,
})

</script>