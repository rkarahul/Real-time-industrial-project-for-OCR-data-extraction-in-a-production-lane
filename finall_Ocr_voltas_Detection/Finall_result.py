from paddleocr import PaddleOCR

# Initialize PaddleOCR reader
ocr = PaddleOCR()

# Path to the image file
image_path = r'images\a.bmp'

# Perform OCR on the image
result = ocr.ocr(image_path)
print("result",result)

# Extract and print the detected text
detected_text = [line[1][0] for res in result for line in res]
# Flag to control execution
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
