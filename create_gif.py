import imageio
import glob 
from pathlib import Path
import cv2
import os
root = Path('/Users/rajatmodi/Downloads/2204')
images = []
filenames = glob.glob(str(root/'**/*.png'),recursive=True)
filenames+=glob.glob(str(root/'**/*.jpg'),recursive=True)
filenames+=glob.glob(str(root/'**/*.jpeg'),recursive=True)

# filenames = [root/d for d in os.listdir(str(root))]
for filename in filenames:
    try:
        img = imageio.imread(str(filename))
        img = cv2.resize(img, (224,224))
        print(filename)
        images.append(img)
    except:
        print("error")
imageio.mimsave('2204.gif', images,fps=1)