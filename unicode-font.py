import io
import json
import random
import sys

import click

def mocking_text(text):
    """Random capitalization"""
    random.seed()
    return "".join(map(lambda x: x.upper() if random.choice((True, False)) else x.lower(), text))

PROGRAMMATIC_ENCODERS = (
    mocking_text,
)

def font_encode(text, charmap, ignore_case=False):
    """Encode text with the given charmap"""
    output = []
    for char in text:
        if ignore_case:
            output.append(charmap.get(char.lower(), charmap.get(char.upper(), char)))
        else:
            output.append(charmap.get(char, char))
    return "".join(output)


@click.command()
@click.argument("instring", required=False)
@click.option("--font", help="Select font. by default will output all font variants")
@click.option("--list-fonts", help="Show font names + example text", is_flag=True)
@click.option("--ignore-case", help="Don't honor captialization", is_flag=True)
def main(instring=None, font=None, list_fonts=False, ignore_case=False):
    with io.open("fonts.json", "rt", encoding="utf8") as f:
        font_map = json.load(f)

    if font is not None:
        if font not in font_map:
            click.echo("font {} not supported".format(font))
            exit(-1)
        font_map = {font: font_map[font]}

    if list_fonts:
        example_text = "Lorum Ipsum 01234"
        for font, charmap in font_map.items():
            print("{} : {}".format(font, font_encode(example_text, charmap["charmap"], ignore_case)))
        exit(0)

    if not sys.stdin.isatty():
        # remove trailing whitespace, eg from 'echo'
        instring = sys.stdin.read().strip()

    if instring:
        for font, charmap in font_map.items():
            print(font_encode(instring, charmap["charmap"], ignore_case))
        for encoder in PROGRAMMATIC_ENCODERS:
            print(encoder(instring))

if __name__ == "__main__":
    main()
