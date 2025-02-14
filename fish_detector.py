import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt

# Load your trained model
model = YOLO("FishNet/final weights/best.pt")  # Path to your trained model

# Path to the unseen image
image_path = "FishNet/FishNet.v11i.yolov8/test/images/Seriola-lalandi_1_jpg.rf.fa7ae81a1c554ea519f22cf7941d459b.jpg"

# Run inference
results = model(source=image_path, augment=True, show=True, conf=0.45, iou=0.5)

# Display the results (optional)
output_image = cv2.imread(results[0].path)
output_image = cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB for plotting
plt.imshow(output_image)
plt.axis("off")
plt.show()
