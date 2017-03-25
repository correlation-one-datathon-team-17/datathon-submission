import sys

'''
Read in csv
'''
def read_file(filename):
    headers = []
    dataset = []
    with open(filename, 'rU') as f:
        headers = f.readline().strip().split(',');
        for line in f:
            row = line.strip().split(",")
            dataset.append(row)
    return headers, dataset


if __name__ == "__main__":

    filename = sys.argv[1]
    headers, dataset = read_file(filename)

    new_dataset = []
    for row in dataset:
        result = []
        borough = row[0]
        day_total = [0] * 7
        for pos in range(1, len(row), 1):
            weekday = (pos + 3) % 7
            day_total[weekday] += int(row[pos])
        result.append(borough)
        result.extend(day_total[1:])
        result.append(day_total[0])
        new_dataset.append(result)

    new_header = ['borough', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print(",".join(new_header))
    for row in new_dataset:
        print(",".join([str(d) for d in row]))
