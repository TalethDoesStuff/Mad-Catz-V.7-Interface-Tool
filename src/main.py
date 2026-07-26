from evdev import UInput, ecodes
from virtual_keyboard import virtual_keyboard
import actions
import hid
import time


def find_mad_catz_control_interface():
    """Returns the control interface path else returns None"""
    for d in hid.enumerate():
        product = (d.get("product_string") or "").lower()

        if "mad" in product and "v.7" in product:
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


def connect():
    while True:
        keyboard_path = find_mad_catz_control_interface()

        if keyboard_path:
            try:
                dev = hid.device()
                dev.open_path(keyboard_path)

                print("Connected:", keyboard_path)
                return dev

            except Exception as e:
                print("Connection failed:", e)

        print("Waiting for Mad Catz...")
        time.sleep(1)


if __name__ == "__main__":

    dev = connect()

    try:
        print("Ready. Press Mad Catz buttons...")

        while True:
            try:
                report = dev.read(64)

                if report:
                    key_code = tuple(report[-2:])
                    key = actions.buttons.get(key_code)

                    if key is not None:
                        print(
                            "Button:",
                            key_code,
                            "-> keycode:",
                            key
                        )
                        if key_code == (2, 0):
                            actions.run_script("")
                        else:
                            actions.press_keys(
                                virtual_keyboard,
                                key
                            )

                        # prevent duplicate triggers
                        time.sleep(0.05)

            except Exception as e:
                print("Device disconnected:", e)

                try:
                    dev.close()
                except:
                    pass

                dev = connect()

    except KeyboardInterrupt:
        print("\nStopping...")

    finally:
        try:
            dev.close()
        except:
            pass