def convert_celsius_to_fahrenheit(input_temp: float):
    res = 1.8 * input_temp + 32
    return round(res, 2)


def convert_fahrenheit_to_celsius(input_temp: float):
    res = (5/9) * (input_temp - 32)
    return round(res, 2)


def subtract_measurement(s: str) -> int:
    res = ''
    for i in s:
        if i.isdigit():
            res += i
    return int(res)


def convert_temperature(measure_format: str, temp_data: str):
    if measure_format == 'C':
        if 'C' in temp_data:
            return temp_data
        else:
            num_to_convert = subtract_measurement(temp_data)
            converted_num = convert_fahrenheit_to_celsius(num_to_convert)
            output_data = str(converted_num)+'°C'
            return output_data
    if measure_format == 'F':
        if 'F' in temp_data:
            return temp_data
        else:
            num_to_convert = subtract_measurement(temp_data)
            converted_num = convert_celsius_to_fahrenheit(num_to_convert)
            output_data = str(converted_num)+'°F'
            return output_data
