import { useState, useEffect } from 'react'
import ClaimStatus from '../components/ClaimStatus'
import Navbar from '../components/Navbar'

export default function ActiveClaim({ onNavigate }) {
  const [timeLeft, setTimeLeft] = useState({ hours: 1, minutes: 48, seconds: 32 })
  const profile = JSON.parse(localStorage.getItem('worker_data') || '{}')

  useEffect(() => {
    const timer = setInterval(() => {
      setTimeLeft(prev => {
        let { hours, minutes, seconds } = prev
        if (seconds > 0) return { hours, minutes, seconds: seconds - 1 }
        if (minutes > 0) return { hours, minutes: minutes - 1, seconds: 59 }
        if (hours > 0) return { hours: hours - 1, minutes: 59, seconds: 59 }
        clearInterval(timer)
        return prev
      })
    }, 1000)
    return () => clearInterval(timer)
  }, [])

  const pad = n => String(n).padStart(2, '0')

  return (
    <div className="min-h-screen bg-navy px-5 pb-24">
      {/* Red alert header */}
      <div className="bg-red-900/20 border-b border-red-500/20 px-5 py-4 -mx-5 mb-4">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-full bg-red-500/20 flex items-center justify-center">
            <span className="text-2xl">⚠️</span>
          </div>
          <div>
            <div className="font-display text-base font-bold text-red-300">Claim Triggered</div>
            <div className="text-xs text-gray-400">Heavy Rain · {profile.zone || 'Tambaram'} · 6:07 PM</div>
          </div>
        </div>
      </div>

      <div className="space-y-4">
        {/* Payout amount */}
        <div className="bg-gradient-to-br from-blue-900/40 to-blue-950/60 border border-blue-500/30 rounded-2xl p-6 text-center">
          <div className="text-xs text-gray-400 uppercase tracking-widest mb-2">Payout Amount</div>
          <div className="font-display text-6xl font-bold text-white">₹720</div>
          <div className="text-xs text-white/50 mt-1">50% of daily income · Heavy Rain trigger</div>
          <div className="mt-4 inline-flex items-center gap-2 bg-green-900/30 border border-green-500/30 text-green-400 text-xs font-semibold px-4 py-2 rounded-full">
            ✓ UPI payout by 8:00 PM
          </div>
        </div>

        {/* Countdown */}
        <div className="glass-card p-5 text-center">
          <div className="text-xs text-gray-400 uppercase tracking-widest mb-2">Estimated Payout In</div>
          <div className="font-display text-4xl font-bold text-primary">
            {pad(timeLeft.hours)}:{pad(timeLeft.minutes)}:{pad(timeLeft.seconds)}
          </div>
        </div>

        {/* Claim progress */}
        <ClaimStatus status="verified" />

        {/* Timeline */}
        <div className="glass-card p-5">
          <div className="text-xs text-gray-400 uppercase tracking-widest mb-4">Claim Timeline</div>
          <div className="space-y-0">
            {[
              ['🌧️', 'Rain detected (35mm/hr)', '6:07 PM', true],
              ['📋', 'Claim auto-initiated', '6:09 PM', true],
              ['🤖', 'AI fraud check passed', '6:11 PM', true],
              ['✅', 'Claim approved', '6:12 PM', true],
              ['💸', 'UPI payout processing...', '—', false],
            ].map(([icon, label, time, done], i) => (
              <div key={i} className="flex items-start gap-3 relative">
                {i < 4 && <div className="absolute left-[14px] top-8 w-0.5 h-6 bg-white/10" />}
                <div className={`w-7 h-7 rounded-full flex items-center justify-center flex-shrink-0 text-sm ${
                  done ? 'bg-green-500/20' : 'bg-white/5'
                }`}>
                  {icon}
                </div>
                <div className="flex-1 flex justify-between items-center py-2 border-b border-white/5 last:border-0">
                  <span className={done ? 'text-sm text-gray-300' : 'text-sm text-gray-500'}>{label}</span>
                  <span className="text-gray-500 text-xs">{time}</span>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Fraud check details */}
        <div className="glass-card p-5">
          <div className="text-xs text-gray-400 uppercase tracking-widest mb-3">Fraud Detection</div>
          <div className="flex items-center gap-3 mb-3">
            <div className="w-10 h-10 rounded-full bg-green-500/20 flex items-center justify-center text-lg">🛡️</div>
            <div>
              <div className="text-sm font-semibold text-green-400">Clean — Auto Approved</div>
              <div className="text-xs text-gray-400">Isolation Forest ML model • Score: -0.12</div>
            </div>
          </div>
          <div className="grid grid-cols-2 gap-3">
            {[
              ['Location', '✓ Verified'],
              ['Account Age', '30+ days'],
              ['Claims/Month', '1 (normal)'],
              ['Activity', '✓ Active'],
            ].map(([k, v]) => (
              <div key={k} className="text-xs">
                <span className="text-gray-500">{k}: </span>
                <span className="text-green-400">{v}</span>
              </div>
            ))}
          </div>
        </div>

        <button onClick={() => onNavigate('dashboard')}
          className="w-full glass-card text-primary font-semibold py-4 rounded-xl hover:bg-white/5 transition">
          ← Back to Dashboard
        </button>
      </div>

      <Navbar active="claims" onNavigate={onNavigate} />
    </div>
  )
}