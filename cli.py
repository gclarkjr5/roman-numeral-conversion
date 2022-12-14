import click
from roman_numerals_conversion.roman_numerals import (
    convert_roman_2_int,
    convert_int_2_roman,
)


# create a main group to create subcommands
@click.group()
def main():
    pass


# subcommands meant to be:
# - integer to roman numeral -> int_2_roman
# - roman numeral to integer -> roman_to_int
# int_2_roman accepts an integer
# roman_2_int accepts a roman numeral


# TODO: enforce argument type to alert user of bad argument


@main.command()
@click.argument("integer")
def int_2_roman(integer):
    result = convert_int_2_roman(integer)
    click.echo(f"converting {integer} to its roman numeral -> {result}")


@main.command()
@click.argument("roman_numeral")
def roman_2_int(roman_numeral):
    result = convert_roman_2_int(roman_numeral)
    click.echo(f"converting {roman_numeral} to its numeric integer -> {result}")


if __name__ == "__main__":
    main()
