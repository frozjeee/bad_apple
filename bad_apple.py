from __future__ import print_function
import cv2 as cv
import os
import sys
import playsound
import threading
import time
import math
import fpstimer


ASCII_CHARS = ['.', ',', ':', ';', '+', '*', '?', '%', 'S', '#', '@']


def createTxt():
  capture = cv.VideoCapture("BadApple.mp4")
  if (capture.isOpened()== False):
    print("Error opening video stream or file")
  perc_length = int(capture.get(cv.CAP_PROP_FRAME_COUNT)) / 100
  counter = 0
  with open("temp.txt", "w") as f:
    while capture.isOpened():
          ret, frame = capture.read()
          if ret == True:
              counter += 1
              print(f"Progress: {round((counter / perc_length), 1)}%", end="\r")
              resize = cv.resize(frame, (210, 50), interpolation=cv.INTER_AREA)
              for line in resize:
                for pixel in line:
                  a = math.ceil(pixel[0] / 23)
                  if a > 11:
                    f.write(ASCII_CHARS[a - 2])
                  elif a == 0:
                    f.write(ASCII_CHARS[a])
                  else:
                    f.write(ASCII_CHARS[a - 1])
              f.write("\n")
          else:
              print("\nDone!")
              break
      

  capture.release()
  cv.destroyAllWindows()


def draw():
  with open("temp.txt", "r") as f:
    timer = fpstimer.FPSTimer(30)
    for line in f: 
        sys.stdout.write(line)
        timer.sleep()


def playSong():
  os.system("mode con: cols=210 lines=50")  
  threading.Thread(target = playsound.playsound, args = ("./bad-apple-audio.mp3",), daemon = True).start()
  threading.Thread(target = draw, daemon = True).start()


def main():
  while True:
    print("----------------------------------")
    print("1. Create txt file")
    print("2. Play audio")
    print("3. Exit")
    print("----------------------------------")
    choice = input("Enter your choice: ")
    if choice == "1":
      createTxt() 
    elif choice == "2":
      playSong()
    elif choice == "3":
      break
    else:
      print("\nInvalid input!")
      continue

if __name__ == "__main__":
  main()

