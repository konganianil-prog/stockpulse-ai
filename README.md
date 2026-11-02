# STOCKPULSE AI — Indian Stock Market Intelligence & Research Platform

[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688.svg?style=flat&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/React-19-61DAFB.svg?style=flat&logo=React&logoColor=black)](https://react.dev)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0+-3178C6.svg?style=flat&logo=TypeScript&logoColor=white)](https://www.typescriptlang.org)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-4.0-38B2AC.svg?style=flat&logo=tailwind-css&logoColor=white)](https://tailwindcss.com)
[![License](https://img.shields.io/badge/Regulatory-AMFI%20%2F%20SEBI%20Compliant%20Research-10B981.svg)](#educational-mandate)

**STOCKPULSE AI** is an advanced, production-grade financial intelligence and research platform specifically architected for the Indian stock market (NSE and BSE).

> **IMPORTANT REGULATORY & EDUCATIONAL MANDATE**  
> **This application is NOT a trading application.** Users cannot execute buy or sell orders through this platform. The purpose is strictly educational research, fundamental analysis, and institutional-grade data intelligence to assist users in making informed, independent decisions.

---

## 🌟 Key Capabilities & Features

### 1. Main Dashboard & Live Indian Market Overview
- **Major Benchmarks:** NIFTY 50, SENSEX, NIFTY BANK, NIFTY IT, NIFTY MIDCAP 100, NIFTY SMALLCAP 100.
- **Participation & Market Breadth:** Advances, Declines, Unchanged, Advance/Decline ratio, 52-week Highs and Lows count.
- **Session Highlights:** Top Gainers, Top Losers, Most Active stocks, and Unusual Volume surges.
- **Authentic News Stream:** Real financial reporting from LiveMint, Economic Times, and Business Standard with automated NLP sentiment classification.

### 2. Comprehensive Stock Research & Intelligence Report
Every Indian stock features a research dossier:
- **Company Information:** Full corporate profile, NSE symbol, BSE security code, ISIN, sector, industry, and official investor relations link.
- **AMFI Market Cap Classification:** Official Large Cap (Rank 1–100), Mid Cap (Rank 101–250), and Small Cap (Rank 251+) categorization adhering strictly to SEBI Circular `SEBI/HO/IMD/DF3/CIR/P/2017/114`.
- **Interactive Multi-Timeframe Charting:** 1D, 1W, 1M, 3M, 6M, 1Y, 3Y, 5Y with selectable overlays (20 SMA, 50 SMA, 200 SMA, 20 EMA) and indicator subcharts (Volume, RSI 14, MACD 12/26/9).
- **Technical Pivots:** Pivot point, Support (S1, S2, S3), Resistance (R1, R2, R3), RSI overbought/oversold status, and moving average momentum.

### 3. Institutional Fundamental Analysis
- **Valuation:** P/E Ratio, Industry P/E average, Price-to-Book (P/B), PEG ratio, Trailing EPS, Book Value, Dividend Yield, and EV/EBITDA.
- **Profitability:** Return on Equity (ROE), ROCE, Net Profit Margin, Operating Margin, EBITDA Margin, YoY Revenue Growth, and YoY Profit Growth.
- **Solvency & Balance Sheet Health:** Total Debt, Debt-to-Equity (D/E), Current Ratio, Interest Coverage Ratio, and Free Cash Flow (FCF).
- **Shareholding Pattern:** Promoter Holding, FII (Foreign Institutional) Holding, DII (Domestic Institutional) Holding, Public Float, and Promoter Pledging percentages.
- **Beginner-Friendly Glossaries:** One-click explainer tooltips for every ratio explaining ideal benchmarks and usage tips.
- **Financial Statements:** Multi-period quarterly results and annual statements.

### 4. AI-Powered Fundamental Research Engine
- **Data-Driven Strengths & Weaknesses:** Evidence-backed assessments citing actual financial numbers (e.g., *"ROE of 48.5% highlights superior capital compounding"* or *"Debt-to-Equity of 0.08 ensures robust balance sheet durability"*).
- **Growth Opportunities & Financial Risks:** Sector-tailored catalysts and regulatory headwinds.

### 5. Multi-Timeframe AI Research Perspectives
- **Horizon-based Perspectives:**
  - Short-Term (1–6 Months)
  - Medium-Term (6–24 Months)
  - Long-Term (3–5 Years)
- **Standardized Research Labels:**
  - *Worth researching*
  - *Consider monitoring*
  - *Wait for better valuation*
  - *Reassess existing investment thesis*
  - *Avoid due to significant risks*
- **Overall Categorisation:** *STRONG FUNDAMENTALS*, *POSITIVE OUTLOOK*, *WATCHLIST*, *NEUTRAL*, *HIGH RISK*, or *WEAK FUNDAMENTALS*.

### 6. AI Market Sentiment Engine
- Aggregated Polarity Breakdown: Positive %, Neutral %, and Negative % from news articles.
- Fear & Greed Index (0 to 100) and top macro market drivers.
- **Clear Methodology Distinction:** Transparently discloses that sentiment is synthesized via NLP from published media and broker notes, clearly distinguished from statistical investor survey data.

### 7. Multi-Factor AI Stock Screener
- Filter across all Indian stocks by:
  - AMFI Market Cap (Large, Mid, Small)
  - Sector & Industry
  - Minimum ROE & ROCE
  - Maximum P/E & Maximum Debt/Equity
  - Minimum Dividend Yield & Technical RSI
- **Predefined Strategies:**
  - *High Growth, Low Debt*
  - *Undervalued Quality Compounders*
  - *Consistent Compounders*
  - *RSI Oversold Quality*
  - *Dividend Champions*
- **CSV Export:** One-click CSV download of screened criteria.

### 8. Dedicated Sector Intelligence
Deep-dive research for 14 Indian sectors:
- Banking, Information Technology, Pharmaceuticals, Healthcare, Automobile, FMCG, Energy, Infrastructure, Real Estate, Metals, Telecom, Renewable Energy, Defence, and Financial Services.
- Performance tracking (1D, 1M, 1Y), top constituent companies, growth drivers, and sector risks.

### 9. Side-by-Side Stock Comparison
- Compare 2 to 5 companies simultaneously across 12+ metrics.
- Highlights individual metric leaders (★) without declaring artificial blanket winners.

### 10. Persistent Research Watchlists
- Real-time price tracking, daily change %, P/E, ROE, and D/E ratios.
- Add/remove stocks, custom watchlist creation, stored in SQLite/PostgreSQL.

### 11. AI Stock Research Assistant (Chatbot)
- Specialized conversational assistant for Indian capital markets.
- Answers queries with real-time stock fundamentals, recent news context, and source timestamps.
- Supports external Gemini API / OpenAI API keys with automatic high-precision local fallback.

### 12. Scenario-Based Future Outlook Modeling
- Bullish Scenario, Base Scenario, and Bearish Scenario with probability assessments and sensitivity trigger factors.

### 13. Financial Calendar
- **Economic Calendar:** RBI MPC rate decisions, CPI Inflation, GDP, IIP.
- **Corporate Earnings:** Upcoming quarterly result announcements.
- **Dividends:** Dividend per share, type, ex-dates, and record dates.
- **IPO Tracker:** Recent and upcoming Indian mainboard & SME listings.

---

## 🛠️ Technology Architecture

```
STOCKPULSE AI
├── backend/                  # FastAPI Python Backend
│   ├── app/
│   │   ├── api/              # REST Endpoints (Auth, Market, Stocks, Screener, Sectors, Comparison, Watchlist, Calendar, AI, News)
│   │   ├── core/             # Config, Database (SQLAlchemy), Security (PBKDF2/JWT)
│   │   ├── models/           # SQLAlchemy ORM Models (User, Company, Ratios, Assessments, Watchlists)
│   │   ├── schemas/          # Pydantic Schemas & Data Contracts
│   │   ├── data_providers/   # AMFI Classifier, Yahoo Finance Feed, RSS News Parser, Financial Calendar
│   │   ├── analysis/         # Technical Indicators, Fundamental Scoring, Sector Analytics, Sentiment
│   │   ├── ai/               # Research Engine, Recommendation Perspectives, Future Outlook, Chatbot
│   │   └── utils/            # Data Seeding Script, Memory Cache
│   ├── run.py                # Backend Entrypoint (Port 8000)
│   ├── requirements.txt      # Python Dependencies
│   └── .env.example          # Configuration Template
├── frontend/                 # React 19 + TypeScript + Vite + Tailwind CSS
│   ├── src/
│   │   ├── components/       # Common, Stock Research, Dashboard, and AI Assistant UI Widgets
│   │   ├── pages/            # 11 Dedicated Pages
│   │   ├── context/          # AuthContext, WatchlistContext
│   │   ├── services/         # REST API Client
│   │   └── types/            # TypeScript Interfaces
│   ├── package.json
│   └── vite.config.ts        # Vite Server with /api Proxy
├── start.bat                 # One-click Windows Launcher
├── start.ps1                 # One-click PowerShell Launcher
└── README.md
```

---

## 🚀 Installation & Quick Start

### Prerequisites
- Python 3.11 or 3.12 (CPython)
- Node.js 20+ (LTS) & NPM

### Step 1: Backend Setup
```bash
# 1. Navigate to the project root
cd "shares app"

# 2. Activate virtual environment (if using pre-installed backend_venv)
backend_venv\Scripts\activate   # On Windows
# source backend_venv/bin/activate # On Linux/macOS

# 3. Seed the database with verified Indian stock records
python backend/app/utils/seed_data.py

# 4. Start the FastAPI backend
python backend/run.py
```
Backend will start on: **http://127.0.0.1:8000**  
Interactive API Docs (Swagger UI): **http://127.0.0.1:8000/docs**

### Step 2: Frontend Setup
In a new terminal window:
```bash
# 1. Navigate to frontend directory
cd frontend

# 2. Install dependencies (if needed)
npm install

# 3. Start Vite dev server
npm run dev
```
Frontend will be live at: **http://localhost:5173**

---

## ⚡ One-Click Startup (Windows)
Double-click `start.bat` or run:
```powershell
.\start.ps1
```
This automatically launches both backend and frontend dev servers.

---

## 🔑 Demo Account Credentials
For instant exploration without registration:
- **Email:** `investor@stockpulse.ai`
- **Password:** `stockpulse2026`

*(You can also freely register new custom accounts via the UI modal).*

---

## ⚖️ Regulatory & Disclaimer Notice
STOCKPULSE AI is built strictly as an educational research tool. Stock market investments are subject to market risks. Past performance and algorithmic assessments do not guarantee future returns. Always read scheme-related and corporate filing documents carefully before investing. Consult a certified SEBI-registered financial advisor for personal investment advice.
