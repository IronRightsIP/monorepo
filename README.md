# 🛡️ IronRights Monorepo

Welcome to the IronRights IP Management Platform — an AI-powered blockchain solution for NFT licensing, infringement monitoring, and creator monetization.

---

## 📁 Monorepo Structure

```
ironrights/
├── apps/
│   ├── frontend/              # Next.js frontend
│   └── backend/               # Node.js + Express API
├── crawler/                   # IP/NFT infringement monitor (Node.js worker)
├── ai-licensing-engine/       # FastAPI microservice for licensing suggestions
├── render.yaml                # Render deployment blueprint
├── .env.example               # Sample environment config
└── .github/workflows/
    └── github_actions_ironrights.yml  # GitHub Actions CI/CD
```

---

## 🚀 Quick Start

### 1. Clone the Repo

```bash
git clone https://github.com/IronRightsIP/ironrights.git
cd ironrights
```

### 2. Setup Environment Variables

```bash
cp .env.example .env
```

> Fill in `.env` with your keys (Infura, MongoDB, Wallet Private Key)

---

## 📦 Monorepo Apps

### 🔷 Frontend (`apps/frontend`)
- Built with **Next.js**
- Connects to backend API and licensing engine
- Start locally:
  ```bash
  cd apps/frontend
  npm install
  npm run dev
  ```

### 🔶 Backend (`apps/backend`)
- Express API for NFT metadata and MongoDB
- Start locally:
  ```bash
  cd apps/backend
  npm install
  npm run start
  ```

### 🕵️ Crawler (`crawler`)
- Detects NFT/IP violations via web3 & scraping
- Start manually:
  ```bash
  cd crawler
  npm install
  npm run start
  ```

### 🤖 Licensing AI (`ai-licensing-engine`)
- FastAPI model to auto-suggest terms
- Start locally:
  ```bash
  cd ai-licensing-engine
  pip install -r requirements.txt
  uvicorn api:app --reload
  ```

---

## ⚙️ Deployment (Render)

You can deploy using the [render.yaml](./render.yaml):

```bash
# From the root
render deploy blueprint
```

---

## ✅ GitHub Actions

This monorepo includes a GitHub Actions CI workflow that installs, builds, and prepares all services.

> File: `.github/workflows/github_actions_ironrights.yml`

---

## 📬 Questions?
Contact: [team@ironrights.io](mailto:team@ironrights.io)
