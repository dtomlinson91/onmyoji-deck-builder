import numpy
from PIL import Image, ImageDraw


def extract_image(filename: str, output_path: str, shikigami_name: str) -> None:
    """
    Extract a combat card from a screenshot from a device. Screenshot for each card
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

    # Convert to numpy array
    initial_image_array = numpy.asarray(initial_image)

    # Create mask polygon using points of the card border
    mask_polygon = [
        (788, 90),
        (788, 567),
        (515, 567),
        (515, 130),
        (496, 110),
        (496, 89),
        (513, 76),
        (523, 76),
        (528, 76),
        (536, 81),
        (651, 39),
        (652, 39),
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
    print(extracted_image.size)

    # crop
    extracted_image = extracted_image.crop((495, 38, 788, 567))

    # save the image
    extracted_image.save(
        f"{output_path}/{shikigami_name}-"
        f"{filename.split('/')[-1].split('.')[-2]}.png"
    )
