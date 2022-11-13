# launchpad mini mk3 macros

simple lil program to add shortcuts to your launchpad

## installation

clone repo

```shell
$ git clone https://github.com/sniiz/lpminimk3-macropad
$ cd lpminimk3-macropad
```

install dependencies with pip - standard stuff right

```shell
$ pip3 install -r requirements.txt
```

# usage and configuration

open config.py in your editor of choice

```shell
$ nvim config.py
```

see instructions there

## config examples

undo & redo buttons

```shell
$ pip3 install pynput
```

```python
from pynput.keyboard import Key, Controller

controller = Controller()

def undo():
    controller.press(Key.ctrl)
    controller.press("z")
    controller.release("z")
    controller.release(Key.ctrl)

def redo():
    controller.press(Key.ctrl)
    controller.press("y")
    controller.release("y")
    controller.release(Key.ctrl)

config = {
    "buttons": [
        {
            "x": 2,
            "y": 0,
            "color": 3,
            "on_press": undo,
            "on_release": None,
        },
        {
            "x": 3,
            "y": 0,
            "color": 2,
            "on_press": redo,
            "on_release": None,
        },
    ]
}
```

"quick look" app

```python
import os

def open_app():
    os.system("open -a Notes")

def close_app():
    os.system("killall Notes")

config = {
    "buttons": [
        {
            "x": 8,
            "y": 1,
            "color": 12,
            "on_press": open_app,
            "on_release": close_app,
        },
    ]
}

```

(i'm out of ideas, feel free to pr)
