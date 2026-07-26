import hid
import time

buttons = {
    (0x01, 0x00): "C1",
    (0x02, 0x00): "C2",
    (0x04, 0x00): "C3",
    (0x08, 0x00): "C4",
    (0x10, 0x00): "C5",
    (0x20, 0x00): "C6",
    (0x40, 0x00): "C7",
    (0x80, 0x00): "C8",

    (0x00, 0x01): "C9",
    (0x00, 0x02): "C10",
    (0x00, 0x04): "C11",
    (0x00, 0x08): "C12",
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

            # Mad Catz V.7 macro/control HID interface
            # change to the value shown by the print above if needed
            if d.get("interface_number") == 1:
                return d["path"]

    return None


path = find_mad_catz_control_interface()

if path is None:
    raise RuntimeError("Mad Catz V.7 control HID interface not found")


dev = hid.device()

try:
    print("Opening:", path)
    dev.open_path(path)

    while True:
        r = dev.read(64)

        if r:
            key_code = tuple(r[-2:])
            button = buttons.get(key_code)

            if button:
                print(button)

except KeyboardInterrupt:
    print("Stopping...")

finally:
    try:
        dev.close()
    except Exception:
        pass