E           = 0  # empty
I           = 1
T           = 2
O           = 3
Z           = 4
S           = 5
L           = 6
J           = 7
W           = 10 # wall

ROWS        = 20 + 2
COLS        = 10 + 2
RECT_SIZE   = 24

GO_DOWN        = 0
GO_LEFT        = 1
GO_RIGHT       = 2
ROTATE         = 3

FPS = 16
RATE = 5

# border-radius ?
DEFAULT_THEME = {
    "bg-color": "#ffffff",
    "wall": { "bg-color": "#858585", "border-size": 1, "border-color": "#000000" },
    "empty": { "bg-color": "#000000", "border-size": 1, "border-color": "#000000" },
    "I": { "bg-color": "#ffffff", "border-size": 1, "border-color": "#000000" },
    "T": { "bg-color": "#ffffff", "border-size": 1, "border-color": "#000000" },
    "O": { "bg-color": "#ffffff", "border-size": 1, "border-color": "#000000" },
    "Z": { "bg-color": "#ffffff", "border-size": 1, "border-color": "#000000" },
    "S": { "bg-color": "#ffffff", "border-size": 1, "border-color": "#000000" },
    "L": { "bg-color": "#ffffff", "border-size": 1, "border-color": "#000000" },
    "J": { "bg-color": "#ffffff", "border-size": 1, "border-color": "#000000" },
    "score": {
        "label": { "font-size": 24, "font-color": "#000000" },
        "value": { "font-size": 24, "font-color": "#ffffff" },
        "box": { "border-size": 1, "border-color": "#000000", "bg-color": "#000000" }
    },
    "next-piece": {
        "label": { "font-size": 24, "font-color": "#000000" },
        "box": { "border-size": 1, "border-color": "#000000", "bg-color": "#000000" }
    },
    "controls": {
        "label": { "font-size": 24, "font-color": "#000000" },
        "value": { "font-size": 16, "font-color": "#ffffff" },
        "box": { "border-size": 1, "border-color": "#000000", "bg-color": "#000000" }
    }
}
