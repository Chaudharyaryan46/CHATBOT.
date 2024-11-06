Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Step 1: Define the data dictionary with conversation history
data = {
    "chatbotId": "0pXI-RFiFnYnLTz9FIgsX",
    "chatbotName": "University Chatbot",
    "startDateStr": "2024-10-04T18:30:00.000Z",
    "endDateStr": "2024-11-04T18:29:59.999Z",
    "conversations": [
        {
            "id": "e07d3cee-88af-491b-b8bc-6571fe8ad4a7",
            "created_at": "2024-11-04T11:45:34.216413+00:00",
            "chatbot_id": "0pXI-RFiFnYnLTz9FIgsX",
            "form_submission": None,
            "source": "Playground",
            "min_score": 0.453744251821211,
            "country": "India",
            "messages": [
                {
                    "role": "assistant",
                    "content": "Hi! What can I help you with?"
                },
                {
                    "id": "ce4d7da3-9f51-4b13-ba1b-4b64ac1e6e7a",
                    "role": "user",
                    "content": "What is fees\n"
                },
                {
                    "id": "1cffb468-fa90-4a95-97e3-18e5a3d7cec8",
                    "role": "assistant",
                    "score": 0.4537442518212111,
                    "content": "The fees for courses can vary depending on the program and level of study. Could you please specify which course or program you are inquiring about? This will help me provide you with more accurate information. Thank you!"
                }
            ],
            "account_id": "b4dfd6b8-35b0-4837-a211-9ebab8040620",
            "last_message_at": "2024-11-04T11:45:34.216413+00:00",
...             "sentiment": None,
...             "topics": []
...         }
...     ]
... }
... 
... # Step 2: Define intents, patterns, and responses for different categories of inquiries
... intents = {
...     "fees": {
...         "patterns": ["fee", "fees", "cost", "tuition"],
...         "response": "The fees for courses vary depending on the program and level of study. Could you specify which program you're interested in?"
...     },
...     "admission": {
...         "patterns": ["admission", "apply", "application", "enrollment"],
...         "response": "Our admissions process varies depending on the program. Would you like more information about undergraduate or graduate admissions?"
...     },
...     "hours": {
...         "patterns": ["hours", "opening", "closing", "schedule"],
...         "response": "The university's hours are generally 9 AM to 5 PM, Monday to Friday. Specific departments may have different schedules."
...     }
... }
... 
... # Step 3: Define the chatbot response function with intent matching
... def get_chatbot_response(user_input):
...     # Check for matching intents in user input
...     for intent, details in intents.items():
...         for pattern in details["patterns"]:
...             if pattern in user_input.lower():
...                 return details["response"]
...     
...     # Default response if no relevant content is found
...     return "I'm here to help! Could you provide more details about your question?"
... 
... # Step 4: Set up a chat loop to simulate user interaction
... print("Chatbot is running. Type 'exit' to quit.")
... while True:
...     user_input = input("You: ")
...     if user_input.lower() in ["exit", "quit"]:
...         print("Chatbot: Goodbye!")
...         break
...     response = get_chatbot_response(user_input)
