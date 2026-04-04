/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,jsx}'],
  theme: {
    extend: {
      colors: {
        navy: '#0A0F1E',
        'navy-light': '#111827',
        'navy-card': '#0f1629',
        primary: '#00D4AA',
        accent: '#00D4AA',
        'accent-2': '#00FFD1',
        coral: '#FF4757',
        amber: '#FFB800',
        success: '#00FF88',
      },
      fontFamily: {
        display: ['Syne', 'system-ui', 'sans-serif'],
        body: ['DM Sans', 'system-ui', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
