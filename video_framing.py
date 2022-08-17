import os
import cv2
import numpy as np

inpath = input("original video path:")
savepath = input("destination jpg path:")
shape_num = int(input("process interval:"))
if shape_num <= 0:
    print('%d should be over 0' %(shape_num))
    exit()
rotate_num = int(input("roate count:"))

print('travelling...')
all_video = []
for root, dirs, files in os.walk(inpath):
    for file in files:
        if os.path.splitext(file)[-1].lower() in ['.mp4','.avi','.h264','.mkv']:
            all_video.append((root, file))
all_num = len(all_video)
print('travelling over detect %s video!' % all_num)
print('Video framing...')

num = 0
for root, file in all_video:
    num += 1
    print('%s/%s' %(num,all_num))
    video_capture = cv2.VideoCapture(os.path.join(root, file))
    i = 0
    newpath = root.replace(inpath, savepath) + '/' + os.path.splitext(file)[0]
    if os.path.isdir(newpath) == False:
        os.makedirs(newpath)

    while True:
        success, frame = video_capture.read()
        if success:
            if i % shape_num == 0:
                img = os.path.splitext(file)[0] + '_%06d.jpg' % i
                for n in range(rotate_num):
                    frame = np.rot90(frame)
                cv2.imencode('.jpg', frame)[1].tofile(os.path.join(newpath, img))
                i += 1;
        else:
            print(os.path.join(root,file), ' process end!')
            break
print('Video framing over!')
