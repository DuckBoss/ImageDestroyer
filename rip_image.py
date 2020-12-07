from PIL import Image
from shutil import copyfile
import os


fileName = "image_name"

count = 1
maxIters = 15
copysrc = "%s.jpg" % fileName
copydst = "%s_copy.jpg" % fileName

copyfile(copysrc, copydst)

for x in range(maxIters+1, 1, -1):
    MainImage = Image.open("%s_copy.jpg" % fileName)
    width, height = MainImage.size
    buffer = os.path.join("%s_copy.jpg" % fileName)
    MainImage = MainImage.resize((int(width/4), int(height/4)), Image.NEAREST)
    if x % 2 == 0:
        newQual = x*2
    else:
        newQual = x
    MainImage.save(buffer, "JPEG", quality=newQual)
    MainImage = Image.open("%s_copy.jpg" % fileName)
    MainImage = MainImage.resize((width, height), Image.NEAREST)
    MainImage.save(buffer)
    count += 1
    print("%s/%s" % (count, maxIters))
