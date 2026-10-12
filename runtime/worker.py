import sys
import os
from pathlib import Path


def main():

    print("AN AI Relight Runtime")
    print("Local AI Worker V6")


    if len(sys.argv) < 2:
        print("No input image")
        return


    input_file = Path(sys.argv[1])


    if not input_file.exists():
        print("Input file not found")
        return


    print("Processing:")
    print(input_file)


    output_dir = input_file.parent / "relight_output"

    output_dir.mkdir(
        exist_ok=True
    )


    print("AI pipeline ready")
    print("Output folder:")
    print(output_dir)



if __name__ == "__main__":
    main()
