import zipfile

from PIL import Image
import pytesseract
import cv2 as cv
import numpy as np

# loading the face detection classifier
face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')

# the rest is up to you!
import zipfile

from PIL import Image
import pytesseract
import cv2 as cv
import numpy as np
import os

# loading the face detection classifier
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')


# the rest is up to you!
def get_all_file_paths(directory):
    # initializing empty file paths list
    file_paths = []

    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    # returning all file paths
    return file_paths


z = zipfile.ZipFile("small_img.zip", 'r')
z.printdir()
z.extractall("./test")

imagePaths = get_all_file_paths("./test")
# imagePaths = [imagePaths[0]]
imagesTuples = []
for p in imagePaths:
    img = cv.imread(p)
    # img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # img = cv.resize(img, (1024, 1024))
    imagesTuples.append([img, "", p])

for i, imagesTuple in enumerate(imagesTuples):
    img = Image.fromarray(imagesTuple[0])
    # display(img)
    text = pytesseract.image_to_string(img)
    imagesTuples[i][1] = text
for i, imagesTuple in enumerate(imagesTuples):
    faces = face_cascade.detectMultiScale(imagesTuple[0], 1.15)
    imagesTuples[i].append(faces)

word = "Christopher"

mL = 0
mT = 0
c = 0
for i, imagesTuple in enumerate(imagesTuples):
    if word.lower() in imagesTuple[1].lower():
        img = imagesTuple[0]
        img = Image.fromarray(img)
        faces = imagesTuple[3]
        maxWidth = max(face[2] for face in faces) * 5
        maxHeight = max(face[3] for face in faces)
        if (len(faces) > 5): maxHeight *= 2
        blackMatrix = np.full((maxHeight, maxWidth), 0, dtype=np.uint8)
        blackMatrix = Image.fromarray(blackMatrix, "L")
        for rec in faces:
            if (rec[2] < 65 and rec[3] < 65): continue
            cropped = img.crop((rec[0], rec[1], rec[0] + rec[2], rec[1] + rec[3]))
            blackMatrix.paste(cropped, (mL, mT, mL + rec[3], mT + rec[2]))
            mL += rec[3]
            c += 1
            if (c > 5):
                c = 1
                mT += maxHeight
            # display(cropped)
        display(blackMatrix)
        print("Results found in file", imagesTuple[2][7:])
        if (len(faces) <= 0):
            print("But there were no faces in that file!")
