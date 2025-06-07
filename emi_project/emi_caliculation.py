def calculate_emi(principal, annual_rate, tenure_months):
    monthly_rate = annual_rate / (12 * 100)  # Convert annual rate to monthly decimal
    emi = principal * monthly_rate * ((1 + monthly_rate) ** tenure_months) / ((1 + monthly_rate) ** tenure_months - 1)
    return emi


def main():
    print("Welcome to the EMI Calculator!")
    try:
        principal = float(input("Enter the principal loan amount: "))
        annual_rate = float(input("Enter the annual interest rate (in %): "))
        tenure_months = int(input("Enter the loan tenure (in months): "))

        emi = calculate_emi(principal, annual_rate, tenure_months)
        total_payment = emi * tenure_months
        total_interest = total_payment - principal

        print(f"\nLoan Details:")
        print(f"Principal Amount: ₹{principal:,.2f}")
        print(f"Annual Interest Rate: {annual_rate}%")
        print(f"Loan Tenure: {tenure_months} months")
        print(f"\nCalculated EMI: ₹{emi:,.2f}")
        print(f"Total Payment (Principal + Interest): ₹{total_payment:,.2f}")
        print(f"Total Interest Payable: ₹{total_interest:,.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values for principal, interest rate, and tenure.")


if __name__ == "__main__":
    main()