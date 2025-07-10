const InsightColor = {
    "Data Mindset": "#2C2750",
    "Analytic Edge": "#6A4267"
};

const spans = document.querySelectorAll(".insight-status");

spans.forEach(span => {
    const text = span.textContent.trim();
    const color = InsightColor[text];
    if (color) {
        span.style.backgroundColor = color;
        span.style.color = "#f8F9FA";
    }
});