from datetime import datetime

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9 / 5 + 32

def get_temperature_category(celsius_val):
    if celsius_val < 0:
        return "Freezing"
    elif 0 <= celsius_val < 15:
        return "Cold"
    elif 15 <= celsius_val <= 25:
        return "Pleasant / Room Temperature"
    elif 26 <= celsius_val <= 38:
        return "Warm / Hot"
    else:
        return "Extreme Heat"

def get_valid_temperature(prompt, scale_name):
    while True:
        try:
            val = float(input(prompt).strip())
            if scale_name == "Celsius" and val < -273.15:
                print("Temperature cannot be below Absolute Zero (-273.15°C).")
                continue
            elif scale_name == "Fahrenheit" and val < -459.67:
                print("Temperature cannot be below Absolute Zero (-459.67°F).")
                continue
            elif scale_name == "Kelvin" and val < 0:
                print("Temperature cannot be below Absolute Zero (0 K).")
                continue
            return val
        except ValueError:
            print("Invalid input! Please enter a valid numerical value.")

def display_reference_table():
    print("\n" + "=" * 60)
    print(f"{'BENCHMARK':<26} {'CELSIUS':<12} {'FAHRENHEIT':<14} {'KELVIN'}")
    print("=" * 60)
    benchmarks = [
        ("Absolute Zero", -273.15, -459.67, 0.00),
        ("Freezing Point of Water", 0.00, 32.00, 273.15),
        ("Room Temperature", 20.00, 68.00, 293.15),
        ("Human Body Temperature", 37.00, 98.60, 310.15),
        ("Boiling Point of Water", 100.00, 212.00, 373.15),
    ]
    for name, c, f, k in benchmarks:
        print(f"{name:<26} {c:>7.2f}°C    {f:>8.2f}°F    {k:>8.2f} K")
    print("=" * 60)

def main():
    history_log = []
    print("\n" + "#" * 50)
    print("       TEMPERATURE CONVERTER")
    print("#" * 50)
    while True:
        print("\n" + "=" * 45)
        print("                 MAIN MENU")
        print("=" * 45)
        print("1. Celsius to Fahrenheit & Kelvin")
        print("2. Fahrenheit to Celsius & Kelvin")
        print("3. Kelvin to Celsius & Fahrenheit")
        print("4. View Standard Benchmark Reference Table")
        print("5. View Conversion History Log")
        print("6. Exit Application")
        print("=" * 45)
        choice = input("Enter your choice (1-6): ").strip()
        if choice == "1":
            celsius = get_valid_temperature(
                "Enter temperature in Celsius (°C): ",
                "Celsius"
            )
            fahr = celsius_to_fahrenheit(celsius)
            kelv = celsius_to_kelvin(celsius)
            feel = get_temperature_category(celsius)
            result_str = (
                f"{celsius:.2f}°C ==> {fahr:.2f}°F | "
                f"{kelv:.2f} K ({feel})"
            )

            print(f"\nResult: {result_str}")
            history_log.append({
                "time": datetime.now().strftime("%H:%M:%S"),
                "conversion": result_str
            })
        elif choice == "2":
            fahr = get_valid_temperature(
                "Enter temperature in Fahrenheit (°F): ",
                "Fahrenheit"
            )
            celsius = fahrenheit_to_celsius(fahr)
            kelv = fahrenheit_to_kelvin(fahr)
            feel = get_temperature_category(celsius)
            result_str = (
                f"{fahr:.2f}°F ==> {celsius:.2f}°C | "
                f"{kelv:.2f} K ({feel})"
            )

            print(f"\nResult: {result_str}")
            history_log.append({
                "time": datetime.now().strftime("%H:%M:%S"),
                "conversion": result_str
            })
        elif choice == "3":
            kelv = get_valid_temperature(
                "Enter temperature in Kelvin (K): ",
                "Kelvin"
            )
            celsius = kelvin_to_celsius(kelv)
            fahr = kelvin_to_fahrenheit(kelv)
            feel = get_temperature_category(celsius)
            result_str = (
                f"{kelv:.2f} K ==> {celsius:.2f}°C | "
                f"{fahr:.2f}°F ({feel})"
            )
            print(f"\nResult: {result_str}")

            history_log.append({
                "time": datetime.now().strftime("%H:%M:%S"),
                "conversion": result_str
            })
        elif choice == "4":
            display_reference_table()
        elif choice == "5":
            if not history_log:
                print("\nNo conversions recorded yet in this session.")
            else:
                print("\n" + "-" * 55)
                print("           RECENT CONVERSION HISTORY")
                print("-" * 55)
                for item in history_log:
                    print(f"[{item['time']}] {item['conversion']}")

                print("-" * 55)
        elif choice == "6":
            print("\nThank you for using the Temperature Converter!")
            print("Goodbye.\n")
            break
        else:
            print("\nInvalid option! Please choose between 1 and 6.")

if __name__ == "__main__":
    main()