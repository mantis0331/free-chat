import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer

# Define a list of greetings and responses
greetings = ["hi", "hello", "hey", "greetings", "wassup"]
greeting_responses = ["hi", "hey", "*nods*", "hi there", "hello"]

# Define a list of farewell keywords and responses
farewells = ["bye", "goodbye", "farewell", "quit", "exit"]
farewell_responses = ["Goodbye!", "See you later!", "Take care!"]

# Define a list of fallback responses
fallback_responses = ["Sorry, I'm not sure I understand.", "Can you please rephrase that?", "I'm still learning. Could you try again?"]

# Preprocess the input text
def preprocess(text):
    # Tokenize the text into sentences
    sent_tokens = sent_tokenize(text.lower())
    # Tokenize the text into words
    word_tokens = word_tokenize(text.lower())
    # Lemmatize the words
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in word_tokens]
    return sent_tokens, lemmatized_tokens

# Generate a chatbot response
def generate_response(user_input):
    chatbot_response = ''
    # Preprocess the user's input
    sent_tokens, lemmatized_tokens = preprocess(user_input)
    
    # Check for greetings
    for word in lemmatized_tokens:
        if word in greetings:
            chatbot_response = random.choice(greeting_responses)
            return chatbot_response
    
    # Check for farewell keywords
    for word in lemmatized_tokens:
        if word in farewells:
            chatbot_response = random.choice(farewell_responses)
            return chatbot_response
    
    # Fallback response if no recognizable keywords are found
    if chatbot_response == '':
        chatbot_response = random.choice(fallback_responses)
    
    return chatbot_response

print("Chatbot: Hi! What can I help you with today? (Type 'bye' to exit)")

while True:
    user_input = input("User: ")
    
    if user_input.lower() in farewells:
        print("Chatbot: " + generate_response(user_input))
        break
    
    response = generate_response(user_input)
    print("Chatbot:", response)