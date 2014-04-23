# Albert Haque
# TwitchPlaysPokemon convert raw data into xml-like format
# April 2014

input_file = open("tpp_rdf_log1.xml","r")
output_file = open("tpp_rdf_log1-full.xml","w")

# Loads the entire file into memory, careful
lines = input_file.readlines()

currentLine = 0
for line in lines:
	if "<DELIMIT>" in line:
		parts = line.split()
		date = parts[0]
		time = parts[1]
		username = parts[2].replace("<DELIMIT>","").replace(":","")
		message = line[line.find("<DELIMIT>")+10:].rstrip("\n")
		output_file.write("<date>" + date + "</date><time>" + time + "</time><user>" + username + "</user><msg>" + message + "</msg>\n")
	else:
		output_file.write(line)

input_file.close()
output_file.close()
