import cognitive_face as CF
import time
from PIL import Image, ImageDraw

KEY = '35d565db844444bcbcc83a770d627fab'  # Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(KEY)
# If you need to, you can change your base API url with:
CF.BaseUrl.set('https://westcentralus.api.cognitive.microsoft.com/face/v1.0/')

# BASE_URL = 'https://westus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
# CF.BaseUrl.set(BASE_URL)

# You can use this example JPG or replace the URL below with your own URL to a JPEG image.
#img_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
img_url='///home/siddharth/Desktop/IMG_TEST.JPG'
img_url2='///home/siddharth/Desktop/IMG_TEST2.JPG'

faces = CF.face.detect(img_url)
# faces2=CF.face.detect(img_url2)
#print(CF.face_list.create('sample2'))

#print(CF.face_list.add_face(img_url2,'sample2'))
# for img in faces:
#     print(CF.face.verify(faces2[0]['faceId'],img['faceId']))
print(CF.face.find_similars(faces[0]['faceId'],'sample2'))
start_time = time.time()
CF.face.
print("--- %s seconds ---" % (time.time() - start_time))
# print(CF.face.verify(faces[0]['faceId'],faces2[0]['faceId']))
# #     print(1)
# else:
#     print(0)


# #Convert width height to a point in a rectangle
# def getRectangle(faceDictionary):
#     rect = faceDictionary['faceRectangle']
#     left = rect['left']
#     top = rect['top']
#     bottom = left + rect['height']
#     right = top + rect['width']
#     return ((left, top), (bottom, right))

# #Download the image from the url
# #response = requests.get(img_url)
# img = Image.open(img_url)

# #For each face returned use the face rectangle and draw a red box.
# draw = ImageDraw.Draw(img)
# for face in faces:
#     draw.rectangle(getRectangle(face), outline='red')
#     img.save('new.jpg')

# #Display the image in the users default image browser.
# img.show()
