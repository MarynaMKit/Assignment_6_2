import csv
import argparse
from convertor.temperature import convert_temperature
from convertor.distance import convert_distance


def get_user_data():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file",
                        help="input file name")
    parser.add_argument("-tm", "--temp_measurement",
                        help="target temperature measurement",
                        action="store")
    parser.add_argument("-dm", "--distance_measurement",
                        help="target distance measurement",
                        action="store")

    args = parser.parse_args()
    user_input = {"data_file": args.input_file,
                  "target_tm": args.temp_measurement,
                  "target_dm": args.distance_measurement}
    return user_input


user_input = get_user_data()

with open(user_input["data_file"], 'r') as file:
    reader = csv.DictReader(file)
    data_from_file = [row for row in reader]

for row in data_from_file:
    if user_input["target_dm"]:
        row["Distance"] = convert_distance(user_input["target_dm"],
                                           row["Distance"])
    if user_input["target_tm"]:
        row["Reading"] = convert_temperature(user_input["target_tm"],
                                             row["Reading"])

with open(f".out/{user_input['data_file']}_updated.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=data_from_file[0].keys())
    writer.writeheader()
    writer.writerows(data_from_file)
