# Social Media Performance Dashboard

An interactive analytics dashboard analysing social media performance for a luxury fashion brand across Instagram, TikTok, and Twitter — built with Python, Pandas, Plotly, and Streamlit.

## What it does

- **KPI overview** — total reach, avg engagement rate, total posts, best platform, best content type
- **Engagement timeline** — monthly engagement rate trends by platform
- **Content type analysis** — which formats drive the most engagement
- **Platform comparison** — normalised radar chart across engagement, reach, and likes
- **Posting time heatmap** — best days and hours to publish
- **Reach vs engagement scatter** — identify high-reach/high-engagement outliers
- **Auto-generated insights** — 5 data-driven recommendations
- **Top 10 posts table** — sorted by engagement rate

## Tech stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Pandas + NumPy | Data manipulation and EDA |
| Plotly Express | Interactive charts |
| Streamlit | Dashboard framework |

## Run locally

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/social-media-dashboard
cd social-media-dashboard

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the dashboard
streamlit run app.py
```

The dataset is generated synthetically on first run (`data/posts.csv`).

## Project structure

```
social-media-dashboard/
├── app.py               # Main Streamlit dashboard
├── data_generator.py    # Synthetic dataset (500 posts, 12 months)
├── eda.py               # Analysis functions (KPIs, groupby, insights)
├── charts.py            # All Plotly visualisations
├── data/
│   └── posts.csv        # Auto-generated on first run
├── requirements.txt
└── README.md
```

## CV writeup

> *"Built an interactive social media performance dashboard in Python analysing 500+ posts across Instagram, TikTok, and Twitter for a luxury fashion brand. Features engagement trend analysis, content type benchmarking, posting time optimisation, and auto-generated strategic insights. Built with Pandas, Plotly, and Streamlit."*

---
Built by Manal Munawwar · [LinkedIn](https://www.linkedin.com/in/manal-munawwar-9122a8269/)
