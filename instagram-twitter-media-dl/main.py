// pip install gallery-dl
import gallery_dl
 
url = input("Enter Instagram or Twitter post URL: ")
gallery_dl.job.DownloadJob(url).run()
 
print("Download complete! Check the 'gallery-dl' folder.")