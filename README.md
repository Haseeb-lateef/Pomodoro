# Pomodoro Timer (Tkinter)

A simple **Pomodoro timer desktop app** built with **Python + Tkinter**. It helps you focus using the Pomodoro technique: work sessions followed by short breaks, with a longer break after multiple cycles.

## Screenshot

<img width="598" height="579" alt="Screenshot 2026-03-02 164336" src="https://github.com/user-attachments/assets/646b72d9-5dee-43fa-8d40-f612e9b02c27" />


## Features

- 25-minute work sessions
- 5-minute short breaks
- 20-minute long break after 4 work sessions
- Start / Reset controls
- Progress checkmarks after each completed work session

## Requirements

- Python 3.x
- Tkinter (usually included with Python on Windows/macOS; on some Linux distros you may need to install it separately)

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Haseeb-lateef/Pomodoro.git
   cd Pomodoro
   ```

2. Run the app:
   ```bash
   python main.py
   ```

## Project Files

- `main.py` — the Tkinter application code
- `tomato.png` — the UI image used in the app (also shown above)

## Notes

- The timer durations are defined in `main.py` as:
  - `WORK_MIN = 25`
  - `SHORT_BREAK_MIN = 5`
  - `LONG_BREAK_MIN = 20`

## License

No license specified yet. If you want, add a `LICENSE` file (MIT is a common choice).
