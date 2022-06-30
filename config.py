# see examples in readme.md
config = {
    "buttons": [],
    # the keymaps themselves
    # example:
    # {
    #     "x": 0,
    #     "y": 0,
    #     "color": 3, # white
    #     "on_press": lambda: print("pressed"),
    #     "on_release": lambda: print("released")
    # }
    # note: you can leave on_release as None if you don't want to do anything
    # but you will need to define on_press

    "use_rgb": False,
    # whether to use rgb or proprietary color codes fo the button colors
    # refer to https://github.com/FMMT666/launchpad.py#color-codes

    "convert_rgb": False,
    # the launchpad mini mk3 uses a 0-63 scale instead of 0-255 for rgb values
    # this converts the rgb values to 0-63
    # refer to https://github.com/FMMT666/launchpad.py#ledctrlxybyrgb-x-y-colorlist-mode-
}
