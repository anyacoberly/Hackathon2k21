import cv2
#This is to open up an external camerafor facial recognition 
# Open  external webcam
camera = cv2.VideoCapture(-1)

# Start the capture loop
while True:
    # Get a frame
    ret_val, frame = camera.read()

    # Show the frame
    cv2.imshow('Webcam Video Feed', frame)

    # Stop the capture by hitting the 'esc' key
    if cv2.waitKey(1) == 27:
        break

# Dispose of all open windows
cv2.destroyAllWindows()
