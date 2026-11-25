#!/usr/bin/env python3
"""Download the exact Kokoro voice model the campaign videos use.

The model is 325 MB, over GitHub's 100 MB file limit, so it is not stored in
the repo. This fetches the same pinned release (kokoro-onnx model-files-v1.0)
into ~/kokoro/ and checks the SHA-256 of each file, so everyone ends up with
byte-for-byte the same voice as the published videos.

    python3 tools/get_voice_model.py
    pip3 install kokoro-onnx soundfile
"""
import hashlib
import os
import urllib.request

BASE = "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/"
FILES = {
    "kokoro-v1.0.onnx": "7d5df8ecf7d4b1878015a32686053fd0eebe2bc377234608764cc0ef3636a6c5",
    "voices-v1.0.bin": "bca610b8308e8d99f32e6fe4197e7ec01679264efed0cac9140fe9c29f1fbf7d",
}
DEST = os.path.expanduser("~/kokoro")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    os.makedirs(DEST, exist_ok=True)
    for name, want in FILES.items():
        path = os.path.join(DEST, name)
        if os.path.exists(path) and sha256(path) == want:
            print(f"ok      {name}")
            continue
        print(f"get     {name} ...")
        urllib.request.urlretrieve(BASE + name, path + ".part")
        got = sha256(path + ".part")
        if got != want:
            os.remove(path + ".part")
            raise SystemExit(f"{name}: checksum mismatch ({got}), not saved")
        os.replace(path + ".part", path)
        print(f"ok      {name}")
    print("Voice model ready in", DEST, "(voice used: af_heart)")


if __name__ == "__main__":
    main()
