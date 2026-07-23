# Imports
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from Arms.Speak import speak

# Define the prompt template for the conversation
template = """
Answer the question below 
try answering in short within 30 words
Do not elaborate your answers

Here is the conversation history: {context}

Question: {question}

Answer:
"""

# Initialize the model and prompt
model = OllamaLLM(model="phi3", temperature=0.5) # Processing is directly dependent on temperature value
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# File to store conversations
conversation_file = "DataBase\\ChatData.txt"

def load_previous_conversations():
    """Load previous conversations from a text file."""
    try:
        with open(conversation_file, "r") as file:
            return file.read()
    except FileNotFoundError:
        return ""  # Return empty string if file does not exist

def save_conversation(user_input, ai_response):
    """Append the current conversation to the text file."""
    with open(conversation_file, "a") as file:
        file.write(f"User:  {user_input}\nSPARC: {ai_response}\n")

def conversation (user):
    # Load previous conversations into context
    context = load_previous_conversations()
    user_input = user
    # Invoke the model with the current context and user input
    result = chain.invoke({"context": context, "question": user_input})
    print(speak(result))
    # Update the context with the latest user input and AI response
    context += f"\nUser: {user_input}\nSPARC: {result}"
    # Save the current conversation to the text file
    save_conversation(user_input, result)
  
