import json
from datetime import datetime

# Read the chat file
with open("chat.txt", "r", encoding="utf-8") as file:
    lines = [line.strip() for line in file if line.strip()]

# Process each line and extract chat data
chat_data = []
for line in lines:
    parts = line.split(":", 2)
    if len(parts) == 3:
        timestamp, user, message = map(str.strip, parts)
        
        # Convert timestamp to a standard datetime format
        try:
            formatted_timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S").isoformat()
        except ValueError:
            formatted_timestamp = timestamp  # Fallback to original if format is unknown
        
        chat_data.append({"timestamp": formatted_timestamp, "user": user, "message": message})
    else:
        print(f"Skipping invalid line: {line}")

# Save to JSON file
with open("chat.json", "w", encoding="utf-8") as json_file:
    json.dump(chat_data, json_file, indent=4, ensure_ascii=False)

print("Chat successfully converted to JSON!")
