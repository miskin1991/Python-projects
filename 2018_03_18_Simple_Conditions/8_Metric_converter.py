amount = float(input())
inputUnit = input()
outputUnit = input()


def convert_units_to_meter (input_value = 0.0, input_unit ="m"):
    if input_unit == "m":
        output_value = input_value
    elif input_unit == "mm":
        output_value = input_value / 1000.0
    elif input_unit == "cm":
        output_value = input_value / 100.0
    elif input_unit == "mi":
        output_value = input_value / 0.000621371192
    elif input_unit == "in":
        output_value = input_value / 39.3700787
    elif input_unit == "km":
        output_value = input_value / 0.001
    elif input_unit == "ft":
        output_value = input_value / 3.2808399
    elif input_unit == "yd":
        output_value = input_value / 1.0936133
    else:
        output_value = 0

    return output_value


def convert_meter_to_units (input_value = 0.0, output_unit ="m"):
    if output_unit == "m":
        output_value = input_value
    elif output_unit == "mm":
        output_value = input_value * 1000.0
    elif output_unit == "cm":
        output_value = input_value * 100.0
    elif output_unit == "mi":
        output_value = input_value * 0.000621371192
    elif output_unit == "in":
        output_value = input_value * 39.3700787
    elif output_unit == "km":
        output_value = input_value * 0.001
    elif output_unit == "ft":
        output_value = input_value * 3.2808399
    elif output_unit == "yd":
        output_value = input_value * 1.0936133
    else:
        output_value = 0.0

    return output_value


amountInMeters = convert_units_to_meter(float(amount),inputUnit)
amountInUnits = convert_meter_to_units(float(amountInMeters), outputUnit)
print("{0} {1}".format(amountInUnits, outputUnit))
