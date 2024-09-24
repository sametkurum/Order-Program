# ORDER PROGRAM
menu = {"doner": 30.00,
         "kebap": 100.00,
         "baklava": 50.00,
         "simit": 10.00}

ordered = []
total = 0

for key, value in menu.items():
    print(f"{key:7}: {value:.2f}TL")

while True:
    food = input("what do you want to (q to quit): ")

    if food.lower() == "q":
        break

    elif food not in menu:
        print("!!you wrote wrong!!")

    elif menu.get(food) is not None:
        ordered.append(food)

for food in ordered:
    total += menu.get(food)
    print(food,end=" ")

print()
print("Total:" ,total, "TL")