# 🤖 Number Guessing Game — Computer Guesses the User's Number

A fun Python console game where the **computer tries to guess the number** you are thinking of, using logic and binary search! 🎯

---

## 📌 Project Description

In this game, **you (the user)** think of a number between 1 and 100, and the **computer will guess it** based on your feedback:
- `'h'` → too high
- `'l'` → too low
- `'c'` → correct

The game continues until the computer correctly guesses the number.

---

## 🎮 How to Play

1. Run the program.
2. Think of a number between 1 and 100 (keep it secret).
3. When the computer makes a guess:
   - Type `'h'` if the guess is **too high**
   - Type `'l'` if the guess is **too low**
   - Type `'c'` if the guess is **correct**
4. The computer will adjust its guess accordingly and try again.

---

## 🧠 Concepts Used

- Binary Search Logic
- Loops and Conditionals
- User Input Handling
- Functions

---


🛠️ Future Improvements


Add GUI using tkinter

Track average number of guesses

Voice-based feedback using speech_recognition

Multiplayer mode



📸 Demo (Console Output)



Think of a number between 1 and 100.
Computer guesses: 50
Is it (h/l/c)? l
Computer guesses: 75
Is it (h/l/c)? h
Computer guesses: 62
Is it (h/l/c)? c
Yay! The computer guessed it in 3 tries!
