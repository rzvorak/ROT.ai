import React, { useEffect, useRef } from 'react';
import { Line } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  LineElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  PointElement, 
} from 'chart.js';

ChartJS.register(LineElement, CategoryScale, LinearScale, Tooltip, PointElement);

const Chart = ({ dataPoints }) => {
  const chartRef = useRef(null); 

  const data = {
    labels: ['1', '2', '3', '4', '5', '6'],
    datasets: [
      {
        data: dataPoints,
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
      <Line data={data} options={options} ref={chartRef} />
    </div>
  );
};

export default Chart;