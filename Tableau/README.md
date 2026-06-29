# Tableau — Дашборд «Стартап-экосистема»

Интерактивный дашборд в Tableau Desktop на тех же данных, что используются в SQL- и Python-проектах.

## Файлы

| Файл | Описание |
|------|----------|
| [startup_ecosystem.tds](./startup_ecosystem.tds) | Источник данных Tableau (CSV) |
| [../data/](../data/) | CSV-файлы: company, funding_round, acquisition, fund и др. |
| [../PowerBI/dashboard.html](../PowerBI/dashboard.html) | HTML-версия дашборда для просмотра без Tableau |

---

## Структура дашборда

### Лист 1 — Overview
| Визуализация | Поля | Тип |
|-------------|------|-----|
| KPI Cards | `COUNTD(company.id)`, `SUM(funding_total)`, `COUNT(acquisition.id)` | BANs |
| Funding by Country | `country_code` × `SUM(funding_total)` | Horizontal bar |
| Status Distribution | `status` × `COUNT(id)` | Pie chart |

### Лист 2 — Funding Trends
| Визуализация | Поля | Тип |
|-------------|------|-----|
| Rounds by Year | `YEAR(funded_at)` × `COUNT(id)` | Bar |
| Raised Amount Trend | `YEAR(funded_at)` × `SUM(raised_amount)` | Line (dual axis) |
| Category Filter | `category_code` | Slicer / Filter |

### Лист 3 — M&A & Funds
| Визуализация | Поля | Тип |
|-------------|------|-----|
| M&A by Payment Type | `term_code` × `SUM(price_amount)` | Stacked bar |
| M&A Timeline | `YEAR(acquired_at)` × `SUM(price_amount)` | Area chart |
| Fund Activity | Calculated field `Fund Activity` × `AVG(investment_rounds)` | Bar |

---

## Calculated Fields (Tableau)

**Fund Activity:**
```
IF [invested_companies] >= 100 THEN "high_activity"
ELSEIF [invested_companies] >= 20 THEN "middle_activity"
ELSE "low_activity"
END
```

**Funding ($M):**
```
SUM([funding_total]) / 1000000
```

**M&A Volume ($M):**
```
SUM([price_amount]) / 1000000
```

---

## Как открыть в Tableau Desktop

1. Скачайте [Tableau Public](https://public.tableau.com/) или используйте Tableau Desktop.
2. **Data → New Data Source → More → Tableau Data Source** → выберите [startup_ecosystem.tds](./startup_ecosystem.tds).
3. Добавьте остальные CSV из [data/](../data/) и настройте связи (Relationships):
   - `company.id` = `funding_round.company_id`
   - `company.id` = `acquisition.acquired_company_id`
   - `fund.id` = `investment.fund_id`
4. Создайте листы по структуре выше.
5. Соберите Dashboard и опубликуйте на Tableau Public (опционально).

---

## Альтернатива без Tableau

Интерактивный HTML-дашборд доступен в [PowerBI/dashboard.html](../PowerBI/dashboard.html) — открывается в любом браузере.

---

[← Вернуться к портфолио](../README.md)
