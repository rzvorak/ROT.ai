import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.preprocessing import StandardScaler
import numpy as np

# Step 1: Define the Model
class TrendPredictionModel(nn.Module):
    def __init__(self, input_size):
        super(TrendPredictionModel, self).__init__()
        # Two hidden layers with ReLU activation functions
        self.fc1 = nn.Linear(input_size, 64)  # First hidden layer (64 neurons)
        self.relu = nn.ReLU()                 # ReLU activation function
        self.fc2 = nn.Linear(64, 64)          # Second hidden layer (64 neurons)
        self.fc3 = nn.Linear(64, 1)           # Output layer (1 value for prediction)

    def forward(self, x):
        x = self.fc1(x)  # First layer
        x = self.relu(x)  # ReLU activation
        x = self.fc2(x)   # Second layer
        x = self.relu(x)  # ReLU activation
        x = self.fc3(x)   # Output layer
        return x

# Step 2: Preprocess the Data
def preprocess_data(data):
    """
    Standardize the data (zero mean, unit variance)
    """
    scaler = StandardScaler()
    return scaler.fit_transform(data)  # Normalize the input data

# Step 3: Example dataset (This is a placeholder; use your actual data)
# Assuming `example_data` has the following features:
# [current_popularity, day_of_week, previous_day_popularity, trend_category_one_hot, ...]

import ast

def read_vectors_from_file(filename):
    vectors = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Parse the line as a literal list using ast.literal_eval
                vector = ast.literal_eval(line.strip())
                
                # Discard the first entry (the string) and keep the rest
                for i in range(1, len(vector)):
                    vector[i]= float(vector[i])
                vectors.append((vector[1:]))  # Slice to remove the first element
                
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return vectors

# Example usage
filename = 'output.txt'
vectors = read_vectors_from_file(filename)
print("Vectors read from file:")
inputArray = []
labels = []
for vector in vectors:
    print(vector)
    inputArray.append(vector[:-1])
    labels.append(vector[-1])
  
# Preprocess data
processed_data = preprocess_data(inputArray)

# Step 4: Split the data into training and testing sets
half_data = len(labels) // 2
train_data = processed_data[:-1 * half_data]
train_labels = labels[:-1 * half_data]
test_data = processed_data[half_data:]
test_labels = labels[half_data:]

# Step 5: Initialize the Model, Loss Function, and Optimizer
input_size = train_data.shape[1]  # Number of features in the input
model = TrendPredictionModel(input_size)  # Initialize the model
criterion = nn.MSELoss()  # Mean Squared Error Loss
optimizer = optim.Adam(model.parameters(), lr=0.001)  # Adam optimizer

# Step 6: Training Loop
num_epochs = 5000  # Number of training epochs

for epoch in range(num_epochs):
    model.train()  # Set the model to training mode
    optimizer.zero_grad()  # Zero the gradients from previous step
    
    # Convert the data to tensors
    inputs = torch.tensor(train_data, dtype=torch.float32)
    labels = torch.tensor(train_labels, dtype=torch.float32)
    
    # Forward pass
    predictions = model(inputs)
    
    # Compute the loss
    loss = criterion(predictions, labels)
    
    # Backward pass and optimization
    loss.backward()
    optimizer.step()

    # Print the loss every 10 epochs
    if (epoch + 1) % 10 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# Step 7: Evaluate the Model
model.eval()  # Set the model to evaluation mode
test_inputs = torch.tensor(test_data, dtype=torch.float32)
test_labels_tensor = torch.tensor(test_labels, dtype=torch.float32)
torch.save(model.state_dict(), 'rot_model.pth')

with torch.no_grad():  # No gradient computation needed during evaluation
    predictions = model(test_inputs)
    # Calculate the test loss
    test_loss = criterion(predictions, test_labels_tensor)
    print(f'Test Loss: {test_loss.item():.4f}')


