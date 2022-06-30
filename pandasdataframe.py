import pandas as pd

cafe = pd.DataFrame({
    "category": ["coffee", "pizza", "coffee", "dessert", "pizza"],
    "price": [2.7, 6.8, 4.1, 5.4, 8.2]
}) 

print(cafe.pivot_table(columns='category', values='price', aggfunc='sum'))