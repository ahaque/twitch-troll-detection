# Albert Haque
# This converts the TwitchPlaysPokemon logs downloaded
# from online into an xml-like format
# April 2014

input_file = open("tpp_logs/tpp_2.log","r")
output_file = open("tpp-web-2.xml","w")

# Loads the entire file into memory, careful
lines = input_file.readlines()

currentLine = 0
for line in lines:
    # If the line is about someone (dis)connecting to IRC, ignore it
    if "-!-" in line:
        continue
    # If this line was partially formatted by me previously (I added the <DELIMIT> tag)
	if "<DELIMIT>" in line:
		parts = line.split()
		date = parts[0]
		time = parts[1]
		username = parts[2].replace("<DELIMIT>","").replace(":","")
		message = line[line.find("<DELIMIT>")+10:].rstrip("\n")
		output_file.write("<date>" + date + "</date><time>" + time + "</time><user>" + username + "</user><msg>" + message + "</msg>\n")
		# If this line is a true, untouched line in the format:
		# YYYY-MM-DD HH:MM(:SS(:ms)) <USERNAME> message-till-end-of-line
    else:
			parts = line.split()
			date = parts[0]
			if "2014-02-17" in date or "2014-02-18" in date or "2014-02-19" in date:
				time = parts[1]
				username = parts[2][1:-1]
				message = line[line.find(">")+2:].rstrip("\n")
				output_file.write("<date>" + date + "</date><time>" + time + "</time><user>" + username + "</user><msg>" + message + "</msg>\n")

input_file.close()
output_file.close()
