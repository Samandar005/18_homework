function toggleSidebar() {
        const sidebar = document.querySelector('aside');
        sidebar.classList.toggle('hidden');
    }

    // Chart initialization
    const ctx = document.getElementById('productsByCategoryChart').getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Electronics', 'Clothing', 'Books', 'Home & Garden', 'Sports', 'Toys'],
            datasets: [{
                label: 'Number of Products',
                data: [65, 45, 30, 38, 25, 32],
                backgroundColor: [
                    'rgba(99, 102, 241, 0.8)',  // Indigo (matching the sidebar)
                    'rgba(99, 102, 241, 0.7)',
                    'rgba(99, 102, 241, 0.6)',
                    'rgba(99, 102, 241, 0.5)',
                    'rgba(99, 102, 241, 0.4)',
                    'rgba(99, 102, 241, 0.3)'
                ],
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