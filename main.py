import csv, sys

def main():
    if len(sys.argv) < 2:
        print("Missing input file")
        sys.exit(0)
    print("Input file present")
    inputFile = sys.argv[1]
    summary = {}
    with open(inputFile, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            date = row["Date"]
            if(not date in summary.values()):
                summary[date] = {"cal":0, "carb":0, "prot":0, "fiber":0}
            summary[date]["cal"] += float(row["Calories"])
            summary[date]["carb"] += float(row["Carbohydrates (g)"])
            summary[date]["prot"] += float(row["Protein (g)"])
            summary[date]["fiber"] += float(row["Fiber"])
        
        totalCal = 0
        totalCarb = 0
        totalProt = 0
        totalFiber = 0
        for day in summary:
            print(summary[day], "\n")
            totalCal += summary[day]["cal"]
            totalCarb += summary[day]["carb"]
            totalProt += summary[day]["prot"]
            totalFiber += summary[day]["fiber"]

        averageCal = totalCal / len(summary)
        averageCarb = totalCarb / len(summary)
        averageProt = totalProt / len(summary)
        averageFiber = totalFiber / len(summary)
        print("For days: ", len(summary))
        print("Calories:", averageCal)
        print("Carbs: ", averageCarb)
        print("Prot: ", averageProt)
        print("Fiber: ", averageFiber)

    with open('data/output.csv', mode='w') as csv_file:
        fieldnames = ['date', 'cal', 'carb','prot','fiber']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for day in summary:
            writer.writerow({'date': day,'cal': summary[day]["cal"], 'carb':summary[day]["carb"], 'prot': summary[day]["prot"], 'fiber': summary[day]["fiber"]})

if __name__ == "__main__":
    main()

