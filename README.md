# 🛡️ GigShield — AI-Powered Parametric Income Insurance for Gig Workers

> *"I don't need much. I just need to know that when it rains, my family still eats that night."*
> — Murugan, Swiggy Delivery Partner, Tambaram, Chennai

**GigShield** is a weekly parametric income insurance platform for gig delivery workers in India. When a verified disruption — heavy rain, extreme heat, a bandh, platform downtime — hits a worker's zone, GigShield detects it automatically, initiates a claim without the worker doing anything, and sends money to their UPI within 2 hours.

No forms. No agents. No waiting.

---

## 📋 Table of Contents

1. [The Problem](#-the-problem)
2. [Meet Murugan — Our Persona](#-meet-murugan--our-persona)
3. [Our Solution](#-our-solution)
4. [How It Works](#-how-it-works)
5. [Parametric Triggers](#-parametric-triggers)
6. [Weekly Premium Model](#-weekly-premium-model)
7. [Loss Simulation Dashboard](#-loss-simulation-dashboard)
8. [AI/ML Integration](#-aiml-integration)
9. [Tech Stack](#-tech-stack)
10. [System Architecture](#-system-architecture)
11. [Platform Choice](#-platform-choice--web-application)
12. [Repository Structure](#-repository-structure)
13. [Development Plan](#-development-plan)
14. [Team](#-team--code4ce)
15. [References](#-references)

---

## 🎯 The Problem

India has over **15 million platform-based gig delivery workers**. They are among the most economically vulnerable working people in the country — yet they are completely excluded from every formal protection system that exists.

When disruptions hit — and in Chennai alone, **7 out of 12 months carry medium to high disruption risk** — delivery workers simply stop earning. Not because they choose to. Because they cannot ride in 35mm/hr rainfall. Because restaurants shut during a bandh. Because their platform goes down. Because the heat index hits 48°C and no one is ordering food.

**The average Chennai delivery worker loses ₹6,000–₹9,000 per year to disruption-related income loss.**

The protection gap exists because:

- **Traditional insurance won't touch them** — no salary slip, no fixed employer, no verifiable income history
- **Microfinance doesn't help** — covers capital needs, not income loss
- **Banks won't lend** — no collateral, no credit score, no proof of income
- **Platforms don't compensate** — workers are classified as "partners", not employees
- **Government schemes don't reach them** — most are unaware, unregistered, or ineligible

This isn't a niche problem. It is a systemic failure affecting millions of people who keep Indian cities fed, and it is entirely solvable with the right technology.

---

## 👤 Meet Murugan — Our Persona

**Murugan, 26 — Swiggy Delivery Partner, Tambaram, Chennai**

Murugan has been delivering for Swiggy for two years. He works 6 days a week, roughly 10 hours a day, covering the Tambaram and Chromepet zones of Chennai. He owns an Activa, rents a room with a friend, and sends ₹2,000 home to his family in Villupuram every month.

On a good week, he earns ₹4,500. On a week with three disruption days — which happens regularly during Chennai's monsoon season — he earns ₹2,950. That's a ₹1,550 loss in seven days, with no warning and no way to recover it.

**A week in Murugan's life during October 2024:**

| Day | Earnings | Reason |
|-----|----------|--------|
| Monday | ₹680 | Normal day |
| Tuesday | ₹320 | Heavy rain — couldn't ride for 4 hours |
| Wednesday | ₹610 | Normal day |
| Thursday | ₹410 | Heatwave — orders dropped sharply |
| Friday | ₹740 | Normal day |
| Saturday | ₹190 | Bandh — almost no orders all day |
| **Total** | **₹2,950** | **Expected: ₹4,500 — Loss: ₹1,550** |

**Why nothing currently helps Murugan:**
- No salary slip → can't apply for a loan
- No employer → not eligible for ESI or group insurance
- Platform "partner" status → no compensation for lost work days
- No credit score → banks won't lend without collateral
- Informal income → most insurance products require documented income proof

**What Murugan needs isn't charity. He needs a system that works as fast as the rain.**

---

## 💡 Our Solution

GigShield is built around one core insight: **the disruptions that cost Murugan money are measurable, verifiable, and predictable.** If we can measure them objectively, we can automate the entire insurance process around them.

That's parametric insurance.

Instead of asking Murugan to prove he lost income, GigShield monitors his zone in real time. When rainfall in Tambaram crosses 20mm/hr, we don't need him to call anyone. We already know he couldn't work. The payout triggers automatically.

**GigShield in one sentence:** A ₹84/week subscription that pays Murugan automatically when the weather or city makes it impossible for him to earn.

**What we cover:** Platform income loss due to external, verifiable disruptions.
**What we don't cover:** Health, accidents, vehicle damage, or personal emergencies.
**Who it's for:** Food delivery workers on Swiggy, Zomato, Dunzo, and Blinkit in Chennai (expanding to other cities in future phases).

---

## ⚡ How It Works

### Step 1 — Onboarding (2 minutes, no documents)

Murugan opens GigShield on his phone browser. He fills in:
- Full name and mobile number
- City and delivery zone (pincode-level)
- Platform (Swiggy / Zomato / Dunzo / Blinkit)
- Average weekly earnings

GigShield instantly generates his risk profile and weekly premium. No documents. No agent visit. No waiting for approval.

### Step 2 — Policy Activation

He pays ₹84 via UPI. His policy activates immediately and runs for 7 days. It auto-renews each week. If he doesn't want to continue, he simply doesn't pay — no cancellation process, no fees.

### Step 3 — Live Zone Monitoring

Our backend polls the OpenWeatherMap API and WAQI API every 30 minutes for every active worker's registered zone. It checks rainfall intensity, temperature, and AQI against our trigger thresholds. The admin panel handles manual triggers for bandh/curfew events.

Murugan's dashboard shows him live zone status — green (safe), amber (watch), red (trigger active).

### Step 4 — Automatic Claim Initiation

When a threshold is crossed:
1. FastAPI backend detects the trigger event
2. All active policies in the affected zone are identified
3. Claims are created automatically in Firestore
4. Push notification sent to each affected worker: *"Heavy rain in your zone. Claim initiated. ₹720 will reach your UPI by 8 PM."*
5. Fraud detection layer runs in the background

Murugan does nothing. He just receives the notification.

### Step 5 — Fraud Check and Payout

Our AI fraud detection model validates the claim against location data, platform activity, and weather records. Clean claims are approved and sent to Razorpay for UPI disbursement. The full cycle — trigger detection to UPI credit — completes within 2 hours.

---

## 🚨 Parametric Triggers

| Trigger | Data Source | Threshold | Payout | Rationale |
|---------|-------------|-----------|--------|-----------|
| Heavy Rainfall | OpenWeatherMap API | >20mm/hr in worker's pincode | 50% of daily income | IMD defines heavy rain at 15.6mm/hr; 20mm is the threshold where delivery becomes unsafe |
| Extreme Heat | OpenWeatherMap API | >43°C for 3+ consecutive hours | 30% of daily income | At 43°C+ order volumes drop sharply and health risk makes riding unsafe |
| Severe Air Pollution | WAQI API | AQI >300 | 40% of daily income | AQI >300 is classified "Hazardous" — outdoor work carries serious health risk |
| Curfew / Bandh | Admin manual trigger | Zone lockdown flag activated | 100% of daily income | Complete work stoppage — full income replacement |
| Platform Downtime | Mock API monitor | 2+ hours of platform unavailability | 60% of daily income | Extended outage eliminates all earning possibility |

**Threshold rationale:** All thresholds are set conservatively to reflect conditions where income loss is near-certain, not just inconvenient. This protects both the worker and the platform's financial sustainability.

---

## 💰 Weekly Premium Model

Gig workers live week to week. A yearly or monthly premium model doesn't fit their cash flow reality. GigShield charges weekly — the same rhythm Murugan earns in.

**Premium Formula:**

```
Weekly Premium = Base Rate + Zone Risk Adjustment + Seasonal Adjustment

Base Rate         : ₹49 (covers standard risk profile)
Zone Risk         : Low zone +₹0 | Medium zone +₹15 | High zone (flood-prone) +₹25
Seasonal          : Off-season +₹0 | Summer (Apr–May) +₹5 | Monsoon (Jun–Nov) +₹10
```

**Zone classification** is based on Chennai Corporation flood zone data and historical disruption frequency per pincode.

**Seasonal adjustment** is based on IMD Chennai historical rainfall and temperature data by month.

**Example — Murugan, Tambaram, October:**

| Component | Amount |
|-----------|--------|
| Base rate | ₹49 |
| Zone risk (Tambaram — High) | +₹25 |
| Seasonal (Monsoon) | +₹10 |
| **Weekly Premium** | **₹84** |
| **Max weekly payout** | **₹3,150** (70% of ₹4,500) |
| **Premium-to-coverage ratio** | **1 : 37.5** |

**Phase 2 upgrade:** The rule-based formula will be upgraded to a scikit-learn regression model trained on historical disruption frequency, zone-level weather data, and platform order volume patterns. This will allow dynamic, worker-specific pricing that reflects actual risk more precisely.

---

## 📊 Loss Simulation Dashboard

One of GigShield's most distinctive features — and the strongest argument for signing up.

When a worker first opens GigShield, before they register, they can enter their zone and weekly earnings and see:

> *"In the last 6 months, there were 14 heavy-rain disruption days in Tambaram. If you had been covered with GigShield, you would have received ₹6,720 in payouts. Your total premium cost would have been ₹1,848. Net benefit: ₹4,872."*

This is built on **historical OpenWeatherMap data** for each pincode, cross-referenced against our trigger thresholds. The numbers are real. The loss is real.

For workers already registered, the dashboard shows:
- Total disruption days this month in their zone
- Claims triggered and amounts paid out
- Cumulative savings since they joined GigShield
- Upcoming high-risk days based on 7-day weather forecast

This feature turns GigShield from an insurance product into a financial planning tool for gig workers.

---

## 🤖 AI/ML Integration

### 1. Premium Calculation Engine

**Phase 1 (Rule-based):** Formula above — deterministic, transparent, explainable.

**Phase 2 (ML-based):** scikit-learn Linear Regression model.
- **Training data:** Historical Chennai weather records (IMD), disruption event logs, zone-level order volume patterns
- **Features:** Zone risk score, month, platform, declared income, historical claim rate for zone
- **Output:** Personalized weekly premium — recalculated each renewal based on updated forecast data
- **Validation:** Cross-validated against known disruption weeks to measure pricing accuracy

### 2. Fraud Detection System

Parametric insurance is theoretically vulnerable to identity fraud and false registrations. Our multi-layer fraud detection addresses this:

| Check | Method | When It Runs |
|-------|--------|-------------|
| Location validation | Worker GPS at claim time vs registered zone | Every claim |
| Activity cross-check | Platform activity timestamp before disruption | Every claim |
| Anomaly detection | scikit-learn Isolation Forest — flags statistical outliers | Every claim |
| Duplicate prevention | One claim per trigger event per worker per day | Database-level constraint |
| Velocity check | Flags register-and-claim within unusual time window | Registration + claim |
| Weather correlation | Claim data cross-checked against actual API readings for that zone and time | Batch validation |

**Isolation Forest** was chosen for anomaly detection because it works well on small, unlabelled datasets — appropriate for our early-stage claim volume.

### 3. Predictive Risk Alerts

- Polls OpenWeatherMap 7-day forecast API daily for each active worker's pincode
- If forecast shows high-risk conditions in the next 48 hours, sends a push notification to uninsured workers in that zone: *"Heavy rain forecast for Tambaram this Thursday. Get covered today for ₹84."*
- For insured workers: *"High risk week ahead — your policy is active. You're covered."*
- This drives both conversions and retention, while genuinely helping workers plan their week

---

## 🛠️ Tech Stack

We chose this stack based on what is right for the problem — not just what we already knew. Every technology choice reflects a deliberate decision about performance, scalability, and fit for a real production insurance platform.

| Layer | Technology | Why |
|-------|-----------|-----|
| Frontend | **React.js 18** | Component architecture handles real-time dashboard updates cleanly; industry standard for dynamic web apps |
| Styling | **Tailwind CSS** | Utility-first, mobile-first, fast to build production-grade UI without custom CSS overhead |
| Backend | **Python + FastAPI** | Async-first, high performance, auto-generates Swagger API docs, production-ready Python framework |
| Database | **Firebase Firestore** | Real-time listeners for live trigger updates, flexible schema for variable worker profiles, generous free tier |
| Authentication | **Firebase Auth** | Phone number OTP login — no password needed, accessible for all literacy levels |
| Weather Data | **OpenWeatherMap API** | Real-time and historical weather by pincode, well-documented, free tier supports our build volume |
| AQI Data | **WAQI API** | City-zone air quality index, free, reliable |
| Payments | **Razorpay Test Mode** | Indian payment gateway, UPI support, clean sandbox environment for demo |
| ML | **Python scikit-learn** | Linear Regression (premium), Isolation Forest (fraud detection), lightweight, fits FastAPI backend |
| Hosting | **Vercel** (frontend) + **Railway** (backend) | Production-grade free tiers, GitHub-connected CI/CD, auto-deploy on push |
| Version Control | **GitHub** | Public repo, clean branch structure, transparent development history |

**Why React over plain HTML/JS:**
GigShield's dashboard requires real-time state updates — live trigger status changes, claim progress tracking, live zone monitoring. React's component state model and re-rendering handles this natively. Achieving the same with vanilla JS would require significant DOM manipulation complexity that doesn't scale.

**Why FastAPI over Flask:**
FastAPI is async by default, meaning our 30-minute trigger polling loop, API calls to OpenWeatherMap, and claim processing pipeline can all run concurrently without blocking. It also auto-generates interactive Swagger documentation, making our API transparent, testable, and judge-readable. Flask is synchronous by default and would require additional libraries to achieve the same.

**Why Firebase Firestore:**
Our trigger monitoring system needs to push real-time updates to worker dashboards the moment a claim is initiated. Firestore's real-time listeners make this possible without polling from the frontend. A traditional SQL database would require a separate WebSocket layer to achieve the same.

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        GIGSHIELD SYSTEM                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   ┌──────────────┐         ┌──────────────────────────┐    │
│   │   React.js   │ ◄─────► │   FastAPI Backend         │    │
│   │   Frontend   │  REST   │   (Python)                │    │
│   │   (Vercel)   │         │   (Railway)               │    │
│   └──────────────┘         └──────────┬───────────────┘    │
│                                        │                     │
│              ┌─────────────────────────┼──────────────┐     │
│              │                         │              │     │
│              ▼                         ▼              ▼     │
│   ┌──────────────────┐  ┌──────────────────┐  ┌──────────┐ │
│   │ Firebase         │  │ OpenWeatherMap   │  │ Razorpay │ │
│   │ Firestore +      │  │ API + WAQI API   │  │ UPI      │ │
│   │ Firebase Auth    │  │ (Trigger Source) │  │ Payout   │ │
│   └──────────────────┘  └──────────────────┘  └──────────┘ │
│                                        │                     │
│                          ┌─────────────▼──────────┐         │
│                          │   scikit-learn ML Layer │         │
│                          │   - Premium Calculator  │         │
│                          │   - Fraud Detection     │         │
│                          │   - Risk Predictor      │         │
│                          └────────────────────────┘         │
└─────────────────────────────────────────────────────────────┘
```

**Data Flow — Claim Trigger:**
```
OpenWeatherMap API (every 30 mins)
        │
        ▼
FastAPI Trigger Monitor
        │
        ├── Threshold crossed? NO → Continue polling
        │
        └── Threshold crossed? YES
                │
                ▼
        Identify active policies in affected zone (Firestore)
                │
                ▼
        Create claim records (Firestore)
                │
                ▼
        ML Fraud Detection (scikit-learn)
                │
                ├── Flagged → Admin review queue
                │
                └── Clean → Razorpay UPI disbursement
                                │
                                ▼
                        Push notification to worker
```

---

## 📱 Platform Choice — Web Application

| Consideration | Our Decision | Reasoning |
|--------------|-------------|-----------|
| Accessibility | Web (browser-based) | No installation needed — works on any Android phone |
| Performance | React PWA-ready | Can be converted to PWA in Phase 3 for offline access and home screen install |
| Device compatibility | Mobile-first responsive | Tailwind ensures clean UI on all screen sizes |
| Demo-ability | Web | Easier to demo to judges without device dependencies |
| Build timeline | Web | Faster iteration cycle vs native mobile in a 6-week sprint |

---

## 📁 Repository Structure

```
gigshield/
│
├── frontend/                          # React.js application
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/                # Reusable UI components
│   │   │   ├── Navbar.jsx
│   │   │   ├── TriggerCard.jsx        # Live zone monitoring card
│   │   │   ├── ClaimStatus.jsx        # Claim progress tracker
│   │   │   ├── PremiumDisplay.jsx     # Premium breakdown card
│   │   │   └── LossSimulator.jsx      # Loss simulation calculator
│   │   ├── pages/                     # Route-level page components
│   │   │   ├── Landing.jsx
│   │   │   ├── Onboarding.jsx
│   │   │   ├── Dashboard.jsx          # Worker dashboard
│   │   │   ├── ActiveClaim.jsx
│   │   │   └── AdminDashboard.jsx
│   │   ├── services/                  # API call functions
│   │   │   ├── api.js                 # FastAPI backend calls
│   │   │   └── firebase.js            # Firestore real-time listeners
│   │   ├── utils/                     # Helper functions
│   │   │   └── premiumCalculator.js
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── tailwind.config.js
│
├── backend/                           # FastAPI application
│   ├── app/
│   │   ├── main.py                    # FastAPI app entry point
│   │   ├── routers/                   # API route handlers
│   │   │   ├── workers.py             # Worker registration, profile
│   │   │   ├── policies.py            # Policy creation, renewal
│   │   │   ├── claims.py              # Claim initiation, status
│   │   │   ├── triggers.py            # Trigger monitoring endpoints
│   │   │   └── admin.py               # Admin dashboard endpoints
│   │   ├── services/                  # Business logic
│   │   │   ├── trigger_monitor.py     # 30-min polling loop
│   │   │   ├── claim_processor.py     # Auto-claim initiation
│   │   │   ├── payout_service.py      # Razorpay UPI disbursement
│   │   │   └── notification_service.py
│   │   ├── ml/                        # ML models
│   │   │   ├── premium_model.py       # scikit-learn regression
│   │   │   ├── fraud_detection.py     # Isolation Forest
│   │   │   └── risk_predictor.py      # 7-day forecast risk scoring
│   │   ├── models/                    # Pydantic data models
│   │   │   ├── worker.py
│   │   │   ├── policy.py
│   │   │   └── claim.py
│   │   └── config.py                  # Environment variables
│   ├── requirements.txt
│   └── Dockerfile
│
├── ml/                                # ML model training notebooks
│   ├── data/                          # Training datasets
│   ├── premium_model_training.ipynb
│   └── fraud_detection_training.ipynb
│
├── docs/                              # Project documentation
│   ├── persona/
│   │   └── murugan_worker_persona.docx
│   ├── wireframes/
│   │   └── gigshield_wireframes_v2.html
│   └── architecture/
│       └── system_architecture.md
│
├── .env.example                       # Environment variable template
├── .gitignore
└── README.md
```

---

## 🗓️ Development Plan

### Phase 1 — Seed (March 4–20) ✅ In Progress
Research, persona development, system design, tech stack finalization, README, wireframes, 2-minute demo video.

**Deliverables:** README.md in GitHub repo + 2-minute video

### Phase 2 — Scale (March 21–April 4)

**Week 1 (March 21–27):**
- React project scaffold + Tailwind setup
- Firebase Firestore schema design
- FastAPI project setup + base routes
- Worker registration and onboarding flow
- Premium calculator (rule-based)

**Week 2 (March 28–April 4):**
- OpenWeatherMap API integration
- 30-minute trigger monitoring loop
- Automatic claim initiation logic
- Razorpay test mode UPI payout flow
- Loss simulation dashboard
- Basic fraud detection layer
- Worker dashboard with live zone monitoring

**Deliverables:** Working MVP + 2-minute demo video

### Phase 3 — Soar (April 5–17)
- scikit-learn ML model for premium calculation
- Isolation Forest fraud detection upgrade
- Predictive risk alert system
- PWA conversion for offline access
- Full end-to-end demo with real payout simulation
- Admin dashboard with live claim management
- Final polish + DemoJam pitch deck

**Deliverables:** Final product + pitch presentation

---

## 👥 Team — Code4ce

| Name | Role | Responsibilities |
|------|------|-----------------|
| **Srinidhi R** | Team Lead & Research | Persona research, product strategy, documentation, coordination |
| **Panbarasi S** | Frontend Development | React.js, Tailwind CSS, dashboard UI, responsive design |
| **Aakas D R** | Backend & AI/ML | FastAPI, Firebase, trigger monitoring, scikit-learn models |
| **Dharshini S S** | Integration & Content | API integration, testing, content, video production |

---

## 📚 References

1. [Zomato vs Swiggy Delivery Partner Earnings — CollegeSearch India](https://www.collegesearch.in/articles/zomato-delivery-boy-salary-vs-swiggy-delivery-boy-salary-inhand-earnings-per-month)
2. [Gig Work and Climate Risk — Mongabay India](https://india.mongabay.com/2025/08/gig-work-heats-up-disaster-body-steps-in-with-advisory/)
3. [Fairwork India Report 2024 — Platform Worker Conditions](https://fair.work/wp-content/uploads/sites/17/2024/10/Fairwork_India_Report_2024.pdf)
4. [India's Booming Gig and Platform Economy — NITI Aayog](https://www.niti.gov.in/sites/default/files/2023-06/Policy_Brief_India's_Booming_Gig_and_Platform_Economy_27062022.pdf)
5. [Gig Worker Income and Disruption Patterns — JETIR](https://www.jetir.org/papers/JETIR2404421.pdf)

---

*Built with purpose by Team Code4ce for Guidewire DEVTrails 2026*
*Seed → Scale → Soar*
