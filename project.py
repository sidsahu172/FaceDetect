import cognitive_face as CF

key = '35d565db844444bcbcc83a770d627fab' # make sure to fill in the key you obtained for Face API
CF.Key.set(key)
CF.BaseUrl.set('https://westcentralus.api.cognitive.microsoft.com/face/v1.0/')

img_url = "https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg"
result = CF.face.detect(img_url)
print result
