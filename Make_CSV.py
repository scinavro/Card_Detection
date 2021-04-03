import csv

with open("mycsv.csv", "w", newline="") as f:
    thewriter = csv.writer(f)

    for i in range(1, 601):
        thewriter.writerow(["sak_five_{}.png".format(i), "0"])

    for i in range(1, 601):
        thewriter.writerow(["man_seven_{}.png".format(i), "1"])

    for i in range(1, 601):
        thewriter.writerow(["man_seven_r_{}.png".format(i), "2"])

    for i in range(1, 601):
        thewriter.writerow(["Choong_{}.png".format(i), "3"])

    for i in range(1, 601):
        thewriter.writerow(["Choong_r_{}.png".format(i), "4"])
