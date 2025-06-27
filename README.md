# 🎮 Tic-Tac-Toe with AI (Python + Tkinter)

A simple and elegant implementation of Tic-Tac-Toe using **Tkinter** for the GUI and an unbeatable **AI opponent** powered by the **Minimax algorithm with Alpha-Beta pruning**.

---

## 🧠 Features

* ✅ Interactive GUI using **Tkinter**
* 🎨 Colored buttons and polished layout
* 🤖 AI opponent using **Minimax + Alpha-Beta Pruning**
* 🔁 Reset functionality to play again instantly
* 🏁 Popup messages for win/draw notifications
* ❌ Player: X 🤖 AI: O

---

## 📦 Requirements

* Python 3.x
* Tkinter (usually included with Python)
* NumPy

Install dependencies (if needed):

```bash
pip install numpy
```

---

## 🚀 How to Run

```bash
python main.py
```

The game window will launch. You start first as Player **X**. The AI (Player **O**) will respond immediately.

---

## 🧠 How the AI Works

The AI uses the **Minimax algorithm** with **alpha-beta pruning**, making it unbeatable. It evaluates all possible future game states and always picks the optimal move.

* Maximizes score for AI (O)
* Minimizes score for Player (X)
* Uses pruning to reduce unnecessary computation

---

## ✨ Customization Ideas

* Add difficulty levels by limiting Minimax depth
* Play against another human
* Track win/loss/draw stats
* Add sound effects and animations

---

## 📝 License

This project is open-source and free to use for learning or personal enjoyment.
