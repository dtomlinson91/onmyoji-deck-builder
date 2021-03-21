import glob

import numpy
from PIL import Image, ImageDraw


def extract_image(filename: str, output_path: str) -> None:
    """
    Extract a character card from a screenshot from a device. Screenshot for each card
    taken from the Shikigami page. Image will be resized and the card extracted.

    Args:
        filename (str): Full path to the input image.
        output_path (str): Full path to the directory where the image should be saved.
    """
    # Open the image, add alpha channel for transparency
    initial_image = Image.open(filename).convert("RGBA")

    # Check for size
    if initial_image.size[0] != 1304:
        basewidth = 1304
        wpercent = basewidth / float(initial_image.size[0])
        hsize = int((float(initial_image.size[1]) * float(wpercent)))
        initial_image = initial_image.resize((basewidth, hsize), Image.ANTIALIAS)
        # initial_image.save(f"{output_path}/{filename.split('/')[-1]}")
        # raise SystemExit

    # Convert to numpy array
    initial_image_array = numpy.asarray(initial_image)

    # Create mask polygon using points of the card border
    mask_polygon = [
        (768, 97),
        (768, 512),
        (534, 512),
        (534, 97),
        (559, 79),
        (580, 70),
        (604, 63),
        (631, 58),
        (651, 58),
        (652, 58),
        (671, 58),
        (698, 63),
        (722, 70),
        (745, 79),
    ]

    # Create the mask
    mask_image = Image.new(
        "L", (initial_image_array.shape[1], initial_image_array.shape[0]), 0
    )
    ImageDraw.Draw(mask_image).polygon(mask_polygon, outline=1, fill=1)
    mask = numpy.array(mask_image)

    # create a new empty image
    extracted_image_array = numpy.empty(initial_image_array.shape, dtype="uint8")

    # copy the colours from the first 3 columns
    extracted_image_array[:, :, :3] = initial_image_array[:, :, :3]

    # apply transparency to the alpha channel (4th column)
    extracted_image_array[:, :, 3] = mask * 255

    # convert back to an image
    extracted_image = Image.fromarray(extracted_image_array, "RGBA")

    # crop
    extracted_image = extracted_image.crop((533, 57, 769, 512))

    # save the image
    extracted_image.save(f"{output_path}/{filename.split('/')[-1].split('.')[-2]}.png")


if __name__ == "__main__":
    for image in glob.glob(
        "/Users/dtomlinson/git-repos/web-dev/onmyoji-deck-builder/."
        "image-extraction/images/characters/*.*"
    ):
        print(image)
        extract_image(
            image,
            "/Users/dtomlinson/git-repos/web-dev/onmyoji-deck-builder/."
            "image-extraction/images/characters/out",
        )
