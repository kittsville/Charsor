import  Tkinter
from    time    import sleep
from    time    import strftime
import  heatmap
import  os

SAMPLE_INTERVAL = 0.1 # How often, in seconds, to poll the cursor position

# Thanks rectangletangle
cursor = Tkinter.Tk()

# Thanks mouad
screenWidth = cursor.winfo_screenwidth()
screenHeight = cursor.winfo_screenheight()

print "Your screen resolution is %dx%d" % (screenWidth, screenHeight)
print 'Monitoring starts now and ends when you kill the script\n'

cursorPositions = []

# Runs until interupt (Ctrl + C) then generates heatmap on exit
try:
    while True:
        horizontalPos, verticalPos = cursor.winfo_pointerxy()
        
        # Flips vertical co-ordinates so heatmap is correct way up
        verticalPos = abs(verticalPos - screenHeight)
        
        cursorPositions.append((horizontalPos, verticalPos))
        
        sleep(SAMPLE_INTERVAL)
except KeyboardInterrupt:
    pass

# Function is only used once so that the heatmap/csv file names don't differ
timestamp = strftime("%Y-%m-%dT%H%M%S")

if not os.path.exists('output'):
    os.makedirs('output')

CSVPath = "output/cursor_%s.csv" % timestamp
MapPath = "output/heatmap_%s.png" % timestamp

# Saves all measured cursor positions to a Comma Separated Value file
# You can open this in Excel, R or any text editor
with open(CSVPath,'w+') as cursorLogFile:
    for position in cursorPositions:
        print >> cursorLogFile, str(position[0]) + ',' + str(position[1])

print 'Saved CSV of cursor positions to ' + CSVPath

# Generates heatmap
# http://jjguy.com/heatmap/
hm = heatmap.Heatmap()
img = hm.heatmap(cursorPositions, dotsize=25, scheme='pbj', size=(screenWidth - 1, screenHeight - 1), area=((0, 0), (screenWidth, screenHeight)))
img.save(MapPath)

print 'Saved heatmap of cursor positions to ' + MapPath
