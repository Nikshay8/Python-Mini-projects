# 🐍 Python Mini Projects

This repository contains simple Python-based mini projects.  
Currently it features:

- 🧠 Number Guessing Game  
- 🐍 Snake Water Gun Game  
- 🌦️ Weather App using Python  
- 🖼️ Image Resizer using OpenCV

All projects are interactive and help beginners understand Python basics like loops, conditionals, dictionaries, user input, API integration, and randomness.

---

## 1️⃣ Number Guessing Game

### 🎯 Objective  
The computer generates a random number between 1 and 100. Your task is to guess the number. It will guide you with:

- "Higher number please" if your guess is too low  
- "Lower number please" if your guess is too high  
- When guessed correctly, it displays the total number of attempts used.

### ✅ Features
- Random number generation  
- Input-based guessing  
- Feedback on guesses  
- Tracks number of attempts  

---

## 2️⃣ Snake Water Gun Game

### 🎮 Game Rules  
This is a variation of the classic Rock-Paper-Scissors game:

- Snake (s) drinks Water (w) → Snake wins 🐍 > 💧  
- Water (w) disables Gun (g) → Water wins 💧 > 🔫  
- Gun (g) kills Snake (s) → Gun wins 🔫 > 🐍  
- Same choices → Draw  

### ✅ Features
- Player vs Computer  
- Random choice for computer  
- Dictionary-based mapping  
- Outcome logic with clear rules  

---

## 3️⃣ Weather App using Python

### 🌤️ Objective  
Get real-time temperature information for any city using a public weather API. The result is spoken aloud using the Windows voice engine.

### ✅ Features
- Takes city name as input  
- Fetches real-time temperature using WeatherAPI  
- Speaks out the weather using Windows TTS  
- Includes a pause and polite closing message  

### 📦 Requirements
Install dependencies:

```bash
pip install requests pywin32
```

---

## 4️⃣ Image Resizer using OpenCV

### 🖼️ Objective  
Resize any image by a defined percentage using the OpenCV library and save the output.

### ✅ Features
- Reads any image file  
- Resizes image based on scale percentage  
- Saves the resized image to disk  
- Customizable file names and scaling factor

### 📦 Requirements
Install OpenCV:

```bash
pip install opencv-python
```

### ▶️ How to Run
1. Place your image in the same folder as `main.py`.
2. Edit the source, destination, and scale_percent variables as needed.
3. Run:

```bash
python main.py
```

---

## 🚀 How to Run All Projects

Clone the repository:

```bash
git clone https://github.com/nikshay8/mini-python-games.git
cd mini-python-games
```

Run any project by navigating to its file and executing:

```bash
python main.py
```

---






