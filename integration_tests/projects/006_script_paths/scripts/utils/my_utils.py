import os
from functools import reduce


def write_data(data, model_name):
    temp_dir = os.environ["temp_dir"]

    with open(reduce(os.path.join, [temp_dir, f"{model_name}.after.txt"]), "w") as write_dir:
        write_dir.write(data)
