<template>
    <section class="bg-yellowMain min-h-[110vh] lg:min-h-[90vh] font-roboto">
      <div
        class="lg:mt-10 flex flex-col lg:flex-row justify-between items-center pt-20 mx-6 lg:mx-0"
      >
        <div class="left flex flex-col flex-1">
          <img
            src="/images/hero-img.png"
            alt="Illustration"
            class="h-[240px] w-[360px] lg:h-[580px] lg:w-[780px]"
            draggable="false"
            loading="lazy"
          />
        </div>
        <div
          class="right flex flex-1 flex-col text-white items-center mr-0 lg:mr-16 mt-[5%]"
        >
          <h1
            class="font-[300] text-6xl lg:text-[5.3rem] lg:leading-[1] text-center md:text-right mr-auto font-montserrat"
          >
            Transform Learning <br />with AcadFlow
          </h1>
          <p class="mt-[14px] font-[300] text-[16px] leading-6 text-center">
            Create courses and manage schools with flexible toolsf
          </p>

          <div class="flex flex-col lg:flex-row gap-4 mt-6">
            <div class="w-full lg:w-auto">
              <FirstButton
                class="mt-[24px] text-white border-solid border-[2px] border-yellow-500 bg-buttonColor py-[0.7rem] px-8 lg:px-12 w-full shadow-lg"
              >
                Register Now
              </FirstButton>
            </div>
            <div class="w-full lg:w-auto">
              <FirstButton
                class="mt-4 lg:mt-[24px] text-white border-solid border-yellow-600 border-[2px] hover:bg-yellow-600 bg-transparent py-[0.7rem] px-8 lg:px-8 w-full shadow-lg"
              >
                <div class="items-center flex flex-row space-x-2">
                  <Icon
                    name="material-symbols:chat-info"
                    style="color: white"
                    size="1rem"
                  ></Icon>
                  <span>Learn more about our platform</span>
                </div>
              </FirstButton>
            </div>
          </div>

          <!-- Icons -->
          <div
            class="flex flex-col text-sm xl:-ml-[60%] mt-[10%] space-y-2 text-buttonColor"
          >
            <div class="flex flex-row items-center space-x-2">
              <Icon
                name="material-symbols:globe-uk"
                style="color: black"
                size="1.2rem"
              ></Icon>
              <p>
                Empowering education globally — connecting learners and
                educators.”
              </p>
            </div>
            <div class="flex flex-row items-center space-x-2">
              <Icon
                name="ri:school-line"
                style="color: black"
                size="1.2rem"
              ></Icon>
              <p>
                Join over 500 schools transforming their teaching experience
                with our platform.
              </p>
            </div>
            <div class="flex flex-row items-center space-x-2">
              <Icon
                name="mdi:account-school"
                style="color: black"
                size="1.2rem"
              ></Icon>
              <p>Join 500+ schools transforming education.</p>
            </div>
          </div>
        </div>
      </div>
      <!-- Stars -->
      <div
        class="absolute -bottom-20 lg:bottom-2 left-1/2 transform -translate-x-1/2 text-center"
      >
        <div class="flex -space-x-3 justify-center">
          <Icon
            v-for="star in 4"
            :key="star"
            name="material-symbols:star"
            style="color: black"
            size="1.8rem"
          />
          <Icon
            name="material-symbols:star-half"
            style="color: black"
            size="1.8rem"
          />
        </div>
        <p class="font-[300] mt-2">
          Trusted by <span class="font-[400]">1.493 users</span>
        </p>
      </div>
    </section>
</template>