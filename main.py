import csv, sys

def main():
    if len(sys.argv) < 2:
        print("Missing input file")
        sys.exit(0)
    print("Input file present")
    inputFile = sys.argv[1]
    with open(inputFile, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        summary = {}
        for row in reader:
            date = row["Date"]
            if(not date in summary.values()):
                summary[date] = {"cal":0, "carb":0, "prot":0}
            summary[date]["cal"] += float(row["Calories"])
            summary[date]["carb"] += float(row["Carbohydrates (g)"])
            summary[date]["prot"] += float(row["Protein (g)"])
        
        totalCal = 0
        totalCarb = 0
        totalProt = 0
        for day in summary:
            print(summary[day], "\n")
            totalCal += summary[day]["cal"]
            totalCarb += summary[day]["carb"]
            totalProt += summary[day]["prot"]

        averageCal = totalCal / len(summary)
        averageCarb = totalCarb / len(summary)
        averageProt = totalProt / len(summary)
        print("For days: ", len(summary))
        print("Calories:", averageCal)
        print("Carbs: ", averageCarb)
        print("Prot: ", averageProt)

if __name__ == "__main__":
    main()

