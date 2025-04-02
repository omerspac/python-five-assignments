import streamlit as st

conversions = {
    "meters": {"kilometers": 0.001, "centimeters": 100, "millimeters": 1000, "miles": 0.000621371, "yards": 1.09361, "feet": 3.28084, "inches": 39.3701},
    "kilometers": {"meters": 1000, "miles": 0.621371, "yards": 1093.61, "feet": 3280.84, "inches": 39370.1},
    "centimeters": {"meters": 0.01, "millimeters": 10, "inches": 0.393701},
    "millimeters": {"meters": 0.001, "centimeters": 0.1, "inches": 0.0393701},
    "miles": {"meters": 1609.34, "kilometers": 1.60934, "yards": 1760, "feet": 5280, "inches": 63360},
    "yards": {"meters": 0.9144, "miles": 0.000568182, "feet": 3, "inches": 36},
    "feet": {"meters": 0.3048, "miles": 0.000189394, "yards": 0.333333, "inches": 12},
    "inches": {"meters": 0.0254, "centimeters": 2.54, "millimeters": 25.4, "feet": 0.0833333, "yards": 0.0277778},

    # Weight units
    "grams": {"kilograms": 0.001, "milligrams": 1000, "pounds": 0.00220462, "ounces": 0.035274},
    "kilograms": {"grams": 1000, "milligrams": 1_000_000, "pounds": 2.20462, "ounces": 35.274},
    "milligrams": {"grams": 0.001, "kilograms": 0.000001},
    "pounds": {"grams": 453.592, "kilograms": 0.453592, "ounces": 16},
    "ounces": {"grams": 28.3495, "kilograms": 0.0283495, "pounds": 0.0625},

    # Volume units
    "liters": {"milliliters": 1000, "cubic meters": 0.001, "gallons": 0.264172, "quarts": 1.05669, "pints": 2.11338, "cups": 4.22675, "fluid ounces": 33.814},
    "milliliters": {"liters": 0.001},
    "cubic meters": {"liters": 1000},
    "gallons": {"liters": 3.78541, "quarts": 4, "pints": 8, "cups": 16, "fluid ounces": 128},
    "quarts": {"liters": 0.946353, "gallons": 0.25, "pints": 2, "cups": 4, "fluid ounces": 32},
    "pints": {"liters": 0.473176, "gallons": 0.125, "quarts": 0.5, "cups": 2, "fluid ounces": 16},
    "cups": {"liters": 0.24, "gallons": 0.0625, "quarts": 0.25, "pints": 0.5, "fluid ounces": 8},
    "fluid ounces": {"liters": 0.0295735, "gallons": 0.0078125, "quarts": 0.03125, "pints": 0.0625, "cups": 0.125},

    # Temperature units
    "celsius": {},
    "fahrenheit": {},
    "kelvin": {}
}

def convert_temperature(value, unit_from, unit_to):
    if unit_from == "celsius":
        if unit_to == "fahrenheit":
            return (value * 9/5) + 32
        elif unit_to == "kelvin":
            return value + 273.15
    elif unit_from == "fahrenheit":
        if unit_to == "celsius":
            return (value - 32) * 5/9
        elif unit_to == "kelvin":
            return (value - 32) * 5/9 + 273.15
    elif unit_from == "kelvin":
        if unit_to == "celsius":
            return value - 273.15
        elif unit_to == "fahrenheit":
            return (value - 273.15) * 9/5 + 32
    return "Conversion not supported"

def convert_unit(value, unit_from, unit_to):
    if unit_from in conversions and unit_to in conversions[unit_from]:
        return value * conversions[unit_from][unit_to]
    elif unit_from in ["celsius", "fahrenheit", "kelvin"] and unit_to in ["celsius", "fahrenheit", "kelvin"]:
        return convert_temperature(value, unit_from, unit_to)
    else:
        return "Conversion not supported"

st.title("Unit Converter")

with st.form(key="unit_converter_form"):
    value = st.number_input("Enter the value to convert", value=1.0)
    unit_from = st.selectbox("Select the unit to convert from", list(conversions.keys()))
    unit_to = st.selectbox("Select the unit to convert to", list(conversions.keys()))

    submitted = st.form_submit_button("Convert")

if submitted:
    result = convert_unit(value, unit_from, unit_to)
    st.success(f"The converted value is {result}")
