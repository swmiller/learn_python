fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
for i, category in enumerate(dirty_dozen):
    print(f"Category {i}:")
    for j, item in enumerate(category):
        print(f"  {j}: {item}")


print(dirty_dozen[1][1])