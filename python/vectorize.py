import cv2
import numpy as np

def get_edges(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    return cv2.Canny(blur, 50, 120)


def extract_contours(edge_img):
    contours, _ = cv2.findContours(
        edge_img,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    paths = []
    for c in contours:
        if len(c) > 10:
            path = [(p[0][0], p[0][1]) for p in c]
            paths.append(path)

    return paths
