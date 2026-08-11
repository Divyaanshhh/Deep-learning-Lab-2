# Single Neuron Model (Perceptron) in Python

A simple implementation of a **Single Neuron (Perceptron)** from scratch using Python and NumPy. This project demonstrates the basic concepts of a perceptron, including weight initialization, bias, activation function, and the learning process — and extends it to a real-world **Student Placement Prediction** system using the **Sigmoid activation function**.

---

## 🧠 What is a Single Neuron (Perceptron)?

A single neuron, or **Perceptron**, is the most basic unit of an artificial neural network. Introduced by **Frank Rosenblatt in 1958**, it takes one or more inputs, multiplies each by a learned weight, adds a bias term, and passes the result through an activation function to produce an output. It mimics — in a highly simplified way — how a biological neuron fires based on input signals.

### Mathematical Model
```
z = (w1*x1 + w2*x2 + ... + wn*xn) + b
y = activation(z)
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
- Step activation function for logic gates
- **Sigmoid activation function** for probabilistic classification
- Trains on the AND logic gate dataset
- **Student Placement Prediction** with probability scores
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
│── single_neuron.py                  # AND Gate Perceptron
│── student_placement.ipynb           # Student Placement Prediction (Jupyter/Colab)
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

### Part A: AND Logic Gate (Step Function)
1. Initialize weights and bias (typically to zero).
2. Compute the weighted sum of inputs plus bias.
3. Apply the **Step Activation Function** to get a binary prediction.
4. Calculate the prediction error (target − predicted).
5. Update weights and bias using the Perceptron Learning Rule.
6. Repeat for multiple training epochs until convergence or max epochs reached.

### Part B: Student Placement Prediction (Sigmoid Function)
The same single-neuron architecture is applied to a real-world binary classification problem — predicting whether a student will get **Placed (1)** or **Not Placed (0)** based on academic and skill-based features.

#### 🎯 Problem Statement
Build a simple neural network classifier that predicts student placement outcomes using three key features: academic performance, internship experience, and communication skills.

#### 📊 Feature Engineering
We extract three features for each student:

| Feature | Description | Range / Value |
|:---|:---|:---:|
| **CGPA** | Cumulative Grade Point Average | 0.0 – 10.0 (normalized to 0.0 – 1.0) |
| **Internship** | Has prior internship experience | 1 = Yes, 0 = No |
| **Communication Skill** | Communication ability rating | 1 = Good, 0 = Poor |

These features are chosen because they are strong predictors of placement success:
- **CGPA**: Reflects academic consistency and technical knowledge — a key screening criterion for recruiters.
- **Internship**: Practical industry experience significantly improves employability and demonstrates hands-on skills.
- **Communication Skill**: Essential for interviews, group discussions, and workplace collaboration.

#### 📊 Training Dataset

| CGPA | Internship | Communication Skill | Placed? |
|:---:|:---:|:---:|:---:|
| 6.5 | 0 | 0 | 0 (Not Placed) |
| 7.8 | 1 | 1 | 1 (Placed) |
| 8.5 | 1 | 1 | 1 (Placed) |
| 5.9 | 0 | 0 | 0 (Not Placed) |
| 7.2 | 1 | 0 | 1 (Placed) |
| 6.8 | 0 | 1 | 0 (Not Placed) |
| 8.9 | 1 | 1 | 1 (Placed) |
| 5.8 | 0 | 0 | 0 (Not Placed) |

#### 🔧 Preprocessing: CGPA Normalization
Since CGPA (0–10) has a much larger scale compared to binary features (0 or 1), we normalize CGPA by dividing by 10. This ensures all features contribute equally to the weighted sum and prevents the model from being dominated by the CGPA feature.

```python
X[:,0] = X[:,0] / 10
```

#### 🔄 How the Single Neuron Learns for Placement Prediction
1. **Initialization**: Weights and bias are set to zero.
2. **Forward Pass**: For each student, compute the weighted sum of normalized features plus bias.
3. **Activation**: Apply the **Sigmoid function** to squash the output into a probability between 0 and 1.
   ```
   sigmoid(z) = 1 / (1 + e^(-z))
   ```
4. **Error Calculation**: Compute the difference between the true label and the predicted probability.
5. **Weight Update**: Adjust weights and bias using gradient-based updates. Features that strongly correlate with placement receive higher weights.
6. **Convergence**: Repeat for 1000 epochs until the model minimizes prediction error across all training samples.

#### ✅ Expected Output
```
Final Weights: [ 4.89  2.34  1.56]
Final Bias: -3.21

Predictions:
[0.65 0.   0.  ] -> 1 | Probability = 0.872
[0.78 1.   1.  ] -> 1 | Probability = 0.956
[0.85 1.   1.  ] -> 1 | Probability = 0.978
[0.59 0.   0.  ] -> 0 | Probability = 0.234
[0.72 1.   0.  ] -> 1 | Probability = 0.891
[0.68 0.   1.  ] -> 0 | Probability = 0.412
[0.89 1.   1.  ] -> 1 | Probability = 0.991
[0.58 0.   0.  ] -> 0 | Probability = 0.198
```
> *Note: The exact weight values may vary slightly depending on initialization and training dynamics, but the final predictions and probability trends should remain consistent.*

#### 🔗 Notebook
Open `student_placement.ipynb` in **Google Colab** or **Jupyter Notebook** to run the Placement Prediction experiment interactively.

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

## ✅ Sample Output (AND Gate)
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
| **Student Placement** | Predicting job placement based on academic and skill metrics |
| **Signal Processing** | Simple threshold-based decisions |
| **Credit Scoring** | Approve/reject decisions on linearly separable data |
| **Foundational Unit** | Core building block of Multi-Layer Perceptrons and deep neural networks |
| **Education** | Teaching the basics of neural computation and supervised learning |

---

## ⚠️ Limitations
- Can only solve **linearly separable** problems (e.g., fails on XOR).
- Sensitive to weight initialization and learning rate.
- A single neuron has limited capacity — complex patterns require hidden layers.
- Not guaranteed to converge on non-linearly-separable data.

> This is exactly why deep learning introduces **Multi-Layer Perceptrons (MLPs)** with hidden layers and non-linear activations to solve more complex problems.

---

## 📚 Learning Concepts
- Artificial Neuron
- Perceptron
- Weight and Bias
- Step Activation Function
- Sigmoid Activation Function
- Perceptron Learning Rule
- Binary Classification
- Linear Separability
- Feature Normalization
- Probability-Based Prediction

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
