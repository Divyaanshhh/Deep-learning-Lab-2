# Single Neuron Model (Perceptron) in Python

A simple implementation of a **Single Neuron (Perceptron)** from scratch using Python and NumPy. This project demonstrates the basic concepts of a perceptron, including weight initialization, bias, activation function, and the learning process.

---

## 🧠 What is a Single Neuron (Perceptron)?

A single neuron, or **Perceptron**, is the most basic unit of an artificial neural network. Introduced by **Frank Rosenblatt in 1958**, it takes one or more inputs, multiplies each by a learned weight, adds a bias term, and passes the result through an activation function to produce an output. It mimics — in a highly simplified way — how a biological neuron fires based on input signals.

### Mathematical Model
```
z = (w1*x1 + w2*x2 + ... + wn*xn) + b
y = 1   if z >= 0
y = 0   if z <  0
```

### Perceptron Learning Rule
```
w_new = w_old + learning_rate * (target - predicted) * input
b_new = b_old + learning_rate * (target - predicted)
```

---

## ✨ Features
- Manual implementation of a single neuron (no ML libraries beyond NumPy)
- Uses the Perceptron Learning Algorithm
- Step activation function
- Trains on the AND logic gate dataset
- Epoch-based training with error tracking
- Easy to understand and beginner-friendly

---

## 🛠️ Technologies Used
- Python 3.x
- NumPy

---

## 📁 Project Structure
```
Single-Neuron-Model/
│── single_neuron.py
│── README.md
```

---

## 🚀 Getting Started

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
**Command Prompt**
```cmd
.venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install numpy
```

---

## ▶️ Run the Program
```bash
python single_neuron.py
```

---

## ⚙️ How It Works
1. Initialize weights and bias (typically to zero).
2. Compute the weighted sum of inputs plus bias.
3. Apply the Step Activation Function to get a binary prediction.
4. Calculate the prediction error (target − predicted).
5. Update weights and bias using the Perceptron Learning Rule.
6. Repeat for multiple training epochs until convergence or max epochs reached.

---

## 📊 Training Dataset (AND Logic Gate)

| Input 1 | Input 2 | Output |
|--------:|--------:|-------:|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

This dataset represents the **AND Logic Gate** — a linearly separable problem, which is why a single neuron can solve it.

---

## ✅ Sample Output
```
Epoch 1/20 - Errors: 2
Epoch 2/20 - Errors: 1
Epoch 3/20 - Errors: 0
Converged early!

Training Completed!
Final Weights: [0.2 0.1]
Final Bias: -0.2

Testing the Single Neuron
[0 0] -> 0
[0 1] -> 0
[1 0] -> 0
[1 1] -> 1
```
> *Exact weight values may vary slightly depending on initialization and learning rate, but predictions on the AND dataset will remain consistent.*

---

## 🌍 Real-World Applications
| Domain | Application |
|---|---|
| **Logic Gates** | AND, OR, NAND, NOR gate simulation |
| **Binary Classification** | Spam detection, pass/fail prediction |
| **Signal Processing** | Simple threshold-based decisions |
| **Credit Scoring** | Approve/reject decisions on linearly separable data |
| **Foundational Unit** | Core building block of Multi-Layer Perceptrons and deep neural networks |
| **Education** | Teaching the basics of neural computation and supervised learning |

---

## ⚠️ Limitations
- Can only solve **linearly separable** problems (e.g., fails on XOR).
- Sensitive to weight initialization and learning rate.
- Produces a hard binary output with no confidence score.
- Not guaranteed to converge on non-linearly-separable data.

> This is exactly why deep learning introduces **Multi-Layer Perceptrons (MLPs)** with hidden layers and non-linear activations to solve more complex problems.

---

## 📚 Learning Concepts
- Artificial Neuron
- Perceptron
- Weight and Bias
- Step Activation Function
- Perceptron Learning Rule
- Binary Classification
- Linear Separability

---

## 🔖 References
- Rosenblatt, F. (1958). *The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain.* Psychological Review.
- Minsky, M. & Papert, S. (1969). *Perceptrons: An Introduction to Computational Geometry.* MIT Press.

---

## 🤝 Contributing
Contributions are welcome. Feel free to fork this repository and submit a pull request.


---

## 👤 Author
**Divyansh**

If you found this project helpful, consider giving it a ⭐ on GitHub!
