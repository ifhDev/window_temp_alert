import time

def wait_time(indoor, outdoor):
    """
    Waits for an appropriate interval depending on the difference between indoor and outdoor temperature.
    
    Prints how long it will wait, then pauses the program.
    """

    if outdoor-indoor>5:
        print("Checking again in 1h.")
        time.sleep(3600)
    elif outdoor-indoor>=2:
        print("Checking again in 30mins.")
        time.sleep(1800)
    else:
        print("Getting close! Checking again in 15mins.")
        time.sleep(900)

# def daytime()