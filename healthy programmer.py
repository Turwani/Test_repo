# Healthy programmer
# 9am - 5pm
# Water- water.mp3,(3.5 litres), input to stop = Drank - log (regular interval)(date time module)
# Eyes- eyes.mp3 - input to stop = EyDone, every 30
# Physical activity- physical.mp3, every 45 min, ExDone

# Rules
# Pygame module to play audio

from pygame import mixer
from datetime import datetime
from time import time
print("\t\t\t\t_________Healthy Program__________\t\t\t\t")


def musicp_layer(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        user_input = input()
        user_input_in_caps = user_input.upper()
        if user_input_in_caps == "OK":
            mixer.music.stop()
        break


def logfunc(message):
    with open("My_log.txt", "a") as f:
        f.write(f"{message} {datetime.now()}\n")


if __name__ == '__main__':
    water_time = time()
    eyes_time = time()
    phyex_time = time()
    watersec = 30*60
    eyesec = 35*60
    physec = 45*60

    while True:
        if time() - water_time > watersec:
            print("Time to drink water. To stop the alarm press 'OK' ")
            musicp_layer("water.mp3")
            water_time = time()
            logfunc("Drank water at")

        if time() - eyes_time > eyesec:
            print("Time to relax eyes. To stop the alarm press 'OK' ")
            musicp_layer("eyes.mp3")
            eyes_time = time()
            logfunc("Eyes relaxed at")

        if time() - phyex_time > physec:
            print("Time to exercise. To stop the alarm press 'OK' ")
            musicp_layer("physical.mp3")
            phyex_time = time()
            logfunc("Workout at")

# from pygame import mixer
# from datetime import datetime
# from time import time
#
# def musiconloop(file, stopper):
#     mixer.init()
#     mixer.music.load(file)
#     mixer.music.play()
#     while True:
#         input_of_user = input()
#         if input_of_user == stopper:
#             mixer.music.stop()
#             break
#
# def log_now(msg):
#     with open("mylogs.txt", "a") as f:
#         f.write(f"{msg} {datetime.now()}\n")
#
# if __name__ == '__main__':
#     # musiconloop("water.mp3", "stop")
#     init_water = time()
#     init_eyes = time()
#     init_exercise = time()
#     watersecs = 5
#     exsecs = 10
#     eyessecs = 15
#
#     while True:
#         if time() - init_water > watersecs:
#             print("Water Drinking time. Enter 'drank' to stop the alarm.")
#             musiconloop("water.mp3", 'drank')
#             init_water = time()
#             log_now("Drank Water at")
#
#         if time() - init_eyes > eyessecs:
#             print("Eye exercise time. Enter 'doneeyes' to stop the alarm.")
#             musiconloop("eyes.mp3", 'doneeyes')
#             init_eyes = time()
#             log_now("Eyes Relaxed at")
#
#         if time() - init_exercise > exsecs:
#             print("Physical Activity Time. Enter 'donephy' to stop the alarm.")
#             musiconloop("physical.mp3", 'donephy')
#             init_exercise = time()
#             log_now("Physical Activity done at")
