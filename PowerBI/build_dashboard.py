"""Build interactive HTML dashboard for startup ecosystem (Plotly)."""

from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
OUTPUT = Path(__file__).resolve().parent / "dashboard.html"


def load_data() -> dict[str, pd.DataFrame]:
    return {
        "company": pd.read_csv(DATA_DIR / "company.csv", parse_dates=["founded_at"]),
        "funding_round": pd.read_csv(DATA_DIR / "funding_round.csv", parse_dates=["funded_at"]),
        "acquisition": pd.read_csv(DATA_DIR / "acquisition.csv", parse_dates=["acquired_at"]),
        "fund": pd.read_csv(DATA_DIR / "fund.csv"),
    }


def kpi_row(company, funding_round, acquisition, fund) -> go.Figure:
    metrics = [
        ("Компаний", len(company)),
        ("Финансирование, млрд $", round(company["funding_total"].sum() / 1e9, 2)),
        ("Средний раунд, млн $", round(funding_round["raised_amount"].mean() / 1e6, 2)),
        ("Сделок M&A", len(acquisition)),
        ("Фондов", len(fund)),
    ]
    fig = make_subplots(rows=1, cols=5, specs=[[{"type": "indicator"}] * 5])
    for i, (label, value) in enumerate(metrics, start=1):
        fig.add_trace(go.Indicator(mode="number", value=value, title={"text": label}), row=1, col=i)
    fig.update_layout(height=160, margin=dict(t=50, b=10, l=10, r=10), title="KPI — Стартап-экосистема")
    return fig


def main() -> None:
    data = load_data()
    company = data["company"]
    funding_round = data["funding_round"]
    acquisition = data["acquisition"]
    fund = data["fund"]

    by_country = (
        company.groupby("country_code", as_index=False)["funding_total"]
        .sum()
        .sort_values("funding_total", ascending=True)
        .tail(10)
    )
    by_country["funding_m"] = by_country["funding_total"] / 1e6

    funding_round["year"] = funding_round["funded_at"].dt.year
    by_year = funding_round.groupby("year", as_index=False).agg(
        rounds=("id", "count"),
        raised=("raised_amount", "sum"),
    )
    by_year["raised_m"] = by_year["raised"] / 1e6

    status_dist = company["status"].value_counts().reset_index()
    status_dist.columns = ["status", "count"]

    acquisition["year"] = acquisition["acquired_at"].dt.year
    mna_year = acquisition.groupby("year", as_index=False)["price_amount"].sum()
    mna_year["price_m"] = mna_year["price_amount"] / 1e6

    fig1 = px.bar(
        by_country, x="funding_m", y="country_code", orientation="h",
        title="Топ-10 стран по финансированию (млн $)",
        labels={"funding_m": "млн $", "country_code": "Страна"},
    )
    fig2 = make_subplots(specs=[[{"secondary_y": True}]])
    fig2.add_trace(go.Bar(x=by_year["year"], y=by_year["rounds"], name="Раунды"), secondary_y=False)
    fig2.add_trace(go.Scatter(x=by_year["year"], y=by_year["raised_m"], name="Сумма, млн $", mode="lines+markers"), secondary_y=True)
    fig2.update_layout(title="Динамика раундов финансирования")
    fig2.update_yaxes(title_text="Число раундов", secondary_y=False)
    fig2.update_yaxes(title_text="млн $", secondary_y=True)

    fig3 = px.pie(status_dist, names="status", values="count", title="Распределение по статусу")
    fig4 = px.line(mna_year, x="year", y="price_m", markers=True, title="Объём сделок M&A по годам (млн $)")

    kpi = kpi_row(company, funding_round, acquisition, fund)

    html_parts = [
        "<html><head><meta charset='utf-8'><title>Startup Ecosystem Dashboard</title>",
        "<style>body{font-family:Segoe UI,Arial,sans-serif;margin:24px;background:#f8f9fa;}",
        "h1{color:#1a1a2e;} .chart{margin-bottom:32px;background:#fff;padding:16px;border-radius:8px;box-shadow:0 1px 4px rgba(0,0,0,.08);}</style></head><body>",
        "<h1>Дашборд: Стартап-экосистема</h1>",
        "<p>Интерактивная BI-визуализация на Plotly. Данные: <code>data/</code></p>",
    ]
    for fig in [kpi, fig1, fig2, fig3, fig4]:
        html_parts.append(f"<div class='chart'>{fig.to_html(full_html=False, include_plotlyjs='cdn')}</div>")
    html_parts.append("</body></html>")

    OUTPUT.write_text("\n".join(html_parts), encoding="utf-8")
    print(f"Dashboard saved to {OUTPUT}")


if __name__ == "__main__":
    main()
