import sys
import pandas as pd
import subprocess
import os

if len(sys.argv) != 2:
    print("Usage: load.py <path_to_dataset>")
    sys.exit(1)

dataset_path = sys.argv[1]
data = pd.read_csv(dataset_path)
print(data.head())

# Pass the data frame path to the next script (dpre.py)
subprocess.call(["python", "dpre.py", dataset_path])
# os.system(f"python dpre.py {dataset_path}")