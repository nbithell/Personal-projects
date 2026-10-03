MIDDLE_HOURS: float = 3.5
CLOSING_HOURS: float = 5.75
RATE_OF_PAY: float = 10.85

middle_shifts = int(input("Enter the amount of middle shifts you have worked "))
closing_shifts = int(input("Enter the amount of closing shifts you have worked "))

middle_hours = middle_shifts * MIDDLE_HOURS
closing_hours = closing_shifts * CLOSING_HOURS

total_hours = middle_hours + closing_hours

overall_pay = total_hours * RATE_OF_PAY

print(f"Your total hours worked {total_hours}")
print(f"Your pay is £{overall_pay:.2f}")

