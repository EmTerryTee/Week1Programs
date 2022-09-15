temp_in_c = 38.4


def convert_temp():
    return temp_in_c * 1.8 + 32


print(f'The current temperature is:\n{temp_in_c}°C or {convert_temp():.2f}°F')
