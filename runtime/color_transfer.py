import cv2
import numpy as np


class ColorTransfer:

    def __init__(self):
        self.version = "Local Color Transfer Engine"


    def transfer(
        self,
        source,
        reference,
        strength=0.35
    ):

        source_float = source.astype(
            np.float32
        )

        reference_float = reference.astype(
            np.float32
        )


        source_mean = np.mean(
            source_float,
            axis=(0,1)
        )

        reference_mean = np.mean(
            reference_float,
            axis=(0,1)
        )


        adjustment = (
            reference_mean -
            source_mean
        )


        result = (
            source_float +
            adjustment * strength
        )


        return np.clip(
            result,
            0,
            255
        ).astype(
            np.uint8
        )
