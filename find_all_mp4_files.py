import glob
import os
for root,dirs,files in os.walk("/"):
    for file in files:
        if file.endswith(".mp4"):
            print(os.path.join(root,file))

