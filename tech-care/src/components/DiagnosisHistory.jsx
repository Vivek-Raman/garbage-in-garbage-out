import { Line } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Tooltip,
  Filler,
} from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Tooltip, Filler);

const monthMap = {
  January: 'Jan',
  February: 'Feb',
  March: 'Mar',
  April: 'Apr',
  May: 'May',
  June: 'Jun',
  July: 'Jul',
  August: 'Aug',
  September: 'Sep',
  October: 'Oct',
  November: 'Nov',
  December: 'Dec',
};

function ArrowUp() {
  return (
    <svg width="10" height="6" viewBox="0 0 10 6" fill="currentColor">
      <path d="M5 0L10 6H0L5 0Z" />
    </svg>
  );
}

function ArrowDown() {
  return (
    <svg width="10" height="6" viewBox="0 0 10 6" fill="currentColor">
      <path d="M5 6L0 0H10L5 6Z" />
    </svg>
  );
}

function LungsIcon() {
  return (
    <svg width="28" height="28" viewBox="0 0 48 48" fill="none">
      <path d="M24 8v16M24 24c-4 0-10 2-12 8s-3 10 1 12 8 0 10-4" stroke="#3A88C8" strokeWidth="2.5" strokeLinecap="round" fill="none" />
      <path d="M24 24c4 0 10 2 12 8s3 10-1 12-8 0-10-4" stroke="#3A88C8" strokeWidth="2.5" strokeLinecap="round" fill="none" />
    </svg>
  );
}

function ThermometerIcon() {
  return (
    <svg width="28" height="28" viewBox="0 0 48 48" fill="none">
      <rect x="20" y="6" width="8" height="28" rx="4" stroke="#E54B6B" strokeWidth="2.5" fill="none" />
      <circle cx="24" cy="36" r="5" stroke="#E54B6B" strokeWidth="2.5" fill="#E54B6B" fillOpacity="0.3" />
      <line x1="24" y1="20" x2="24" y2="32" stroke="#E54B6B" strokeWidth="2.5" strokeLinecap="round" />
    </svg>
  );
}

function HeartIcon() {
  return (
    <svg width="28" height="28" viewBox="0 0 48 48" fill="none">
      <path d="M24 40s-14-8.5-14-18a8 8 0 0 1 14-5.3A8 8 0 0 1 38 22c0 9.5-14 18-14 18z" stroke="#E54B6B" strokeWidth="2.5" fill="#E54B6B" fillOpacity="0.15" strokeLinecap="round" strokeLinejoin="round" />
    </svg>
  );
}

export default function DiagnosisHistory({ patient }) {
  const last6 = patient.diagnosis_history.slice(0, 6);
  const history = [...last6].reverse();
  const latest = patient.diagnosis_history[0];

  const labels = history.map(
    (h) => `${monthMap[h.month] || h.month}, ${h.year}`
  );
  const systolicData = history.map((h) => h.blood_pressure.systolic.value);
  const diastolicData = history.map((h) => h.blood_pressure.diastolic.value);

  const chartData = {
    labels,
    datasets: [
      {
        label: 'Systolic',
        data: systolicData,
        borderColor: '#E66FD2',
        backgroundColor: 'rgba(230, 111, 210, 0.08)',
        pointBackgroundColor: '#E66FD2',
        pointBorderColor: '#fff',
        pointBorderWidth: 2,
        pointRadius: 6,
        pointHoverRadius: 8,
        tension: 0.4,
        borderWidth: 2,
      },
      {
        label: 'Diastolic',
        data: diastolicData,
        borderColor: '#8C6FE6',
        backgroundColor: 'rgba(140, 111, 230, 0.08)',
        pointBackgroundColor: '#8C6FE6',
        pointBorderColor: '#fff',
        pointBorderWidth: 2,
        pointRadius: 6,
        pointHoverRadius: 8,
        tension: 0.4,
        borderWidth: 2,
      },
    ],
  };

  const chartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { display: false },
      tooltip: {
        backgroundColor: '#072635',
        titleFont: { family: 'Manrope', size: 12 },
        bodyFont: { family: 'Manrope', size: 12 },
        padding: 10,
        cornerRadius: 8,
      },
    },
    scales: {
      x: {
        grid: { display: false },
        ticks: {
          font: { family: 'Manrope', size: 11 },
          color: '#707070',
        },
      },
      y: {
        min: 60,
        max: 180,
        ticks: {
          stepSize: 20,
          font: { family: 'Manrope', size: 11 },
          color: '#707070',
        },
        grid: {
          color: '#E8E8E8',
        },
      },
    },
  };

  const vitalCards = [
    {
      label: 'Respiratory Rate',
      value: latest.respiratory_rate.value,
      unit: 'bpm',
      level: latest.respiratory_rate.levels,
      bg: '#E0F3FA',
      icon: <LungsIcon />,
    },
    {
      label: 'Temperature',
      value: latest.temperature.value,
      unit: '°F',
      level: latest.temperature.levels,
      bg: '#FFE6E9',
      icon: <ThermometerIcon />,
    },
    {
      label: 'Heart Rate',
      value: latest.heart_rate.value,
      unit: 'bpm',
      level: latest.heart_rate.levels,
      bg: '#FFE6F1',
      icon: <HeartIcon />,
    },
  ];

  return (
    <div className="flex flex-col gap-5">
      <div className="bg-white rounded-2xl p-5">
        <h2 className="text-2xl font-extrabold text-navy mb-4">Diagnosis History</h2>

        <div className="bg-[#F4F0FE] rounded-xl p-5 flex gap-5">
          <div className="flex-1">
            <div className="flex items-center justify-between mb-3">
              <h3 className="text-lg font-bold text-navy">Blood Pressure</h3>
              <span className="text-sm text-navy/60 flex items-center gap-1">
                Last 6 months
                <svg width="10" height="6" viewBox="0 0 10 6" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">
                  <path d="M1 1l4 4 4-4" />
                </svg>
              </span>
            </div>
            <div className="h-52">
              <Line data={chartData} options={chartOptions} />
            </div>
          </div>

          <div className="w-40 flex-shrink-0 flex flex-col justify-center gap-5 pl-5 border-l border-gray-200/60">
            <div>
              <div className="flex items-center gap-2 mb-1">
                <span className="w-3 h-3 rounded-full bg-[#E66FD2]" />
                <span className="text-sm font-semibold text-navy/70">Systolic</span>
              </div>
              <p className="text-2xl font-extrabold text-navy">{latest.blood_pressure.systolic.value}</p>
              <p className="text-xs text-navy/50 flex items-center gap-1 mt-0.5">
                {latest.blood_pressure.systolic.levels === 'Higher than Average' && <ArrowUp />}
                {latest.blood_pressure.systolic.levels === 'Lower than Average' && <ArrowDown />}
                {latest.blood_pressure.systolic.levels}
              </p>
            </div>
            <div className="w-full h-px bg-gray-200" />
            <div>
              <div className="flex items-center gap-2 mb-1">
                <span className="w-3 h-3 rounded-full bg-[#8C6FE6]" />
                <span className="text-sm font-semibold text-navy/70">Diastolic</span>
              </div>
              <p className="text-2xl font-extrabold text-navy">{latest.blood_pressure.diastolic.value}</p>
              <p className="text-xs text-navy/50 flex items-center gap-1 mt-0.5">
                {latest.blood_pressure.diastolic.levels === 'Higher than Average' && <ArrowUp />}
                {latest.blood_pressure.diastolic.levels === 'Lower than Average' && <ArrowDown />}
                {latest.blood_pressure.diastolic.levels}
              </p>
            </div>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-3 gap-5">
        {vitalCards.map((card) => (
          <div
            key={card.label}
            className="rounded-2xl p-4"
            style={{ backgroundColor: card.bg }}
          >
            <div className="w-16 h-16 rounded-full flex items-center justify-center mb-3 mx-auto" style={{ backgroundColor: `${card.bg}CC` }}>
              {card.icon}
            </div>
            <p className="text-sm font-medium text-navy/70 mb-2">{card.label}</p>
            <p className="text-[28px] font-extrabold text-navy leading-tight">
              {card.value}
              <span className="text-base font-semibold ml-0.5">{card.unit}</span>
            </p>
            <p className="text-xs text-navy/50 mt-2 flex items-center gap-1">
              {card.level === 'Higher than Average' && <ArrowUp />}
              {card.level === 'Lower than Average' && <ArrowDown />}
              {card.level}
            </p>
          </div>
        ))}
      </div>

      <div className="bg-white rounded-2xl p-5">
        <h2 className="text-2xl font-extrabold text-navy mb-4">Diagnostic List</h2>
        <div className="overflow-hidden rounded-xl">
          <table className="w-full text-left">
            <thead>
              <tr className="bg-[#F6F7F8]">
                <th className="px-4 py-3 text-sm font-bold text-navy/70 rounded-l-xl">Problem/Diagnosis</th>
                <th className="px-4 py-3 text-sm font-bold text-navy/70">Description</th>
                <th className="px-4 py-3 text-sm font-bold text-navy/70 rounded-r-xl">Status</th>
              </tr>
            </thead>
            <tbody>
              {patient.diagnostic_list.map((d, i) => (
                <tr key={i} className="border-t border-gray-100">
                  <td className="px-4 py-3 text-sm text-navy">{d.name}</td>
                  <td className="px-4 py-3 text-sm text-navy/60">{d.description}</td>
                  <td className="px-4 py-3 text-sm text-navy/60">{d.status}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
