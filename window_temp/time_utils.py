import datetime
import time

def is_daytime():
    """
    Returns True if current time is between 04:00 and 16:00 inclusive.
    """
    hour = datetime.datetime.now().hour
    return 4 <= hour <= 16

def wait_time(indoor, outdoor):
    """
    Waits for an appropriate interval depending on the temperature difference
    and whether it's daytime (closing windows) or nighttime (opening windows).
    """
    if is_daytime():
        # Morning/daytime: close when indoor < outdoor
        diff = indoor - outdoor  # positive means cooler outside
    else:
        # Evening/night: open when outdoor < indoor
        diff = outdoor - indoor  # positive means warmer outside

    diff = abs(diff)

    if diff > 5:
        print("Checking again in 1h.")
        time.sleep(3600)
    elif diff >= 2:
        print("Checking again in 30mins.")
        time.sleep(1800)
    else:
        print("Getting close! Checking again in 15mins.")
        time.sleep(900)