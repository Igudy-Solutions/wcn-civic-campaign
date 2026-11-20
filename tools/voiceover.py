#!/usr/bin/env python3
"""Voiceover for the election reel, made with Kokoro (open TTS, Apache 2.0).

One WAV per scene into Specials/Election Reel/vo/, plus durations.json, which
tools/reel.py reads to time each scene to its line.

Model files (download once, about 350 MB) go in ~/kokoro/:
  https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx
  https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
  pip3 install kokoro-onnx soundfile

To use a real voice instead, record each line as vo/NN.wav and run
reel.py; it reads the lengths from the files.
"""
import json
import os
import soundfile as sf
from kokoro_onnx import Kokoro

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
VO = os.path.join(ROOT, "Specials", "Election Reel", "vo")
VOICE = os.environ.get("WCN_VOICE", "af_heart")
SPEED = 1.0

# Spelled the way it should be said. One line per scene.
# INEC is said as one word, "eye-neck", never spelled out.
LINES = [
    "Fifty seven days. Nigeria votes on Saturday, the sixteenth of January.",
    "In twenty twenty three, seventy three percent of registered voters stayed home.",
    "Turnout was twenty six point seven percent, the lowest since nineteen ninety nine. "
    "The race was won by about one point eight million votes.",
    "Now, over one hundred and three million Nigerians are registered. That includes you.",
    "Mark two Saturdays. January sixteenth, for President and the National Assembly. "
    "February sixth, for Governor and State Assembly.",
    "No P V C, no vote. Collect yours at your Eye-neck office, in person.",
    "Your vote is your voice. Don't sell it. Don't waste it.",
    "Show up. Follow World Changers Network.",
]


def main():
    os.makedirs(VO, exist_ok=True)
    home = os.path.expanduser("~/kokoro")
    k = Kokoro(os.path.join(home, "kokoro-v1.0.onnx"), os.path.join(home, "voices-v1.0.bin"))
    durs = []
    for i, line in enumerate(LINES, 1):
        audio, sr = k.create(line, voice=VOICE, speed=SPEED, lang="en-us")
        path = os.path.join(VO, f"{i:02d}.wav")
        sf.write(path, audio, sr)
        durs.append(round(len(audio) / sr, 2))
        print(f"  {i:02d}  {durs[-1]:5.2f}s  {line}")
    with open(os.path.join(VO, "durations.json"), "w") as fh:
        json.dump(durs, fh)


if __name__ == "__main__":
    main()
