#generate trainfile.txt

import os
trainfile=open("C:\\Users\\Nikunj\\Desktop\\Bala Project\\trainfile.txt","w")
vid_path="C:\\Users\\Nikunj\\Desktop\\Bala Project\\UCF11_updated_mpg"
actionlist=os.listdir(vid_path)
i=0
for action in actionlist:
    actionpath=os.path.join(vid_path,action)
    list2=os.listdir(actionpath)
    for item in list2:
        fname=item.split(".")[0]
        trainfile.write(action+"/"+fname+" "+str(i)+"\n")
    i=i+1