/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./app/app.vue",
    "./app.vue",
    "./error.vue",
  ],
  theme: {
    extend: {
      fontFamily: {
        roboto: ['Roboto', 'sans-serif'],
        montserrat: ['Montserrat', 'sans-serif'],
        inter: ['Inter', 'sans-serif']
      },
      colors: {
        buttonColor: '#003366',
        yellowMain: '#EAAA00',
        milkWhite: '#F5F5F5',
        lightGray: '#949494',
        darkGray: '2D2D2D'
      }
    },
  },
  plugins: [],
}