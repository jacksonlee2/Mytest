# TRYING TO DEVELOP A SMALL ALARM CLOCK WHICH WILL RING AFTER CERTAIN AMOUNT OF
#GIVEN TIME
#initialisation
import time
import subprocess
import os

# THE FIRST HALF CONVERTS MINUTES TO SECONDS
loop = 1;
while loop == 1:
    
    a = input('Enter the time: ');
    a = int(a);
    a = a*60;
    print(a);
    time.sleep(a);
    if a==1200:
        subprocess.Popen(['notify-send',"Time to take a break sir!"]);
        os.system("xdg-open break.jpg")
        
    else:
        subprocess.Popen(['notify-send',"Time completed"]);
        os.system("xdg-open Downloads/song.mp3")
        
