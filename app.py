import streamlit as st
import pandas as pd
import os
from data_generator import generate_posts
from eda import load_data, kpi_summary, monthly_engagement, content_type_performance, platform_comparison, posting_time_heatmap, top_posts, insight_bullets
from charts import engagement_timeline, content_type_bar, platform_radar, heatmap_chart, reach_vs_engagement_scatter

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Social Media Performance Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] { background: #F9FAFB; }
    .kpi-card {
        background: white;
        border-radius: 12px;
        padding: 1.2rem 1.4rem;
        border: 1px solid #E5E7EB;
        text-align: center;
    }
    .kpi-label { font-size: 12px; color: #6B7280; text-transform: uppercase; letter-spacing: .06em; margin-bottom: 4px; }
    .kpi-value { font-size: 28px; font-weight: 700; color: #111827; line-height: 1.1; }
    .kpi-sub { font-size: 12px; color: #9CA3AF; margin-top: 4px; }
    .insight-card {
        background: #EFF6FF;
        border-left: 3px solid #3B82F6;
        border-radius: 0 8px 8px 0;
        padding: .75rem 1rem;
        margin-bottom: .5rem;
        font-size: 14px;
        color: #1E3A5F;
    }
    h1 { color: #111827 !important; }
    .section-title { font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: .1em; color: #9CA3AF; margin: 1.5rem 0 .5rem; }
</style>
""", unsafe_allow_html=True)

# ── Data loading ──────────────────────────────────────────────────────────────
@st.cache_data
def get_data():
    if not os.path.exists("data/posts.csv"):
        generate_posts()
    return load_data()

df_raw = get_data()

# ── Sidebar filters ───────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### Filters")
    platforms = st.multiselect(
        "Platform",
        options=df_raw["platform"].unique().tolist(),
        default=df_raw["platform"].unique().tolist(),
    )
    content_types = st.multiselect(
        "Content type",
        options=df_raw["content_type"].unique().tolist(),
        default=df_raw["content_type"].unique().tolist(),
    )
    months = st.multiselect(
        "Month",
        options=sorted(df_raw["month_num"].unique()),
        default=sorted(df_raw["month_num"].unique()),
        format_func=lambda m: df_raw[df_raw["month_num"] == m]["month"].iloc[0],
    )
    st.markdown("---")
    st.caption("Social Media Performance Dashboard · Built by Manal Munawwar")

# ── Filter data ───────────────────────────────────────────────────────────────
df = df_raw[
    df_raw["platform"].isin(platforms) &
    df_raw["content_type"].isin(content_types) &
    df_raw["month_num"].isin(months)
]

if df.empty:
    st.warning("No data matches your filters. Please adjust the sidebar.")
    st.stop()

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("## Social Media Performance Dashboard")
st.markdown(f"<span style='color:#6B7280;font-size:14px'>Analysing **{len(df):,}** posts · Luxury fashion brand · 2024</span>", unsafe_allow_html=True)
st.markdown("---")

# ── KPI Cards ─────────────────────────────────────────────────────────────────
kpis = kpi_summary(df)
k1, k2, k3, k4, k5 = st.columns(5)

def kpi_card(col, label, value, sub=""):
    col.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">{label}</div>
        <div class="kpi-value">{value}</div>
        <div class="kpi-sub">{sub}</div>
    </div>""", unsafe_allow_html=True)

kpi_card(k1, "Total reach", f"{kpis['total_reach']:,.0f}", "across all posts")
kpi_card(k2, "Avg engagement rate", f"{kpis['avg_eng_rate']}%", "likes + comments + shares")
kpi_card(k3, "Total posts", f"{kpis['total_posts']:,}", "published")
kpi_card(k4, "Best platform", kpis['best_platform'], "by avg engagement")
kpi_card(k5, "Best content type", kpis['best_content'].split()[0] + "…", "by avg engagement")

st.markdown("<br>", unsafe_allow_html=True)

# ── Row 1: Timeline + Content type ───────────────────────────────────────────
col_a, col_b = st.columns([3, 2])

with col_a:
    monthly = monthly_engagement(df)
    st.plotly_chart(engagement_timeline(monthly), use_container_width=True)

with col_b:
    content_perf = content_type_performance(df)
    st.plotly_chart(content_type_bar(content_perf), use_container_width=True)

# ── Row 2: Platform radar + Heatmap ──────────────────────────────────────────
col_c, col_d = st.columns([1, 2])

with col_c:
    plat_comp = platform_comparison(df)
    st.plotly_chart(platform_radar(plat_comp), use_container_width=True)

with col_d:
    heatmap_data = posting_time_heatmap(df)
    st.plotly_chart(heatmap_chart(heatmap_data), use_container_width=True)

# ── Row 3: Scatter ────────────────────────────────────────────────────────────
st.plotly_chart(reach_vs_engagement_scatter(df), use_container_width=True)

# ── Insights ──────────────────────────────────────────────────────────────────
st.markdown("### Key insights")
insights = insight_bullets(df)
for insight in insights:
    st.markdown(f'<div class="insight-card">{insight}</div>', unsafe_allow_html=True)

# ── Top Posts Table ───────────────────────────────────────────────────────────
st.markdown("### Top 10 posts by engagement rate")
top = top_posts(df)
st.dataframe(
    top.style.format({
        "engagement_rate": "{:.2f}%",
        "reach": "{:,.0f}",
        "likes": "{:,.0f}",
        "comments": "{:,.0f}",
        "shares": "{:,.0f}",
    }).background_gradient(subset=["engagement_rate"], cmap="Blues"),
    use_container_width=True,
    hide_index=True,
)
