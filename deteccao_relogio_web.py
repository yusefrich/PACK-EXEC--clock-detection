#!/usr/bin/python3
import cv2


# captura de image
video = cv2.VideoCapture(0)

# referencia do classificador
classificador = cv2.CascadeClassifier('haarcascade_relogio_parede.xml')

# loop para iterar sobre cada frame da imagem
while True:
    # frame statico da imagem
    ret, frame = video.read()

    # deteccoes efetuadas pelo classificador
    deteccoes = classificador.detectMultiScale(frame, scaleFactor=1.09)

    # render de cada deteccao na tela
    for (x, y, l, a) in deteccoes:
        cv2.rectangle(frame, (x, y), (x + l, y + a), (255, 0, 225), 2)

    # intancia que renderiza cada frame capturado com as deteccoes
    cv2.imshow('Video da web', frame)

    # input para sair da instancia que renderiza
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# limpa referencias
captura.release()
cv2.destroyAllWindows()
