# THM Security Footage Room
The new CTF blue room requires analysis of hundreds of packets, with each packet transporting a JFIF image containing a frame of the flag. To automate the extraction process, I made 2 simple scripts. The first one, extractor.py, extracts all the JFIF images from the
packet capture and puts them into an images/ directory. The second, Convert2VID.py, takes those images and stitches them into a video.
 
# Instructions
1. Clone the Repository
2. Create python Virutal envrironment and install packages with:\
   ```pip install -r requirements.txt```
3. Copy pcap file into the cloned repository (Alternatively, edit extractor.py and change ```pcap_file``` to absolute path to the pcap file)
4. Execute extractor.py
5. (OPTIONAL) Execute Convert2VID.py
