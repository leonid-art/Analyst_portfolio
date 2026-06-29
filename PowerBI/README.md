# Power BI — Дашборд «Стартап-экосистема»

Интерактивный BI-дашборд по данным венчурной экосистемы: KPI, география, динамика раундов, M&A.

## Файлы

| Файл | Описание |
|------|----------|
| [dashboard.html](./dashboard.html) | Интерактивный дашборд (Plotly) — открывается в браузере |
| [build_dashboard.py](./build_dashboard.py) | Скрипт генерации HTML-дашборда |
| [measures.dax](./measures.dax) | Готовые меры DAX для Power BI Desktop |
| [../data/](../data/) | CSV-источники данных |

---

## Структура дашборда

### Страница 1 — Обзор (KPI)
- Общее число компаний
- Суммарное финансирование (млрд $)
- Средний размер раунда (млн $)
- Число сделок M&A
- Количество венчурных фондов

### Страница 2 — Финансирование
- **Bar chart:** топ-10 стран по объёму финансирования
- **Combo chart:** число раундов и сумма привлечённых средств по годам
- **Slicer:** фильтр по категории (`category_code`) и статусу

### Страница 3 — M&A и фонды
- **Pie chart:** распределение компаний по статусу
- **Line chart:** объём сделок M&A по годам
- **Table:** топ фондов по `invested_companies` с сегментацией активности

---

## Как собрать в Power BI Desktop

1. **Импорт данных:** `Get Data → Text/CSV` — загрузите все файлы из [data/](../data/).
2. **Модель данных** — связи между таблицами:

```
company (1) ──< funding_round (N)
company (1) ──< people (N)
people  (1) ──< education (N)
company (1) ──< acquisition (N)  [acquired_company_id]
company (1) ──< acquisition (N)  [acquiring_company_id]
funding_round (1) ──< investment (N)
fund (1) ──< investment (N)
```

3. **Меры:** скопируйте выражения из [measures.dax](./measures.dax) в Power BI.
4. **Визуализации:** повторите структуру из [dashboard.html](./dashboard.html).

---

## Быстрый просмотр (без Power BI)

```bash
pip install pandas plotly
python PowerBI/build_dashboard.py
```

Откройте `PowerBI/dashboard.html` в браузере.

---

[← Вернуться к портфолио](../README.md)
