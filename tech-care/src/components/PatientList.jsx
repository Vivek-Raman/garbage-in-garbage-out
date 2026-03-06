export default function PatientList({ patients, selectedIndex, onSelect }) {
  return (
    <div className="bg-white rounded-2xl h-full flex flex-col">
      <div className="flex items-center justify-between px-5 pt-5 pb-3">
        <h2 className="text-2xl font-extrabold text-navy">Patients</h2>
        <button className="text-navy/60 hover:text-navy">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <circle cx="11" cy="11" r="8" />
            <line x1="21" y1="21" x2="16.65" y2="16.65" />
          </svg>
        </button>
      </div>
      <div className="overflow-y-auto flex-1 px-2">
        {patients.map((patient, idx) => (
          <button
            key={patient.name}
            onClick={() => onSelect(idx)}
            className={`w-full flex items-center gap-3 px-3 py-3 rounded-xl transition-colors text-left ${
              idx === selectedIndex
                ? 'bg-cyan-light'
                : 'hover:bg-gray-50'
            }`}
          >
            <img
              src={patient.profile_picture}
              alt={patient.name}
              className="w-11 h-11 rounded-full object-cover flex-shrink-0"
            />
            <div className="flex-1 min-w-0">
              <p className="text-sm font-bold text-navy truncate">{patient.name}</p>
              <p className="text-xs text-navy/50">{patient.gender}, {patient.age}</p>
            </div>
            <button
              className="text-navy/40 hover:text-navy flex-shrink-0"
              onClick={(e) => e.stopPropagation()}
            >
              <svg width="4" height="18" viewBox="0 0 4 18" fill="currentColor">
                <circle cx="2" cy="2" r="2" />
                <circle cx="2" cy="9" r="2" />
                <circle cx="2" cy="16" r="2" />
              </svg>
            </button>
          </button>
        ))}
      </div>
    </div>
  );
}
