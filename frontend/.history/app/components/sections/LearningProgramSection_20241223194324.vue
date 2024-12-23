<section class="mt-12 min-h-[120vh] lg:min-h-[90vh] bg-milkWhite">
    <div
      class="flex flex-col lg:flex-row justify-center lg:justify-between items-center mx-4"
    >
      <div class="flex-shrink-0 w-full lg:w-[54%] mt-16 flex justify-center">
        <img
          src="/images/learning.png"
          alt="Illustration"
          class="h-[220px] w-[360px] lg:h-[600px] lg:w-[660px]"
          draggable="false"
          loading="lazy"
          data-aos="fade-right"
          data-aos-offset="200"
          data-aos-easing="ease-in-sine"
        />
      </div>
      <div class="flex flex-col items-center w-full mt-6">
        <div
          data-aos="fade-left"
          data-aos-offset="180"
          data-aos-easing="ease-in-sine"
        >
          <h1
            class="font-[500] text-6xl lg:text-6xl text lg:leading-[1] mt-12 font-montserrat text-center lg:mr-[15%]"
          >
            Engaging Courses
          </h1>
          <p class="text-center lg:mr-[18%] mt-[20px] font-roboto-[300]">
            Perfect for self-paced learning, interactive lessons, or
            feedback-driven programs that students<br />
            can purchase and complete on their schedule.
          </p>
        </div>
        <div class="space-y-12 mt-8">
          <LearningProgramFeatures
            :num="1"
            data-aos="fade-left"
            data-aos-offset="150"
            data-aos-easing="ease-in-sine"
          >
            Set up a course or workshop effortlessly—add a title, an image,
            and get started in minutes!</LearningProgramFeatures
          >
          <LearningProgramFeatures
            :num="2"
            data-aos="fade-left"
            data-aos-offset="150"
            data-aos-easing="ease-in-sine"
          >
            Enrich your course with interactive content using 20+ customizable
            lesson blocks designed to engage
            learners.</LearningProgramFeatures
          >
          <LearningProgramFeatures
            :num="3"
            data-aos="fade-left"
            data-aos-offset="130"
            data-aos-easing="ease-in-sine"
            >Easily enroll students by sharing their email addresses—we’ll
            handle the rest to provide a seamless
            experience.</LearningProgramFeatures
          >
          <LearningProgramFeatures
            :num="4"
            data-aos="fade-left"
            data-aos-offset="120"
            data-aos-easing="ease-in-sine"
            >Monitor student progress and provide tailored feedback on
            assignments to help them succeed.</LearningProgramFeatures
          >
        </div>
      </div>
    </div>
  </section>