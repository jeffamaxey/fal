import os
from functools import reduce

model_name = context.current_model.name if context.current_model else "GLOBAL"

output = f"Model name: {model_name}"

temp_dir = os.environ["temp_dir"]
print(temp_dir)
with open(reduce(os.path.join, [temp_dir, f"{model_name}.after.txt"]), "w") as write_dir:
    write_dir.write(output)
