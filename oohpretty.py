import cv2
import sys

print (cv2.__version__)
major_ver = 3
minor_ver = 4
subminor_ver = 0

if __name__ == '__main__' :
    tracker = cv2.TrackerMIL_create()

    # Read video, the 0 means webcam, can also change tostring of  file location
    video = cv2.VideoCapture(0)

    # Read first frame.
    ok, frame = video.read()
    if not ok:
        print ('Cannot read video file')
        sys.exit()

    # Define an initial bounding box, this is arbirtary
    bbox = (287, 23, 86, 320)
    # Uncomment the line below to select a different bounding box
    #note to self, roi = region of interest
    cv2.putText(frame, "Drag a box around your nose, then press escape!", (10,40), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
    bbox = cv2.selectROI(frame, False)

    # Initialize tracker with first frame and bounding box
    ok = tracker.init(frame, bbox)

    while True:
        # Read a new frame
        ok, frame = video.read()
        #error catching if you dont get a new frame(if ok doesnt exist)
        if not ok:
            break
        # Update tracker
        ok, bbox = tracker.update(frame)

        # Draw bounding box
        if ok:
            # Tracking success
            #point 1 = (bbox[0].bbox[1])
            #p1 = (int(bbox[0]), int(bbox[1]))

            #p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            #cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
            aylmao = int(bbox[0]+bbox[2]/2), int(bbox[1]+bbox[3]/2)
            cv2.circle(frame,aylmao,25,(0,0,255),-1)
        else :
            # Tracking failure
            cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)

        # Display result(imshow is imageshow)
        cv2.imshow("Tracking", frame)

        # Exit if ESC pressed
        k = cv2.waitKey(1) & 0xff
        if k == 27 : break
