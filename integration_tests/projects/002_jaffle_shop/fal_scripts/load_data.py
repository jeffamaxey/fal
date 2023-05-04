import pandas as pd
import io
import os
from functools import reduce

model_name = context.current_model.name

output = f"Model name: {model_name}"
output = output + f"\nStatus: {context.current_model.status}"

temp_dir = os.environ["temp_dir"]
with open(reduce(os.path.join, [temp_dir, model_name + ".load_data.txt"]), "w") as write_dir:
    write_dir.write(output)
