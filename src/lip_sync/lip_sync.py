# lip_sync.py
import cv2
import dlib
import numpy as np

class LipSync:
    def __init__(self, shape_predictor_path):
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor(shape_predictor_path)

    def get_lip_points(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rects = self.detector(gray, 0)
        if len(rects) > 0:
            shape = self.predictor(gray, rects[0])
            shape = shape.parts()
            lip_points = []
            for i in range(48, 61):
                lip_points.append([shape[i].x, shape[i].y])
            return lip_points
        else:
            return None

def get_lip_mask(lip_points, frame):
    if lip_points is not None:
        lip_points = np.array(lip_points, np.int32)
        cv2.fillPoly(frame, [lip_points], (255, 255, 255))
        lip_mask = cv2.inRange(frame, (255, 255, 255), (255, 255, 255))
        return lip_mask
    else:
        return None
