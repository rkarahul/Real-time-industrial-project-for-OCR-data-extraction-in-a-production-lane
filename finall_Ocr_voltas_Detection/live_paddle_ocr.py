import cv2
from paddleocr import PaddleOCR

# Initialize PaddleOCR
ocr = PaddleOCR(lang='en')

# Initialize the webcam
cam = cv2.VideoCapture(0)

# Continuously capture frames from the webcam
while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to capture frame")
        break
    
    # Perform OCR on the current frame
    result = ocr.ocr(frame, cls=False)

    # Extract and print the detected text
    detected_text = [line[1][0] for res in result for line in res]
    total_volume_found = False

    # Find "Total Volume" and print the next value
    for i, text in enumerate(detected_text):
        if text == 'UNITS PER YEAR':
            if i + 1 < len(detected_text):
                next_value = detected_text[i - 1]
                print("Power Consumption Value:", next_value)
            else:
                print("No next value found after 'Power Consumption Value'.")
                
                
        if text == 'Total Volume':
            if i + 1 < len(detected_text):
                next_value = detected_text[i + 1]
                print("Total Volume:", next_value)
                total_volume_found = True  # Set flag to True after execution
            else:
                print("No next value found after 'Total Volume'.")

    # Display the frame
    cv2.imshow('OCR', frame)
    
    # Check for key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture and close any open windows
cam.release()
cv2.destroyAllWindows()
