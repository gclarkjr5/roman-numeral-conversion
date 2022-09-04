import click
from roman_numerals_conversion.roman_numerals import convert


@click.command()
@click.option(
    "--input",
    "-i",
    required=True,
    help="the number to convert (should be a numeral or an integer)",
)
def main(input):
    """main entry point"""
    result = convert(input)
    print(result)


if __name__ == "__main__":
    main()
