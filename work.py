users = [
    {"name": "Alice", "role": "admin"},
    {"name": "Bob", "role": "user"},
    {"name": "Charlie", "role": "admin"},
    {"name": "David"},
    {"name": "Eve", "role": "moderator"}]

for i in users:
    try:
        if i["role"] == "admin":
            print(i["name"])
        else:
            print("No")
    except KeyError:
        continue
    