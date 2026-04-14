import cv2

def get_frame(cam=0, width=320, height=240):
    cap = cv2.VideoCapture(cam)
    ret, frame = cap.read()
    cap.release()

    frame = cv2.resize(frame, (width, height))
    return frame
