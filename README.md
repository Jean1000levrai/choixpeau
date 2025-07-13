
# Choixpeau Magique 🧙‍♂️🎩

A graphical Python application inspired by the **Harry Potter Sorting Hat**. Enter your traits, and the Choixpeau will assign you to your Hogwarts house using the **Manhattan distance algorithm** and a dataset of fictional students.

---

## 🧠 How It Works

The app reads a dataset of students from `choixpeauMagique.csv`, each labeled with a Hogwarts house and traits:
- Courage
- Loyalty
- Wisdom
- Cunning

When you enter your own traits, the algorithm compares them to the dataset using **Manhattan distance** and assigns you the house that is most common among your **7 nearest neighbors**.

---

## 📁 Project Structure

- `src/main.py`
- `src/gui.py`
- `src/function.py`
- `src/open_img_tk.py`
- `choixpeauMagique.csv`
- `img/`

---

## 🖥️ Features

- 🪄 **GUI** interface with animations using `tkinter`
- 📊 **Data-driven** sorting using k-Nearest Neighbors (k-NN, k=7)
- 🎓 Hogwarts-style house assignment
- 🖼️ Visual assets support (Sorting Hat images & speech bubble)

---

## 📦 Requirements

- Python 3.7+
- Required packages listed in `requirements.txt` (you must create this file with needed libraries, e.g., `Pillow`)

---

## 🔧 Installation & Usage
 
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Jean1000levrai/choixpeau.git
   cd choixpeau```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt```

3. **Run the application**:
   ```bash
      python src/main.py```

---

## 📄 License

This project is licensed under the

---

## 🖼️ Screenshots
