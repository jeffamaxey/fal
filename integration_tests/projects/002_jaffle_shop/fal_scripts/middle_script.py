import os
from functools import reduce
from main_check_2 import main_check

model_name = context.current_model.name

output = f"Model name: {model_name}"
output = f"{output}\nStatus: {context.current_model.status}\n"

output += f"top name: {__name__}\n"
output = main_check(output)
if __name__ == "__main__":
    output += "passed main if\n"

temp_dir = os.environ["temp_dir"]
print(temp_dir)
with open(reduce(os.path.join, [temp_dir, f"{model_name}.middle_script.txt"]), "w") as write_dir:
    write_dir.write(output)
