# Real-Time Face Detection & Recognition using OpenCV 🎭
## مشروع التعرف على الوجوه في الوقت الفعلي باستخدام OpenCV

---

## 📌 Project Overview | نبذة عن المشروع

This project implements a real-time Computer Vision task for **Face Detection and Recognition** using **Python** and **OpenCV**. It accesses the system's live webcam stream, processes frames in real time, detects human facial features using the pre-trained **Haar Cascade Classifier**, and highlights faces with bounding boxes and dynamic text.

هذا المشروع يمثّل تطبيقاً لمهام الرؤية الحاسوبية (Computer Vision) للكشف عن الوجوه البشرية والتعرف عليها في الوقت الفعلي عبر كاميرا الجهاز (Webcam)، اعتماداً على مكتبة **OpenCV** وخوارزمية **Haar Cascade Classifier**.

---

## 🎯 Project Objectives & Requirements | أهداف ومتطلبات المشروع

* **Task Standard:** Real-time face detection using feature classification algorithms.
* **Input Source:** Live video capture from computer's built-in webcam.
* **Core Processing:**
  * Frame-by-frame webcam video capture.
  * Frame conversion from BGR to Grayscale for optimized processing.
  * Multi-scale face detection using pre-trained XML cascades.
* **Output:** Rendering bounding boxes around detected faces with text overlays (`Face Detected`).

---

## 🔄 System Architecture & Workflow | آلية العمل وهيكلية النظام

```text
[ Live Webcam Stream ] 
       │
       ▼
[ Frame Reading (cv2.VideoCapture) ]
       │
       ▼
[ Convert Frame to Grayscale (cv2.cvtColor) ]
       │
       ▼
[ Haar Cascade MultiScale Classifier (detectMultiScale) ]
       │
       ▼
[ Draw Rectangle & Text Overlay (cv2.rectangle & cv2.putText) ]


       │
       ▼
[ Display Output Window (cv2.imshow) ] ── (Press 'q' to Exit) ──► [ Release Camera & Destroy Windows ]


---

## 🛠️ Prerequisites & Installation | المتطلبات الأساسية والتثبيت

### 1. Requirements | المتطلبات

Before running the project, ensure you have the following installed:

- Python 3.x
- VS Code (or any preferred IDE)
- Functional Webcam

قبل تشغيل المشروع، تأكد من توفر المتطلبات التالية:

- Python 3.x
- برنامج VS Code (أو أي بيئة تطوير أخرى)
- كاميرا ويب تعمل بشكل صحيح

### 2. Required Libraries Installation | تثبيت المكتبات المطلوبة

Open the Terminal inside VS Code and install OpenCV:

افتح الطرفية (Terminal) داخل VS Code وثبت مكتبة OpenCV باستخدام الأمر التالي:

```bash
pip install opencv-python
```

If you encounter missing module errors or binary incompatibility issues, install the OpenCV Contrib package:

إذا ظهرت أخطاء متعلقة بالمكتبات أو عدم التوافق، قم بتثبيت النسخة الكاملة:

```bash
pip install opencv-contrib-python
```

---

## 🚀 How to Run & Exit | طريقة التشغيل والإغلاق

### Running the Project | تشغيل المشروع

1. Ensure that both **main.py** and **haarcascade_frontalface_default.xml** are located in the same project folder.
2. Open the project using VS Code.
3. Launch the Terminal.
4. Run the following command:

```bash
python main.py
```

### Exiting the Application | إغلاق البرنامج

1. Click on the webcam display window to make it active.
2. Press the **Q** key on your keyboard.
3. The webcam stream will stop and the application will close safely.

---

## 🔧 Troubleshooting & Fixes | حل المشاكل الشائعة

### 1. AttributeError: module 'cv2' has no attribute 'CascadeClassifier'

**Cause:**
A local file named `cv2.py` is conflicting with the OpenCV library, or OpenCV is installed incorrectly.

**Solution:**

- Rename or remove any local file named `cv2.py`.
- Reinstall OpenCV using:

```bash
pip install opencv-contrib-python
```

---

### 2. cv2.error: Assertion failed (!empty())

**Cause:**
The Haar Cascade XML file cannot be found.

**Solution:**

Ensure that:

- `haarcascade_frontalface_default.xml`
- `main.py`

are located in the **same project directory**.

---

### 3. Camera Opens then Closes Immediately

**Cause:**
Some Windows systems require the DirectShow backend for webcam access.

**Solution:**

Replace:

```python
cap = cv2.VideoCapture(0)
```

with:

```python
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
```

---

## 📝 Project Details | تفاصيل المشروع

| Category | Description |
|----------|-------------|
| **Programming Language** | Python |
| **Main Library** | OpenCV |
| **Domain** | Computer Vision |
| **Detection Algorithm** | Haar Feature-based Cascade Classifiers |
| **Input Source** | Live Webcam |
| **Output** | Real-time Face Detection with Bounding Boxes |
