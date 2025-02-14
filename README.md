# 🐟 Sydney Fish Classification with YOLOv8

## 📌 Project Overview  
This is a computer vision project that uses **YOLOv8**, pretrained on the **Fish4Knowledge dataset**, as a starting point to identify fish species local to **Sydney, Australia**. The model is fine-tuned with a custom dataset and provides a classification prediction for test images.  

## 🎯 Motivation  
Many beginners on **Facebook forums and other online communities** often ask for help identifying fish species. Existing identification apps require users to manually select multiple features (similar to **Akinator-style** guessing). This project leverages **deep learning** to automatically find **optimised weights**, making fish identification much easier and more accessible.  

## 📂 Dataset  
- **Base Model Dataset**: Fish4Knowledge (Pretrained YOLOv8)  
- **Custom Dataset**: Collected images of local Sydney fish species  

## 🚀 Features  
✅ Transfer learning with YOLOv8  
✅ Custom fish dataset for fine-tuning  
✅ Bounding box detection & classification  
✅ Image-based fish species prediction 

## Notes
- This model currently works with identifying Flathead, Aussie Salmon and Kingfish (more to come)
- Training was done on Google Colab
- My annotations were done on RoboFlow (https://app.roboflow.com/fishnet-79l5t/fishnet-7l4ug/11)
