import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

def generate_posts(n=500, seed=42):
    np.random.seed(seed)

    platforms = ["Instagram", "TikTok", "Twitter"]
    content_types = ["Product showcase", "Behind the scenes", "Campaign launch", "Influencer collab", "Brand story"]
    platform_weights = [0.45, 0.35, 0.20]

    start_date = datetime(2024, 1, 1)
    dates = [start_date + timedelta(days=np.random.randint(0, 365)) for _ in range(n)]

    platform = np.random.choice(platforms, size=n, p=platform_weights)
    content_type = np.random.choice(content_types, size=n)

    # Reach varies by platform
    reach_base = {"Instagram": 8000, "TikTok": 25000, "Twitter": 3000}
    reach = np.array([
        int(np.random.lognormal(mean=np.log(reach_base[p]), sigma=0.6))
        for p in platform
    ])

    # Engagement rate varies by content type (realistic luxury brand rates)
    eng_rate_base = {
        "Product showcase": 0.038,
        "Behind the scenes": 0.062,
        "Campaign launch": 0.055,
        "Influencer collab": 0.071,
        "Brand story": 0.048,
    }
    eng_rates = np.array([
        max(0.005, np.random.normal(eng_rate_base[ct], 0.015))
        for ct in content_type
    ])

    likes = (reach * eng_rates * np.random.uniform(0.7, 1.0, n)).astype(int)
    comments = (likes * np.random.uniform(0.04, 0.12, n)).astype(int)
    shares = (likes * np.random.uniform(0.02, 0.08, n)).astype(int)
    saves = (likes * np.random.uniform(0.05, 0.20, n)).astype(int)

    # Seasonal boosts: Ramadan (Mar), summer (Jun-Jul), end of year (Nov-Dec)
    month_boosts = {3: 1.4, 6: 1.2, 7: 1.2, 11: 1.3, 12: 1.5}
    for i, d in enumerate(dates):
        boost = month_boosts.get(d.month, 1.0)
        likes[i] = int(likes[i] * boost)
        reach[i] = int(reach[i] * boost)

    df = pd.DataFrame({
        "date": dates,
        "platform": platform,
        "content_type": content_type,
        "reach": reach,
        "likes": likes,
        "comments": comments,
        "shares": shares,
        "saves": saves,
    })

    df["engagement_rate"] = ((df["likes"] + df["comments"] + df["shares"]) / df["reach"] * 100).round(2)
    df["day_of_week"] = df["date"].apply(lambda d: d.strftime("%A"))
    df["hour"] = np.random.choice(range(7, 23), size=n, p=[
        0.02, 0.04, 0.08, 0.12, 0.13, 0.12, 0.10, 0.09, 0.08, 0.07, 0.06, 0.05, 0.02, 0.02, 0.0, 0.0
    ])
    df["month"] = df["date"].apply(lambda d: d.strftime("%b"))
    df["month_num"] = df["date"].apply(lambda d: d.month)
    df = df.sort_values("date").reset_index(drop=True)

    os.makedirs("data", exist_ok=True)
    df.to_csv("data/posts.csv", index=False)
    print(f"Generated {len(df)} posts → data/posts.csv")
    return df


if __name__ == "__main__":
    generate_posts()
