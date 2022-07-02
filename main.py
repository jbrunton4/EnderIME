# !/usr/bin/env

# Import the pynput module for key capture and simulation
from pynput import keyboard
from pynput.keyboard import Key, Controller
from os import system, remove
from time import sleep
from sys import exit

# create a keyboard controller to simulate typing
kb = Controller()

# define the key
ender_key = {
    "a": "⏃",
    "b": "⏚",
    "c": "☊",
    "d": "⎅",
    "e": "⟒",
    "f": "⎎",
    "g": "☌",
    "h": "⊑",
    "i": "⟟",
    "j": "⟊",
    "k": "☍",
    "l": "⌰",
    "m": "⋔",
    "n": "⋏",
    "o": "⍜",
    "p": "⌿",
    "q": "☌",
    "r": "⍀",
    "s": "⌇",
    "t": "⏁",
    "u": "⎍",
    "v": "⎐",
    "w": "⍙",
    "x": "⌖",
    "y": "⊬",
    "z": "⋉",
}

# create a counter for killing the program
esc_count = 0


def on_press(key: Key) -> None:

    # if esc key is pressed 5 times, quit the program
    global esc_count
    if key == Key.esc:
        esc_count += 1
    else:
        esc_count = 0
    if esc_count >= 5:
        print("\007")
        exit(0)

    # letter substitution
    try:
        if key.char.lower() not in list(ender_key.keys()):
            return

        kb.press(Key.backspace)
        kb.release(Key.backspace)

        kb.type(ender_key[key.char.lower()])
    except AttributeError:  # if the key does not have an associated character
        pass


def main() -> None:

    # show an info box for escaping the program
    with open("temp.vbs", "w") as fh:
        fh.write('x = MsgBox("Press ESC 5 times to exit the IME. A sound will be played when exiting.", 0, "Info")')
    system("start temp.vbs")
    sleep(0.1)
    remove("temp.vbs")

    # listen for key presses, and on press, run the substitution function
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=None
    )
    listener.start()
    listener.join()


# run if not imported
if __name__ == "__main__":
    main()
