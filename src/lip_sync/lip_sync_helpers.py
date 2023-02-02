# lip_sync_helpers.py
import numpy as np
import cv2

class LipSyncHelpers:
    def __init__(self):
        pass

    def get_mouth_coordinates(self, landmarks):
        mouth_points = []
        for i in range(48, 61):
            mouth_points.append(landmarks[i])
        mouth_points = np.array(mouth_points, np.int32)
        return mouth_points

    def get_mask(self, frame, mouth_points):
        mask = np.zeros_like(frame)
        cv2.fillPoly(mask, [mouth_points], (255, 255, 255))
        return mask

    def get_roi(self, frame, mask):
        roi = cv2.bitwise_and(frame, mask)
        return roi

    def get_cropped_mouth(self, roi, mouth_points):
        x, y, w, h = cv2.boundingRect(mouth_points)
        cropped_mouth = roi[y:y+h, x:x+w]
        return cropped_mouth
