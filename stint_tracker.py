# Stint Laptime Tracker V_0_2
# Github AJC-A


import sys
import ac
import acsys

# AC requires function to be defined this way and for 
# the name of the function to be returned

l_lapcount = 0
lapcount = 0

l_laptime = 0
laptime = 0


# ---------------------------------------------------------------------------------
def acMain(ac_version):
    global l_lapcount, l_laptime
    # Define app window for lap count and lap timer. Create output csv file
    # The shortcut to access the console mid game is the Home key
    appWindow = ac.newApp("stint_tracker")
    ac.setSize(appWindow, 200, 200)

    ac.log("** Stint tracker** Hello, I fired up okay!")
    ac.console("** Stint Tracker** Hello, I fired up okay!")

    l_lapcount = ac.addLabel(appWindow, "Laps Completed: 0")
    ac.setPosition(l_lapcount, 3, 30)

    l_laptime = ac.addLabel(appWindow, "Start time: 0")
    ac.setPosition(l_laptime, 3, 60)

    with open('stintoutputfile.csv', 'a') as f:
        f.write("Start of Stint\n")
        f.write("Lap Number, Lap Time\n")

    return "stint_tracker"


# ---------------------------------------------------------------------------------

def acUpdate(deltaT):
    global l_lapcount, lapcount, l_laptime, laptime

    # Don't write anything to the console from here unless it's in an if statement - it causes a crash, deltaT must
    # be approx every ms

    # Update current lap time in app window
    laptime = (ac.getCarState(0, acsys.CS.LapTime)) / 1000
    ac.setText(l_laptime, "Current lap (s): {}".format(laptime))

    # if statement using difference between lapcount and the laps output from AC to record data

    laps = ac.getCarState(0, acsys.CS.LapCount)

    if laps > lapcount:
        # Uses the difference between laps and lap count to limit recording to once per lap
        lapcount = laps
        ac.setText(l_lapcount, "Laps Completed: {}".format(lapcount))

        # Write last lap data to csv
        last_lap_raw = ((ac.getCarState(0, acsys.CS.LastLap))) / 1000
        ac.console("**Last_lap recorded")
        last_lap_m = last_lap_raw // 60
        last_lap_s = last_lap_raw % 60
        ac.console("**Last_lap split into minutes and seconds")
        with open('stintoutputfile.csv', 'a') as f:
            f.write("{},{:.0f}:{:.3f}\n".format(lapcount, last_lap_m, last_lap_s))
            ac.console("** stint tracker: lap written to file")
            ac.console("{},{:.0f}:{:.3f}\n".format(lapcount, last_lap_m, last_lap_s))
# ----------------------------------------------------------------------------------
