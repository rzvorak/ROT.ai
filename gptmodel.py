
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
example_data = np.random.rand(1000, 10)  # 1000 examples, 10 features (example)
example_labels = np.random.rand(1000, 1)  # 1000 labels: multiplier in a week

# Preprocess data
processed_data = preprocess_data(example_data)
processed_labels = example_labels

# Step 4: Split the data into training and testing sets
train_data = processed_data[:800]
train_labels = processed_labels[:800]
test_data = processed_data[800:]
test_labels = processed_labels[800:]

# Step 5: Initialize the Model, Loss Function, and Optimizer
input_size = train_data.shape[1]  # Number of features in the input
model = TrendPredictionModel(input_size)  # Initialize the model
criterion = nn.MSELoss()  # Mean Squared Error Loss
optimizer = optim.Adam(model.parameters(), lr=0.001)  # Adam optimizer

# Step 6: Training Loop
num_epochs = 100  # Number of training epochs

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

with torch.no_grad():  # No gradient computation needed during evaluation
    predictions = model(test_inputs)
    # Calculate the test loss
    test_loss = criterion(predictions, test_labels_tensor)
    print(f'Test Loss: {test_loss.item():.4f}')
