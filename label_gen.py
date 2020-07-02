import os

img_path = 'C:\\Users\\Nikunj\\Desktop\\Bala Project\\videotoimgucf11\\'
f1 = open('C:\\Users\\Nikunj\\Desktop\\Bala Project\\trainfile.txt','r')
f2 = open('C:\\Users\\Nikunj\\Desktop\\Bala Project\\testfile.txt','r')

train_list = f1.readlines()
test_list = f2.readlines()

f3 = open('train_list.txt', 'w')
f4 = open('test_list.txt', 'w')

clip_length = 16

for line in train_list:
    name = line.split(' ')[0]
    image_path = img_path+name
    label = line.split(' ')[-1]
    images = os.listdir(image_path)
    nb = len(images) // clip_length
    for i in range(nb):
        f3.write(name+' '+ str(i*clip_length+1)+' '+label)


for line in test_list:
    name = line.split(' ')[0]
    image_path = img_path+name
    label = line.split(' ')[-1]
    images = os.listdir(image_path)
    nb = len(images) // clip_length
    for i in range(nb):
        f4.write(name+' '+ str(i*clip_length+1)+' '+label)

f1.close()
f2.close()
f3.close()
f4.close()