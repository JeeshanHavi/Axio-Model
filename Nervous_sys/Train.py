import numpy as np
import json
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from Nervous_sys.LanguageProcessor import bag_of_words, tokenize, stem
from Nervous_sys.DeepNeuralNetwork import DeepNeuralNet
import logging
from typing import List, Tuple, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO)

class ChatDataset(Dataset):
    def __init__(self, x_data: np.ndarray, y_data: np.ndarray):
        self.n_samples = len(x_data)
        self.x_data = x_data
        self.y_data = y_data

    def __getitem__(self, index: int) -> Tuple[np.ndarray, int]:
        return self.x_data[index], self.y_data[index]

    def __len__(self) -> int:
        return self.n_samples

def load_intents(file_path: str) -> Dict[str, Any]:
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        logging.error(f"Error loading intents file: {e}")
        raise

def preprocess_data(intents: Dict[str, Any]) -> Tuple[np.ndarray, np.ndarray, List[str], List[str]]:
    all_words = []
    tags = []
    xy = []

    for intent in intents['intents']:
        tag = intent['tag']
        tags.append(tag)

        for pattern in intent['patterns']:
            w = tokenize(pattern)
            all_words.extend(w)
            xy.append((w, tag))

    ignore_words = [',', '?', '/', '.', '!']
    all_words = [stem(w) for w in all_words if w not in ignore_words]
    all_words = sorted(set(all_words))
    tags = sorted(set(tags))

    x_train = []
    y_train = []

    for (pattern_sentence, tag) in xy:
        bag = bag_of_words(pattern_sentence, all_words)
        x_train.append(bag)
        label = tags.index(tag)
        y_train.append(label)

    return np.array(x_train), np.array(y_train), all_words, tags

def train_model(x_train: np.ndarray, y_train: np.ndarray, num_epochs: int, batch_size: int, learning_rate: float, input_size: int, hidden_size: int, output_size: int) -> nn.Module:
    dataset = ChatDataset(x_train, y_train)
    train_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True, num_workers=0)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = DeepNeuralNet(input_size, hidden_size, output_size).to(device=device)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

    for epoch in range(num_epochs):
        for (words, labels) in train_loader:
            words = words.to(device)
            labels = labels.to(dtype=torch.long).to(device)
            outputs = model(words)
            loss = criterion(outputs, labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        if (epoch + 1) % 100 == 0:
            logging.info(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}')

    logging.info(f'Final Loss : {loss.item():.4f}')
    return model

def save_model(model: nn.Module, input_size: int, hidden_size: int, output_size: int, all_words: List[str], tags: List[str], file_path: str) -> None:
    data = {
        "model_state": model.state_dict(),
        "input_size": input_size,
        "hidden_size": hidden_size,
        "output_size": output_size,
        "all_words": all_words,
        "tags": tags
    }
    torch.save(data, file_path)
    logging.info(f"Training Complete, File Saved To {file_path}")

def load_model(file_path: str) -> Tuple[nn.Module, int, int, int, List[str], List[str]]:
    data = torch.load(file_path)
    model = DeepNeuralNet(data["input_size"], data["hidden_size"], data["output_size"])
    model.load_state_dict(data["model_state"])
    return model, data["input_size"], data["hidden_size"], data["output_size"], data["all_words"], data["tags"]

def predict(model: nn.Module, input_size: int, hidden_size: int, output_size: int, all_words: List[str], tags: List[str], sentence: str) -> str:
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)
    model.eval()

    sentence = tokenize(sentence)
    sentence = [stem(w) for w in sentence if w not in [',', '?', '/', '.', '!']]
    bag = bag_of_words(sentence, all_words)
    bag = torch.from_numpy(np.array(bag)).to(device)

    output = model(bag)
    _, predicted = torch.max(output, dim=0)
    return tags[predicted]

if __name__ == "__main__":
    intents_file_path = 'DataBase\\intents.json'
    intents = load_intents(intents_file_path)

    x_train, y_train, all_words, tags = preprocess_data(intents)

    num_epochs = 1000
    batch_size = 8
    learning_rate = 0.001
    input_size = len(x_train[0])
    hidden_size = 8
    output_size = len(tags)

    logging.info("Training SPARC Neural Engine.....")
    model = train_model(x_train, y_train, num_epochs, batch_size, learning_rate, input_size, hidden_size, output_size)

    model_file_path = "Database\\traindata.pth"
    save_model(model, input_size, hidden_size, output_size, all_words, tags, model_file_path)
    
