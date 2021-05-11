import csv

def average(file: str) -> str:
    try:
        with open(file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            heights = []
            weights = []
            for row in reader:
                heights.append(float(row[reader.fieldnames[1]]))
                weights.append(float(row[reader.fieldnames[2]]))
        avg_height = sum(heights) / len(heights)
        print(avg_height)
        avg_weights = sum(weights) / len(weights)
        print(avg_weights)

        return 'Average height~: ' + str(round(avg_height*2.54, 2)) + ' cm' + '<br>' + 'Average weight~: ' + str(round(avg_weights/2.2046)) + ' kg' + '<br>' + 'Collected: ' + str(len(heights)) + ' items'
    except Exception:

        return 'OOOOps!! Check filename!'