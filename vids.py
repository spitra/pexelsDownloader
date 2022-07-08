import requests

#This script works to batch-download videos from pexels according to user specifications.
#Page var sets the initial page to start downloads from. Numvids var is used for naming conventions of downloaded video files.
page = 3
numvids = 155
API_KEY = '[YOUR KEY HERE]'
BASE_VIDEO_URL = 'https://api.pexels.com/videos'
#Json params for Pexels api. In this case set up to download nature timelapse videos. 
PARAMS = {'query' : 'nature timelapse', 'orientation' : 'landscape', 'size':'medium', 'page':page, 'per_page' : '80' }

#Api calls to get list of videos according to params. 
response = requests.get(f"{BASE_VIDEO_URL}/search", params=PARAMS, headers={'Authorization': API_KEY})
nextPage = response.json()['next_page']
videos = response.json()['videos']
#Initializing list for video urls for download later.
urls = []
#Prints out current stats w/ reminder to change vars when run again to prevent duplicates and file naming issues. 
print(f'STATS OF THIS RUNTIME: \n NUMVIDS:{numvids} \n PAGE: {page} \n REMEMBER TO CHANGE THESE NEXT TIME')
print('Getting links, hold tight!')
#Uses returned Json object containing each video's information, finds the url, and appends it to url list.
for vid in videos:
	for vidFile in vid['video_files']:	
		if vidFile['width'] == 1920 and vidFile['height'] == 1080:
			urls.append(vidFile['link'])
#Batch downloads videos found in 'url' list and saves them to pc. 			
print('Starting download, hold tight!')		
for link in urls:
	file_name = '[PATH TO DESTINATION FOLDER]' +'video' + str(numvids) + '.mp4'
	response = requests.get(link, stream=True)
	with open(file_name, 'wb') as f:
		for chunk in response.iter_content(chunk_size = 1024 * 1024):
			if chunk:
				f.write(chunk)
	numvids += 1

print('Done!')
