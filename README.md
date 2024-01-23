0) download the images in this email, you can use these as your test images 
1) download the repo
2) Install the required packages, I've included an env.yml for a conda environement if you want to initialize from there, or you can read it and install things the way you prefer.
3) run the main.py code on the images from the email.  The result should be images preprocessed with our current dataloader
4) now, we want to add the LetterBox augmentation function from the yolov5 package to our preprocessing, but we are getting an error implementing it.  	- install the yolov5 package 	- pull the ‘development’ branch of the repo, and run main again.
   * Branch info: The only changes to the code base from the branch change are two lines of code in CustomDataset.py:
     1) importing the letterbox function from the yolov5 package
     2)adding the letterbox function to our yolov5dataset class
5) fix the bug so that it produces the preprocessed images again
Email the images back to me! 
