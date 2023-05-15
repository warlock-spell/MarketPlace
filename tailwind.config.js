/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./**/templates/**/*.{html,js}",
    ],
    theme: {
        extend: {
            colors: {
                'regal-blue': '#243c5a',
                'mighty-orange': '#ed8811',
            },
        },
    },
    plugins: [],
}
