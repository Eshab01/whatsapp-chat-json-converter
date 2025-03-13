# WhatsApp Chat to JSON Converter

A Python script that converts WhatsApp text chat exports into structured JSON format.

## Features
- Parses WhatsApp text chat files (.txt)
- Supports messages with timestamps, sender names, and message content
- Outputs clean, structured JSON for easy further analysis or processing

## Prerequisites
- Python 3.x

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/whatsapp-chat-json-converter.git
   ```
2. Navigate to the directory:
   ```bash
   cd whatsapp-chat-json-converter
   ```
3. Install any required packages (if applicable):
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Export a WhatsApp chat as a .txt file.
2. Run the script with:
   ```bash
   python chat_converter.py <path_to_chat_file.txt>
   ```
3. The script will generate a JSON file with the same name as your chat file.

### Example Output
```json
[
  {
    "date": "01/01/2024",
    "time": "10:45 AM",
    "sender": "John",
    "message": "Happy New Year!"
  },
  {
    "date": "01/01/2024",
    "time": "10:46 AM",
    "sender": "Doe",
    "message": "Happy New Year to you too!"
  }
]
```

## To-Do
- Add support for different date/time formats
- Handle multimedia messages
- Improve error handling

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

## License
This project is licensed under the MIT License.

---

Happy converting! 🚀

