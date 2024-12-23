<template>
    <section class="mt-12 min-h-[120vh] lg:min-h-[90vh] bg-yellowMain">
      <h1
        class="font-[500] text-4xl lg:text-4xl text lg:leading-[1] pt-12 font-montserrat text-center"
        data-aos="fade-center"
        data-aos-offset="400"
        data-aos-easing="ease-in-sine"
      >
        To begin, please register <br>on our platform
      </h1>
      <div class="container mx-auto py-6 grid grid-cols-1 lg:grid-cols-2 gap-6">
        <!-- Left Side -->
        <div class="left flex flex-col items-center mt-20 order-2 lg:order-1"
        data-aos="fade-right"
        data-aos-offset="300"
        data-aos-easing="ease-in-sine">
          <h3 class="text-3xl">Sign up</h3>
          <div class="flex flex-col w-full max-w-[80%] mt-6 space-y-4 items-center">
            <SignUpInput :text="'Enter your name'" ></SignUpInput>
            <SignUpInput :text="'Enter your email address'"></SignUpInput>
            <SignUpInput :text="'Enter your password'"></SignUpInput>
            <SignUpInput :text="'Enter your password again'"></SignUpInput>
          </div>
          <p class="text-white ml-44 text-sm mt-2">Already have an account? <span class="cursor-pointer hover:underline">Log in</span></p>
          <FirstButton class="mt-[24px] text-white border-solid border-[2px] border-yellow-500 bg-buttonColor py-[0.7rem] w-[40%] shadow-lg">Register</FirstButton>
        </div>

        <!-- Right Side -->
        <div class="right flex justify-center lg:justify-end items-center order-1 lg:order-2">
          <img
            src="/images/register-form.png"
            alt="Illustration"
            class="h-[380px] w-[420px] lg:h-[600px] lg:w-[660px]"
            draggable="false"
            loading="lazy"
            data-aos="fade-left"
            data-aos-offset="340"
            data-aos-easing="ease-in-sine"
          />
        </div>
      </div>
    </section>
</template>