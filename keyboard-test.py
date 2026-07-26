import hid
import time
import os
from evdev import UInput, ecodes

ui = UInput({
    ecodes.EV_KEY: [
        29, 30, 31, 32, 33, 34, 35, 36, 37, 47,
        183, 184, 185, 186
    ]
}, name="Mad Catz V.7 virtual keyboard")



def press_key(keycode):
    ui.write(ecodes.EV_KEY, keycode, 1)
    ui.syn()

    ui.write(ecodes.EV_KEY, keycode, 0)
    ui.syn()

def press_keys(keys):
    for keycode in keys:
        ui.write(ecodes.EV_KEY, keycode, 1)
        ui.syn()
    for keycode in keys:
        ui.write(ecodes.EV_KEY, keycode, 0)
        ui.syn()


# Mad Catz V.7 buttons -> Linux keycodes
# https://github.com/torvalds/linux/blob/master/include/uapi/linux/input-event-codes.h
buttons = {
    (0x01, 0x00): [29, 47],
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


def find_mad_catz_control_interface():
    for d in hid.enumerate():
        product = (d.get("product_string") or "").lower()

        if "mad" in product or "v.7" in product:
            print(
                "Found:",
                d.get("product_string"),
                "path:",
                d["path"],
                "interface:",
                d.get("interface_number")
            )

            # Macro button interface
            if d.get("interface_number") == 1:
                return d["path"]

    return None


path = find_mad_catz_control_interface()

if path is None:
    raise RuntimeError(
        "Mad Catz V.7 control HID interface not found"
    )


dev = hid.device()

try:
    print("Opening:", path)

    dev.open_path(path)

    print("Ready. Press Mad Catz buttons...")

    while True:
        try:
            report = dev.read(64)

            if report:
                key_code = tuple(report[-2:])
                key = buttons.get(key_code)

                if key is not None:
                    print("Button:", key_code, "-> keycode:", key)
                    press_keys(key)

                    # prevent duplicate triggers
                    time.sleep(0.05)
        except:
            pass

except KeyboardInterrupt:
    print("\nStopping...")

finally:
    try:
        dev.close()
    except Exception:
        pass