# Define conversion factors
CONVERSION_FACTORS = {
    'cm': {
        'm': 0.01,
        'km': 0.00001,
        'in': 0.393701,
        'ft': 0.0328084,
        'yd': 0.0109361,
        'mi': 0.00000621371,
    },
    'm': {
        'cm': 100,
        'km': 0.001,
        'in': 39.3701,
        'ft': 3.28084,
        'yd': 1.09361,
        'mi': 0.000621371,
    },
    'km': {
        'cm': 100000,
        'm': 1000,
        'in': 39370.1,
        'ft': 3280.84,
        'yd': 1093.61,
        'mi': 0.621371,
    },
    'in': {
        'cm': 2.54,
        'm': 0.0254,
        'km': 0.0000254,
        'ft': 0.0833333,
        'yd': 0.0277778,
        'mi': 0.0000157828,
    },
    'ft': {
        'cm': 30.48,
        'm': 0.3048,
        'km': 0.0003048,
        'in': 12,
        'yd': 0.333333,
        'mi': 0.000189394,
    },
    'yd': {
        'cm': 91.44,
        'm': 0.9144,
        'km': 0.0009144,
        'in': 36,
        'ft': 3,
        'mi': 0.000568182,
    },
    'mi': {
        'cm': 160934,
        'm': 1609.34,
        'km': 1.60934,
        'in': 63360,
        'ft': 5280,
        'yd': 1760,
    },
    'g': {
        'kg': 0.001,
        'oz': 0.035274,
        'lb': 0.00220462,
    },
    'kg': {
        'g': 1000,
        'oz': 35.274,
        'lb': 2.20462,
    },
    'oz': {
        'g': 28.3495,
        'kg': 0.0283495,
        'lb': 0.0625,
    },
    'lb': {
        'g': 453.592,
        'kg': 0.453592,
        'oz': 16,
    },
}

def convert(value, unit_from, unit_to):
    """Converts a value from one unit to another"""
    factor = CONVERSION_FACTORS[unit_from][unit_to]
    converted_value = value * factor
    return converted_value

# Get user input
value = float(input("Enter the value you want to convert: "))
unit_from = input("Enter the starting unit: ")
unit_to = input("Enter the unit you want to convert to: ")

# Convert the value
converted_value = convert(value, unit_from, unit_to)

# Display the result
print(f"{value} {unit_from} = {converted_value} {unit_to}")
