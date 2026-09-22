import os
from pathlib import Path

MODEL_PATH = Path(
    os.getenv(
        "DEHAZING_MODEL_PATH",
        Path(__file__).resolve().parents[2] / "Nilesh_cycleGAN_dehaze_saved_model",
    )
)
model = None


def get_model():
    """Load and return the dehazing model once, when image processing needs it."""
    global model
    if model is None:
        import tensorflow as tf
        from keras.layers import TFSMLayer

        model = TFSMLayer(str(MODEL_PATH), call_endpoint="serving_default")
    return model