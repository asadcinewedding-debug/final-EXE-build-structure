import cv2
import numpy as np


class FaceProtection:

    def __init__(self):
        self.name = "YuNet Face Protection"


    def create_face_mask(self, image):

        height, width = image.shape[:2]

        mask = np.zeros(
            (height, width),
            dtype=np.uint8
        )


        # placeholder face protection region
        # real YuNet detection will connect later

        center_x = width // 2
        center_y = height // 3


        cv2.ellipse(
            mask,
            (
                center_x,
                center_y
            ),
            (
                width//8,
                height//10
            ),
            0,
            0,
            360,
            255,
            -1
        )


        return mask



    def protect(
        self,
        original,
        relighted
    ):

        mask = self.create_face_mask(
            original
        )


        result = relighted.copy()


        result[mask > 0] = (
            original[mask > 0]
        )


        return result
