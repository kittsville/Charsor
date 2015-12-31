import  Tkinter
from    time    import sleep
import  heatmap

SAMPLE_FREQUENCY = 10 # How many times a second to poll the cursor position

# Thanks rectangletangle
cursor = Tkinter.Tk()

# Thanks mouad
screenWidth = cursor.winfo_screenwidth()
screenHeight = cursor.winfo_screenheight()

print screenWidth, screenHeight

points = []

# Runs until interupt (Ctrl + C) then generates heatmap on exit
try:
    while True:
        horizontalPos, verticalPos = cursor.winfo_pointerxy()
        
        # Flips vertical co-ordinates so heatmap is correct way up
        verticalPos = abs(verticalPos - screenHeight)
        
        points.append((horizontalPos, verticalPos))
        
        sleep(0.1)
except KeyboardInterrupt:
    pass


hm = heatmap.Heatmap()
img = hm.heatmap(points, dotsize=15, size=(screenWidth - 1, screenHeight - 1), area=((0, 0), (screenWidth - 1, screenHeight - 1)))
img.save("classic.png")