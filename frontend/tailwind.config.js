/** @type {import('tailwindcss').Config} */
export default {
  darkMode: 'class',
  content: [
    './index.html',
    './src/**/*.{vue,js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      transitionDuration: {
        DEFAULT: '300ms',
      },
      transitionTimingFunction: {
        DEFAULT: 'cubic-bezier(0.4, 0, 0.2, 1)',
      },
      fontFamily: {
        sans: ['Vazirmatn', 'Inter', 'system-ui', '-apple-system', 'sans-serif'],
        latin: ['Inter', 'system-ui', '-apple-system', 'sans-serif'],
      },
      colors: {
        brand: {
          50: '#FFF9E0',
          100: '#FFF3BF',
          200: '#FFE680',
          300: '#FFD940',
          400: '#FFD700',
          500: '#E6C200',
          600: '#B89800',
          700: '#8A7200',
          800: '#5C4C00',
          900: '#2E2600',
          950: '#171300',
        },
        gold: {
          DEFAULT: '#FFD700',
          dark: '#B8860B',
          light: '#FFE44D',
        },
        surface: {
          base: 'var(--bg-base)',
          card: 'var(--bg-card)',
          elevated: 'var(--bg-elevated, var(--bg-card))',
          input: 'var(--bg-input)',
          hover: 'var(--bg-hover)',
          navbar: 'var(--bg-navbar)',
          footer: 'var(--bg-footer)',
        },
        success: {
          light: '#D1FAE5',
          DEFAULT: '#10B981',
          dark: '#065F46',
        },
        danger: {
          light: '#FEE2E2',
          DEFAULT: '#EF4444',
          dark: '#991B1B',
        },
        warning: {
          light: '#FEF3C7',
          DEFAULT: '#F59E0B',
          dark: '#92400E',
        },
      },
      boxShadow: {
        soft: '0 2px 15px -3px rgba(0, 0, 0, 0.07), 0 10px 20px -2px rgba(0, 0, 0, 0.04)',
        glow: '0 0 15px rgba(255, 215, 0, 0.15), 0 0 30px rgba(255, 215, 0, 0.05)',
        card: '0 1px 3px rgba(0, 0, 0, 0.08), 0 4px 12px rgba(0, 0, 0, 0.04)',
      },
      backdropBlur: {
        xs: '2px',
      },
    },
  },
  plugins: [],
}
