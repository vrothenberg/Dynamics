def readFile(filePath):
    """Reading a file and returning a list of lines"""
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]



def fileToList(filePath):
    fileLines = readFile(filePath)
    data = []
    for line in fileLines:
        splitLine = line.split('\t')
        for element in splitLine:
            data.append(element)
    return data 



# data = list(map(int, fileToList('numbers.txt')))
# data.sort()
# print(data)
# fields = [(12,14), (15,17), (18,20), (21,23), (24,26)]
# counts = []
# for field in fields:
#     lower, upper = field
#     total = 0
#     for element in data:
#         if element >= lower and element <= upper:
#             total += 1
#     counts.append(total)
#     rel_freq = float(total)/len(data)
#     print("%d-%d: %d %f %.2f%%" % (lower, upper, total, rel_freq, rel_freq*100))

# print(sum(counts), len(data))

lines = readFile('states.txt')
incomes = []
for line in lines:
    incomes.append(float(line.split('\t')[1]))

incomes.sort()
fields = [(65.0, 69.9), (70.0,74.9), (75.0,79.9), (80.0,84.9), (85.0,89.9), (90.0, 94.9), (95.0, 99.9), (100.0, 104.9), (105.0, 109.9), (110.0, 114.9)]
counts = []
for field in fields:
    lower, upper = field
    freq = 0
    for element in incomes:
        if element >= lower and element <= upper:
            freq += 1
    counts.append(freq)
    rel_freq = float(freq)/len(incomes)
    print("%f-%f: %d %f %.2f%%" % (lower, upper, freq, rel_freq, rel_freq*100))

print(sum(counts))


x = [1,2,3,4,5]

def mean(arr, population=False):
    n = len(x)
    if not population:
        n -= 1
