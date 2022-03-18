
from PIL import Image
import numpy as np

lemur = Image.open('lemur.png')
flag = Image.open('flag.png')

np_lemur = np.array(lemur)
np_flag = np.array(flag)

output = np.bitwise_xor(np_lemur, np_flag)
Image.fromarray(output).show()