# Written By. Eun-Sol Kim
# If Filename does not start with 'fromWhatName',
# then change the name to 'toWhatNameReplace'.
# fileDirect: should contain exact directory for that folder


import glob, os

fileDirect = "/Users/eun-solkim/BBox-Label-Tool-master/"
fromWhatName = "DonotEnter"
toWhatNameReplace = ""

i = 0
for filename in os.listdir(fileDirect):
	if filename != ".DS_Store":
		if !filename.startswith(fromWhatName):
			os.rename(fileDirect + "%s" %(filename), fileDirect + toWhatNameReplace + "%d.JPEG" % (i))
	i += 1