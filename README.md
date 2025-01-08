# Jiggler

Jiggler is a Python-based tool designed to detect user inactivity and simulate mouse movements to keep the system active. It leverages the `pynput` and `pyautogui` libraries to monitor user inputs and perform automated actions when inactivity is detected.

---

## Features

- Detects user activity via mouse movements, clicks, scrolls, and keyboard inputs.
- Simulates mouse movements after a specified period of inactivity (default: 30 seconds).
- Logs the time and coordinates of simulated mouse movements.
- Safe shutdown with keyboard interrupt handling.

---

## Prerequisites

Ensure you have Python 3.6 or higher installed. Install the required libraries by running:

```bash
pip install pynput pyautogui
```

---

## Installation

```bash
git clone https://github.com/Junsung-Kim/Jiggler.git
cd Jiggler
```

---

## Usage

Run the script directly with:

```bash
python jiggler.py
```

The program will:

- Monitor user activity.
- Simulate mouse movements if no activity is detected for 30 seconds.
- Output logs of simulated movements to the console.

To stop the program, press `Ctrl+C`.

---

## Customization

You can customize the inactivity timeout by modifying the following constant in the script:

```python
INACTIVITY_THRESHOLD = 30  # seconds
```

Replace `30` with your desired timeout in seconds.

---

## Example Output

When the program simulates mouse movements, you’ll see logs like:

```plaintext
2025-01-08 03:45:12,123 - Mouse moved: (500, 500) -> (1024, 768)
```

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

---

## Disclaimer

This tool is intended for personal use. Please ensure compliance with your organization's policies before using it in a professional environment.

