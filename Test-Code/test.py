import cv2
import cv2.aruco as aruco

# Set up Aruco dictionary
aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_250)
parameters = aruco.DetectorParameters_create()

# Set up video capture
cap = cv2.VideoCapture(0)

while True:
    # Read frame from video capture
    ret, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect markers
    corners, ids, _ = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

    # Draw detected markers on image
    img = aruco.drawDetectedMarkers(img, corners, ids)

    # Display image
    cv2.imshow("Output", img)

    # Check for user input
    key = cv2.waitKey(1)
    if key == 27: # Esc key
        break

# Release video capture
cap.release()
cv2.destroyAllWindows()
