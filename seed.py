"""Наполнение БД тестовыми данными. Запуск: python seed.py"""
from sqlmodel import Session, select

from app.db import engine, init_db
from app.models import Category, Item, StockTransaction, Supplier


def seed() -> None:
    init_db()
    with Session(engine) as session:
        if session.exec(select(Category)).first():
            print("База уже содержит данные — посев пропущен.")
            return

        categories = [
            Category(name="Электроника", description="Гаджеты и аксессуары"),
            Category(name="Канцелярия", description="Бумага, ручки, блокноты"),
            Category(name="Бытовая техника", description="Техника для дома"),
            Category(name="Инструменты", description="Ручной и электроинструмент"),
        ]
        suppliers = [
            Supplier(name="ТОО «ТехноСнаб»", phone="+7 701 111 22 33", email="sales@technosnab.kz"),
            Supplier(name="ИП Офис-Плюс", phone="+7 702 222 33 44", email="info@officeplus.kz"),
            Supplier(name="ТОО «ДомМаркет»", phone="+7 707 333 44 55", email="order@dommarket.kz"),
        ]
        session.add_all(categories + suppliers)
        session.commit()
        for obj in categories + suppliers:
            session.refresh(obj)

        el, st, ap, tl = categories
        s1, s2, s3 = suppliers
        items = [
            Item(name="Наушники беспроводные", sku="EL-001", price=15990, quantity=40, category_id=el.id, supplier_id=s1.id),
            Item(name="Зарядное устройство 65W", sku="EL-002", price=8990, quantity=75, category_id=el.id, supplier_id=s1.id),
            Item(name="Бумага А4 (500 л.)", sku="ST-001", price=2490, quantity=300, category_id=st.id, supplier_id=s2.id),
            Item(name="Ручка шариковая синяя", sku="ST-002", price=120, quantity=1500, category_id=st.id, supplier_id=s2.id),
            Item(name="Чайник электрический", sku="AP-001", price=11990, quantity=25, category_id=ap.id, supplier_id=s3.id),
            Item(name="Пылесос вертикальный", sku="AP-002", price=45990, quantity=12, category_id=ap.id, supplier_id=s3.id),
            Item(name="Шуруповёрт аккумуляторный", sku="TL-001", price=27990, quantity=18, category_id=tl.id, supplier_id=s3.id),
        ]
        session.add_all(items)
        session.commit()
        for it in items:
            session.refresh(it)

        transactions = [
            StockTransaction(operation="IN", amount=50, item_id=items[0].id),
            StockTransaction(operation="OUT", amount=10, item_id=items[0].id),
            StockTransaction(operation="IN", amount=100, item_id=items[2].id),
            StockTransaction(operation="OUT", amount=20, item_id=items[2].id),
            StockTransaction(operation="IN", amount=15, item_id=items[4].id),
        ]
        session.add_all(transactions)
        session.commit()
        print("Готово: добавлено "
              f"{len(categories)} категорий, {len(suppliers)} поставщиков, "
              f"{len(items)} товаров, {len(transactions)} операций.")


if __name__ == "__main__":
    seed()
