import React, { useEffect, useRef } from 'react';
import { Line } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  LineElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  PointElement, // Explicitly register the PointElement
} from 'chart.js';

// Register the necessary chart components
ChartJS.register(LineElement, CategoryScale, LinearScale, Tooltip, PointElement);

const Chart = () => {
  const chartRef = useRef(null); // Create a ref for the chart instance

  const data = {
    labels: ['1', '2', '3', '4', '5', '6'],
    datasets: [
      {
        data: [10, 5, 4, 8, 5, 0], // Y-values for the chart
        borderColor: '#d4d4d4',
        fill: false,
        pointRadius: 0,
      },
    ],
  };

  const options = {
    responsive: true,
    scales: {
        x: {
            ticks: {
                display: false,
            },
        },
        y: {
            ticks: {
                display: false,
            },
        },
    },
  };

  // Clean up the chart instance when the component is unmounted or updated
  useEffect(() => {
    const chartInstance = chartRef.current.chartInstance;

    return () => {
      if (chartInstance) {
        chartInstance.destroy();
      }
    };
  }, []);

  return (
    <div>
      {/* Assign the ref to the Line chart */}
      <Line data={data} options={options} ref={chartRef} />
    </div>
  );
};

export default Chart;