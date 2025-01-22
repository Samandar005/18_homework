function generateBackgroundColors(baseColor, count, opacityStep) {
    const colors = [];
    for (let i = 0; i < count; i++) {
        const opacity = 1 - i * opacityStep; // Gradually reduce opacity
        colors.push(`rgba(${baseColor}, ${opacity.toFixed(2)})`);
    }
    return colors;
}
    // Usage
    const baseColor = '99, 102, 241'; // Base RGB color
    const count = {{ category_names|length }}; // Number of colors
    const opacityStep = 0.1; // Opacity step reduction
    const backgroundColors = generateBackgroundColors(baseColor, count, opacityStep);
    // Chart initialization
    const ctx = document.getElementById('productsByCategoryChart').getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: {{ category_names|safe }},
                datasets: [{
                    label: 'Number of Products',
                    data: {{ category_product_counts }},
                    backgroundColor: backgroundColors,
                    borderColor: [
                        'rgb(99, 102, 241)',
                        'rgb(99, 102, 241)',
                        'rgb(99, 102, 241)',
                        'rgb(99, 102, 241)',
                        'rgb(99, 102, 241)',
                        'rgb(99, 102, 241)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: true,
                        grid: {
                            color: 'rgba(0, 0, 0, 0.1)'
                        }
                    },
                    x: {
                        grid: {
                            display: false
                        }
                    }
                },
                plugins: {
                    legend: {
                        display: false
                    }
                }
            }
        });
</script>