# 🚀 CareerGenie Talent Discovery MVP

A lightweight recruiter tool that discovers, ranks, and manages developers from GitHub using structured filters.

---

## 🔍 Overview

CareerGenie Talent Discovery is a mini sourcing platform that allows recruiters to:

- Find developers using GitHub data
- Filter candidates based on skills and activity
- Score and rank candidates automatically
- Send personalized outreach messages
- Track shortlisted candidates (mini ATS)

---

## ✨ Features

### 🔎 Smart Filtering
- Filter by programming language
- Filter by location
- Minimum followers
- Minimum repositories

### 📊 Candidate Scoring
- Activity-based scoring
- Popularity (followers)
- Repository engagement (stars)

### 🧠 Role Inference
Automatically classifies candidates as:
- Backend Engineer
- Frontend Engineer
- ML Engineer

### 📩 Outreach System
- Write custom messages per candidate
- Invite candidates directly
- Store message + candidate together

### 📌 Saved Candidates Panel
- View invited candidates in sidebar
- Track outreach messages

### 📤 Export
- Download candidate list as CSV

---

## 🛠 Tech Stack

- **Python**
- **Streamlit** (UI)
- **GitHub REST API**
- **uv** (Python package manager)

---

## ⚙️ Setup

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/careergenie-talent-discovery-mvp.git
cd careergenie-talent-discovery-mvp
