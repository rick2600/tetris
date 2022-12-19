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

FPS            = 13
FPS_INC        = 30
RATE           = 5


DEFAULT_THEME = {
    "bg-color": "#2e2e2e",
    "wall": { "bg-color": "#d6d6d6", "border-size": 1, "border-color": "#2e2e2e" },
    "empty": { "bg-color": "#2e2e2e", "border-size": 1, "border-color": "#2e2e2e" },
    "I": { "bg-color": "#6c99bb", "border-size": 1, "border-color": "#2e2e2e" },
    "T": { "bg-color": "#b05279", "border-size": 1, "border-color": "#2e2e2e" },
    "O": { "bg-color": "#9e86c8", "border-size": 1, "border-color": "#2e2e2e" },
    "Z": { "bg-color": "#e87d3e", "border-size": 1, "border-color": "#2e2e2e" },
    "S": { "bg-color": "#e87d3e", "border-size": 1, "border-color": "#2e2e2e" },
    "L": { "bg-color": "#b4d273", "border-size": 1, "border-color": "#2e2e2e" },
    "J": { "bg-color": "#b4d273", "border-size": 1, "border-color": "#2e2e2e" },
    "score": {
        "label": { "font-size": 24, "font-color": "#d6d6d6" },
        "value": { "font-size": 24, "font-color": "#d6d6d6" },
        "box": { "border-size": 1, "border-color": "#d6d6d6", "bg-color": "#2e2e2e" }
    },
    "next-piece": {
        "label": { "font-size": 24, "font-color": "#d6d6d6" },
        "box": { "border-size": 1, "border-color": "#d6d6d6", "bg-color": "#2e2e2e" }
    },
    "controls": {
        "label": { "font-size": 24, "font-color": "#d6d6d6" },
        "value": { "font-size": 16, "font-color": "#d6d6d6" },
        "box": { "border-size": 1, "border-color": "#d6d6d6", "bg-color": "#2e2e2e" }
    },
    "status": {
        "value": { "font-size": 24, "font-color": "#d6d6d6" }
    },
    "refs": ["https://gist.github.com/r-malon/8fc669332215c8028697a0bbfbfbb32a"]
}

