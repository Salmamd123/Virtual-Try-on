import cv2
import dlib

def apply_sunglass_effect(image_path, sunglasses_path, landmarks_model_path):
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # Read the sunglasses
    sunglasses = cv2.imread(sunglasses_path, cv2.IMREAD_UNCHANGED)

    # Load the facial landmarks model
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(landmarks_model_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = detector(gray, 1)

    # Iterate over the detected faces
    for face in faces:
        # Estimate facial landmarks for the current face
        landmarks = predictor(gray, face)

        # Get the coordinates of relevant facial landmarks
        nose_tip = (landmarks.part(29).x, landmarks.part(29).y)
        left_ear = (landmarks.part(0).x, landmarks.part(0).y)
        right_ear = (landmarks.part(16).x, landmarks.part(16).y)
        left_eye = (landmarks.part(36).x, landmarks.part(36).y)
        right_eye = (landmarks.part(45).x, landmarks.part(45).y)

        # Calculate the dimensions of the sunglasses
        sunglass_width = right_ear[0] - left_ear[0]
        sunglass_height = int((sunglasses.shape[0] / sunglasses.shape[1]) * sunglass_width)

        # Resize the sunglasses image
        sunglasses_resized = cv2.resize(sunglasses, (sunglass_width, sunglass_height))

        # Calculate the position for placing the sunglasses
        x_offset = int(left_eye[0] - (sunglass_width * 0.18))
        y_offset = int(nose_tip[1] - (sunglass_height * 0.7))

        # Overlay the sunglasses on the image
        for c in range(0, 3):
            image[y_offset:y_offset+sunglass_height, x_offset:x_offset+sunglass_width, c] = \
                sunglasses_resized[:, :, c] * (sunglasses_resized[:, :, 3] / 255.0) + \
                image[y_offset:y_offset+sunglass_height, x_offset:x_offset+sunglass_width, c] * (1.0 - sunglasses_resized[:, :, 3] / 255.0)

    # Display the resulting image
    return image
    
   

# Example usage
image_1=apply_sunglass_effect("sravani 2.jpg","glass.png","shape_predictor_68_face_landmarks.dat")
image_0=apply_sunglass_effect("sravani 2.jpg","glass1.png","shape_predictor_68_face_landmarks.dat")
image_2=apply_sunglass_effect("sravani 2.jpg","glass33.png","shape_predictor_68_face_landmarks.dat")
image_3=apply_sunglass_effect("sravani 2.jpg","glass3.png","shape_predictor_68_face_landmarks.dat")
