def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

def inches_to_centimeters(inches):
    centimeters = inches * 2.54
    return centimeters

def centimeters_to_inches(centimeters):
    inches = centimeters / 2.54
    return inches

# Temperature Conversion
print("Temperature Conversion:")
fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius} degrees Celsius.")

celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")

# Measurement Conversion
print("\nMeasurement Conversion:")
inches = float(input("Enter the measurement in inches: "))
centimeters = inches_to_centimeters(inches)
print(f"{inches} inches is equal to {centimeters} centimeters.")

centimeters = float(input("Enter the measurement in centimeters: "))
inches = centimeters_to_inches(centimeters)
print(f"{centimeters} centimeters is equal to {inches} inches.")
