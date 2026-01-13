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
        "ingredients": ["black bean patty", "vegan bun", "lettuce", "tomato", "onion", "vegan mayo", "spices"]
    },
    {
        "name": "Margherita Pizza",
        "description": "Classic pizza with tomato sauce, mozzarella and basil.",
        "category": "main_course",
        "diet": "vegetarian",
        "price": 30.0,
        "ingredients": ["pizza dough", "tomato sauce", "mozzarella cheese", "fresh basil", "olive oil"]
    },
    {
        "name": "Chocolate Cake",
        "description": "Rich chocolate cake with dark cocoa.",
        "category": "dessert",
        "diet": "vegetarian",
        "price": 15.0,
        "ingredients": ["flour", "sugar", "dark cocoa powder", "eggs", "butter", "baking powder", "vanilla extract"]
    },
    {
        "name": "Rice & Bean Paella",
        "description": "Spanish-style vegan paella with rice, beans, bell peppers, and saffron.",
        "category": "main_course",
        "diet": "vegan",
        "price": 28.0,
        "ingredients": ["bomba rice", "white beans", "red bell peppers", "saffron", "vegetable broth", "garlic", "smoked paprika"]
    },
    {
        "name": "Brazilian Rice & Beans",
        "description": "Classic Brazilian dish with white rice, black beans, garlic, and herbs.",
        "category": "main_course",
        "diet": "vegan",
        "price": 26.0,
        "ingredients": ["long grain white rice", "black beans", "garlic", "onion", "bay leaves", "fresh parsley", "olive oil"]
    },
    {
        "name": "Cuban Rice & Beans",
        "description": "Cuban-style rice with black beans, cumin, and sweet peppers.",
        "category": "main_course",
        "diet": "vegan",
        "price": 27.0,
        "ingredients": ["white rice", "black beans", "green bell peppers", "cumin", "oregano", "onion", "garlic"]
    },
    {
        "name": "Mexican Rice & Beans Bowl",
        "description": "Rice and pinto beans with corn, avocado, and tomato salsa.",
        "category": "main_course",
        "diet": "vegan",
        "price": 25.0,
        "ingredients": ["brown rice", "pinto beans", "sweet corn", "avocado", "tomato salsa", "cilantro", "lime"]
    },
    {
        "name": "Moroccan Rice & Chickpeas",
        "description": "Fragrant rice with chickpeas, raisins, and Moroccan spices.",
        "category": "main_course",
        "diet": "vegan",
        "price": 29.0,
        "ingredients": ["basmati rice", "chickpeas", "raisins", "turmeric", "cinnamon", "coriander", "toasted almonds"]
    },
    {
        "name": "Lemon Herb Rice Pilaf",
        "description": "Fluffy rice pilaf with lemon zest, parsley, and olive oil.",
        "category": "main_course",
        "diet": "vegan",
        "price": 24.0,
        "ingredients": ["long grain rice", "lemon zest", "fresh parsley", "vegetable stock", "olive oil", "shallots"]
    },
    {
        "name": "Wild Mushroom Rice Risotto",
        "description": "Creamy vegan risotto with wild mushrooms and white wine.",
        "category": "main_course",
        "diet": "vegan",
        "price": 32.0,
        "ingredients": ["arborio rice", "porcini mushrooms", "shiitake mushrooms", "dry white wine", "vegetable broth", "nutritional yeast", "garlic"]
    },
    {
        "name": "Thai Coconut Rice",
        "description": "Jasmine rice cooked in coconut milk with lemongrass and fresh herbs.",
        "category": "main_course",
        "diet": "vegan",
        "price": 26.0,
        "ingredients": ["jasmine rice", "coconut milk", "lemongrass", "ginger", "fresh cilantro", "thai basil"]
    },
    {
        "name": "Roasted Veggie Rice Bowl",
        "description": "Rice bowl with roasted zucchini, bell peppers, carrots, and olive oil.",
        "category": "main_course",
        "diet": "vegan",
        "price": 27.0,
        "ingredients": ["white rice", "zucchini", "red bell peppers", "carrots", "olive oil", "dried oregano", "sea salt"]
    },
    {
        "name": "Saffron Rice with Peas",
        "description": "Golden saffron rice with sweet peas and a touch of garlic.",
        "category": "main_course",
        "diet": "vegan",
        "price": 30.0,
        "ingredients": ["basmati rice", "saffron threads", "green peas", "garlic", "vegetable bouillon", "onion"]
    },
    {
        "name": "Grilled Salmon",
        "description": "Fresh salmon fillet grilled to perfection, served with lemon.",
        "category": "main_course",
        "diet": "omnivore",
        "price": 40.0,
        "ingredients": ["salmon fillet", "lemon slices", "olive oil", "black pepper", "sea salt", "fresh dill"]
    },
    {
        "name": "Caesar Salad",
        "description": "Crisp romaine lettuce, parmesan, croutons, and Caesar dressing.",
        "category": "appetizer",
        "diet": "vegetarian",
        "price": 18.0,
        "ingredients": ["romaine lettuce", "parmesan cheese", "croutons", "vegetarian caesar dressing", "black pepper"]
    },
    {
        "name": "Chicken Tikka Masala",
        "description": "Tender chicken pieces in a creamy spiced tomato sauce.",
        "category": "main_course",
        "diet": "omnivore",
        "price": 35.0,
        "ingredients": ["chicken breast", "tomato purée", "heavy cream", "ginger", "garlic", "garam masala", "turmeric", "cumin"]
    },
    {
        "name": "Falafel Wrap",
        "description": "Chickpea falafel with fresh veggies and tahini in a wrap.",
        "category": "main_course",
        "diet": "vegan",
        "price": 22.0,
        "ingredients": ["chickpea falafel", "tortilla wrap", "cucumber", "tomato", "pickled onions", "tahini sauce"]
    },
    {
        "name": "Miso Soup",
        "description": "Traditional Japanese soup with tofu, seaweed, and miso broth.",
        "category": "appetizer",
        "diet": "vegan",
        "price": 12.0,
        "ingredients": ["miso paste", "firm tofu", "wakame seaweed", "vegetable dashi", "green onions"]
    },
    {
        "name": "Beef Steak",
        "description": "Juicy grilled beef steak served with garlic butter.",
        "category": "main_course",
        "diet": "omnivore",
        "price": 50.0,
        "ingredients": ["beef sirloin", "unsalted butter", "garlic cloves", "fresh rosemary", "salt", "cracked pepper"]
    },
    {
        "name": "Greek Salad",
        "description": "Tomatoes, cucumber, olives, feta cheese, and olive oil.",
        "category": "appetizer",
        "diet": "vegetarian",
        "price": 20.0,
        "ingredients": ["vine tomatoes", "cucumber", "kalamata olives", "feta cheese", "red onion", "extra virgin olive oil", "dried oregano"]
    },
    {
        "name": "Shrimp Pasta",
        "description": "Pasta tossed with shrimp, garlic, and olive oil.",
        "category": "main_course",
        "diet": "omnivore",
        "price": 38.0,
        "ingredients": ["linguine pasta", "shrimp", "garlic", "extra virgin olive oil", "red pepper flakes", "fresh parsley", "lemon juice"]
    },
    {
        "name": "Lentil Soup",
        "description": "Hearty soup made with lentils, vegetables, and spices.",
        "category": "appetizer",
        "diet": "vegan",
        "price": 14.0,
        "ingredients": ["brown lentils", "carrots", "celery", "onion", "vegetable stock", "cumin", "spinach"]
    },
    {
        "name": "Tiramisu",
        "description": "Classic Italian dessert with coffee-soaked ladyfingers and mascarpone.",
        "category": "dessert",
        "diet": "vegetarian",
        "price": 17.0,
        "ingredients": ["ladyfinger biscuits", "espresso coffee", "mascarpone cheese", "eggs", "sugar", "cocoa powder"]
    }
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
            ingredients=item.get("ingredients", [])
        )

        print(f"✅ Ingested: {item['name']} ({item_id})")

if __name__ == "__main__":
    print("Starting bulk menu ingestion...\n")
    bulk_ingest_menu(MENU_ITEMS)
    print("\n✅ Bulk ingestion completed.")
