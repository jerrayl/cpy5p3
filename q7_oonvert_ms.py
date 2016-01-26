#convert miliseconds to hours,minutes,seconds

def convert_ms(n):
    i=n
    hours=0
    minutes=0
    seconds=0
    while i>=3600000:
        hours+=1
        i-=3600000
    while i>=60000:
        minutes+=1
        i-=60000
    while i>=1000:
        seconds+=1
        i-=1000
    print("{0}:{1}:{2}".format(hours,minutes,seconds))

