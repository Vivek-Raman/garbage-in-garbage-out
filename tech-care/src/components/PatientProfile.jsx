function formatDate(dateStr) {
  const months = ['January','February','March','April','May','June','July','August','September','October','November','December'];
  if (dateStr.includes('/')) {
    const [month, day, year] = dateStr.split('/').map(Number);
    return `${months[month - 1]} ${day}, ${year}`;
  }
  const [year, month, day] = dateStr.split('-').map(Number);
  return `${months[month - 1]} ${day}, ${year}`;
}

const CalendarIcon = () => (
  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">
    <rect x="3" y="4" width="18" height="18" rx="2" ry="2" />
    <line x1="16" y1="2" x2="16" y2="6" />
    <line x1="8" y1="2" x2="8" y2="6" />
    <line x1="3" y1="10" x2="21" y2="10" />
  </svg>
);

const GenderIcon = () => (
  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">
    <circle cx="12" cy="8" r="5" />
    <line x1="12" y1="13" x2="12" y2="22" />
    <line x1="9" y1="18" x2="15" y2="18" />
  </svg>
);

const PhoneIcon = () => (
  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">
    <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z" />
  </svg>
);

const EmergencyIcon = () => (
  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">
    <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z" />
  </svg>
);

const InsuranceIcon = () => (
  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">
    <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
  </svg>
);

const DownloadIcon = () => (
  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
    <polyline points="7 10 12 15 17 10" />
    <line x1="12" y1="15" x2="12" y2="3" />
  </svg>
);

export default function PatientProfile({ patient }) {
  const infoRows = [
    { icon: <CalendarIcon />, label: 'Date Of Birth', value: formatDate(patient.date_of_birth) },
    { icon: <GenderIcon />, label: 'Gender', value: patient.gender },
    { icon: <PhoneIcon />, label: 'Contact Info.', value: patient.phone_number },
    { icon: <EmergencyIcon />, label: 'Emergency Contacts', value: patient.emergency_contact },
    { icon: <InsuranceIcon />, label: 'Insurance Provider', value: patient.insurance_type },
  ];

  return (
    <div className="flex flex-col gap-5">
      <div className="bg-white rounded-2xl p-5 flex flex-col items-center">
        <img
          src={patient.profile_picture}
          alt={patient.name}
          className="w-48 h-48 rounded-full object-cover mb-4"
        />
        <h2 className="text-2xl font-extrabold text-navy mb-6">{patient.name}</h2>

        <div className="w-full space-y-5">
          {infoRows.map((row) => (
            <div key={row.label} className="flex items-center gap-3">
              <span className="text-navy/60">{row.icon}</span>
              <div>
                <p className="text-xs text-navy/50">{row.label}</p>
                <p className="text-sm font-bold text-navy">{row.value}</p>
              </div>
            </div>
          ))}
        </div>

        <button className="mt-6 bg-[#01F0D0] text-navy text-sm font-bold py-2.5 px-10 rounded-full hover:bg-[#00D4B8] transition-colors">
          Show All Information
        </button>
      </div>

      <div className="bg-white rounded-2xl p-5">
        <h2 className="text-2xl font-extrabold text-navy mb-4">Lab Results</h2>
        <div className="space-y-1">
          {patient.lab_results.map((result) => (
            <div
              key={result}
              className="flex items-center justify-between px-3 py-3 rounded-lg hover:bg-[#F6F7F8] transition-colors"
            >
              <span className="text-sm text-navy">{result}</span>
              <button className="text-navy/40 hover:text-navy">
                <DownloadIcon />
              </button>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
