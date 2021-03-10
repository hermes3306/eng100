import datetime;
import os;

def myswitch(x):
	return {
		'01': "66.sh",
		'02': "67.sh",
		'03': "68.sh",
		'04': "69.sh",
		'05': "70.sh",
		'06': "71.sh",
		'07': "72.sh",
		'08': "73.sh",
		'09': "74.sh",
		'10': "75.sh",
		'11': "76.sh",
		'12': "77.sh",
		'13': "78.sh",
		'14': "79.sh",
		'15': "80.sh",
		'16': "51.sh",
		'17': "52.sh",
		'18': "53.sh",
		'19': "54.sh",
		'20': "55.sh",
		'21': "56.sh",
		'22': "57.sh",
		'23': "58.sh",
		'23': "59.sh",
		'24': "60.sh",
		'25': "61.sh",
		'26': "62.sh",
		'27': "62.sh",
		'28': "63.sh",
		'29': "64.sh",
		'30': "65.sh",
		'31': "66.sh",
	}.get(x, "*.sh") #default

now = datetime.datetime.now()
print(now)

day = now.strftime("%d")
print(day)

print(myswitch(day))
os.system('/home/pi/Music/C/' + myswitch(day))

