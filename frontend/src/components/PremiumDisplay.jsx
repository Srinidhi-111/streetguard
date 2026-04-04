import { calculatePremium, getMaxPayout } from '../utils/premiumCalculator'

export default function PremiumDisplay({ zone = 'Tambaram', season, weeklyEarnings = 4500 }) {
  const premium = calculatePremium(zone, season)
  const maxPayout = getMaxPayout(weeklyEarnings)

  return (
    <div className="space-y-4">
      {/* Big premium card */}
      <div className="bg-gradient-to-br from-blue-900/40 to-blue-950/60 border border-blue-500/30 rounded-2xl p-6 text-center">
        <div className="text-xs text-gray-400 uppercase tracking-widest mb-2">Your Weekly Premium</div>
        <div className="font-display text-5xl font-bold text-white">₹{premium.total}</div>
        <div className="text-xs text-primary mt-2">per week · auto-renewed every Monday</div>
      </div>

      {/* Breakdown */}
      <div className="glass-card p-5">
        <div className="text-xs text-gray-400 uppercase tracking-widest mb-3">Premium Breakdown</div>
        {[
          ['Base premium', `₹${premium.base}`],
          [`Zone risk (${zone})`, `+₹${premium.zoneAdjustment}`],
          [`Seasonal (${premium.season})`, `+₹${premium.seasonalAdjustment}`],
        ].map(([label, val]) => (
          <div key={label} className="flex justify-between text-sm py-2.5 border-b border-white/5 last:border-0">
            <span className="text-gray-400">{label}</span>
            <span className="text-white font-semibold">{val}</span>
          </div>
        ))}
        <div className="flex justify-between pt-3 mt-1">
          <span className="text-white font-bold">Total</span>
          <span className="text-primary font-bold text-lg">₹{premium.total}</span>
        </div>
      </div>

      {/* Coverage */}
      <div className="glass-card p-5">
        <div className="text-xs text-gray-400 uppercase tracking-widest mb-3">What You're Covered For</div>
        {[
          ['Max weekly payout', `₹${maxPayout.toLocaleString()}`, 'text-green-400'],
          ['Coverage rate', '70% of income', 'text-white'],
          ['Payout time', 'Within 2 hours', 'text-white'],
          ['Premium-to-coverage', `1 : ${Math.round(maxPayout / premium.total)}`, 'text-primary'],
        ].map(([label, val, color]) => (
          <div key={label} className="flex justify-between text-sm py-2.5 border-b border-white/5 last:border-0">
            <span className="text-gray-400">{label}</span>
            <span className={`font-semibold ${color}`}>{val}</span>
          </div>
        ))}
      </div>

      {/* Triggers covered */}
      <div className="glass-card p-5">
        <div className="text-xs text-gray-400 uppercase tracking-widest mb-3">Triggers Covered</div>
        <div className="flex flex-wrap gap-2">
          {[
            ['🌧️ Heavy Rain', '>20mm/hr', '50%'],
            ['🌡️ Extreme Heat', '>43°C', '30%'],
            ['💨 Poor AQI', '>300', '40%'],
            ['🚫 Bandh/Curfew', 'Manual', '100%'],
            ['📱 Platform Down', '>2hrs', '60%'],
          ].map(([name, threshold, payout]) => (
            <div key={name} className="bg-primary/10 border border-primary/20 rounded-xl px-3 py-2 text-xs">
              <div className="text-primary font-semibold">{name}</div>
              <div className="text-white/40 mt-0.5">{threshold} → {payout}</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}