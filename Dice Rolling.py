import random
import sys

MIN_ROLLS = 1
MAX_ROLLS = 1000
FACES = range(1, 7)


def get_num_rolls():
    while True:
        text = input("Number of rolls: ").strip()
        try:
            n = int(text)
        except ValueError:
            n = None
        if n is not None and MIN_ROLLS <= n <= MAX_ROLLS:
            return n
        print("Invalid input. Enter a whole number from 1 to 1000.")


def roll_die():
    return random.randint(1, 6)


def roll_many(n):
    return [roll_die() for _ in range(n)]


def get_manual_rolls(n):
    while True:
        parts = input("Rolls: ").replace(",", " ").split()
        try:
            rolls = [int(p) for p in parts]
        except ValueError:
            rolls = []
        if len(rolls) == n and all(r in FACES for r in rolls):
            return rolls
        print(f"Invalid rolls. Enter exactly {n} numbers, each from 1 to 6.")


def count_frequency(rolls):
    freq = {face: 0 for face in FACES}
    for r in rolls:
        freq[r] += 1
    return freq


def calculate_statistics(rolls, freq):
    total = sum(rolls)
    average = total / len(rolls)
    top_count = max(freq.values())
    top_faces = [face for face, c in freq.items() if c == top_count]
    return total, average, top_faces, top_count


def format_faces(faces):
    if len(faces) == 1:
        return str(faces[0])
    return ", ".join(str(f) for f in faces[:-1]) + f" and {faces[-1]}"


def display_results(freq, total, average, top_faces, top_count):
    print("Frequency: " + " | ".join(f"{face}:{freq[face]}" for face in FACES))
    print(f"Total: {total} | Average: {average:.2f}")
    times = "time" if top_count == 1 else "times"
    if len(top_faces) == 1:
        print(f"Most frequent: {top_faces[0]} ({top_count} {times})")
    else:
        print(f"Most frequent: {format_faces(top_faces)} ({top_count} {times} each)")


def ask_play_again():
    while True:
        answer = input("Play again? (y/n): ").strip().lower()
        if answer in ("y", "n"):
            return answer == "y"
        print("Please enter y or n.")


def main():
    test_mode = "--test" in sys.argv
    while True:
        n = get_num_rolls()
        rolls = get_manual_rolls(n) if test_mode else roll_many(n)
        freq = count_frequency(rolls)
        total, average, top_faces, top_count = calculate_statistics(rolls, freq)
        display_results(freq, total, average, top_faces, top_count)
        if not ask_play_again():
            print("Thanks for playing!")
            break
        print()


if __name__ == "__main__":
    main()
