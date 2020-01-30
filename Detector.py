import cv2
import numpy as np
from matplotlib import pyplot as pt

def roi(im,ve):
    mask = np.zeros_like(im)
    match_mask = 255
    cv2.fillPoly(mask, ve, match_mask)
    masked_img = cv2.bitwise_and(im, mask)
    return masked_img

def draw_line(im, lin) :
    im = np.copy(im)
    line_im = np.zeros((im.shape[0], im.shape[1], 3), dtype=np.uint8)
    for l in lin:
        for x1, y1, x2, y2 in l:
            cv2.line(im, (x1, y1), (x2, y2), (0, 0, 180), thickness=2)
    return im

img = cv2.imread('lane_2.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
height = img.shape[0]
width = img.shape[1]

region_of_interest_vertices = [(0, height), (width/3, height/1.8), (width/1.2, height)]

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
canny = cv2.Canny(gray, 220, 280)
cropped_image=roi(canny, np.array([region_of_interest_vertices], np.int32))
lines=cv2.HoughLinesP(cropped_image,1, np.pi/60, 90, lines=np.array([]), minLineLength=115, maxLineGap=10)
img_detect= draw_line(img, lines)

cv2.imshow('lane', img_detect)
cv2.waitKey(0)
cv2.destroyAllWindows()

