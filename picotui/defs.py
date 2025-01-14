# Colors

C_BLACK    = 0
C_RED      = 1
C_GREEN    = 2
C_YELLOW   = 3
C_BLUE     = 4
C_MAGENTA  = 5
C_CYAN     = 6
C_WHITE    = 7
ATTR_INTENSITY = 8
C_GRAY     = C_BLACK | ATTR_INTENSITY
C_B_RED      = C_RED | ATTR_INTENSITY
C_B_GREEN    = C_GREEN | ATTR_INTENSITY
C_B_YELLOW   = C_YELLOW | ATTR_INTENSITY
C_B_BLUE     = C_BLUE | ATTR_INTENSITY
C_B_MAGENTA  = C_MAGENTA | ATTR_INTENSITY
C_B_CYAN     = C_CYAN | ATTR_INTENSITY
C_B_WHITE    = C_WHITE | ATTR_INTENSITY

def C_PAIR(fg, bg):
    return (bg << 4) + fg

# Keys

KEY_UP = 1
KEY_DOWN = 2
KEY_LEFT = 3
KEY_RIGHT = 4
KEY_HOME = 5
KEY_END = 6
KEY_PGUP = 7
KEY_PGDN = 8
KEY_QUIT = 9
KEY_ENTER = 10
KEY_BACKSPACE = 11
KEY_DELETE = 12
KEY_TAB = b"\t"
KEY_SHIFT_TAB = b"\x1b[Z"
KEY_ESC = 20
KEY_F1 = 30
KEY_F2 = 31
KEY_F3 = 32
KEY_F4 = 33
KEY_F5 = b'\x1b[15~'
KEY_F6 = b'\x1b[17~'
KEY_F7 = b'\x1b[18~'
KEY_F8 = b'\x1b[19~'
KEY_F9 = b'\x1b[20~'
KEY_F10 = b'\x1b[21~'

VIM_KEYMAP = {
str.encode('k'): KEY_UP,
str.encode('j'): KEY_DOWN,
str.encode('h'): KEY_LEFT,
str.encode('l'): KEY_RIGHT
# b"\x1b[5~": KEY_PGUP, // ctrl+d, ctrl+u?
# b"\x1b[6~": KEY_PGDN,
}

KEYMAP = {
b"\x1b[A": KEY_UP,
b"\x1b[B": KEY_DOWN,
b"\x1b[D": KEY_LEFT,
b"\x1b[C": KEY_RIGHT,
b"\x1b[H": KEY_HOME,
b"\x1b[F": KEY_END,
b"\x1bOH": KEY_HOME,
b"\x1bOF": KEY_END,
b"\x1b[1~": KEY_HOME,
b"\x1b[4~": KEY_END,
b"\x1b[5~": KEY_PGUP,
b"\x1b[6~": KEY_PGDN,
b"\x03": KEY_QUIT,
b"\r": KEY_ENTER,
b"\x7f": KEY_BACKSPACE,
b"\x1b[3~": KEY_DELETE,
b"\x1b": KEY_ESC,
b"\x1bOP": KEY_F1,
b"\x1bOQ": KEY_F2,
b"\x1bOR": KEY_F3,
b"\x1bOS": KEY_F4,
}

# Unicode symbols in UTF-8

# DOWNWARDS ARROW
DOWN_ARROW = b"\xe2\x86\x93"
# BLACK DOWN-POINTING TRIANGLE
DOWN_TRIANGLE = b"\xe2\x96\xbc"
