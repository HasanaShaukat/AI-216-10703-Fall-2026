def calculate_percentage(obtained, total):
    if total <= 0:
        raise ValueError("Total marks must be greater than 0.")

    if obtained < 0:
        raise ValueError("Obtained marks cannot be negative.")

    if obtained > total:
        raise ValueError("Obtained marks cannot be greater than total marks.")

    return (obtained / total) * 100


try:
    obtained = float(input("Enter obtained marks: "))
    total = float(input("Enter total marks: "))

except ValueError:
    print("Invalid input. Please enter numeric values.")

else:
    try:
        percentage = calculate_percentage(obtained, total)
    except ValueError as error:
        print("Error:", error)
    else:
        print("Percentage:", percentage)

finally:
    print("Percentage calculation completed.")