import json
import csv

raw_users = [
    {"id": 1, "name": "Alice", "status": "active", "score": 85},
    {"id": 2, "name": "Bob", "status": "inactive", "score": 42},
    {"id": 3, "name": "Charlie", "status": "active", "score": 91}
]
processed_users = []
for user in raw_users:
    if user["status"] == "active":
        # Add new processed data field
        user["grade"] = "A" if user["score"] >= 90 else "B"
        processed_users.append(user)

print(f"Processed {len(processed_users)} active users.")

with open("processed_results.json", "w") as json_file:
    json.dump(processed_users, json_file, indent=4)
print("Successfully saved to 'processed_results.json'")

if processed_users:
    headers = processed_users[0].keys() 
    
    with open("processed_results.csv", "w", newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(processed_users)
print("Successfully saved to 'processed_results.csv'")