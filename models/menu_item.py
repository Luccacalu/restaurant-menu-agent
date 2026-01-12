from dataclasses import dataclass
from typing import List, Literal

@dataclass
class MenuItem:
    id: str
    name: str
    description: str
    category: Literal["main_course", "dessert", "appetizer"]
    diet: Literal["vegan", "vegetarian", "omnivore"]
    ingredients: List[str]
    price: float
    created_at: str

    def to_text(self) -> str:
        ingredients_text = ", ".join(self.ingredients)

        return f"""
        {self.name}
        Description: {self.description}
        Ingredients: {ingredients_text}
        Category: {self.category}
        Diet: {self.diet}
        Price: ${self.price:.2f}
        Added to menu on: {self.created_at}
        """
