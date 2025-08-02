import cv2 #openCV
import mediapipe as mp


webcan = cv2.VideoCapture(0)
solucao_reconhecimento_rosto = mp.solutions.face_detection
reconhecedor_rosto = solucao_reconhecimento_rosto.FaceDetection()
desenho = mp.solutions.drawing_utils


while True:
    verificador, frame = webcan.read()
    if not verificador:
        break


    lista_rostos = reconhecedor_rosto.process(frame)

    if lista_rostos.detections:
        for rosto in lista_rostos.detections:
            desenho.draw_detection(frame, rosto)


    cv2.imshow("Rostos na webcam", frame)


    if cv2.waitKey(5) == 27:
        break


webcan.release()

