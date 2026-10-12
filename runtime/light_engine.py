import cv2
import numpy as np


class LightEngine:

    def __init__(self):
        self.version = "V6 Local Relight Engine"


    def create_light_map(self, image):

        height, width = image.shape[:2]

        # soft cinematic light field
        y, x = np.mgrid[0:height, 0:width]

        center_x = width * 0.5
        center_y = height * 0.35

        distance = np.sqrt(
            (x-center_x)**2 +
            (y-center_y)**2
        )

        light = 1 - (
            distance /
            distance.max()
        )


        light = np.clip(
            light,
            0,
            1
        )


        return light.astype(
            np.float32
        )



    def apply_light(
        self,
        image,
        strength=0.35
    ):

        light_map = self.create_light_map(
            image
        )


        result = image.astype(
            np.float32
        )


        for c in range(3):

            result[:,:,c] += (
                light_map *
                255 *
                strength
            )


        return np.clip(
            result,
            0,
            255
        ).astype(
            np.uint8
        )
