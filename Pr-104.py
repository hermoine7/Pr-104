from collections import Counter
import csv

with open('HeightWeight.csv', newline='') as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)

totalWeight = 0
totalPeople = len(fileData)
sortedData = []

for data in fileData:
    totalWeight += float(data[2])
    sortedData.append(float(data[2]))

sortedData.sort()

def getMean(totalWeight, totalPeople):
    mean = totalWeight / totalPeople
    print("Mean: ", mean)

def getMedian(totalPeople, sortedData):
    if totalPeople % 2 == 0:
        med1 = float(sortedData[totalPeople//2])
        med2 = float(sortedData[totalPeople//2 - 1])
        median = (med1 + med2) / 2
    else:
        median = float(sortedData[totalPeople//2])
    print("Median: ", median)

def getMode(sortedData):
    data = Counter(sortedData)
    modeRange = {
                            "75-85": 0,
                            "85-95": 0,
                            "95-105": 0,
                            "105-115": 0,
                            "115-125": 0,
                            "125-135": 0,
                            "135-145": 0,
                            "145-155": 0,
                            "155-165": 0,
                            "165-175": 0
                        }
    for weight, occurence in data.items():
        if 75 < weight < 85:
            modeRange["75-85"] += occurence
        elif 85 < weight < 95:
            modeRange["85-95"] += occurence
        elif 95 < weight < 105:
            modeRange["95-105"] += occurence
        elif 105 < weight < 115:
            modeRange["105-115"] += occurence
        elif 115 < weight < 125:
            modeRange["115-125"] += occurence
        elif 125 < weight < 135:
            modeRange["125-135"] += occurence
        elif 135 < weight < 145:
            modeRange["135-145"] += occurence
        elif 145 < weight < 155:
            modeRange["145-155"] += occurence
        elif 155 < weight < 165:
            modeRange["155-165"] += occurence
        elif 165 < weight < 175:
            modeRange["165-175"] += occurence
            
    modeRange2, modeOccurence = 0, 0
    for range, occurence in modeRange.items():
        if occurence > modeOccurence:
            modeRange2, modeOccurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
    mode = float((modeRange2[0] + modeRange2[1]) / 2)
    print("Mode: ", mode)

getMean(totalWeight, totalPeople)
getMedian(totalPeople, sortedData)
getMode(sortedData)
