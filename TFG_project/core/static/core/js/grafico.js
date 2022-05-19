import { DateTime } from 'luxon';


    const ctx = document.getElementById('myChart').getContext('2d');

    const psas = JSON.parse('{{ psas.psas }}');
    const tduplis = JSON.parse('{{ psas.tduplis }}');
    const fechas = '{{ psas.fechas }}'.replace(new RegExp("&" + "#" + "x27;", "g"), "").split("[")[1].split("]")[0].split(",");

    const DATA_COUNT = psas.length;
    const labels = [];

    for (let i = 0; i < DATA_COUNT; ++i) {
        labels.push(DateTime.fromISO(fechas[i]));
    }

    const data = {
        labels: labels,
        datasets: [
            {
                label: 'PSA',
                data: psas,
                borderColor: 'rgba(255,0,0,0.5)',
                backgroundColor: 'rgba(255, 0, 0, 1)',
                yAxisID: 'y',
            },
            {
                label: 'Tiempo de duplicación',
                data: tduplis,
                borderColor: 'rgba(0,0,255,0.5)',
                backgroundColor: 'rgba(0, 0, 255, 1)',
                yAxisID: 'y1',
            }
        ]
    };
    const config = {
        type: 'bar',
        data: data,
        options: {
            responsive: true,
            interaction: {
                mode: 'index',
                intersect: false,
            },
            stacked: false,
            plugins: {
                title: {
                    display: true,
                    text: 'Chart.js Line Chart - Multi Axis'
                }
            },
            scales: {

                yAxes: [
                    {
                        type: 'linear',
                        display: true,
                        position: 'left',
                        id: "y",
                        ticks: {
                            beginAtZero: true
                        }

                    },
                    {
                        type: 'linear',
                        display: true,
                        position: 'right',
                        id: "y1",
                        grid: {
                            drawOnChartArea: false, // only want the grid lines for one axis to show up
                        },
                        ticks: {
                            beginAtZero: true
                        }
                    },
                ]
            },
        }
    };

    const chart = new Chart(ctx, config);
