import { useState, useEffect } from 'react'
import Landing from './pages/Landing'
import Onboarding from './pages/Onboarding'
import Dashboard from './pages/Dashboard'
import Policy from './pages/Policy'
import ActiveClaim from './pages/ActiveClaim'
import Profile from './pages/Profile'
import AdminDashboard from './pages/AdminDashboard'

export default function App() {
  const [page, setPage] = useState(window.location.hash.slice(1) || 'landing')

  useEffect(() => {
    const handler = () => setPage(window.location.hash.slice(1) || 'landing')
    window.addEventListener('hashchange', handler)
    return () => window.removeEventListener('hashchange', handler)
  }, [])

  const navigate = (p) => {
    window.location.hash = p
  }

  switch (page) {
    case 'onboard':
      return <Onboarding onNavigate={navigate} />
    case 'dashboard':
      return <Dashboard onNavigate={navigate} />
    case 'policy':
      return <Policy onNavigate={navigate} />
    case 'claims':
      return <ActiveClaim onNavigate={navigate} />
    case 'profile':
      return <Profile onNavigate={navigate} />
    case 'admin':
      return <AdminDashboard onNavigate={navigate} />
    default:
      return <Landing onNavigate={navigate} />
  }
}
