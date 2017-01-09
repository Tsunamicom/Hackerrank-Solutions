# https://www.hackerrank.com/challenges/digital-camera-day-or-night

lastinput = True
daycount = 0
nightcount = 0
while lastinput != False:
    try:
        currentline = input()
    except:
        break
    if currentline == None:
        lastinput = True
        break
    else:
        for pixel in currentline.split(' '):
            if sum(map(int, pixel.split(','))) > 240:
                daycount += 1
            else:
                nightcount += 1

if daycount > nightcount:
    print('day')
else:
    print('night')
