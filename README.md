# University Chatbot

A simple chatbot implementation designed to handle university-related queries. This project was created as part of a Data Science Internship assignment to demonstrate natural language processing and conversational AI capabilities.

## Features

- Handles common university-related queries about:
  - Fees and tuition
  - Admission process
  - University working hours
- Simple pattern matching for intent recognition
- Extensible architecture for adding new intents and responses
- Proper error handling and logging
- Easy to setup and run

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/university-chatbot.git
cd university-chatbot
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
- On Windows:
  ```bash
  .\venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

4. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the chatbot:
```bash
python -m src.chatbot
```

2. Start chatting with the bot! Example interactions:
```
You: What are the university fees?
Chatbot: The fees for courses vary depending on the program and level of study. Could you specify which program you're interested in?

You: How can I apply for admission?
Chatbot: Our admissions process varies depending on the program. Would you like more information about undergraduate or graduate admissions?
```

3. Type 'exit' or 'quit' to end the conversation.

## Project Structure

```
university_chatbot/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── chatbot.py
│   ├── config.py
│   └── data/
│       └── intents.json
└── tests/
    ├── __init__.py
    └── test_chatbot.py
```

## Extending the Chatbot

To add new intents and responses, modify the `src/data/intents.json` file. The format is:

```json
{
    "intent_name": {
        "patterns": ["pattern1", "pattern2"],
        "response": "Response for this intent"
    }
}
```

## Testing

Run the tests using pytest:
```bash
pytest tests/
```

## Future Improvements

- Implement more sophisticated NLP techniques for intent recognition
- Add support for multi-turn conversations
- Integrate with a database for dynamic responses
- Add support for multiple languages
- Implement sentiment analysis
- Add API endpoint for web integration

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Created as part of Data Science Internship program
- Inspired by common university FAQ systems
- Built using Python best practices and design patterns
