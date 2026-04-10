import pandas as pd
import numpy as np


def load_data(path="data/posts.csv"):
    df = pd.read_csv(path, parse_dates=["date"])
    return df


def kpi_summary(df):
    """Returns top-level KPIs for the dashboard header."""
    total_reach = df["reach"].sum()
    avg_eng_rate = df["engagement_rate"].mean()
    total_posts = len(df)
    best_platform = df.groupby("platform")["engagement_rate"].mean().idxmax()
    best_content = df.groupby("content_type")["engagement_rate"].mean().idxmax()
    total_interactions = (df["likes"] + df["comments"] + df["shares"]).sum()

    return {
        "total_reach": total_reach,
        "avg_eng_rate": round(avg_eng_rate, 2),
        "total_posts": total_posts,
        "best_platform": best_platform,
        "best_content": best_content,
        "total_interactions": total_interactions,
    }


def monthly_engagement(df):
    """Monthly avg engagement rate by platform."""
    monthly = (
        df.groupby(["month_num", "month", "platform"])["engagement_rate"]
        .mean()
        .reset_index()
        .sort_values("month_num")
    )
    return monthly


def content_type_performance(df):
    """Avg engagement rate and reach per content type."""
    perf = (
        df.groupby("content_type")
        .agg(
            avg_engagement=("engagement_rate", "mean"),
            avg_reach=("reach", "mean"),
            total_posts=("engagement_rate", "count"),
        )
        .round(2)
        .reset_index()
        .sort_values("avg_engagement", ascending=False)
    )
    return perf


def platform_comparison(df):
    """Compare platforms across key metrics."""
    comp = (
        df.groupby("platform")
        .agg(
            avg_engagement=("engagement_rate", "mean"),
            avg_reach=("reach", "mean"),
            avg_likes=("likes", "mean"),
            total_posts=("engagement_rate", "count"),
        )
        .round(2)
        .reset_index()
    )
    return comp


def posting_time_heatmap(df):
    """Posts count and avg engagement by day × hour."""
    days_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    heatmap = (
        df.groupby(["day_of_week", "hour"])["engagement_rate"]
        .mean()
        .reset_index()
    )
    heatmap["day_of_week"] = pd.Categorical(heatmap["day_of_week"], categories=days_order, ordered=True)
    heatmap = heatmap.sort_values("day_of_week")
    return heatmap


def top_posts(df, n=10):
    """Top n posts by engagement rate."""
    top = (
        df.nlargest(n, "engagement_rate")[
            ["date", "platform", "content_type", "reach", "likes", "comments", "shares", "engagement_rate"]
        ]
        .reset_index(drop=True)
    )
    top["date"] = top["date"].dt.strftime("%d %b %Y")
    return top


def insight_bullets(df):
    """Auto-generate 4 insight strings from the data."""
    kpis = kpi_summary(df)
    content_perf = content_type_performance(df)
    top_content = content_perf.iloc[0]
    bottom_content = content_perf.iloc[-1]

    best_month = (
        df.groupby(["month_num", "month"])["engagement_rate"]
        .mean()
        .reset_index()
        .sort_values("engagement_rate", ascending=False)
        .iloc[0]
    )

    best_day = (
        df.groupby("day_of_week")["engagement_rate"]
        .mean()
        .idxmax()
    )

    return [
        f"**{top_content['content_type']}** posts drive the highest engagement at {top_content['avg_engagement']:.1f}% — prioritise this format.",
        f"**{kpis['best_platform']}** is your best-performing platform by average engagement rate.",
        f"**{best_month['month']}** is your peak month — likely driven by seasonal campaign activity.",
        f"**{best_day}** consistently delivers above-average engagement. Schedule key posts accordingly.",
        f"**{bottom_content['content_type']}** posts underperform at {bottom_content['avg_engagement']:.1f}% — consider refreshing the format or reducing frequency.",
    ]
