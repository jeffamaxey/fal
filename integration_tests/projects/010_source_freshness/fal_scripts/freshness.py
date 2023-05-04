from typing import List
import os
from fal import DbtSource

# TODO add real test for freshness
sources: List[DbtSource] = list_sources()
output = "".join(
    f"({node.name}, {node.table_name}) {node.freshness.status}\n"
    for node in sources
    if node.freshness
)
temp_dir = os.environ["temp_dir"]
with open(os.path.join(temp_dir, "GLOBAL.freshness.txt"), "w") as write_dir:
    write_dir.write(output)
