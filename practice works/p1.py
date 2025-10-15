from abhi_library import FarToCel,CelToFar

far = int(input("Enter fahrenheit value: "))
cel = FarToCel(far)

print(f"The temperature in Celsius is: {cel:.2f}°C")

cel = int(input("Enter celsius value: "))
far = CelToFar(cel)
print(f"The temperature in Fahrenheit is: {far:.2f}°F")