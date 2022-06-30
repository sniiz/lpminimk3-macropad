# this file does not need to be edited
# shortcuts are mapped in config.py
from launchpad_py import LaunchpadMiniMk3
from config import config

print("starting...")
pad = LaunchpadMiniMk3()
pad.Open()
print("started!")


def main():
    pressed = []

    pad.LedAllOn(0)
    if config["use_rgb"]:
        for button in config["buttons"]:
            pad.LedCtrlXYByRGB(button["x"], button["y"], button["color"])
    else:
        for button in config["buttons"]:
            pad.LedCtrlXYByCode(button["x"], button["y"], button["color"])

    while 1:
        press = pad.ButtonStateXY()
        if press:
            if press[-1]:
                pressed.append(press[:-1])
                for button in config["buttons"]:
                    if button["x"] == press[0] and button["y"] == press[1]:
                        button["on_press"]()
            else:
                if press[:-1] in pressed:
                    pressed.remove(press[:-1])
                    for button in config["buttons"]:
                        if button["x"] == press[0] and button["y"] == press[1]:
                            if button["on_release"]:
                                button["on_release"]()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pad.LedAllOn(0)
        pad.LedSetMode(0)
        pad.Close()
        exit()
    except Exception as e:
        pad.LedAllOn(0)
        pad.LedSetMode(0)
        pad.Close()
        raise e
