/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      './templates/**/*.html',
  ],
  theme: {
    extend: {
      fontFamily: {
        nunito: ['Nunito']
      },
      height: {
        'sidebar': '42rem',
      }
    },
  },
}
