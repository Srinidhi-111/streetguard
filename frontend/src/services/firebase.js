// Firebase configuration — graceful fallback for demo mode
// When valid Firebase config is not available, exports mock objects
// so that other files importing from here don't crash

let db = null
let auth = null
let app = null

try {
  const { initializeApp } = await import('firebase/app')
  const { getFirestore } = await import('firebase/firestore')
  const { getAuth } = await import('firebase/auth')

  const firebaseConfig = {
    apiKey: import.meta.env.VITE_FIREBASE_API_KEY || "demo",
    authDomain: import.meta.env.VITE_FIREBASE_AUTH_DOMAIN || "gigshield-fd4a1.firebaseapp.com",
    projectId: import.meta.env.VITE_FIREBASE_PROJECT_ID || "gigshield-fd4a1",
    storageBucket: import.meta.env.VITE_FIREBASE_STORAGE_BUCKET || "gigshield-fd4a1.appspot.com",
    messagingSenderId: import.meta.env.VITE_FIREBASE_MESSAGING_SENDER_ID || "demo",
    appId: import.meta.env.VITE_FIREBASE_APP_ID || "demo"
  }

  app = initializeApp(firebaseConfig)
  db = getFirestore(app)
  auth = getAuth(app)
} catch (e) {
  console.warn('Firebase not available — running in demo mode')
}

export { db, auth }
export default app