import { useState, useEffect } from 'react';
import Header from './components/Header';
import PatientList from './components/PatientList';
import DiagnosisHistory from './components/DiagnosisHistory';
import PatientProfile from './components/PatientProfile';

const API_URL = 'https://fedskillstest.coalitiontechnologies.workers.dev';
const USERNAME = 'coalition';
const PASSWORD = 'skills-test';

export default function App() {
  const [patients, setPatients] = useState([]);
  const [selectedIndex, setSelectedIndex] = useState(3);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const headers = new Headers();
    headers.set('Authorization', 'Basic ' + btoa(`${USERNAME}:${PASSWORD}`));

    fetch(API_URL, { headers })
      .then((res) => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return res.json();
      })
      .then((data) => {
        setPatients(data);
        const jessicaIdx = data.findIndex((p) => p.name === 'Jessica Taylor');
        if (jessicaIdx !== -1) setSelectedIndex(jessicaIdx);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return (
      <div className="min-h-screen bg-[#F6F7F8] font-manrope flex items-center justify-center">
        <div className="flex flex-col items-center gap-4">
          <div className="w-10 h-10 border-4 border-[#01F0D0] border-t-transparent rounded-full animate-spin" />
          <p className="text-navy/60 text-sm font-medium">Loading patients...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen bg-[#F6F7F8] font-manrope flex items-center justify-center">
        <div className="bg-white rounded-2xl p-8 text-center max-w-md shadow-sm">
          <p className="text-red-500 font-bold text-lg mb-2">Failed to load patients</p>
          <p className="text-navy/50 text-sm">{error}</p>
        </div>
      </div>
    );
  }

  const patient = patients[selectedIndex];
  if (!patient) return null;

  return (
    <div className="min-h-screen bg-[#F6F7F8] font-manrope">
      <Header />

      <main className="grid grid-cols-[280px_1fr_320px] gap-[30px] px-[18px] py-[30px] max-w-[1600px] mx-auto">
        <aside className="max-h-[calc(100vh-110px)] sticky top-[30px]">
          <PatientList
            patients={patients}
            selectedIndex={selectedIndex}
            onSelect={setSelectedIndex}
          />
        </aside>

        <section className="min-w-0">
          <DiagnosisHistory patient={patient} />
        </section>

        <aside>
          <PatientProfile patient={patient} />
        </aside>
      </main>
    </div>
  );
}
