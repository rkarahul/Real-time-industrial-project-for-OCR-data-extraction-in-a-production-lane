# import paddle
# import paddle.distributed as dist
# from paddleocr import PaddleOCR,draw_ocr

# ocr = PaddleOCR(lang='en') # need to run only once to download and load model into memory
# img_path = 'image.png'
# result = ocr.ocr(img_path, cls=False)
# for idx in range(len(result)):
#     res = result[idx]
#     for line in res:
#         print(line)

# import paddle
# import paddle.distributed as dist
# from paddleocr import PaddleOCR, draw_ocr

# ocr = PaddleOCR(lang='en')  # need to run only once to download and load model into memory
# # img_path = 'image.png'
# img_path = 'image.bmp'
# result = ocr.ocr(img_path, cls=False)

# # Extract text from each tuple in the OCR result
# detected_text = [line[1][0] for res in result for line in res]

# # Print the extracted text
# for text in detected_text:
#     print(text)


############################ Folder images
import os
from paddleocr import PaddleOCR

# Initialize PaddleOCR
ocr = PaddleOCR(lang='en')

# Path to the folder containing images
folder_path = 'images'

# Iterate over each image in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.bmp'):
        # Path to the current image file
        img_path = os.path.join(folder_path, filename)
        
        # Perform OCR on the current image
        result = ocr.ocr(img_path, cls=False)

        # Extract and print the detected text
        detected_text = [line[1][0] for res in result for line in res]
        # Flag to control execution
        total_volume_found = False
        print(f"Detected text in {filename}:")
        # Find "Total Volume" and print the next value
        for i, text in enumerate(detected_text):
            if text == 'UNITS PER YEAR':
                if i + 1 < len(detected_text):
                    next_value = detected_text[i - 1]
                    print("Star Value:", next_value)
                else:
                    print("No next value found after 'Star value'.")
                    
                    
            if text == 'Total Volume':
                if i + 1 < len(detected_text):
                    next_value = detected_text[i + 1]
                    print("Total Volume:", next_value)
                    total_volume_found = True  # Set flag to True after execution
                else:
                    print("No next value found after 'Total Volume'.")


