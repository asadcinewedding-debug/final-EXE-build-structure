import sys
from pathlib import Path
import cv2

from light_engine import LightEngine
from face_protection import FaceProtection
from color_transfer import ColorTransfer


def process_image(input_path):

    image = cv2.imread(str(input_path))

    if image is None:
        raise RuntimeError("Cannot read input image")

    light_engine = LightEngine()
    face_protection = FaceProtection()
    color_transfer = ColorTransfer()

    # create cinematic light transformation
    relighted = light_engine.apply_light(
        image,
        strength=0.25
    )

    # transfer color mood
    colored = color_transfer.transfer(
        image,
        relighted,
        strength=0.35
    )

    # restore protected face details
    final = face_protection.protect(
        image,
        colored
    )

    output = input_path.parent / "relight_output"
    output.mkdir(exist_ok=True)

    output_file = output / f"{input_path.stem}_relight.jpg"

    cv2.imwrite(
        str(output_file),
        final
    )

    return output_file


def main():

    print("AN AI Relight Runtime")
    print("Local AI Worker V6")

    if len(sys.argv) < 2:
        print("No input image")
        return 1

    input_file = Path(sys.argv[1])

    if not input_file.exists():
        print("Input file not found")
        return 2

    print("Processing:", input_file)

    result = process_image(input_file)

    print("Completed")
    print("Output:", result)

    return 0


if __name__ == "__main__":
    main()
