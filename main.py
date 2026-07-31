import cv2

# تحميل نموذج Haar Cascade المخصص للتعرف على الوجوه
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# فتح كاميرا الجهاز (0 هي الكاميرا المدمجة)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    # قراءة إطار من الكاميرا
    ret, frame = cap.read()
    if not ret:
        print("تعذر الاتصال بالكاميرا")
        break

    # تحويل الصورة إلى الأبيض والأسود لتحسين سرعة ودقة المعالجة
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # الكشف عن الوجوه في الصورة
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # رسم مستطيل حول كل وجه مكتشف
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, 'Face Detected', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # عرض النتيجة في نافذة
    cv2.imshow('Face Detection - OpenCV', frame)

    # الضغط على حرف 'q' للإغلاق
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# تحرير الكاميرا وإغلاق النوافذ
cap.release()
cv2.destroyAllWindows()