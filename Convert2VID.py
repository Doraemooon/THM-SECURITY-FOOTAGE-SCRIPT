import cv2
import os
import re

image_directory = "images/"
output_video_path = "flag.mp4"
fps=20

def extractNum(path):
	return int(re.findall(r"\d+", path)[0])

images = sorted([os.path.join(image_directory, f) for f in os.listdir(image_directory)], key=extractNum)

first_image = cv2.imread(images[0])
height, width, _ = first_image.shape
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

for filepath in images:
	image = cv2.imread(filepath)
	video.write(image)
	
video.release()
cv2.destroyAllWindows()

print("\033[92m{}\033[00m".format(f"SUCCESSFULLY CONVERTED IMAGES TO VIDEO, HAPPY HUNTING!!!"))
