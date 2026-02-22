# AlphaLoop: Autonomous AI Investment Analyst

## Design Document & Architecture Spec

**Date:** 2026-02-21
**Author:** David Zhang
**Status:** Draft / Phase 0

---

## 1. Vision & Philosophy (The "No-Chatbot" Revolution)

**Core Concept:**
Moving beyond passive "Chatbots" (Request/Response) to active **"Autonomous Agents"** (Loop/Lifecycle).
AlphaLoop is a digital employee that works 24/7. It does not wait for user input. It proactively monitors financial markets, consumes vast amounts of unstructured data (News, 10-K, Twitter), performs deep reasoning, and pushes critical insights to the user.

**Value Proposition:**

* **Active Monitoring:** 24/7 surveillance of Crypto/US Stocks.
* **Cognitive Automation:** Autonomous research, reasoning, and report generation.
* **Self-Reflection:** The system tracks its own predictions and corrects its logic over time.

---

## 2. System Architecture

The system follows a **Trinity Architecture**:

1. **The Face (Client):** iOS Native (SwiftUI) - Visualization & Notification.
2. **The Body (Server):** Python (FastAPI) - API Gateway & Data Ingestion.
3. **The Brain (Agent):** Python (LangGraph) - State Management & Reasoning Loop.

### High-Level Stack

* **Mobile:** iOS 17+, SwiftUI, Charts, Live Activities, Core Data.
* **Backend:** Python 3.11, FastAPI, SQLModel (Async).
* **AI Orchestration:** **LangGraph** (Stateful Multi-Actor Applications).
* **Model:** DeepSeek-V3 / R1 (via API).
* **Database:** PostgreSQL (Structured Data) + pgvector / ChromaDB (Vector Embeddings).
* **Infrastructure:** Docker Compose (Always-on VPS).

---

## 3. The Autonomous Loop (LangGraph Workflow)

The core logic is a **Cyclic Graph**, not a linear Chain.

### The "Life" Cycle

1. **Wake Up (Scheduler):** Triggered by time (e.g., every 15 mins) or events (Price Alert).
2. **Perceive (Sensor Node):**
   * Fetch Market Data (`yfinance`, `ccxt`).
   * Fetch Unstructured Data (News API, Twitter, SEC EDGAR).
3. **Filter (Attention Node):**
   * Discard noise. Focus on high-impact signals (e.g., "Earnings Miss", "Regulatory Ban").
4. **Reason (Analyst Node):**
   * **LLM Processing:** "Given the CPI data and current BTC trend, is this a bull trap?"
   * **Tool Use:** Search for historical parallels.
5. **Act (Executor Node):**
   * **Write Report:** Generate a Markdown brief.
   * **Push Notification:** If urgency > 8/10, trigger APNs.
6. **Reflect (Critic Node):**
   * Compare yesterday's prediction with today's reality.
   * Update "World Model" (Context) if wrong.
7. **Sleep:** Wait for the next cycle.

---

## 4. Key Features & Modules

### A. The "Smart Brief" (Automated Reporting)

* **Input:** 50+ news articles, 10-K filings.
* **Process:** Map-Reduce Summary via LLM.
* **Output:** A concise, structured Markdown report (Risks, Opportunities, Catalyst).
* **UI:** Rendered natively in iOS with expandable sections.

### B. Sentiment & Emotion Analysis

* **Metric:** "Fear & Greed" Index derived from raw text, not just price.
* **Visualization:** SwiftUI Charts (Gauge/Dashboard).

### C. Self-Reflection (The "Killer Feature")

* **Mechanism:**
  * Day T: Agent predicts "TSLA up due to robotaxi hype". Saves state.
  * Day T+1: Agent checks TSLA price. If down, Agent generates a "Post-Mortem" log: *I overweighted social sentiment and underweighted macro interest rates.*
* **Display:** A transparent "Win Rate" or "Learning Log" visible to the user.

---

## 5. Implementation Roadmap (MVP)

### Phase 1: The Heartbeat (Infrastructure)

* **Goal:** A Python process that runs forever and logs "I am alive" every hour.
* **Tech:** Python, Docker, LangGraph (Simple Loop).

### Phase 2: The Senses (Data Ingestion)

* **Goal:** Automated fetching of Price + News.
* **Tech:** `yfinance`, NewsAPI/Tavily, PostgreSQL schema design.

### Phase 3: The Brain (Reasoning & Agent)

* **Goal:** DeepSeek V3 integration for analysis and summarization.
* **Tech:** LangGraph State Machine, Prompt Engineering (Analyst Persona).

### Phase 4: The Face (iOS Client)

* **Goal:** Mobile visualization of the Agent's work.
* **Tech:** SwiftUI, Network Layer, Markdown Rendering, Push Notifications.

---

## 6. Interview Narrative (Why this matters)

* **"No-Chatbot":** Demonstrates understanding of the next wave of AI (Agentic Workflows).
* **"Full-Stack":** iOS (Product) + Python (AI) + DB (Data Engineering).
* **"Fintech Native":** Handles structured (Price) and unstructured (Text) financial data effectively.
