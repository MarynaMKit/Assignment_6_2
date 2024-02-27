from convertor.temperature import subtract_measurement


def convert_meeters_to_feet(input_distance: float):
    output_distance = input_distance/0.3048
    return round(output_distance, 2)


def convert_feet_to_meeters(input_distance: float):
    output_distance = input_distance*0.3048
    return round(output_distance, 2)


def convert_distance(measure_format: str, distance_data: str):
    if measure_format == 'm':
        if 'm' in distance_data:
            return distance_data
        else:
            num_to_convert = subtract_measurement(distance_data)
            converted_num = convert_feet_to_meeters(num_to_convert)
            output_data = str(converted_num)+'m'
            return output_data
    if measure_format == 'ft':
        if 'ft' in distance_data:
            return distance_data
        else:
            num_to_convert = subtract_measurement(distance_data)
            converted_num = convert_meeters_to_feet(num_to_convert)
            output_data = str(converted_num)+'ft'
            return output_data
