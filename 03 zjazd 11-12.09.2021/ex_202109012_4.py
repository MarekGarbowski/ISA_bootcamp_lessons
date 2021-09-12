
with open('files/moj_csv.csv', 'r') as f:
    results = []
    for line in f:
            words = line.split(',')
            results.append((words[0], words[1:]))
    print(results)

