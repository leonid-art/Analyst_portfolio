"""Generate sample startup ecosystem data matching SQL schema."""

from __future__ import annotations

import random
from datetime import date, timedelta
from pathlib import Path

import pandas as pd

RANDOM_SEED = 42
DATA_DIR = Path(__file__).resolve().parent.parent / "data"

COUNTRIES = ["USA", "GBR", "DEU", "FRA", "ISR", "CAN", "IND", "CHN", "JPN", "BRA"]
CATEGORIES = ["social", "news", "software", "mobile", "games", "ecommerce", "fintech", "health"]
STATUSES = ["operating", "operating", "operating", "acquired", "ipo", "closed"]
UNIVERSITIES = [
    "Stanford University", "MIT", "Harvard University", "UC Berkeley",
    "Oxford University", "Cambridge University", "ETH Zurich", "Technion",
    "Moscow State University", "HSE University",
]
FIRST_NAMES = ["Alex", "Maria", "John", "Anna", "David", "Elena", "Michael", "Sophia", "James", "Olga"]
LAST_NAMES = ["Smith", "Johnson", "Brown", "Kowalski", "Ivanov", "Lee", "Garcia", "Kim", "Müller", "Petrov"]


def random_date(start: date, end: date) -> date:
    delta = (end - start).days
    return start + timedelta(days=random.randint(0, delta))


def generate_companies(n: int = 120) -> pd.DataFrame:
    rows = []
    for i in range(1, n + 1):
        status = random.choice(STATUSES)
        founded = random_date(date(2005, 1, 1), date(2020, 12, 31))
        closed = None
        if status == "closed":
            closed = random_date(founded, date(2023, 12, 31))
        rows.append({
            "id": i,
            "name": f"Startup_{i:03d}",
            "category_code": random.choice(CATEGORIES),
            "status": status,
            "founded_at": founded.isoformat(),
            "closed_at": closed.isoformat() if closed else None,
            "domain": f"startup{i}.com",
            "twitter_username": f"startup{i}",
            "country_code": random.choice(COUNTRIES),
            "investment_rounds": random.randint(0, 8),
            "funding_rounds": random.randint(1, 6),
            "funding_total": round(random.uniform(100_000, 50_000_000), 2),
            "milestones": random.randint(0, 12),
        })
    return pd.DataFrame(rows)


def generate_people(companies: pd.DataFrame, per_company: tuple[int, int] = (2, 8)) -> pd.DataFrame:
    rows = []
    pid = 1
    for _, company in companies.iterrows():
        for _ in range(random.randint(*per_company)):
            rows.append({
                "id": pid,
                "first_name": random.choice(FIRST_NAMES),
                "last_name": random.choice(LAST_NAMES),
                "company_id": company["id"],
                "twitter_username": f"user{pid}",
            })
            pid += 1
    return pd.DataFrame(rows)


def generate_education(people: pd.DataFrame) -> pd.DataFrame:
    rows = []
    eid = 1
    for _, person in people.iterrows():
        if random.random() < 0.85:
            rows.append({
                "id": eid,
                "person_id": person["id"],
                "degree_type": random.choice(["bachelor", "master", "phd", "mba"]),
                "instituition": random.choice(UNIVERSITIES),
                "graduated_at": random_date(date(1995, 1, 1), date(2018, 12, 31)).isoformat(),
            })
            eid += 1
    return pd.DataFrame(rows)


def generate_funds(n: int = 40) -> pd.DataFrame:
    rows = []
    for i in range(1, n + 1):
        rows.append({
            "id": i,
            "name": f"Fund_{i:02d}",
            "founded_at": random_date(date(1990, 1, 1), date(2015, 12, 31)).isoformat(),
            "domain": f"fund{i}.vc",
            "twitter_username": f"fund{i}",
            "country_code": random.choice(COUNTRIES),
            "investment_rounds": random.randint(5, 200),
            "invested_companies": random.randint(1, 150),
            "milestones": random.randint(0, 10),
        })
    return pd.DataFrame(rows)


def generate_funding_rounds(companies: pd.DataFrame) -> pd.DataFrame:
    rows = []
    rid = 1
    round_types = ["seed", "angel", "series-a", "series-b", "series-c"]
    for _, company in companies.iterrows():
        n_rounds = random.randint(1, min(company["funding_rounds"], 5))
        round_dates = sorted(
            random_date(date(2010, 1, 1), date(2023, 12, 31))
            for _ in range(n_rounds)
        )
        for idx, funded_at in enumerate(round_dates):
            rows.append({
                "id": rid,
                "company_id": company["id"],
                "funded_at": funded_at.isoformat(),
                "funding_round_type": random.choice(round_types),
                "raised_amount": round(random.uniform(50_000, 10_000_000), 2),
                "pre_money_valuation": round(random.uniform(500_000, 100_000_000), 2),
                "participants": random.randint(1, 8),
                "is_first_round": 1 if idx == 0 else 0,
                "is_last_round": 1 if idx == n_rounds - 1 else 0,
            })
            rid += 1
    return pd.DataFrame(rows)


def generate_investments(funding_rounds: pd.DataFrame, funds: pd.DataFrame, companies: pd.DataFrame) -> pd.DataFrame:
    rows = []
    iid = 1
    for _, fr in funding_rounds.iterrows():
        for fund_id in random.sample(list(funds["id"]), k=random.randint(1, 3)):
            rows.append({
                "id": iid,
                "funding_round_id": fr["id"],
                "company_id": fr["company_id"],
                "fund_id": fund_id,
            })
            iid += 1
    return pd.DataFrame(rows)


def generate_acquisitions(companies: pd.DataFrame, n: int = 35) -> pd.DataFrame:
    acquired = companies[companies["status"].isin(["acquired", "closed"])].sample(
        n=min(n, len(companies)), random_state=RANDOM_SEED
    )
    acquirers = companies[companies["status"].isin(["operating", "ipo", "acquired"])]
    rows = []
    for i, (_, target) in enumerate(acquired.iterrows(), start=1):
        acquirer = acquirers.sample(1).iloc[0]
        rows.append({
            "id": i,
            "acquiring_company_id": int(acquirer["id"]),
            "acquired_company_id": int(target["id"]),
            "term_code": random.choice(["cash", "stock", "cash_and_stock"]),
            "price_amount": round(random.uniform(100_000, 20_000_000), 2),
            "acquired_at": random_date(date(2010, 1, 1), date(2023, 12, 31)).isoformat(),
        })
    return pd.DataFrame(rows)


def main() -> None:
    random.seed(RANDOM_SEED)
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    companies = generate_companies()
    people = generate_people(companies)
    education = generate_education(people)
    funds = generate_funds()
    funding_rounds = generate_funding_rounds(companies)
    investments = generate_investments(funding_rounds, funds, companies)
    acquisitions = generate_acquisitions(companies)

    datasets = {
        "company": companies,
        "people": people,
        "education": education,
        "fund": funds,
        "funding_round": funding_rounds,
        "investment": investments,
        "acquisition": acquisitions,
    }

    for name, df in datasets.items():
        path = DATA_DIR / f"{name}.csv"
        df.to_csv(path, index=False)
        print(f"Saved {path} ({len(df)} rows)")


if __name__ == "__main__":
    main()
