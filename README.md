This test is designed to evaluate some necessary development skills. It tests the tester's ability to use github, install required packages, basic debugging and ablity to learn things they don't know, if necessary. Feel free to use any tools you like, including chatgpt! 

For this task, we are cleaning up our tracker code to make it run faster, and with that, we are switching to the torch.Dataloader class for dataset management. 

0) download the images in this email, you can use these as your test images 
1) download the repo
2) Install the required packages, I've included an env.yml for a conda environment if you want to initialize from there, or you can use the requrements.txt file (untested by me) 
3) run the main.py code on the images from the email.  
  - The resulting images should be saved in the 'output' folder in the github directory. These are images preprocessed with our current dataloader. 
4) Next, we want to add the LetterBox augmentation function from the yolov5 package to our preprocessing, but we are getting an error implementing it.
  - note: the yolov5 package should be installed from step 2, but depending on your system, you might need to install it manually ('pip install yolov5' worked for this) 
  - pull the ‘development’ branch of the repo, and run main again. The only changes to the code base from the branch change are two lines of code in CustomDataset.py:
     1) importing the letterbox function from the yolov5 package (line 10) 
     2) adding the letterbox function to our yolov5dataset transform (line 18)
6) Fix the error that occurs with this addition, so that it produces the preprocessed images again. You can edit main or CustomDataset.py
7) Email the final images back to me! 
