# covid-flask-service

# 🦠 COVID-19 Flask Service + Jenkins Automation

This project implements a Python Flask service that provides COVID-19 statistics using an external public API.  
The service is deployed using Docker and tested via a Jenkins pipeline.

---

## 🚀 Project Features

- 🔍 Fetches COVID-19 data for any country from an external API.
- 🧪 Provides 4 API endpoints:
  - `/status` — check if backend API is reachable
  - `/newCasesPeak?country=COUNTRY` — highest number of new cases in the past 30 days
  - `/recoveredPeak?country=COUNTRY` — highest number of recovered cases in the past 30 days
  - `/deathsPeak?country=COUNTRY` — highest number of deaths in the past 30 days
- ✅ JSON responses with error handling
- 🐳 Dockerized Flask app
- 🤖 Automated using Jenkins Pipeline
- 📦 Code hosted in a public GitHub repository

---