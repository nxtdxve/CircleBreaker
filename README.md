# CircleBreaker for neal.fun's Circle Game

This script automates the task of drawing shapes on the [neal.fun circle game](https://neal.fun/perfect-circle/). It consistently achieves high scores by drawing specific shapes, particularly triangles.

## Requirements

- Python 3.x
- `pyautogui` module
- `keyboard` module

## Installation

1. Install the required Python modules:

```bash
pip install pyautogui keyboard
```

2. Clone this repository or download the script.

## Usage

1. Open the [neal.fun circle game](https://neal.fun/perfect-circle/) in a web browser.
2. Make sure the browser is in full-screen mode and is on the primary monitor.
3. Run the script:

```bash
python perfect circle.py
```

4. Follow the on-screen instructions:
    - Press 's' to start drawing a shape.
    - Press 'e' to exit.

## Why a Triangle?

During testing, it was observed that the triangle shape consistently achieves a near-perfect score in the game. This might seem counterintuitive, as a triangle is far from a circle. However, the game's scoring mechanism seems to prioritize the completion of shapes, the overlap of the starting and ending points, and possibly the total path length of the drawn shape. The triangle, being a simpler shape with fewer vertices, might meet these criteria more effectively than more complex shapes, leading to a higher score. This behavior highlights the quirks and unexpected behaviors in the game's scoring mechanism.

## Notes

- This script has been optimized for a triangle shape.
- The script assumes that the browser is maximized and running on the primary monitor. It may not work correctly if these conditions are not met.
- The game evaluates the drawn shapes in a specific way, so the shape drawn might not always resemble a perfect circle, even if the score is high.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).
