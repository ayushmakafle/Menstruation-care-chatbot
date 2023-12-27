import nltk
import pandas as pd
from nltk.chat.util import Chat, reflections

# Load dataset from CSV file
def load_dataset(file_path, input_column='Intent', response_column='Response'):
    dataset = pd.read_csv(file_path)
    patterns = []
    for index, row in dataset.iterrows():
        input_pattern = row[input_column]
        response = row[response_column]
        patterns.append((input_pattern, [response]))
    return patterns

# Load all datasets from the datas folder
def load_all_datasets():
    datasets = ['Fertility Dost Chatbot.csv', 'Flo.csv', 'General Mai.csv','Hello Clue.csv','Menstrual Hygeine.csv','New Periods Curriculum.csv', 'Real Data.csv','Real Person Data.csv','Sexually Transmitted Infections.csv']
    all_patterns = []
    for dataset in datasets:
        file_path = f'datas/{dataset}'
        all_patterns.extend(load_dataset(file_path))
    return all_patterns

# Create a chatbot with the loaded patterns and reflections
chatbot = Chat(load_all_datasets(), reflections)

# Function to start the chat
def start_chat():
    print("Simple Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Simple Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Simple Chatbot:", response)

# Start the chat when the script is run
if __name__ == "__main__":
    start_chat()
