module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      // tailwind에 없는 것을 확장해서 사용가능
      spacing: {
        // classname: css
        "25vh": "25vh",
        "50vh": "50vh",
        "75vh": "75vh"
      }
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
