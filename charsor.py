import  Tkinter
from    time    import sleep
from    time    import time
import  heatmap

SAMPLE_FREQUENCY = 10 # How many times a second to poll the cursor position

# Thanks rectangletangle
cursor = Tkinter.Tk()

# Thanks mouad
screenWidth = cursor.winfo_screenwidth()
screenHeight = cursor.winfo_screenheight()

print screenWidth, screenHeight

cursorPositions = []

# Runs until interupt (Ctrl + C) then generates heatmap on exit
try:
    while True:
        horizontalPos, verticalPos = cursor.winfo_pointerxy()
        
        # Flips vertical co-ordinates so heatmap is correct way up
        verticalPos = abs(verticalPos - screenHeight)
        
        cursorPositions.append((horizontalPos, verticalPos))
        
        sleep(0.1)
except KeyboardInterrupt:
    pass

# Function is only used once so that the heatmap/csv file names don't differ
currentTime = time()

with open("cursor_%d.csv" % currentTime,'w+') as cursorLogFile:
    for position in cursorPositions:
        print >> cursorLogFile, str(position[0]) + ',' + str(position[1])

hm = heatmap.Heatmap()
img = hm.heatmap(cursorPositions, dotsize=15, size=(screenWidth - 1, screenHeight - 1), area=((0, 0), (screenWidth - 1, screenHeight - 1)))
img.save("heatmap_%d.png" % currentTime)