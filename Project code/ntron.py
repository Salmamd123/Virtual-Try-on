import cv2
import dlib

def apply_necklace_overlay(image_path, necklace_path, landmarks_model_path):
    # Load the hero image
    image = cv2.imread(image_path)

    # Load the necklace image with transparency
    necklace = cv2.imread(necklace_path, cv2.IMREAD_UNCHANGED)

    # Initialize the face detector and facial landmark predictor
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(landmarks_model_path)

    # Convert the hero image to grayscale for face detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = detector(gray, 1)

    # Iterate over the detected faces
    for face in faces:
        # Estimate facial landmarks for the current face
        landmarks = predictor(gray, face)
        
        # Get the coordinates of relevant facial landmarks
        nose_tip = (landmarks.part(30).x, landmarks.part(30).y)
        left_ear = (landmarks.part(0).x, landmarks.part(1).y)
        right_ear = (landmarks.part(14).x, landmarks.part(15).y)
        left_eye = (landmarks.part(37).x, landmarks.part(36).y)
        right_eye = (landmarks.part(43).x, landmarks.part(45).y)

        # Calculate the dimensions of the necklace
        necklace_width = right_ear[0] - left_ear[0]
        necklace_height = int((necklace.shape[0] / necklace.shape[1]) * necklace_width)

        # Resize the necklace image
        necklace_resized = cv2.resize(necklace, (necklace_width, necklace_height))

        # Calculate the position for placing the necklace
        x_offset = int(int(left_eye[0] - (necklace_width * 0.2)) * 0.92)
        y_offset = int(int(int(nose_tip[1] - (necklace_height * 0.2))) * 1.5)

        # Overlay the necklace on the image
        for c in range(0, 3):
            image[y_offset:y_offset+necklace_height, x_offset:x_offset+necklace_width, c] = \
                necklace_resized[:, :, c] * (necklace_resized[:, :, 3] / 255.0) + \
                image[y_offset:y_offset+necklace_height, x_offset:x_offset+necklace_width, c] * (1.0 - necklace_resized[:, :, 3] / 255.0)

    return image

# Example usage
image=apply_necklace_overlay("iu.jpg","necklac1.png","shape_predictor_68_face_landmarks.dat")
image_1=apply_necklace_overlay("iu.jpg","necklace 2.png","shape_predictor_68_face_landmarks.dat")
image_2=apply_necklace_overlay("iu.jpg","necklace 3.png","shape_predictor_68_face_landmarks.dat")
image_3=apply_necklace_overlay("iu.jpg","necklace 4.png","shape_predictor_68_face_landmarks.dat")
