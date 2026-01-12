from uuid import uuid4
from typing import List, Dict

from services.ingest_service import ingest_menu_item

MENU_ITEMS: List[Dict] = [
    {
        "name": "Vegan Burger",
        "description": "A delicious plant-based burger made with beans and spices.",
        "category": "main_course",
        "diet": "vegan",
        "price": 25.0,
    },
    {
        "name": "Margherita Pizza",
        "description": "Classic pizza with tomato sauce, mozzarella and basil.",
        "category": "main_course",
        "diet": "vegetarian",
        "price": 30.0,
    },
    {
        "name": "Chocolate Cake",
        "description": "Rich chocolate cake with dark cocoa.",
        "category": "dessert",
        "diet": "vegetarian",
        "price": 15.0,
    },
    {
        "name": "Grilled Salmon",
        "description": "Fresh salmon fillet grilled to perfection, served with lemon.",
        "category": "main_course",
        "diet": "omnivore",
        "price": 40.0,
    },
    {
        "name": "Caesar Salad",
        "description": "Crisp romaine lettuce, parmesan, croutons, and Caesar dressing.",
        "category": "appetizer",
        "diet": "vegetarian",
        "price": 18.0,
    },
    {
        "name": "Chicken Tikka Masala",
        "description": "Tender chicken pieces in a creamy spiced tomato sauce.",
        "category": "main_course",
        "diet": "omnivore",
        "price": 35.0,
    },
    {
        "name": "Falafel Wrap",
        "description": "Chickpea falafel with fresh veggies and tahini in a wrap.",
        "category": "main_course",
        "diet": "vegan",
        "price": 22.0,
    },
    {
        "name": "Miso Soup",
        "description": "Traditional Japanese soup with tofu, seaweed, and miso broth.",
        "category": "appetizer",
        "diet": "vegan",
        "price": 12.0,
    },
    {
        "name": "Beef Steak",
        "description": "Juicy grilled beef steak served with garlic butter.",
        "category": "main_course",
        "diet": "omnivore",
        "price": 50.0,
    },
    {
        "name": "Greek Salad",
        "description": "Tomatoes, cucumber, olives, feta cheese, and olive oil.",
        "category": "appetizer",
        "diet": "vegetarian",
        "price": 20.0,
    },
    {
        "name": "Shrimp Pasta",
        "description": "Pasta tossed with shrimp, garlic, and olive oil.",
        "category": "main_course",
        "diet": "omnivore",
        "price": 38.0,
    },
    {
        "name": "Lentil Soup",
        "description": "Hearty soup made with lentils, vegetables, and spices.",
        "category": "appetizer",
        "diet": "vegan",
        "price": 14.0,
    },
    {
        "name": "Tiramisu",
        "description": "Classic Italian dessert with coffee-soaked ladyfingers and mascarpone.",
        "category": "dessert",
        "diet": "vegetarian",
        "price": 17.0,
    },
]

def bulk_ingest_menu(items: List[Dict]):
    for item in items:
        item_id = item.get("id") or str(uuid4())

        ingest_menu_item(
            id=item_id,
            name=item["name"],
            description=item["description"],
            category=item["category"],
            diet=item["diet"],
            price=item["price"],
        )

        print(f"✅ Ingested: {item['name']} ({item_id})")

if __name__ == "__main__":
    print("Starting bulk menu ingestion...\n")
    bulk_ingest_menu(MENU_ITEMS)
    print("\n✅ Bulk ingestion completed.")
