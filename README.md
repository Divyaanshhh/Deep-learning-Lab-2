# Single Neuron Model (Perceptron) in Python

A simple implementation of a **Single Neuron (Perceptron)** from scratch using Python and NumPy. This project demonstrates the basic concepts of a perceptron, including weight initialization, bias, activation function, and the learning process.

---

##  Features

- Manual implementation of a single neuron
- Uses the Perceptron Learning Algorithm
- Step activation function
- Trains on the AND logic gate dataset
- Easy to understand and beginner-friendly

---

##  Technologies Used

- Python 3.x
- NumPy

---

##  Project Structure

```
Single-Neuron-Model/
│── single_neuron.py
│── README.md
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Single-Neuron-Model.git
```

### 2. Navigate to the Project Folder

```bash
cd Single-Neuron-Model
```

### 3. Create a Virtual Environment (Optional)

**Windows**

```bash
python -m venv .venv
```

Activate the environment:

**PowerShell**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install numpy
```

---

##  Run the Program

```bash
python single_neuron.py
```

---

## How It Works

1. Initialize weights and bias.
2. Compute the weighted sum of inputs.
3. Apply the Step Activation Function.
4. Calculate the prediction error.
5. Update weights and bias using the Perceptron Learning Rule.
6. Repeat for multiple training epochs.

---

##  Training Dataset

| Input 1 | Input 2 | Output |
|--------:|--------:|-------:|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

This dataset represents the **AND Logic Gate**.

---

##  Sample Output

```
Training Completed!

Final Weights: [0.2 0.1]
Final Bias: -0.2

Testing the Single Neuron

[0 0] -> 0
[0 1] -> 0
[1 0] -> 0
[1 1] -> 1
```

---

## 📚 Learning Concepts

- Artificial Neuron
- Perceptron
- Weight and Bias
- Step Activation Function
- Perceptron Learning Rule
- Binary Classification

---

## Contributing

Contributions are welcome. Feel free to fork this repository and submit a pull request.

---

##  License

This project is licensed under the MIT License.

---

##  Author

**Divyansh**

If you found this project helpful, consider giving it a ⭐ on GitHub!
