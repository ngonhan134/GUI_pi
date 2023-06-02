
import time
import random
def GetDistance():
    # Generate a random distance between 0 and 100 cm
    distance = random.uniform(0, 100)
    print("Random Distance:", distance, "cm")
    return distance


def Detected_Object():
    consecutive_count = 0
    required_consecutive_count = 2
    while True:
        distance = GetDistance()
        if distance < 30:
            consecutive_count += 1
        else:
            consecutive_count = 0
        if consecutive_count >= required_consecutive_count:
            return True
        
        time.sleep(0.5)

def open_door():
    print("Opening the door")

    time.sleep(2)

    time.sleep(1)
    print("Door is opened")

def close_door():
    print("Closing the door")
    time.sleep(2)

    print("Door is closed")