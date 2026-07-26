from evdev import UInput, ecodes
import subprocess
import os
from pathlib import Path
import pwd


def run_script(s):
    user = os.environ["SUDO_USER"]
    user_info = pwd.getpwnam(user)

    uid = user_info.pw_uid
    home = Path(user_info.pw_dir)

    script_path = home / ".config/Mad-Catz.V.7-Interfact-Tool/script.sh"

    env = {
        "DISPLAY": ":0",
        "XDG_RUNTIME_DIR": f"/run/user/{uid}",
        "DBUS_SESSION_BUS_ADDRESS": f"unix:path=/run/user/{uid}/bus",
    }

    subprocess.run(
        [
            "sudo",
            "-u",
            user,
            "env",
            *[f"{k}={v}" for k, v in env.items()],
            "bash",
            str(script_path),
        ],
        check=True,
    )
"""This File holds the logic for doing actions"""

CONFIG_DIR_PATH = Path("/home/zeeh/.config/Mad-Catz.V.7-Interfact-Tool")

# https://github.com/torvalds/linux/blob/master/include/uapi/linux/input-event-codes.h
buttons = {
    (0x01, 0x00): [29],
    (0x02, 0x00): [31],
    (0x04, 0x00): [32],
    (0x08, 0x00): [33],
    (0x10, 0x00): [34],
    (0x20, 0x00): [35],
    (0x40, 0x00): [36],
    (0x80, 0x00): [37],

    (0x00, 0x01): [183],
    (0x00, 0x02): [184],
    (0x00, 0x04): [185],
    (0x00, 0x08): [186],
}

def check_config():
    if not CONFIG_DIR_PATH.exists:
        os.mkdir(CONFIG_DIR_PATH)


def press_keys(keys):
    pass

def press_key(kb, keycode):
    kb.write(ecodes.EV_KEY, keycode, 1)
    kb.syn()

    kb.write(ecodes.EV_KEY, keycode, 0)
    kb.syn()

def press_keys(kb, keys):
    for keycode in keys:
        kb.write(ecodes.EV_KEY, keycode, 1)
        kb.syn()
    for keycode in keys:
        kb.write(ecodes.EV_KEY, keycode, 0)
        kb.syn()