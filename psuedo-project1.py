TEMPS = []
COUNTA = 0

while COUNTA < 7:
    numTemp = int(input("What is today's temp?: "))
    TEMPS.append(numTemp)
    print(TEMPS)
    COUNTA = COUNTA + 1

MIN_TEMP = min(TEMPS)
MAX_TEMP = max(TEMPS)
AVG_TEMP = sum(TEMPS) / COUNTA
print(f"Min: {MIN_TEMP}, Max: {MAX_TEMP}, Avg: {AVG_TEMP}")
