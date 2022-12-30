import cv2

# Set up the tracker
tracker = cv2.TrackerKCF_create()

# Read the first frame of the video
video = cv2.VideoCapture(0)
success, frame = video.read()

# Select the bounding box for the object to be tracked
bbox = cv2.selectROI(frame, False)

# Initialize the tracker with the bounding box coordinates
tracker.init(frame, bbox)

while True:
    # Read a new frame
    success, frame = video.read()
    if not success:
        break

    # Update the tracker
    success, bbox = tracker.update(frame)

    # Draw the bounding box
    if success:
        # Draw the bounding box on the frame
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
    else:
        # Tracking failed
        cv2.putText(frame, "Tracking failed", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    # Display the frame
    cv2.imshow("Frame", frame)

    # Check for user input
    key = cv2.waitKey(1)
    if key == 27:  # Esc key
        break

# Release the video capture and destroy all windows
video.release()
cv2.destroyAllWindows()
