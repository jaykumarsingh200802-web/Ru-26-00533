## 📌 Problem Statement

Build a program that rolls a die a number of times chosen by the user, and shows the frequency of each face, the total, the average and the most frequent face.

- Number of rolls must be from **1 to 1000**.
- A die has faces **1 to 6**.
- For testing, the rolls are fixed as given in each input.

---

## ✨ Features

- Rolls a die 1–1000 times using Python's `random` module
- Stores the frequency of each face in a **dictionary**
- Shows **total**, **average** (2 decimal places) and **most frequent face**
- Handles **ties** (e.g. `2 and 4 (2 times each)`)
- **Input validation** for the number of rolls (rejects `0`, `abc`, `-3`, `1001`, decimals, etc.)
- **Play again? (y/n)** option at the end
- **Test mode** (`--test`) to enter fixed rolls and repeat the given test cases

---

## ⚙️ Requirements

- Python 3.6 or above
- No external libraries needed (only built-in `random` and `sys`)

---

## 🚀 How to Run

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/dice-rolling-game.git
cd dice-rolling-game

# 2. Normal mode (random rolls)
python dice_game.py

# 3. Test mode (you enter the rolls yourself)
python dice_game.py --test
```

---

## 🧩 Project Structure

```
dice-rolling-game/
├── dice_game.py    # Main program
└── README.md       # Documentation
```

---

## 🔧 Functions Used

| Function | Purpose |
|---|---|
| `get_num_rolls()` | Reads and validates the number of rolls (1–1000) |
| `roll_die()` | Rolls the die once (`random.randint(1, 6)`) |
| `roll_many(n)` | Rolls the die `n` times using a loop |
| `get_manual_rolls(n)` | Test mode: reads fixed rolls typed by the user |
| `count_frequency(rolls)` | Builds the frequency dictionary `{face: count}` |
| `calculate_statistics(rolls, freq)` | Returns total, average and most frequent face(s) |
| `format_faces(faces)` | Formats ties like `2 and 4` |
| `display_results(...)` | Prints frequency, total, average, most frequent |
| `ask_play_again()` | Handles the `Play again? (y/n)` question |
| `main()` | Controls the program flow |

---

## 🧠 Algorithm

1. Ask the user for the number of rolls; repeat until a whole number from 1 to 1000 is entered.
2. Roll the die that many times (or take fixed rolls in test mode).
3. Count how many times each face (1–6) appeared and store it in a dictionary.
4. **Total** = sum of all rolls; **Average** = total ÷ number of rolls.
5. **Most frequent face** = face(s) with the highest count.
6. Display the results and ask `Play again? (y/n)`.
7. If `y`, repeat from step 1; if `n`, print `Thanks for playing!` and exit.

---

## 🧪 Test Cases

Run with `python dice_game.py --test`.

### Test Case 1 – Normal Input
```
Number of rolls: 5
Rolls: 3 6 3 1 5
Frequency: 1:1 | 2:0 | 3:2 | 4:0 | 5:1 | 6:1
Total: 18 | Average: 3.60
Most frequent: 3 (2 times)
```

### Test Case 2 – Boundary / Minimum Input
```
Number of rolls: 1
Rolls: 6
Frequency: 1:0 | 2:0 | 3:0 | 4:0 | 5:0 | 6:1
Total: 6 | Average: 6.00
Most frequent: 6 (1 time)
```

### Test Case 3 – Invalid Input
```
Number of rolls: 0
Invalid input. Enter a whole number from 1 to 1000.
Number of rolls: abc
Invalid input. Enter a whole number from 1 to 1000.
Number of rolls: -3
Invalid input. Enter a whole number from 1 to 1000.
Number of rolls: 2
Rolls: 1 2
Frequency: 1:1 | 2:1 | 3:0 | 4:0 | 5:0 | 6:0
Total: 3 | Average: 1.50
Most frequent: 1 and 2 (1 time each)
```

### Test Case 4 – Different Valid Scenario
```
Number of rolls: 6
Rolls: 2 2 4 4 5 1
Frequency: 1:1 | 2:2 | 3:0 | 4:2 | 5:1 | 6:0
Total: 18 | Average: 3.00
Most frequent: 2 and 4 (2 times each)
Play again? (y/n): n
Thanks for playing!
```

| Test Case | Description | Result |
|---|---|---|
| 1 | Normal input | ✅ Pass |
| 2 | Boundary / minimum input | ✅ Pass |
| 3 | Invalid input | ✅ Pass |
| 4 | Different valid scenario | ✅ Pass |

---

## 🎮 Sample Run (Normal Mode)

```
Number of rolls: 10
Frequency: 1:1 | 2:2 | 3:3 | 4:0 | 5:2 | 6:2
Total: 36 | Average: 3.60
Most frequent: 3 (3 times)
Play again? (y/n): n
Thanks for playing!
```

_(Rolls are random, so your output will differ.)_

---

## ✅ Requirements Checklist

- [x] Solution in Python 3 (single `.py` file), run from the console
- [x] Uses the `random` module and a loop to roll the die
- [x] Frequency of each face stored in a dictionary
- [x] Functions to roll the die, calculate statistics and display results
- [x] Validates the number of rolls and asks `Play again? (y/n)`
- [x] Passes all 4 given test cases

---

## 🔮 Future Improvements

- Show a bar chart (text or graphical) of the frequencies
- Support dice with a custom number of faces
- Save results to a file

---

## 📄 Conclusion

The Dice Rolling Game meets all the bare-minimum requirements of the problem statement. It makes good use of the `random` module, loops, functions, dictionaries and basic statistics, and handles invalid input safely.
