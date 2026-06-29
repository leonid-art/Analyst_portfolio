# Python — EDA и визуализация

Exploratory Data Analysis стартап-экосистемы на Python: загрузка CSV, статистика, графики matplotlib/seaborn и интерактивные chart-ы plotly.

## Файлы

| Файл | Описание |
|------|----------|
| [startup_analysis.ipynb](./startup_analysis.ipynb) | Jupyter Notebook с полным анализом |
| [generate_data.py](./generate_data.py) | Генератор синтетических CSV (схема = SQL-проект) |
| [requirements.txt](./requirements.txt) | Зависимости Python |

---

## Что внутри ноутбука

1. Загрузка данных из `data/`
2. Общая статистика (KPI)
3. Финансирование по странам (bar chart)
4. Распределение по статусу и категории (pie + bar)
5. Динамика раундов по годам (combo chart)
6. Сегментация активности фондов (plotly bar)
7. Анализ сделок M&A (bar + line)
8. Интерактивная choropleth-карта финансирования
9. Выводы

---

## Запуск

```bash
cd Python
pip install -r requirements.txt

# Сгенерировать CSV (если ещё не созданы)
python generate_data.py

# Запустить Jupyter
jupyter notebook startup_analysis.ipynb
```

---

## Связь с другими проектами

- **SQL** — та же схема БД, запросы в [sql_tasks.sql](../SQL/sql_tasks.sql)
- **Power BI / Tableau** — те же CSV в [data/](../data/)

---

[← Вернуться к портфолио](../README.md)
