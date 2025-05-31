import importlib.metadata

def get_version(pkg_name):
    try:
        return importlib.metadata.version(pkg_name)
    except importlib.metadata.PackageNotFoundError:
        return "Not installed"
    except Exception as e:
        return f"Error: {e}"

import numpy as np
import flask
import tensorflow as tf
import cv2
from PIL import Image

print("Library Versions:")
print("-----------------")
print("socketio version:", get_version("python-socketio"))
print("eventlet version:", get_version("eventlet"))
print("NumPy version:", np.__version__)
print("Flask version:", flask.__version__)
print("TensorFlow version:", tf.__version__)
print("Pillow (PIL) version:", Image.__version__)
print("OpenCV version:", cv2.__version__)
print("base64: standard library (no version)")
print("io: standard library (no version)")