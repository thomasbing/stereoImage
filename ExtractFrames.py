import numpy as np
import cv2

#video_path = 'testVideo/IMG_3082.MOV'
video_path = 'testVideo/IMG_3085.MOV'
save_path = 'FrameSave/'
videoCap = cv2.VideoCapture(video_path)
count = 0
'''
while True:
    success, image = videoCap.read()
    if success == True:
        cv2.imwrite(save_path+'frame{}.jpg'.format(count), image) 
        if cv2.waitKey(10) == 27:             
            break
        count += 1
    else:
        print('complete!')
        break
'''
#print(videoCap.get(cv2.CAP_PROP_FRAME_COUNT))

height = videoCap.get(cv2.CAP_PROP_FRAME_HEIGHT)
#print(height)
width = videoCap.get(cv2.CAP_PROP_FRAME_WIDTH)
#print(width)
frameNum = videoCap.get(cv2.CAP_PROP_FRAME_COUNT)

numPixel = 2

Pano_right = np.zeros((int(width), int(frameNum)*numPixel, 3))
Pano_left = np.zeros((int(width), int(frameNum)*numPixel, 3))
for i in range(int(frameNum)):
    success, image = videoCap.read()
    #right view
    tmp_right = image[870:870+numPixel,:,:]  
    tmp_right = np.rollaxis(tmp_right, 1)
    Pano_right[:,i*numPixel:(i+1)*numPixel,:] = tmp_right

    #left view
    tmp_left = image[206:206+numPixel,:,:]  
    tmp_left = np.rollaxis(tmp_left, 1)
    Pano_left[:,i*numPixel:(i+1)*numPixel,:] = tmp_left

cv2.imwrite('Pano_right.jpg', Pano_right)
print('right done!')
cv2.imwrite('Pano_left.jpg', Pano_left)
print('left done!')