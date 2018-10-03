import os
import sys
import subprocess
import pandas as pd
import numpy as np
from sklearn import preprocessing, neighbors
from sklearn.cluster import KMeans
np.set_printoptions(threshold=np.inf)


usage = "\nusage: python loader.py OUTFILE.pcap OUTFILE.csv"

if len(sys.argv) != 3:
	print(usage)

else:

	pcap = sys.argv[1]
	csv = sys.argv[2]
	n_features = 14
	n_clusters = 2

	command = """C:\\"Program Files"\\Wireshark\\tshark.exe -r """ + pcap + """ -T fields -e frame.number -e eth.src -e eth.dst -e frame.len -e frame.time_delta -e http.accept -e http.request -e http.cookie -e http.host -e ssl.handshake -e tcp.len -e tcp.flags -e tcp.ack -e tcp.analysis -E header=y -E separator=, -E quote=d -E occurrence=f > """ + csv

	print(command)

	gen_csv = subprocess.Popen(command, shell=True)
	gen_csv.wait()

	# ------------------------------------
	dataset = pd.read_csv("./" + csv)
	le = preprocessing.LabelEncoder()
	print(dataset)


	dataArray = [y for x in dataset.get_values() for y in x]
	print(dataArray)
	le.fit(dataArray)
	
	#print(le.classes_)
	#print("\n\n\n")
	#dataset = le.fit_transform(dataset)
	#dataset = dataset.tolist()

	#dataset = [dataset[i:i + n_features] for i in range(0, len(dataset), n_features)]
	#print(dataset)

	#kmeans = KMeans(n_clusters = n_clusters).fit(dataset)

	#print(kmeans.labels_)

	#testRow = [dataset[2931]]
	#print(le.inverse_transform(testRow))

	#prediction = kmeans.predict(testRow)
	#print(prediction)


