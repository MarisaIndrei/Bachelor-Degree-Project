import cv2
import mediapipe as mp
import time
import smtplib, ssl

class poseDetector():

    def __init__(self,
                 static_image_mode=False,
                 model_complexity=1,
                 smooth_landmarks=True,
                 enable_segmentation=False,
                 smooth_segmentation=True,
                 min_detection_confidence=0.5,
                 min_tracking_confidence=0.5):
        self.static_image_mode = static_image_mode
        self.model_complexity = model_complexity
        self.smooth_landmarks = smooth_landmarks
        self.enable_segmentation = enable_segmentation
        self.smooth_segmentation = smooth_segmentation
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence


        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.static_image_mode, self.model_complexity, self.smooth_landmarks,
                                     self.enable_segmentation, self.smooth_segmentation, self.min_detection_confidence, self.min_tracking_confidence)

    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)

        return img

    def findPosition(self, img, draw=True):

        lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                # print(id, lm)
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

        return lmList

def send_mail_test():
    port = 465  # For SSL
    password = 'opdwqjciifewcolb' #input("Type your password and press enter: ")

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("user.user09112000@gmail.com", password)
        # TODO: Send email here
        server.sendmail('user.user09112000@gmail.com', 'user.user09112000@gmail.com',
                        "Warning missing accident has been reported")  # recipients mail with mail m
def main():

    captureDevice = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    captureDevice.set(3, 1280)
    captureDevice.set(4, 960)
    pTime = 0
    detector = poseDetector()

    curr_time = 0

    # the output will be written to output.avi
    out = cv2.VideoWriter(
        'output.avi',
        cv2.VideoWriter_fourcc(*'MJPG'),
        15.,
        (640, 480))
    while captureDevice.isOpened():
        succes, img = captureDevice.read()
        img = detector.findPose(img)
        lmList = detector.findPosition(img, draw = False)
        if len(lmList) != 0:
            print(lmList[0])
            # cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
            # cv2.circle(img, (lmList[0][1], lmList[0][2]), 15, (0, 0, 255), cv2.FILLED)
        else:
            if curr_time ==0:
                curr_time = time.time()
            else:
                tmp_time = time.time()
                if tmp_time - curr_time >15:
                    print("MISSING DETECTION")
                    send_mail_test()

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime


        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)


        out.write(img.astype('uint8'))
        cv2.imshow("People Detection", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # out.release()
        cv2.waitKey(1)



if __name__ == "__main__":
    main()
