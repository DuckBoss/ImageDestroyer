from PIL import Image
from shutil import copyfile
import os


fileName = "wtflevelsofquality"

count = 0
maxIters = 25
copysrc = "%s.jpg" % fileName
copydst = "%s_copy.jpg" % fileName

copyfile(copysrc, copydst)

for x in range(maxIters+1, 1, -1):
    MainImage = Image.open("%s.jpg" % fileName)
    width, height = MainImage.size
    buffer = os.path.join("%s.jpg" % fileName)
    MainImage = MainImage.resize((150, 150), Image.MEDIANCUT)
    if x % 2 == 0:
        newQual = x*2
    else:
        newQual = x
    MainImage.save(buffer, "JPEG", quality=newQual)
    MainImage = Image.open("%s.jpg" % fileName)
    MainImage = MainImage.resize((width, height), Image.MEDIANCUT)
    MainImage.save(buffer)
    count += 1
    print("%s/%s" % (count, maxIters))
