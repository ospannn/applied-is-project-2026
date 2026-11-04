# applied-is-project-2026

Информационная система **«Учёт товаров на складе»** (FastAPI + SQLModel + Streamlit).

## Предметная область
Система хранит товары, их категории и поставщиков, а также журнал движения товаров (приход/расход).

## ER-диаграмма
![ER-диаграмма](docs/er_diagram.png)

Связи: Category 1—N Item, Supplier 1—N Item, Item 1—N StockTransaction.

## Структура проекта
```
app/
  models.py     # ORM-модели SQLModel
  db.py         # engine, init_db(), get_session()
  routers/      # эндпоинты FastAPI (ЛР №3)
frontend/app.py # интерфейс Streamlit
seed.py         # создание БД и тестовые данные
requirements.txt
```

## Запуск
```bash
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Mac/Linux
pip install -r requirements.txt
python seed.py                 # создаёт database.db и наполняет данными
```
