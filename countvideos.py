import os
vid_path="C:\\Users\\Nikunj\\Desktop\\Bala Project\\UCF11_updated_mpg"
actionlist=os.listdir(vid_path)
sum=0
for action in actionlist:
    actionpath=os.path.join(vid_path,action)
    videos=os.listdir(actionpath)
    print(action+"   "+str(len(videos)*0.7)+"    "+str(len(videos)*0.3))
    sum=sum+len (videos)
print(sum)
