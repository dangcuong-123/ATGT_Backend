import cv2
import numpy as np 
from imutils.video import VideoStream
import warnings
warnings.filterwarnings("ignore")

video = VideoStream(src=0).start()
#Chua cac diem nguoi dung chon de tao da giac
list_points = []
points = []

def handle_left_click(event, x, y, flags, points):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append([x, y])
    

def left_click_detect(event, x, y, flags, points):
    if (event == cv2.EVENT_LBUTTONDOWN):
        print(f"\tClick on {x}, {y}")
        points.append([x,y])
        print(points)

def draw_polygon(frame, points):
    for point in points:
        frame = cv2.circle(frame, (point[0], point[1]), 5, (0,0,255), -1)
    
    frame = cv2.polylines(frame, [np.int32(points)], False, (255,0,0), thickness=2)
    return frame

while True:
    frame = video.read()
    frame = cv2.flip(frame, 1)

    #Ve polygon
    # for points in list_points:
    #     print(points)
    #     frame = draw_polygon(frame, points)
    # frame = draw_polygon(frame, list_points)
    frame = draw_polygon(frame, points)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('c'):
        points.append(points[0])
        list_points.append(points)
        points = []

    elif key == ord('e'):
        pass
        list_points.append(points)

    #Hien thi anh ra man hinh
    cv2.imshow('Intrusion Warning', frame)
    
    cv2.setMouseCallback('Intrusion Warning', handle_left_click, points)

video.stop()
cv2.destroyAllWindows()


# # import numpy as np
# # import cv2 as cv
# # ix,iy,sx,sy = -1,-1,-1,-1
# # list_point = []
# # # mouse callback function
# # def draw_lines(event, x, y, flags, param):
# #     global ix,iy,sx,sy
# #     # if the left mouse button was clicked, record the starting
# #     if event == cv.EVENT_LBUTTONDOWN:

# #         # draw circle of 2px
# #         cv.circle(img, (x, y), 3, (0, 0, 127), -1)

# #         if ix != -1: # if ix and iy are not first points, then draw a line
# #             cv.line(img, (ix, iy), (x, y), (0, 0, 127), 2, cv.LINE_AA)
# #         else: # if ix and iy are first points, store as starting points
# #             sx, sy = x, y
# #         ix,iy = x, y
        
# #     elif event == cv.EVENT_RBUTTONDOWN:
# #         ix, iy = -1, -1 # reset ix and iy
# #         if flags == ord('c'): # if alt key is pressed, create line between start and end points to create polygon
# #             cv.line(img, (x, y), (sx, sy), (0, 0, 127), 2, cv.LINE_AA)

# # # read image from path and add callback
# # img = cv.resize(cv.imread("paylak2.jpg"), (1280, 720))
# # cv.namedWindow('image') 
# # cv.setMouseCallback('image',draw_lines)

# # while(1):
# #     cv.imshow('image',img)
# #     if cv.waitKey(20) & 0xFF == 27:
# #         break

# # cv.destroyAllWindows()



# cap = cv2.VideoCapture("files/long_video.mp4")  # Open video file
# polygon = []
# points = []
# while (cap.isOpened()):
#     ret, frame = cap.read()  # read a frame
#     if not ret:
#         print('EOF')
#         break

#     frame = cv2.polylines(frame, polygon, False, (255, 0, 0), thickness=5)

#     cv2.imshow('Frame', frame)
#     # Abort and exit with 'Q'
#     key = cv2.waitKey(25)
#     if (key == ord('q')):
#         break
#     elif (key== ord('p')): 
#         polygon = [np.int32(points)]
#         points = []

#     cv2.setMouseCallback('Frame', left_click_detect, points)


# cap.release()  # release video file
# cv2.destroyAllWindows()  # close all openCV windows


