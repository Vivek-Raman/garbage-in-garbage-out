const navItems = [
  { label: 'Overview', icon: 'home' },
  { label: 'Patients', icon: 'people', active: true },
  { label: 'Schedule', icon: 'calendar' },
  { label: 'Message', icon: 'chat' },
  { label: 'Transactions', icon: 'card' },
];

const icons = {
  home: (
    <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z" />
      <polyline points="9 22 9 12 15 12 15 22" />
    </svg>
  ),
  people: (
    <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2" />
      <circle cx="9" cy="7" r="4" />
      <path d="M23 21v-2a4 4 0 0 0-3-3.87" />
      <path d="M16 3.13a4 4 0 0 1 0 7.75" />
    </svg>
  ),
  calendar: (
    <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <rect x="3" y="4" width="18" height="18" rx="2" ry="2" />
      <line x1="16" y1="2" x2="16" y2="6" />
      <line x1="8" y1="2" x2="8" y2="6" />
      <line x1="3" y1="10" x2="21" y2="10" />
    </svg>
  ),
  chat: (
    <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
    </svg>
  ),
  card: (
    <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <rect x="1" y="4" width="22" height="16" rx="2" ry="2" />
      <line x1="1" y1="10" x2="23" y2="10" />
    </svg>
  ),
};

export default function Header() {
  return (
    <header className="bg-white rounded-[70px] mx-[18px] mt-[18px] px-8 py-3 flex items-center justify-between">
      <div className="flex items-center gap-2 flex-shrink-0">
        <svg width="48" height="48" viewBox="0 0 48 48" fill="none">
          <path d="M20 8L28 12V24L20 32L12 24V12L20 8Z" fill="#01F0D0" />
          <path d="M28 12V24L20 20V8L28 12Z" fill="#072635" opacity="0.25" />
        </svg>
        <span className="text-2xl font-extrabold text-navy tracking-tight">
          Tech<span className="text-[#01F0D0]">.</span>Care
        </span>
      </div>

      <nav className="flex items-center gap-1">
        {navItems.map((item) => (
          <button
            key={item.label}
            className={`flex items-center gap-2 px-4 py-2.5 rounded-full text-sm font-semibold transition-colors ${
              item.active
                ? 'bg-cyan-active text-navy'
                : 'text-navy/70 hover:bg-gray-100'
            }`}
          >
            {icons[item.icon]}
            {item.label}
          </button>
        ))}
      </nav>

      <div className="flex items-center gap-3 flex-shrink-0">
        <img
          src="https://fedskillstest.ct.digital/5.png"
          alt="Dr. Jose Simmons"
          className="w-11 h-11 rounded-full object-cover"
        />
        <div className="text-right">
          <p className="text-sm font-bold text-navy leading-tight">Dr. Jose Simmons</p>
          <p className="text-xs text-navy/60">General Practitioner</p>
        </div>
        <div className="w-px h-10 bg-[#EDEDED] mx-1" />
        <button className="text-navy/60 hover:text-navy">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <circle cx="12" cy="12" r="3" />
            <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z" />
          </svg>
        </button>
        <button className="text-navy/60 hover:text-navy">
          <svg width="4" height="18" viewBox="0 0 4 18" fill="currentColor">
            <circle cx="2" cy="2" r="2" />
            <circle cx="2" cy="9" r="2" />
            <circle cx="2" cy="16" r="2" />
          </svg>
        </button>
      </div>
    </header>
  );
}
