import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Brand colour palette
PLATFORM_COLORS = {
    "Instagram": "#C13584",
    "TikTok": "#010101",
    "Twitter": "#1DA1F2",
}

CONTENT_COLORS = px.colors.qualitative.Set2

CHART_FONT = dict(family="Inter, sans-serif", size=13, color="#374151")
LAYOUT_BASE = dict(
    font=CHART_FONT,
    plot_bgcolor="white",
    paper_bgcolor="white",
    margin=dict(l=20, r=20, t=40, b=20),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
)


def engagement_timeline(monthly_df):
    fig = px.line(
        monthly_df,
        x="month",
        y="avg_engagement",
        color="platform",
        color_discrete_map=PLATFORM_COLORS,
        markers=True,
        labels={"avg_engagement": "Avg engagement rate (%)", "month": "Month", "platform": "Platform"},
        title="Monthly engagement rate by platform",
    )
    fig.update_traces(line_width=2.5, marker_size=7)
    fig.update_layout(**LAYOUT_BASE)
    fig.update_yaxes(ticksuffix="%", gridcolor="#F3F4F6")
    fig.update_xaxes(gridcolor="#F3F4F6")
    return fig


def content_type_bar(content_df):
    fig = px.bar(
        content_df,
        x="content_type",
        y="avg_engagement",
        color="content_type",
        color_discrete_sequence=CONTENT_COLORS,
        text="avg_engagement",
        labels={"avg_engagement": "Avg engagement rate (%)", "content_type": "Content type"},
        title="Engagement rate by content type",
    )
    fig.update_traces(
        texttemplate="%{text:.1f}%",
        textposition="outside",
        marker_line_width=0,
    )
    fig.update_layout(**LAYOUT_BASE, showlegend=False)
    fig.update_yaxes(ticksuffix="%", gridcolor="#F3F4F6")
    fig.update_xaxes(tickangle=-20)
    return fig


def platform_radar(platform_df):
    """Normalised radar chart comparing platforms across 3 metrics."""
    metrics = ["avg_engagement", "avg_reach", "avg_likes"]
    labels = ["Engagement rate", "Avg reach", "Avg likes"]

    # Normalise 0–1
    norm_df = platform_df.copy()
    for m in metrics:
        norm_df[m] = (norm_df[m] - norm_df[m].min()) / (norm_df[m].max() - norm_df[m].min() + 1e-9)

    fig = go.Figure()
    for _, row in norm_df.iterrows():
        values = [row[m] for m in metrics]
        values += [values[0]]  # close the polygon
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=labels + [labels[0]],
            fill="toself",
            name=row["platform"],
            line_color=PLATFORM_COLORS.get(row["platform"], "#888"),
            opacity=0.7,
        ))

    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
        title="Platform comparison (normalised)",
        font=CHART_FONT,
        paper_bgcolor="white",
        margin=dict(l=40, r=40, t=60, b=20),
        legend=dict(orientation="h", y=-0.1),
    )
    return fig


def heatmap_chart(heatmap_df):
    pivot = heatmap_df.pivot_table(
        index="day_of_week", columns="hour", values="engagement_rate", aggfunc="mean"
    ).fillna(0)

    fig = px.imshow(
        pivot,
        color_continuous_scale="Blues",
        labels=dict(x="Hour of day", y="Day of week", color="Engagement %"),
        title="Best times to post (avg engagement rate)",
        aspect="auto",
    )
    fig.update_layout(
        font=CHART_FONT,
        paper_bgcolor="white",
        plot_bgcolor="white",
        margin=dict(l=20, r=20, t=40, b=20),
        coloraxis_colorbar=dict(ticksuffix="%"),
    )
    return fig


def reach_vs_engagement_scatter(df):
    sample = df.sample(min(300, len(df)), random_state=1)
    fig = px.scatter(
        sample,
        x="reach",
        y="engagement_rate",
        color="platform",
        size="likes",
        hover_data=["content_type", "date"],
        color_discrete_map=PLATFORM_COLORS,
        labels={"reach": "Post reach", "engagement_rate": "Engagement rate (%)", "platform": "Platform"},
        title="Reach vs engagement rate",
        opacity=0.7,
    )
    fig.update_layout(**LAYOUT_BASE)
    fig.update_yaxes(ticksuffix="%", gridcolor="#F3F4F6")
    fig.update_xaxes(gridcolor="#F3F4F6")
    return fig
