import Hobot.GPIO as GPIO
import cv2, time

led_pin = 32
button_pin = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN)

cap = cv2.VideoCapture(0)

print("Ready. Press button to capture.")

try:
    while True:
        if GPIO.input(button_pin) == GPIO.HIGH:
            print("Button Pressed! Capturing...")
            GPIO.output(led_pin, GPIO.HIGH)

            ret, frame = cap.read()
            if ret:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                edges = cv2.Canny(gray, 100, 200)

                ts = int(time.time())
                cv2.imwrite(f"image_{ts}.jpg", frame)
                cv2.imwrite(f"edges_{ts}.jpg", edges)
                print("Saved images.")

            time.sleep(0.5)
            GPIO.output(led_pin, GPIO.LOW)

            while GPIO.input(button_pin) == GPIO.HIGH:
                time.sleep(0.05)

        time.sleep(0.05)

finally:
    print("Cleaning up...")
    cap.release()
    GPIO.cleanup()
