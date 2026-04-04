export default function Navbar({ active = 'dashboard', onNavigate }) {
  const items = [
    { icon: '🏠', label: 'Home', key: 'dashboard' },
    { icon: '📋', label: 'Claims', key: 'claims' },
    { icon: '💳', label: 'Policy', key: 'policy' },
    { icon: '👤', label: 'Profile', key: 'profile' },
  ]

  return (
    <div className="fixed bottom-0 left-0 right-0 bg-navy/95 backdrop-blur-md border-t border-white/10 flex justify-around py-3 z-50">
      {items.map(({ icon, label, key }) => (
        <button
          key={key}
          onClick={() => onNavigate && onNavigate(key)}
          className={`flex flex-col items-center gap-1 text-xs transition-all ${
            active === key ? 'text-primary scale-110' : 'text-gray-500 hover:text-white/60'
          }`}
        >
          <span className="text-lg">{icon}</span>
          <span className="font-medium">{label}</span>
          {active === key && <div className="w-1 h-1 rounded-full bg-primary" />}
        </button>
      ))}
    </div>
  )
}