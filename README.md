# Social Media Performance Dashboard 📊

An interactive Streamlit dashboard analyzing simulated social media performance for a luxury fashion brand across Instagram, TikTok, and Twitter — KPIs, engagement trends, content-type performance, platform comparison, posting-time heatmaps, and auto-generated insights.

## How It Works

1. **Synthetic data** — On first run, `data_generator.py` generates **500 simulated posts** for 2024 (`generate_posts()`), saved to `data/posts.csv`. Each post has:
   - A platform (`Instagram` 45%, `TikTok` 35%, `Twitter` 20%)
   - A content type (`Product showcase`, `Behind the scenes`, `Campaign launch`, `Influencer collab`, `Brand story`)
   - Reach drawn from a log-normal distribution scaled per platform (TikTok > Instagram > Twitter)
   - Engagement rate drawn per content type (e.g., Influencer collabs ~7.1% base rate, Product showcases ~3.8%)
   - Likes/comments/shares/saves derived from reach × engagement rate with randomized ratios
   - Seasonal boosts applied to likes/reach in March, June–July, and November–December (simulating Ramadan, summer, and year-end campaign spikes)
   - Day-of-week and hour-of-day fields with a realistic posting-time distribution (peak activity late morning/early afternoon)
2. **Analysis layer (`eda.py`)** — Computes:
   - Top-level KPIs (total reach, average engagement rate, total posts, best platform, best content type)
   - Monthly engagement trends by platform
   - Content-type performance (avg engagement, avg reach, post count)
   - Platform comparison table
   - Day × hour posting-time heatmap
   - Top 10 posts by engagement rate
   - Five auto-generated, data-driven insight bullets (best content type, best platform, peak month, best posting day, underperforming content type)
3. **Visualization layer (`charts.py`)** — Builds the Plotly charts: engagement timeline, content-type bar chart, platform radar, heatmap, and a reach-vs-engagement scatter plot.
4. **App (`app.py`)** — Wires it all together with custom CSS-styled KPI cards, sidebar filters (platform, content type, month), and a styled top-posts table.

## Tech Stack

| Component | Library |
|---|---|
| UI | Streamlit |
| Data processing | Pandas, NumPy |
| Charts | Plotly |
| (Imported, unused directly in app.py) | Matplotlib |

## Project Structure

```
social-media-dashboard/
├── app.py               # Main Streamlit app: layout, filters, KPI cards, chart placement
├── data_generator.py     # Generates 500 synthetic posts → data/posts.csv
├── eda.py                 # KPI calculations, aggregations, auto-generated insights
├── charts.py               # Plotly chart builders (timeline, bar, radar, heatmap, scatter)
├── requirements.txt         # streamlit, pandas, numpy, plotly, matplotlib
└── README.md
```

> Note: this repo currently has no LICENSE file — consider adding one (e.g., MIT, matching your other projects) if you intend others to reuse the code.

## Getting Started

### Prerequisites

- Python 3.9+

### Installation

```bash
git clone https://github.com/manal-munawwar/social-media-dashboard.git
cd social-media-dashboard
pip install -r requirements.txt
```

### Run

```bash
streamlit run app.py
```

On first launch, since `data/posts.csv` doesn't exist yet, the app automatically calls `generate_posts()` to create it. Subsequent runs reuse the cached file.

### Usage

1. Use the sidebar to filter by **platform**, **content type**, and **month**.
2. View the five KPI cards: total reach, average engagement rate, total posts, best platform, best content type.
3. Explore the charts:
   - Monthly engagement timeline by platform
   - Content-type performance bar chart
   - Platform comparison radar chart
   - Day × hour posting-time heatmap
   - Reach vs. engagement scatter plot
4. Read the auto-generated **Key Insights** section.
5. Review the **Top 10 posts by engagement rate** table.

## Notes & Limitations

- All data is **synthetically generated** (seeded with `np.random.seed(42)` for reproducibility) — this is a demo/portfolio dashboard, not connected to any real social media API.
- `matplotlib` is listed in `requirements.txt` but isn't directly imported in `app.py`; it may be a leftover dependency or used implicitly by another library.
- No way to plug in real data without modifying `data_generator.py` or replacing `data/posts.csv` with your own CSV in the same schema.

## Possible Improvements

- Add a toggle to load real exported social data (CSV upload) instead of only synthetic data
- Parameterize the data generator (date range, platforms, brand type) via the UI
- Add export/download buttons for charts and the insights summary
- Add a LICENSE file

## Author

**Manal Munawwar**
- GitHub: [@manal-munawwar](https://github.com/manal-munawwar)
