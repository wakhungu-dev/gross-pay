# program to compute temperature in Celsius
def celcius_to_fahrenheit():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius * 9/5 + 32
    # display the result
    print(f"Temperature in Fahrenheit: {fahrenheit}")

if __name__ == "__main__":
    celcius_to_fahrenheit()