# Program to compute gross pay based on user input
def compute_gross_pay():
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    pay = hours * rate
    print(f"Pay: {pay}")

if __name__ == "__main__":
    compute_gross_pay()
# End of program
