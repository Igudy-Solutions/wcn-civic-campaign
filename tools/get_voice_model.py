#!/usr/bin/env python3
"""Download the exact Kokoro voice model the campaign videos use.

The model is 325 MB, over GitHub's 100 MB file limit for git, so it is kept on
this repo's Releases page (tag voice-model-v1.0) instead of in the git tree.
This fetches that pinned copy (same files as kokoro-onnx model-files-v1.0)
into ~/kokoro/ and checks the SHA-256 of each file, so everyone ends up with
byte-for-byte the same voice as the published videos.

    python3 tools/get_voice_model.py
    pip3 install kokoro-onnx soundfile
"""
import hashlib
import os
import urllib.request

# Copy kept on this repo's own Releases page (tag voice-model-v1.0); the
# upstream kokoro-onnx release is the fallback. Same files, same checksums.
SOURCES = [
    "https://github.com/Igudy-Solutions/wcn-civic-campaign/releases/download/voice-model-v1.0/",
    "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/",
]
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
        for base in SOURCES:
            try:
                urllib.request.urlretrieve(base + name, path + ".part")
            except OSError as err:
                print(f"        {base}: {err}")
                continue
            got = sha256(path + ".part")
            if got == want:
                os.replace(path + ".part", path)
                break
            os.remove(path + ".part")
            print(f"        {base}: checksum mismatch ({got})")
        else:
            raise SystemExit(f"{name}: no source gave the right file, not saved")
        print(f"ok      {name}")
    print("Voice model ready in", DEST, "(voice used: af_heart)")


if __name__ == "__main__":
    main()
