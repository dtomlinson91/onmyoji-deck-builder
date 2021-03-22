import glob

import extract_combat
import extract_spell
import extract_form
import extract_field

SHIKIGAMI_NAME = "kodokushi"


def main(shikigami_name: str):
    # combat cards
    for image in glob.glob(
        "/Users/dtomlinson/git-repos/web-dev/onmyoji-deck-builder/."
        "image-extraction/images/combat/*.*"
    ):
        print(image)
        extract_combat.extract_image(
            image,
            "/Users/dtomlinson/git-repos/web-dev/onmyoji-deck-builder/."
            "image-extraction/images/combat/out",
            shikigami_name,
        )

    # spell cards
    for image in glob.glob(
        "/Users/dtomlinson/git-repos/web-dev/onmyoji-deck-builder/."
        "image-extraction/images/spells/*.*"
    ):
        print(image)
        extract_spell.extract_image(
            image,
            "/Users/dtomlinson/git-repos/web-dev/onmyoji-deck-builder/."
            "image-extraction/images/spells/out",
            shikigami_name,
        )

    # form cards
    for image in glob.glob(
        "/Users/dtomlinson/git-repos/web-dev/onmyoji-deck-builder/."
        "image-extraction/images/forms/*.*"
    ):
        print(image)
        extract_form.extract_image(
            image,
            "/Users/dtomlinson/git-repos/web-dev/onmyoji-deck-builder/."
            "image-extraction/images/forms/out",
            shikigami_name,
        )

    # field cards
    for image in glob.glob(
        "/Users/dtomlinson/git-repos/web-dev/onmyoji-deck-builder/."
        "image-extraction/images/fields/*.*"
    ):
        print(image)
        extract_field.extract_image(
            image,
            "/Users/dtomlinson/git-repos/web-dev/onmyoji-deck-builder/."
            "image-extraction/images/fields/out",
            shikigami_name,
        )


if __name__ == "__main__":
    main(SHIKIGAMI_NAME)
