import csv

def mean(data, index):
    total = sum(d[index] for d in data)
    return total / len(data)

def linRegression(data):
    mean_x = mean(data, 0)
    mean_y = mean(data, 1)

    exp1 = sum((d[0] - mean_x) * (d[1] - mean_y) for d in data)
    exp2 = sum((d[0] - mean_x) ** 2 for d in data)

    a = exp1 / exp2
    b = mean_y - (a * mean_x)
    
    return a, b

if __name__ == "__main__":
    data = []
    with open("data.csv", "r") as datafile:
        reader = csv.reader(datafile)
        next(reader) 
        for row in reader:
            data.append((float(row[0]), float(row[1])))

    with open("output.txt", "w") as datafile1:
        ans = linRegression(data)
        for d in data[:-1]:
            x, y = d
            datafile1.write(f"{x}  {y}  {ans[0] * x + ans[1]}\n")
        print(ans)
