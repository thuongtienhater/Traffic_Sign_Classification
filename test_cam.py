import cv2

for i in range(5):  # thử các index từ 0 đến 2
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"✅ Camera mở thành công tại index {i}")
        ret, frame = cap.read()
        if ret:
            print(f"✅ Đọc được frame từ camera {i}")
            cv2.imshow("Camera Test", frame)
            cv2.waitKey(0)
        else:
            print(f"⚠️ Không đọc được frame từ camera {i}")
        cap.release()
        cv2.destroyAllWindows()
    else:
        print(f"❌ Không mở được camera tại index {i}")
