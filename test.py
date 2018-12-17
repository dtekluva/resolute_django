# import time
# import pytz
# from datetime import datetime
# dt = datetime(2018, 1, 1)
# print(dt)
# milliseconds = int(round(dt.timestamp() * 1000))
# print(milliseconds)

# tz = pytz.timezone('Africa/Lagos')
# lagos = datetime.now(tz)
# formatedDate = lagos.strftime("%Y-%m-%d %H:%M:%S")
# print(round(lagos.timestamp()))


numberGames = {}

numberGames[(1,2,4)] = 8

numberGames[(4,2,1)] = 10

numberGames[(1,2)] = 12

sum = 0

for k in numberGames:

    sum += numberGames[k]



print(len(numberGames) + sum)