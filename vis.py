import pandas as pd
import sys
import subprocess
import matplotlib.pyplot as plt
import os

if len(sys.argv) != 2:
    print("Usage: vis.py <data_frame_path>")
    sys.exit(1)

data_frame_path = sys.argv[1]

data = pd.read_csv(data_frame_path)

education_counts = data['Education'].value_counts()
education_counts.plot(kind='bar', title='Education Distribution')
plt.xlabel('Education Level')
plt.ylabel('Count')

plt.savefig("vis.png")

subprocess.call(["python", "model.py", data_frame_path])
