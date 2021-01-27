import numpy as np
import cv2
import pdb

drawing = False # true if mouse is pressed
previous_x, previous_y = False, False
ix, iy = -1, -1


# mouse callback function
def draw_circle(event, x, y, flags, param):
    global drawing, mode, previous_x, previous_y

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True

    # draw a circle of mouse is moved
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.circle(img, (x, y), 7, (0, 0, 255), -1)

            # take average of prev and current point, and draw a circle on this point because of the input lag mouse
            if previous_x & previous_y:
                avg_x = round(abs(previous_x + x) / 2)
                avg_y = round(abs(previous_y + y) / 2)
                cv2.circle(img, (avg_x, avg_y), 7, (0, 0, 255), -1)
                cv2.circle(img, (avg_x + 3, avg_y+3), 7, (0, 0, 255), -1)
                # cv2.circle(img, (avg_x + 1, avg_y + 1), 7, (0, 0, 255), -1)

    # set drawing to false if left button is released
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

    previous_x = x
    previous_y = y


# create a 512x512 black grid
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()