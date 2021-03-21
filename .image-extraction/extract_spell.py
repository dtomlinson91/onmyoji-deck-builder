import numpy
from PIL import Image, ImageDraw


def extract_image(filename: str, output_path: str, shikigami_name: str) -> None:
    """
    Extract a spell card from a screenshot from a device. Mask is valid for 1304x603
    screenshot from an iPhone 12 Pro.

    Args:
        filename (str): Full path to the input image.
        output_path (str): Full path where the image should be saved.
    """
    # Open the image, add alpha channel for transparency
    initial_image = Image.open(filename).convert("RGBA")

    # Check for size
    if initial_image.size[0] != 1304:
        basewidth = 1304
        wpercent = basewidth / float(initial_image.size[0])
        hsize = int((float(initial_image.size[1]) * float(wpercent)))
        initial_image = initial_image.resize((basewidth, hsize), Image.ANTIALIAS)

    # Convert to numpy array
    initial_image_array = numpy.asarray(initial_image)

    # Create mask polygon using points of the card border (iPhone 12 Pro screenshot)
    mask_polygon = [
        (535, 60),
        (768, 60),
        (788, 85),
        (788, 567),
        (515, 567),
        (515, 130),
        (496, 110),
        (496, 91),
        (513, 73),
        (523, 73),
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
    extracted_image = extracted_image.crop((496, 59, 788, 567))

    # save the image
    extracted_image.save(
        f"{output_path}/{shikigami_name}-"
        f"{filename.split('/')[-1].split('.')[-2]}.png"
    )
