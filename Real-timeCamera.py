import cv2

# to open the camera
video_cap=cv2.VideoCapture(0)

# not to shutdown and run the camera in infinite loop
while True:
    # reading the images
    ret,video_data=video_cap.read()

    # show the title and show the images
    cv2.imshow("Real time camera",video_data)

    # shuting the camera with the key
    if cv2.waitKey(10)==ord ("a"):
        break

# realsing the camera
video_cap.release()    
