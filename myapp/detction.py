# pip install ultralytics
#             opencv-python


from ultralytics import YOLO
import cv2
import math

# Load your custom-trained model here (replace path accordingly)
model = YOLO(r'C:\Users\hp\PycharmProjects\UnderWatertrash\60_epochs_denoised.pt')

# Define your class names — should match your model's training classes
classNames = ['mask', 'can', 'cellphone', 'electronics','glass-bottle','glow','metal','mise','net','plastic-bag','plastic-bottle','plastic','rod','sunglass','tyre']

# Confidence threshold (lowered to 0.3 for better detection)
confidence_threshold = 0.2

# Path to input image
image_path = r"C:\Users\hp\PycharmProjects\UnderWatertrash\media\trash_image11.webp"

# Read image
img = cv2.imread(image_path)
if img is None:
    print("⚠️ Failed to load image. Check the image path and file.")
    exit()

# Run detection
results = model(img)

detected_classes = set()

for r in results:
    boxes = r.boxes
    # Debug: print all detected class indices and confidences
    print("Detected classes (indices):", boxes.cls.cpu().numpy())
    print("Confidences:", boxes.conf.cpu().numpy())

    for box in boxes:

        print(box,"============")
        conf = float(box.conf[0])
        cls = int(box.cls[0])

        if conf >= confidence_threshold:

            print(cls,"detected")
            # if cls < len(classNames):
            #     class_name = classNames[cls]
            #     detected_classes.add(class_name)

# if detected_classes:
#     print("Detected trash items in image:")
#     for item in detected_classes:
#         print(f"- {item}")
# else:
#     print("No trash items detected in the image.")
