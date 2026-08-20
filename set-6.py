# Products belonging to different categories.
category1 = {"Laptop", "Mouse", "Keyboard", "Monitor"}
category2 = {"Keyboard", "Monitor", "Printer", "Scanner"}

common_products = category1.intersection(category2)

print("Products belonging to both categories:", common_products)


# Q25. Represent friends of two users using sets.
user1 = {"Amit", "Rahul", "Sneha", "Priya", "Kiran"}
user2 = {"Sneha", "Priya", "Rohan", "Neha", "Kiran"}

mutual_friends = user1.intersection(user2)
unique_user1 = user1.difference(user2)
unique_user2 = user2.difference(user1)
total_unique = user1.union(user2)

print("\nQ25. Mutual friends:", mutual_friends)
print("Friends unique to User 1:", unique_user1)
print("Friends unique to User 2:", unique_user2)
print("Total unique friends:", total_unique)