import numpy as np
from PIL import Image

img1 = np.array(Image.open('入职申明1.jpg'))
img2 = np.array(Image.open('入职申明2.jpg'))

print(img2)

a = np.concatenate((img2,img1),axis=0)
print(a.shape)

pil_img = Image.fromarray(a)
pil_img = pil_img.resize((403*3,604*3))
print(pil_img.mode)
# RGB

pil_img.save('lena_save_pillow.jpg')