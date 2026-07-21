import numpy as np

# Step 1: Training Data
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# Desired Output (AND Gate)
y = np.array([0, 0, 0, 1])

# Step 2: Initialize Weights and Bias
weights = np.zeros(2)
bias = 0
learning_rate = 0.1

# Step 3: Activation Function
def step_function(x):
    if x >= 0:
        return 1
    else:
        return 0

# Step 4: Training
epochs = 10

for epoch in range(epochs):
    print(f"\nEpoch {epoch + 1}")

    for i in range(len(X)):
        # Weighted Sum
        linear_output = np.dot(X[i], weights) + bias

        # Prediction
        prediction = step_function(linear_output)

        # Error
        error = y[i] - prediction

        # Update Weights and Bias
        weights = weights + learning_rate * error * X[i]
        bias = bias + learning_rate * error

        print(f"Input: {X[i]} Prediction: {prediction} Error: {error}")

print("\nTraining Completed!")

print("\nFinal Weights:", weights)
print("Final Bias:", bias)

# Step 5: Testing
print("\nTesting the Single Neuron")

for i in range(len(X)):
    output = step_function(np.dot(X[i], weights) + bias)
    print(f"{X[i]} -> {output}")
