import { initializeApp } from 'firebase/app'
import { getFirestore } from 'firebase/firestore'
import { getAuth } from 'firebase/auth'

const firebaseConfig = {
  apiKey: import.meta.env.VITE_FIREBASE_API_KEY || "demo",
  authDomain: import.meta.env.VITE_FIREBASE_AUTH_DOMAIN || "gigshield-fd4a1.firebaseapp.com",
  projectId: import.meta.env.VITE_FIREBASE_PROJECT_ID || "gigshield-fd4a1",
  storageBucket: import.meta.env.VITE_FIREBASE_STORAGE_BUCKET || "gigshield-fd4a1.appspot.com",
  messagingSenderId: import.meta.env.VITE_FIREBASE_MESSAGING_SENDER_ID || "demo",
  appId: import.meta.env.VITE_FIREBASE_APP_ID || "demo"
}

const app = initializeApp(firebaseConfig)
export const db = getFirestore(app)
export const auth = getAuth(app)
export default app