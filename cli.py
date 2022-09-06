import click
from conversion.roman_numerals import convert_roman_2_int, convert_int_2_roman


@click.group()
def main():
    pass


@main.command()
@click.argument("integer")
def int_2_roman(integer):
    result = convert_int_2_roman(integer)
    click.echo(f"converting {integer} to its roman numeral -> {result}")
    # convert_integer(integer)


@main.command()
@click.argument("roman_numeral")
def roman_2_int(roman_numeral):
    result = convert_roman_2_int(roman_numeral)
    click.echo(f"converting {roman_numeral} to its numeric integer -> {result}")


if __name__ == "__main__":
    main()
