"""speak.py
Uses pyttsx3 to speak a short message aloud."""

import pyttsx3


def main():
    engine = pyttsx3.init()
    engine.say("Hello, your code is working!")
    engine.runAndWait()


if __name__ == "__main__":
    main()
