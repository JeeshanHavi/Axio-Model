import torch
import numpy as np
from Nervous_sys.LanguageProcessor import tokenize, stem, bag_of_words
from Nervous_sys.DeepNeuralNetwork import DeepNeuralNet

def load_model(file_path: str):
    """Load the pre-trained model and associated data."""
    data = torch.load(file_path)
    model = DeepNeuralNet(data["input_size"], data["hidden_size"], data["output_size"])
    model.load_state_dict(data["model_state"])
    return model, data["input_size"], data["hidden_size"], data["output_size"], data["all_words"], data["tags"]

def predict(model, input_size, hidden_size, output_size, all_words, tags, sentence):
    """Predict the intent of the user's input."""
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)
    model.eval()

    sentence = tokenize(sentence)
    sentence = [stem(w) for w in sentence if w not in [',', '?', '/', '.', '!']]
    bag = bag_of_words(sentence, all_words)
    
    # Reshape the bag of words to have a batch dimension
    bag = np.array(bag).reshape(1, -1)  # Reshape to (1, input_size)
    bag = torch.from_numpy(bag).to(device)

    output = model(bag)
    _, predicted = torch.max(output, dim=1)  # Use dim=1 for batch dimension
    return tags[predicted.item()]

def chatbot(user):
    """Run the chatbot."""
    model_file_path = "Database\\traindata.pth"
    model, input_size, hidden_size, output_size, all_words, tags = load_model(model_file_path)
    while True:
        sentence = user
        intent = predict(model, input_size, hidden_size, output_size, all_words, tags, sentence)
        print(f"SPARC: {intent}")
