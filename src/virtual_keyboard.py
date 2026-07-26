from evdev import UInput, ecodes

"""This file holds the varible and this one only"""
virtual_keyboard = UInput({
    ecodes.EV_KEY: [
        # Letters A-Z
        30, 48, 46, 32, 18, 33, 34, 35, 23, 36,
        37, 50, 49, 38, 24, 25, 16, 19, 31, 20,
        22, 47, 17, 45, 21, 44,

        # Numbers 0-9
        11, 2, 3, 4, 5, 6, 7, 8, 9, 10,

        # Number row symbols
        12, 13,

        # Function keys F1-F12
        59, 60, 61, 62, 63, 64,
        65, 66, 67, 68, 87, 88,

        # Modifier keys
        29,   # Left Ctrl
        97,   # Right Ctrl
        42,   # Left Shift
        54,   # Right Shift
        56,   # Left Alt
        100,  # Right Alt / AltGr
        125,  # Left GUI / Windows
        126,  # Right GUI

        # Lock keys
        58,   # Caps Lock
        69,   # Num Lock
        70,   # Scroll Lock

        # Enter, Escape, Backspace, Tab, Space
        1,    # Escape
        14,   # Backspace
        15,   # Tab
        28,   # Enter
        57,   # Space

        # Punctuation keys
        39,   # ;
        40,   # '
        41,   # `
        51,   # ,
        52,   # .
        53,   # /
        43,   # Backslash
        26,   # [
        27,   # ]
        86,   # ISO extra key

        # Arrow/navigation keys
        103,  # Up
        108,  # Down
        105,  # Left
        106,  # Right
        102,  # Home
        107,  # End
        104,  # Page Up
        109,  # Page Down
        110,  # Insert
        111,  # Delete

        # Keypad
        71, 72, 73,
        75, 76, 77,
        79, 80, 81,
        82, 83,
        96,   # Keypad Enter

        # Multimedia/common special keys
        113,  # Mute
        114,  # Volume Down
        115,  # Volume Up
        116,  # Power
        117,  # Keypad =
        
        # Additional common keys
        119,  # Pause
        127,  # Menu
        183, 184, 185, 186
    ]
}, name="Mad Catz V.7 virtual keybinds keyboard")