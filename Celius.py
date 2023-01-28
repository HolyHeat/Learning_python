def convert_celius_fahrenheit(convert_temperature_celius):
    return convert_temperature_celius * 1.8 + 32


convert_temperature_celius = int(input("Enter Celius temperature : "))

print(str(convert_celius_fahrenheit(convert_temperature_celius)) + " is current temperature in Fahrenheit ")