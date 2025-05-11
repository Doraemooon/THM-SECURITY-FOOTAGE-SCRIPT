import pyshark
import os

image_directory = 'images/'
image_counter = 1
cap = pyshark.FileCapture('security-footage-1648933966395.pcap', display_filter='frame.len gt 10000')

if not os.path.exists(image_directory):  #Make a directory to store the extracted images
	print(f"Making directory: {image_directory}")
	os.makedirs(image_directory)
	
if os.listdir(image_directory):  #Check if the directory is empty. If it is not empty CLEAR the directory
	print("Directory to store extracted images is not empty. Proceeding with removal...")
	existing_images = os.listdir(image_directory)
	for f in existing_images:
		file_path = os.path.join(image_directory, f)
		print(f"Removing: {file_path}")
		os.remove(file_path)

def findImage(load):  #Extract the JFIF image part only from each packet
	index = load.find('ffd8ff')
	if index != -1:
		return load[index:]
		
def toImage(hex_value, value):  #Write the JFIF hex image data to file
	filename = image_directory + f"image{value}.jpg"
	byte_data = bytes.fromhex(hex_value)
	with open(filename, 'wb') as f:
		f.write(byte_data)
	print(f"Successfully extracted image to image{value}.jpg")

for packets in cap:
	payload = packets.tcp.payload.split(':')  #The output seperates hex values with ':'. We have to remove.
	payload = ''.join(payload)
	toImage(findImage(payload), image_counter)
	image_counter += 1

print("\033[92m{}\033[00m".format(f"ALL IMAGE EXTRACTED TO {image_directory}, HAPPY HUNTING!!!"))
