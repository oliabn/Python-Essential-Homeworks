"""task3
Створіть список товарів в інтернет-магазині.
Серіалізуйте його за допомогою pickle та збережіть у JSON.
"""

import pickle

items = ["quadcopter engines", "speed regulators", "propellers",
         "power splitter 3.5 mm", "boards", "batteries",
         "charger", "radio control device", "wires", "rame"]

with open('items.json', 'wb') as file:
    b_items = pickle.dumps(items)
    file.write(b_items)

with open('items.json', 'rb') as file:
    print(pickle.load(file))
