from passlib.hash import sha512_crypt
from itertools import permutations
import sys
from time import time

filename = "shadow"

start = time()


#possible date of births in a year are '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
#'21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'.
DOB = ['01', '20', '07','30','23', '04', '29', '05', '08',  '17', '18', '19'] #All possible DOB used by each groups

#possible month of births in a year are '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'
MOB = ['10', '07','12', '06', '03','08','11', '04', '05',] #All possible MOB used by each groups

#Using the hint given we know each group has a constant 5 characters(2 DOB, 2 MOB & 1 special character). Hence 5 characters was
#removed from each hint to get the number of characters of the firstname for each group.
#grp1 = ['terah', 'itunu', 'osele', 'judah']
grp1 = ['judah'] #After social engineering & to minimize program running time 
#grp2 = ['kelechi' ,'osigomu']
grp2 = ['osigomu'] #After social engineering & to minimize program running time 
grp3 = ['ilerioluwakiiye']
grp4 = ['nzubechi']
#grp5 = ['hilary', 'donald', 'victor', 'samuel']
grp5 = ['donald'] #After social engineering & to minimize program running time 
grp6 = ['macauley']
#grp7 = ['samuel', 'joseph']
grp7 = ['joseph'] #After social engineering & to minimize program running time 
#grp8 = ['ekene', 'ahmed', 'tosin']
grp8 = ['ahmed'] #After social engineering & to minimize program running time 
#grp9 = ['favour', 'daniel']
grp9 = ['favour'] #After social engineering & to minimize program running time 
#grp10 = ['damilola', 'emmanuel', 'chinenye']
grp10 = ['damilola'] #After social engineering & to minimize program running time 
grp11 = ['chiamaka']

#prompt user to input group number
grp = input("</>Please input a group number>>>>>>>>>>>>>>>>>>> ")

def extract_info(name_of_file):
	f = open(name_of_file,"r")
	lines = f.read().split()
	f.close()
	
	usernames = []
	salts = []
	hashes = []
	select_user = []
	select_hash = []
	select_salt = []

	for line in lines:
		if "$6" in line:
			sections = line.split("$") 
			usernames.append(sections[0].split(":")[0]) 
			salts.append(sections[2]) 
			hashes.append(sections[3].split(":")[0])
	#To seperate each groups username, hashed paswords and salts and append to diffferent lists
	if grp == "1":
		select_user.append(usernames[0])
		select_hash.append(hashes[0])
		select_salt.append(salts[0])
	elif grp == "2":
		select_user.append(usernames[1])
		select_hash.append(hashes[1])
		select_salt.append(salts[1])
	elif grp == "3":
		select_user.append(usernames[2])
		select_hash.append(hashes[2])
		select_salt.append(salts[2])
	elif grp == "4":
		select_user.append(usernames[3])
		select_hash.append(hashes[3])
		select_salt.append(salts[3])
	elif grp == "5":
		select_user.append(usernames[4])
		select_hash.append(hashes[4])
		select_salt.append(salts[4])
	elif grp == "6":
		select_user.append(usernames[5])
		select_hash.append(hashes[5])
		select_salt.append(salts[5])
	elif grp == "7":
		select_user.append(usernames[6])
		select_hash.append(hashes[6])
		select_salt.append(salts[6])
	elif grp == "8":
		select_user.append(usernames[7])
		select_hash.append(hashes[7])
		select_salt.append(salts[7])
	elif grp == "9":
		select_user.append(usernames[8])
		select_hash.append(hashes[8])
		select_salt.append(salts[8])
	elif grp == "10":
		select_user.append(usernames[9])
		select_hash.append(hashes[9])
		select_salt.append(salts[9])
	elif grp == "11":
		select_user.append(usernames[10])
		select_hash.append(hashes[10])
		select_salt.append(salts[10])
 
	return select_user, select_salt, select_hash

#passing filename into function extract_info and placing the returned values inside (username, salts, hashes) 
(username, salts, hashes) = extract_info(filename)

def find_password(usernames, salts, hashes):

	#All special possible special characters to be used are "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", ",", ".", "<", ">", "/", "?", "+", "="
	special_char = ["@","%","+","#","?","=","!","<"] #All special characters used by each groups
			
	decodedusernames = [] 
	decodedpasswords = []

	if grp == "1":
		for n in grp1:
			for d in DOB:
				for m in MOB:
					for c in special_char:
						# permu = permutations([n,c,'05','28'],4)
						permu = permutations([n,d,m,c],4)
						for p in list(permu):
							newpass = ''.join(p);
							for i in range(len(hashes)):
								if hashes[i] == sha512_crypt.using(rounds=5000, salt=salts[i]).hash(newpass).split("$")[-1]:
									decodedusernames.append(usernames[i])
									decodedpasswords.append(newpass)
									print("Decoded login:")
									print("############################################################")
									print(decodedusernames[i]+" Password is: "+decodedpasswords[i])
									print("############################################################")
									end = time()
									timer = end - start
									print("time: "+str(timer)+"s")
									sys.exit()
								# else:
								# 	print(usernames[i]+" password is not "+newpass)
	elif grp == "2":
		for n in grp2:
			for d in DOB:
				for m in MOB:
					for c in special_char:
						# permu = permutations([n,c,'05','28'],4)
						permu = permutations([n,d,m,c],4)
						for p in list(permu):
							newpass = ''.join(p);
							for i in range(len(hashes)):
								if hashes[i] == sha512_crypt.using(rounds=5000, salt=salts[i]).hash(newpass).split("$")[-1]:
									decodedusernames.append(usernames[i])
									decodedpasswords.append(newpass)
									print("Decoded login:")
									print("############################################################")
									print(decodedusernames[i]+" Password is: "+decodedpasswords[i])
									print("############################################################")
									end = time()
									timer = end - start
									print("time: " +str(timer)+"s")
									sys.exit()
								# else:
								# 	print(usernames[i]+" password is not "+newpass)
	elif grp == "3":
		for n in grp3:
			for d in DOB:
				for m in MOB:
					for c in special_char:
						# permu = permutations([n,c,'05','28'],4)
						permu = permutations([n,d,m,c],4)
						for p in list(permu):
							newpass = ''.join(p);
							for i in range(len(hashes)):
								if hashes[i] == sha512_crypt.using(rounds=5000, salt=salts[i]).hash(newpass).split("$")[-1]:
									decodedusernames.append(usernames[i])
									decodedpasswords.append(newpass)
									print("Decoded login:")
									print("############################################################")
									print(decodedusernames[i]+" Password is: "+decodedpasswords[i])
									print("############################################################")
									end = time()
									timer = end - start
									print("time: "+str(timer)+"s")
									sys.exit()
								# else:
								# 	print(usernames[i]+" password is not "+newpass)					
	elif grp == "4":
		for n in grp4:
			for d in DOB:
				for m in MOB:
					for c in special_char:
						# permu = permutations([n,c,'05','28'],4)
						permu = permutations([n,d,m,c],4)
						for p in list(permu):
							newpass = ''.join(p);
							for i in range(len(hashes)):
								if hashes[i] == sha512_crypt.using(rounds=5000, salt=salts[i]).hash(newpass).split("$")[-1]:
									decodedusernames.append(usernames[i])
									decodedpasswords.append(newpass)
									print("Decoded login:")
									print("############################################################")
									print(decodedusernames[i]+" Password is: "+decodedpasswords[i])
									print("############################################################")
									end = time()
									timer = end - start
									print("time: "+str(timer)+"s")
									sys.exit()
								# else:
								# 	print(usernames[i]+" password is not "+newpass)						
	elif grp == "5":
		for n in grp5:
			for d in DOB:
				for m in MOB:
					for c in special_char:
						# permu = permutations([n,c,'05','28'],4)
						permu = permutations([n,d,m,c],4)
						for p in list(permu):
							newpass = ''.join(p);
							for i in range(len(hashes)):
								if hashes[i] == sha512_crypt.using(rounds=5000, salt=salts[i]).hash(newpass).split("$")[-1]:
									decodedusernames.append(usernames[i])
									decodedpasswords.append(newpass)
									print("Decoded login:")
									print("############################################################")
									print(decodedusernames[i]+" Password is: "+decodedpasswords[i])
									print("############################################################")
									end = time()
									timer = end - start
									print("time: "+str(timer)+"s")
									sys.exit()
								# else:
								# 	print(usernames[i]+" password is not "+newpass)					
	elif grp == "6":
		for n in grp6:
			for d in DOB:
				for m in MOB:
					for c in special_char:
						# permu = permutations([n,c,'05','28'],4)
						permu = permutations([n,d,m,c],4)
						for p in list(permu):
							newpass = ''.join(p);
							for i in range(len(hashes)):
								if hashes[i] == sha512_crypt.using(rounds=5000, salt=salts[i]).hash(newpass).split("$")[-1]:
									decodedusernames.append(usernames[i])
									decodedpasswords.append(newpass)
									print("Decoded login:")
									print("############################################################")
									print(decodedusernames[i]+" Password is: "+decodedpasswords[i])
									print("############################################################")
									end = time()
									timer = end - start
									print("time: "+str(timer)+"s")
									sys.exit()
								# else:
								# 	print(usernames[i]+" password is not "+newpass)								
	elif grp == "7":
		for n in grp7:
			for d in DOB:
				for m in MOB:
					for c in special_char:
						# permu = permutations([n,c,'05','28'],4)
						permu = permutations([n,d,m,c],4)
						for p in list(permu):
							newpass = ''.join(p);
							for i in range(len(hashes)):
								if hashes[i] == sha512_crypt.using(rounds=5000, salt=salts[i]).hash(newpass).split("$")[-1]:
									decodedusernames.append(usernames[i])
									decodedpasswords.append(newpass)
									print("Decoded login:")
									print("############################################################")
									print(decodedusernames[i]+" Password is: "+decodedpasswords[i])
									print("############################################################")
									end = time()
									timer = end - start
									print("time: "+str(timer)+"s")
									sys.exit()
								# else:
								# 	print(usernames[i]+" password is not "+newpass)							
	elif grp == "8":
		for n in grp8:
			for d in DOB:
				for m in MOB:
					for c in special_char:
						# permu = permutations([n,c,'05','28'],4)
						permu = permutations([n,d,m,c],4)
						for p in list(permu):
							newpass = ''.join(p);
							for i in range(len(hashes)):
								if hashes[i] == sha512_crypt.using(rounds=5000, salt=salts[i]).hash(newpass).split("$")[-1]:
									decodedusernames.append(usernames[i])
									decodedpasswords.append(newpass)
									print("Decoded login:")
									print("############################################################")
									print(decodedusernames[i]+" Password is: "+decodedpasswords[i])
									print("############################################################")
									end = time()
									timer = end - start
									print("time: "+str(timer)+"s")
									sys.exit()
#								else:
#									print(usernames[i]+" password is not "+newpass)						
	elif grp == "9":
		for n in grp9:
			for d in DOB:
				for m in MOB:
					for c in special_char:
						# permu = permutations([n,c,'05','28'],4)
						permu = permutations([n,d,m,c],4)
						for p in list(permu):
							newpass = ''.join(p);
							for i in range(len(hashes)):
								if hashes[i] == sha512_crypt.using(rounds=5000, salt=salts[i]).hash(newpass).split("$")[-1]:
									decodedusernames.append(usernames[i])
									decodedpasswords.append(newpass)
									print("Decoded login:")
									print("############################################################")
									print(decodedusernames[i]+" Password is: "+decodedpasswords[i])
									print("############################################################")
									end = time()
									timer = end - start
									print("time: "+str(timer)+"s")
									sys.exit()
#								else:
#									print(usernames[i]+" password is not "+newpass)									
	elif grp == "10":
		for n in grp10:
			for d in DOB:
				for m in MOB:
					for c in special_char:
						# permu = permutations([n,c,'05','28'],4)
						permu = permutations([n,d,m,c],4)
						for p in list(permu):
							newpass = ''.join(p);
							for i in range(len(hashes)):
								if hashes[i] == sha512_crypt.using(rounds=5000, salt=salts[i]).hash(newpass).split("$")[-1]:
									decodedusernames.append(usernames[i])
									decodedpasswords.append(newpass)
									print("Decoded login:")
									print("############################################################")
									print(decodedusernames[i]+" Password is: "+decodedpasswords[i])
									print("############################################################")
									end = time()
									timer = end - start
									print("time: "+str(timer)+"s")
									sys.exit()
#								else:
#									print(usernames[i]+" password is not "+newpass)					
	elif grp == "11":
		for n in grp11:
			for d in DOB:
				for m in MOB:
					for c in special_char:
						# permu = permutations([n,c,'05','28'],4)
						permu = permutations([n,d,m,c],4)
						for p in list(permu):
							newpass = ''.join(p);
						
							# Finally, we iterate through our hashes in the shadow file and check for comparisms
							for i in range(len(hashes)):
								if hashes[i] == sha512_crypt.using(rounds=5000, salt=salts[i]).hash(newpass).split("$")[-1]:
									decodedusernames.append(usernames[i])
									decodedpasswords.append(newpass)
									print("Decoded login:")
									print("############################################################")
									print(decodedusernames[i]+" Password is: "+decodedpasswords[i])
									print("############################################################")
									end = time()
									timer = end - start
									print("time: "+str(timer)+"s")
									sys.exit()
#								else:
#									print(usernames[i]+" password is not "+newpass)
	else:
		print("############################################################")
		print("invalid input please re-run the program and try again")
		print("############################################################")
		sys.exit()

# calling and passing parameters in find_password 
find_password(username, salts, hashes)

		

		
	
