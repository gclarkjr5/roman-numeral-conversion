import click
from roman_numerals_conversion.roman_numerals import convert

@click.command()
# @click.option(
#     '--conversion',
#     '-c',
#     required=True,
#     type=click.Choice(['r_2_n', 'n_2_r'],
#     case_sensitive=False),
#     help='convert from roman numerals to numeric or vice versa'
# )
@click.option(
    '--input',
    '-i',
    required=True,
    help='the number to convert (should be a numeral or an integer)'
)

def convert_numerals(input):
    result = convert(input)
    print(result)

if __name__ == '__main__':
    convert_numerals()