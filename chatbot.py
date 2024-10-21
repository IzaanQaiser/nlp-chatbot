import cohere #import co:here library for NLP
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

class Chatbot: # Define a class for the Chatbot which can manage interactions
    def __init__(self): # constructor method to initialise chatbot instance
        self.cohere_client = cohere.Client(f"{api_key}") # Create co:here client object with API key (self means it is an object)
        self.context = [] # conversation history for context

    def get_response(self, user_input): # Define a function get a response based on the users input
        self.context.append(f"User: {user_input}") # Adds the users message to the conversation history
        prompt = "\n".join(self.context) + "\nBot:" # Joins all lines of context and adds "Bot:"
        response = self.cohere_client.generate( # Generates a response based on the constructed prompt
            model='command-xlarge', # Specify which model to use
            prompt = prompt, # gives the constructed prompt with conversation context to the model
            max_tokens = 50, # Maximum amount of tokens that can be used in the response (50)
            temperature = 0.9, # Set the randomness of the response - the higher, the more random
            stop_sequences = ["User:", "Bot:"] # Define the sequences where the generation should stop
        ).generations[0].text.strip() # Access the generated text and remove whitespace

        self.context.append(f"Bot: {response}") # Formatting as - Bot: [response]

        return response # Returns the response so it can be used by the caller
    
    def reset_context(self): # Method to reset conversation Context
        self.context = [] # Reset the context to be an empty list