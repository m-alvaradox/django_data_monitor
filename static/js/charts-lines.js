/**
 * For usage, visit Chart.js docs https://www.chartjs.org/docs/latest/
 */
// Obtén los datos dinámicos del bloque generado por Django
const conteosData = JSON.parse(document.getElementById('conteos-data').textContent);
const labels = Object.keys(conteosData);
const chartData = Object.values(conteosData); // <-- CAMBIA ESTO

const lineConfig = {
  type: 'line',
  data: {
    labels: labels,
    datasets: [
      {
        label: 'Votos por plato',
        backgroundColor: '#0694a2',
        borderColor: '#0694a2',
        data: chartData, // <-- Y AQUÍ
        fill: false,
      }
    ],
  },
  options: {
    responsive: true,
    plugins: {
      legend: {
        display: true,
      },
      tooltip: {
        mode: 'index',
        intersect: false,
      }
    },
    hover: {
      mode: 'nearest',
      intersect: true,
    },
    scales: {
      x: {
        display: true,
        title: {
          display: true,
          text: 'Plato',
        },
      },
      y: {
        display: true,
        title: {
          display: true,
          text: 'Votos',
        },
        beginAtZero: true,
      },
    },
  },
}

// Espera a que el DOM esté listo
document.addEventListener('DOMContentLoaded', function() {
  const lineCtx = document.getElementById('line');
  if (lineCtx) {
    window.myLine = new Chart(lineCtx, lineConfig);
  }
});