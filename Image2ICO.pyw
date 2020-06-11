import os
import sys
from PIL import Image
Image.open(sys.argv[1]).save('%s.ico' % os.path.splitext(sys.argv[1])[0])if len(sys.argv) >= 1 else sys.exit()
