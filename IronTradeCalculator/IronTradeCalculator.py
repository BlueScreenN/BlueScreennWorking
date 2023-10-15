import math

results = []
total_vat = 0

while True:
    try:
        iron_type = int(input("Please select the type of iron 1-Full Length, 2-Rod, 3-Cut: "))
        if iron_type not in [1, 2, 3]:
            print("Invalid option. Please select 1, 2, or 3.")
            continue

        if iron_type == 1:
            iron_type = "Full Length"
            weight, thickness_in_mm = map(float, input("Please enter the weight (in kilograms) and thickness (in millimeters) of Full Length iron: ").split())
            quantity = None
        elif iron_type == 2:
            iron_type = "Rod"
            weight, thickness_in_mm = map(float, input("Please enter the weight (in kilograms) and thickness (in millimeters) of Rod iron: ").split())
            quantity = None
        elif iron_type == 3:
            iron_type = "Cut"
            quantity_option = int(input("Please enter 1 for quantity or 2 for weight: "))

            if quantity_option == 1:
                quantity, thickness_in_mm, length = map(float, input("Please enter the quantity, thickness (in millimeters), and length: ").split())
                weight = None
            elif quantity_option == 2:
                weight, thickness_in_mm, length = map(float, input("Please enter the weight (in kilograms), thickness (in millimeters), and length: ").split())
                quantity = None
            else:
                print("Invalid option. Please select 1 or 2.")
                continue

        first_price, first_kilogram = map(float, input("Enter the first price and kilograms: ").split())
        second_price, second_kilogram = map(float, input("Enter the second price and kilograms: ").split())

        first_price_factor = first_price * first_kilogram / 1000
        second_price_factor = second_price * second_kilogram / 1000
        first_price_divided = first_price_factor / 1.2 * 1.1
        second_price_divided = second_price_factor / 1.2 * 1.1

        vat_2 = (first_price_factor - first_price_divided) + (second_price_factor - second_price_divided)

        result_1 = (first_kilogram * first_price / 1.2) * 1.1
        result_2 = (second_kilogram * second_price / 1.2) * 1.1

        if iron_type == "Cut":
            results.append({
                "Iron Type": iron_type,
                "Quantity": quantity,
                "Thickness (mm)": thickness_in_mm,
                "Result 1": result_1,
                "Result 2": result_2,
                "Total Result": result_1 + result_2
            })
        else:
            results.append({
                "Iron Type": iron_type,
                "Weight (kg)": weight,
                "Thickness (mm)": thickness_in_mm,
                "Result 1": result_1,
                "Result 2": result_2,
                "Total Result": result_1 + result_2
            })

        total_vat += math.ceil(vat_2)

    except ValueError:
        print("Possibly incorrect data was entered, please try again!")
        continue

    continue_option = input("Would you like to make another entry? (Y/N): ")
    if continue_option.lower() != "y":
        break

# Display the results
for i, result in enumerate(results, start=1):
    print(f"\nProduct {i}")
    for key, value in result.items():
        if value is not None:
            print(f"{key}: {value}")

if len(results) == 1:
    print("\nVAT Value: ", total_vat)
elif len(results) >= 2:
    print("\nTotal VAT: ", total_vat)
    print("VAT, the withholding tax amount you need to pay to the tax office: '{}'".format(total_vat))

print("\nIron Construction Transport Industry and Trade Ltd.")


