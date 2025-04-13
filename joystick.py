import pyvjoy
import serial

j = pyvjoy.VJoyDevice(1)
arduino = serial.Serial('COM4', 9600)

def mapear(valor, in_min, in_max, out_min, out_max):
    return int((valor - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

while True:
    try:
        dado = arduino.readline().decode().strip()
        if "," in dado:
            partes = dado.split(",")
            if len(partes) == 4 and all(p.isdigit() for p in partes):
                valor = int(partes[0])
                acelerador = int(partes[1])
                subir = int(partes[2])
                descer = int(partes[3])

                # Eixo X (volante)
                eixoX = mapear(valor, 0, 1023, 0, 32767)
                j.set_axis(pyvjoy.HID_USAGE_X, eixoX)

                # Eixo Y (acelerador)
                if acelerador == 1:
                    j.set_axis(pyvjoy.HID_USAGE_Y, 32767)
                else:
                    j.set_axis(pyvjoy.HID_USAGE_Y, 0)

                # Botões para marchas
                j.set_button(1, subir)  # Botão 1: subir marcha
                j.set_button(2, descer)  # Botão 2: descer marcha

    except Exception as e:
        print("Erro:", e)
