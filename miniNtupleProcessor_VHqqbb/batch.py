import os
import time

# configName = "CombMassNewVtag"
# sampleList = ["WH", "ZH", "ttbar", "Wjets", "Zjets", "JZXW"]
sampleList = ["WH", "ZH", "ttbar", "Wjets", "Zjets"]

for sampleName in sampleList:
	if sampleName == "JZXW":
		nworkers = 200
	elif (sampleName == "WH") or (sampleName == "ZH"):
		nworkers = 70
	else:
		nworkers = 70

	# cmd = "python run.py -f %s -n %s" % (sampleName+"_"+configName, nworkers)
	cmd = "python run.py -f %s -n %s" % (sampleName, nworkers)
	print cmd
	os.system(cmd)
	time.sleep(2)

	cmd = "hadd hist_%s.root outputSys/FT/output/0.*/*.root" % (sampleName)
	print cmd
	os.system(cmd)
	time.sleep(2)
