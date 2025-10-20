# 🖼️ Fake Image Detection System

This project is designed to detect whether an uploaded image is **fake or real** using AI techniques.  
The system allows users to upload an image, and it responds with the **fakeness detection result** along with additional functionalities in later versions.

---

## 🚀 Features

### Version 1
- User can upload an image to the system.
- User will get a response if the picture is fake or not.
- User can see the **reason for fakeness**.

### Version 2
- User can view the **history** of uploaded images.
- User can delete any of the images.

### Version 3
- User can **share results** of the detection on social media.

### Version 4
- The system can **generate a badge** on the image with verification.

---

## 🧩 System Flow (High-Level)

1. **User uploads an image** from the client side (web or mobile).
2. Backend receives the image and stores it in the **File Service**.
3. A unique **File Key & ID** are generated and saved in the **Database**.
4. The AI module:
   - Downloads the file.
   - Checks for **image fakeness**.
   - Sends back the result.
5. Backend stores the response and sends the result back to the **client side**.

---

## 📊 Flow Diagram

Below is the sequence diagram of the process:

![Fake Image Detection Flow Diagram](./4296f3c9-6a9a-489b-ae7c-a6aef7b6332b.jpg)

---

## 📝 Definitions

- **Client Side**: Frontend Web and Mobile (used by end-users).
- **Backend**: Handles business logic, communication with database, and AI model.
- **Database**: Stores file keys, IDs, and detection results.
- **AI**: Downloads and processes the image to check fakeness.
- **File Service**: Storage system for uploaded images.

---

## ✅ Assumptions

- User must be **logged in** to use the system.

---

## 👨‍💻 Team Members

(Add your team members here)

---

## 🔮 Future Work
- Enhance AI models for better accuracy.
- Support for **video fakeness detection**.
- Integration with **browser extensions** and **social media platforms**.
