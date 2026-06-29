# Портфолио аналитика данных

Репозиторий с практическими проектами: SQL-аналитика, Python EDA, BI-дашборды (Power BI / Tableau) и решения тестовых заданий в MS Excel.

**GitHub:** [leonid-art/Analyst_portfolio](https://github.com/leonid-art/Analyst_portfolio)

---

## Навыки и инструменты

| Область | Инструменты |
|---------|-------------|
| Работа с данными | SQL (PostgreSQL), Python (pandas), MS Excel |
| SQL | SELECT, JOIN, подзапросы, CTE, агрегации, CASE |
| Python | pandas, matplotlib, seaborn, plotly, Jupyter |
| BI | Power BI (DAX), Tableau, интерактивные дашборды |
| Excel | Формулы, сводные таблицы, визуализация |
| Подход | EDA, структурирование задач, документирование решений |

---

## Проекты

### [SQL — Анализ стартап-экосистемы](./SQL/)

Работа с реляционной базой данных о венчурных инвестициях, компаниях, фондах и сделках M&A.

- [Описание проекта и схема БД](./SQL/README.md)
- [DDL: создание таблиц](./SQL/table_from_task.sql)
- [Решения SQL-задач (23 запроса)](./SQL/sql_tasks.sql)

**Что демонстрирует:** проектирование схемы, JOIN-ы, подзапросы, CTE, бизнес-метрики.

---

### [Python — EDA и визуализация](./Python/)

Exploratory Data Analysis на Python: статистика, графики и интерактивные chart-ы.

- [Jupyter Notebook](./Python/startup_analysis.ipynb)
- [Генератор данных](./Python/generate_data.py)
- [CSV-данные](./data/)

**Что демонстрирует:** pandas, matplotlib, seaborn, plotly, выводы на основе данных.

---

### [Power BI — Дашборд](./PowerBI/)

Интерактивный BI-дашборд: KPI, география, динамика раундов, M&A.

- [Интерактивный дашборд (HTML)](./PowerBI/dashboard.html)
- [Меры DAX](./PowerBI/measures.dax)
- [Инструкция по сборке в Power BI Desktop](./PowerBI/README.md)

---

### [Tableau — Дашборд](./Tableau/)

Структура дашборда и источник данных для Tableau Desktop / Public.

- [Источник данных (.tds)](./Tableau/startup_ecosystem.tds)
- [Инструкция и calculated fields](./Tableau/README.md)

---

### [MS Excel — Тестовые задания](./Excel/)

- [Выполненное ТЗ для аналитика (2026)](./Excel/Выполненное%20ТЗ%20для%20аналитика_2026.xlsx)
- [ТЗ для аналитика (2026)](./Excel/ТЗ%20для%20аналитика_2026.xlsx)
- [Тестовое задание с решением](./Excel/Тестовое%20задание%20с%20решением.xls)

---

## Структура репозитория

```
Analyst_portfolio/
├── README.md
├── data/                  ← CSV-данные (общие для Python, Power BI, Tableau)
├── SQL/
├── Python/
├── PowerBI/
├── Tableau/
└── Excel/
```
