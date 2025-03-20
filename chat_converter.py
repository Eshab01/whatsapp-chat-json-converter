import json
import argparse
from datetime import datetime

# Set up command-line arguments with defaults
parser = argparse.ArgumentParser(description="Convert chat logs to JSON format.")
parser.add_argument("input_file", nargs="?", default="chat.txt", help="Path to the input chat file (default: chat.txt)")
parser.add_argument("output_file", nargs="?", default="chat.json", help="Path to the output JSON file (default: chat.json)")
args = parser.parse_args()

# Read the chat file
with open(args.input_file, "r", encoding="utf-8") as file:
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
with open(args.output_file, "w", encoding="utf-8") as json_file:
    json.dump(chat_data, json_file, indent=4, ensure_ascii=False)

print(f"Chat successfully converted to JSON and saved to {args.output_file}!")
