import glob

import numpy
from PIL import Image, ImageDraw


def extract_image(filename: str, output_path: str, shikigami_name: str) -> None:
    """
    Extract a field card from a screenshot from a device. Screenshot for each card
    taken from the Hyakabun scrollery. Image will be resized and the card extracted.

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
        (788, 68),
        (788, 568),
        (515, 568),
        (515, 130),
        (495, 112),
        (491, 104),
        (491, 96),
        (495, 88),
        (515, 72),
        (515, 68),
        (500, 46),
        (499, 46),
        (499, 43),
        (502, 43),
        (512, 47),
        (523, 49),
        (534, 51),
        (550, 52),
        (567, 52),
        (584, 53),
        (719, 53),
        (736, 52),
        (753, 52),
        (769, 51),
        (774, 50),
        (779, 49),
        (785, 48),
        (790, 47),
        (794, 46),
        (803, 43),
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
    extracted_image = extracted_image.crop((490, 42, 803, 568))

    # save the image
    extracted_image.save(
        f"{output_path}/{shikigami_name}-"
        f"{filename.split('/')[-1].split('.')[-2]}.png"
    )
