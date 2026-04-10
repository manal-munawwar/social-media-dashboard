# 📊 Social Media Performance Dashboard

An interactive analytics dashboard designed to analyze social media performance for a luxury fashion brand across Instagram, TikTok, and Twitter — built with Python, Pandas, Plotly, and Streamlit.

🔗 **Live App:** [https://social-media-dashboard-zfto2azatuxa8sed6z6quo.streamlit.app]

---

## 🚀 Overview

This project delivers an end-to-end analytics solution — from data generation and transformation to visualization and automated insights.

It enables data-driven decision-making by identifying:
- Top-performing platforms
- High-impact content types
- Optimal posting times
- Engagement trends over time

---

## 📈 Key Features

- **KPI Overview**  
  Total reach, average engagement rate, total posts, best platform, and best content type  

- **Engagement Timeline**  
  Monthly engagement trends segmented by platform  

- **Content Type Analysis**  
  Identifies which formats drive the highest engagement  

- **Platform Comparison**  
  Radar chart comparing engagement, reach, and likes across platforms  

- **Posting Time Heatmap**  
  Highlights best days and hours for publishing  

- **Reach vs Engagement Analysis**  
  Scatter plot to identify high-performing outliers  

- **Automated Insights Engine**  
  Generates 5 actionable, data-driven recommendations  

- **Top Posts Leaderboard**  
  Top 10 posts ranked by engagement rate with visual styling  

---

## 🛠️ Tech Stack

| Tool              | Purpose                          |
|------------------|----------------------------------|
| Python           | Core programming language        |
| Pandas + NumPy   | Data processing & analysis       |
| Plotly Express   | Interactive visualizations       |
| Streamlit        | Dashboard framework & deployment |
| Matplotlib       | Styled data tables              |

---

## ⚙️ Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/social-media-dashboard
cd social-media-dashboard

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the dashboard
streamlit run app.py

The dataset is generated synthetically on first run (`data/posts.csv`).
```

## 📂 Project Structure

social-media-dashboard/
├── app.py # Main Streamlit dashboard
├── data_generator.py # Synthetic dataset (500 posts, 12 months)
├── eda.py # Analysis logic (KPIs, aggregations, insights)
├── charts.py # Plotly visualisations
├── data/
│ └── posts.csv # Auto-generated dataset
├── requirements.txt
└── README.md

---
---
### 👤 Author

**Manal Munawwar**  
🔗 [LinkedIn](https://www.linkedin.com/in/manal-munawwar-9122a8269/)
