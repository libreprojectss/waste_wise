/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        core: {
          primary: "#000000",
          secondary: "#7C8DB5",
          white: "#FFFFFF",
          border: "#E6EDFF",
          indigo: "#347AE2",
          red: "#FF3B30",
          green: "#34C759",
          orange: "#FF9500",
        },
        neutral: {
          50: "#F4F4F4",
          100: "#E5E5E5",
          200: "#D4D4D4",
          300: "#ACACAC",
          400: "#808080",
          500: "#525252",
          600: "#404040",
          700: "#252527",
          800: "#222222",
          900: "#171717",
        },
        supporting: {
          warning: "#FDB22F",
          "warning-light": "#FFF9EF",
          error: "#D12E24",
          "error-light": "#FBEFEF",
          success: "#317D35",
          "success-light": "#EFF5EF",
          info: "#146DFC",
          "info-light": "#EFF1F5",
        },
        shade: {
          light: "#FFFFFF",
          dark: "#000000",
        },
      },
    },
  },
  plugins: [],
};
