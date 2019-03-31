bashCommand="wget http://www.geocities.jp/himaruya/"
import subprocess
import os
for x in os.listdir("../hetFolder"):
	process = subprocess.Popen((bashCommand+x).split(), stdout=subprocess.PIPE)
	output, error = process.communicate()