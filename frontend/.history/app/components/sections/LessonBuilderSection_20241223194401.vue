<template>
    <section class="mt-12 min-h-[120vh] lg:min-h-[90vh] bg-yellowMain">
      <div class="container mx-auto py-12">
        <h1
          class="font-[500] text-5xl lg:text-6xl text lg:leading-[1] pt-4 font-montserrat text-center"
          data-aos="fade-center"
          data-aos-offset="400"
          data-aos-easing="ease-in-sine"
        >
          Lesson Builder <br />
          Interactive Blocks
        </h1>
        <!-- Grid for Features -->
        <div
          class="grid grid-cols-1 lg:grid-cols-2 gap-y-16 gap-x-8 mt-16 place-items-center"
        >
          <LessonBuilderFeature
            title="Interactive Exercises"
            data-aos="fade-right"
            data-aos-offset="200"
            data-aos-easing="ease-in-sine"
            >Design dynamic lessons with various interactive exercises, such as
            fill-in-the-blanks, multiple-choice questions, reorder elements,
            True/False, match pairs, and open-ended responses. These exercises
            foster engagement and cater to different learning
            styles.</LessonBuilderFeature
          >
          <LessonBuilderFeature
            title="Multimedia blocks"
            data-aos="fade-left"
            data-aos-offset="200"
            data-aos-easing="ease-in-sine"
            >Enhance your lessons with multimedia content including audio,
            video, images, and galleries. These elements create an immersive
            learning experience and make the lessons more engaging for
            students.</LessonBuilderFeature
          >
          <LessonBuilderFeature
            title="Integration blocks"
            data-aos="fade-right"
            data-aos-offset="200"
            data-aos-easing="ease-in-sine"
            >Easily integrate content from popular platforms like YouTube,
            WordWall, and Quizlet. Add videos, quizzes, and other resources
            seamlessly to enrich your lessons with external
            content.</LessonBuilderFeature
          >
          <LessonBuilderFeature
            title="Additional Tools"
            data-aos="fade-left"
            data-aos-offset="200"
            data-aos-easing="ease-in-sine"
            >Customize lessons with helpful elements such as titles, text
            blocks, file download buttons, external links, and Teacher’s notes.
            These tools provide clarity and offer additional resources to guide
            students through their learning.</LessonBuilderFeature
          >
        </div>
      </div>
    </section>
</template>