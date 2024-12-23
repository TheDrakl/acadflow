<template>
    <div>
        <div class="flex justify-between items-center font-roboto">
            <div
                class="bg-yellowMain w-14 h-14 lg:w-16 lg:h-16 flex items-center justify-center rounded-full mr-4 text-white text-xl lg:text-2xl shadow-lg"
            >
                {{ num }}
            </div>
            <div class="flex-1 min-w-0 text-base lg:text-xl max-w-[80%] mr-auto">
                <slot></slot>
            </div>
        </div>
    </div>

</template>