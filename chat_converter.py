import json

with open("chat.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

chat_data = []
for line in lines:
    if line.strip():
        try:
            timestamp, user, message = line.split(":", 2)
            chat_data.append({
                "timestamp": timestamp.strip(),
                "user": user.strip(),
                "message": message.strip()
            })
        except ValueError:
            continue

with open("chat.json", "w", encoding="utf-8") as json_file:
    json.dump(chat_data, json_file, indent=4, ensure_ascii=False)

print("chat successfully converted to JSON!")