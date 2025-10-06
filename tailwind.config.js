/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./dedicacion/templates/**/*.html",
    "./templates/**/*.html",
    "./**/*.html",
  ],
  theme: {
    extend: {
      colors: {
        'love-pink': '#fdf2f8',
        'love-purple': '#faf5ff',
        'soft-rose': '#fecdd3',
        'warm-pink': '#fbcfe8',
        'light-lavender': '#e9d5ff',
      },
      fontFamily: {
        'cursive': ['"Dancing Script"', 'cursive'],
        'elegant': ['"Playfair Display"', 'serif'],
        'simple': ['"Inter"', 'sans-serif'],
      },
      animation: {
        'float': 'float 6s ease-in-out infinite',
        'sparkle': 'sparkle 2s ease-in-out infinite',
        'gentle-bounce': 'gentle-bounce 3s ease-in-out infinite',
        'pulse-soft': 'pulse-soft 4s ease-in-out infinite',
      },
      keyframes: {
        float: {
          '0%, 100%': { transform: 'translateY(0px) rotate(0deg)' },
          '50%': { transform: 'translateY(-20px) rotate(5deg)' },
        },
        sparkle: {
          '0%, 100%': { opacity: '0.3', transform: 'scale(1)' },
          '50%': { opacity: '1', transform: 'scale(1.2)' },
        },
        'gentle-bounce': {
          '0%, 100%': { transform: 'translateY(0)' },
          '50%': { transform: 'translateY(-15px)' },
        },
        'pulse-soft': {
          '0%, 100%': { opacity: '0.6' },
          '50%': { opacity: '1' },
        }
      },
      backgroundImage: {
        'gradient-love': 'linear-gradient(135deg, #fdf2f8 0%, #faf5ff 50%, #f0f9ff 100%)',
      }
    },
  },
  plugins: [],
}