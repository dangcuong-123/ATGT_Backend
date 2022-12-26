import cv2
import numpy as np 
import warnings
warnings.filterwarnings("ignore")

class Camera:
    def __init__(self, width=1280, height=720, device=0):
        """
        Initialize Camera class.
        :param width: capture width
        :param height: capture height
        :param device: device enumerate
        """
        self.cap = cv2.VideoCapture('/home/tomorrow/Job/atgt/ATGT_backend/vid1.mp4')
        # self.cap = cv2.VideoCapture('/home/tomorrow/Job/Pionero/face-id/new-version/data/test/ori/filename.avi')
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc(*'MJPG'))

        self.width = width
        self.height = height

    def get_frame(self):
        """
        Get a single frame from the capture source.
        :return: Return frame if successfully read, else return None
        """
        ret, frame = self.cap.read()

        if not ret:
            return None
        return frame

    def get_size(self):
        """
        Return tuple of current resolution.
        :return: (width, height)
        """
        return self.cap.get(cv2.CAP_PROP_FRAME_WIDTH), self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def __del__(self):
        self.cap.release()

def handle_left_click(event, x, y, flags, shapes):
    # Bam chuot trai de ve
    if event == cv2.EVENT_LBUTTONDOWN:
        shapes['polygon'].append([x, y])
    # Bam 'Alt' de kthuc 1 hinh, bat dau hinh moi
    if flags == cv2.EVENT_FLAG_ALTKEY:
        shapes['polygon'].append(shapes['polygon'][0])
        shapes['list_polygons'].append(shapes['polygon'])
        shapes['polygon'] = []     

def draw_polygon(frame, points):
    for point in points:
        frame = cv2.circle(frame, (point[0], point[1]), 5, (0,0,255), -1)
    
    frame = cv2.polylines(frame, [np.int32(points)], False, (255,0,0), thickness=2)
    return frame

def draw_multi_polygon(frame, list_points):
    for points in list_points:
        draw_polygon(frame, points)
    return frame

if __name__ == '__main__':
    camera = Camera(1280, 720)
    shapes = {'polygon': [], 'list_polygons': []}
    result = cv2.VideoWriter('filename.avi', 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, size)
    while True:
        # Capture the video frame by frame
        frame = camera.get_frame()
        if len(shapes['list_polygons']) == 0:
            frame = draw_polygon(frame, shapes['polygon'])
            cv2.imshow('Intrusion Warning', frame)
        else:
            frame = draw_polygon(frame, shapes['polygon'])
            cv2.imshow('Intrusion Warning', frame)
            frame = draw_multi_polygon(frame, shapes['list_polygons'])
            cv2.imshow('Intrusion Warning', frame)
        if frame is None:
            break            

        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        # Exit if 'q' is pressed
        # if cv2.waitKey(1) & 0xFF == ord('c'):
        #     shapes['polygon'].append(shapes['polygon'][0])
        #     shapes['list_polygons'].append(shapes['polygon'])
        #     shapes['polygon'] = []

        cv2.setMouseCallback('Intrusion Warning', handle_left_click, shapes)
        print(shapes)
    del camera
