import pandas as pd
import sys
from sklearn.cluster import KMeans
import subprocess

if len(sys.argv) != 2:
    print("Usage: model.py <data_frame_path>")
    sys.exit(1)

data_frame_path = sys.argv[1]

data = pd.read_csv(data_frame_path)

selected_columns = data[['Year_Birth', 'Z_CostContact', 'Z_Revenue', 'Response']]

kmeans = KMeans(n_clusters=3, n_init=10)

kmeans.fit(selected_columns)


cluster_labels = kmeans.labels_

cluster_counts = pd.Series(cluster_labels).value_counts().sort_index()

cluster_counts.to_csv("k.txt", header=False, sep="\t")

subprocess.call(["bash", "final.sh"])
