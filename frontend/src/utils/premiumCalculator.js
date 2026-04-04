/**
 * StreetGuard Premium Calculator
 * Weekly Premium = Base Rate + Zone Risk Adjustment + Seasonal Adjustment
 */

const ZONE_RISK = {
  'Tambaram': { level: 'High', score: 75, adjustment: 25 },
  'Chromepet': { level: 'High', score: 75, adjustment: 25 },
  'Adyar': { level: 'High', score: 75, adjustment: 25 },
  'Velachery': { level: 'Medium', score: 50, adjustment: 15 },
  'T. Nagar': { level: 'Medium', score: 50, adjustment: 15 },
  'OMR': { level: 'Medium', score: 50, adjustment: 15 },
  'Anna Nagar': { level: 'Low', score: 25, adjustment: 0 },
  'Porur': { level: 'Low', score: 25, adjustment: 0 },
}

const SEASON_ADJUSTMENT = {
  monsoon: 10,   // Jun–Nov
  summer: 5,     // Apr–May
  normal: 0,     // Dec–Mar
}

const BASE_RATE = 49
const COVERAGE_RATE = 0.7

export function getZoneRisk(zone) {
  return ZONE_RISK[zone] || { level: 'Low', score: 25, adjustment: 0 }
}

export function getCurrentSeason() {
  const month = new Date().getMonth() + 1
  if (month >= 6 && month <= 11) return 'monsoon'
  if (month >= 4 && month <= 5) return 'summer'
  return 'normal'
}

export function calculatePremium(zone, season = null) {
  if (!season) season = getCurrentSeason()
  const risk = getZoneRisk(zone)
  const seasonAdj = SEASON_ADJUSTMENT[season] || 0
  return {
    base: BASE_RATE,
    zoneAdjustment: risk.adjustment,
    seasonalAdjustment: seasonAdj,
    total: BASE_RATE + risk.adjustment + seasonAdj,
    riskLevel: risk.level,
    riskScore: risk.score,
    season,
  }
}

export function getMaxPayout(weeklyEarnings) {
  return Math.round(weeklyEarnings * COVERAGE_RATE)
}

export function getCoverageRatio(premium, weeklyEarnings) {
  const maxPayout = getMaxPayout(weeklyEarnings)
  return Math.round(maxPayout / premium * 10) / 10
}
