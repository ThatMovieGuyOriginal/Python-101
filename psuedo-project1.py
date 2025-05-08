START

LIST = TEMPS[]
COUNTA = 0
MIN_TEMP = 0
MAX_TEMP = 0
AVG_TEMP = 0

while COUNTA < 7:
    numTemp = input("What is today's temp?: ")
    TEMPS.append(numTemp)
    print(TEMPS[])
    COUNTA = COUNTA + 1

MIN_TEMP = min.(TEMPS)
MAX_TEMP = max.(TEMPS)
AVG_TEMP = avg.(TEMPS)
print(f"Min: {MIN_TEMP}, Max: {MAX_TEMP}, Avg: {AVG_TEMP}")

END