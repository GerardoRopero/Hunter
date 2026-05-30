# drug_encoder.py

import csv


def encode_dataset(path):
    xs = []

    y_drugY = []
    y_drugA = []
    y_drugB = []
    y_drugC = []
    y_drugX = []

    with open(path, "r") as f:

        reader = csv.reader(f)

        next(reader)

        for row in reader:

            age = float(row[0])

            sex = 0
            if row[1] == "M":
                sex = 1

            bp = 0

            if row[2] == "NORMAL":
                bp = 1

            if row[2] == "HIGH":
                bp = 2

            chol = 0

            if row[3] == "HIGH":
                chol = 1

            nak = float(row[4])

            fila = [
                age,
                sex,
                bp,
                chol,
                nak
            ]

            xs.append(fila)

            drug = row[5]

            y_drugY.append(1 if drug == "DrugY" else 0)
            y_drugA.append(1 if drug == "drugA" else 0)
            y_drugB.append(1 if drug == "drugB" else 0)
            y_drugC.append(1 if drug == "drugC" else 0)
            y_drugX.append(1 if drug == "drugX" else 0)

    return {
        "xs": xs,
        "y_drugY": y_drugY,
        "y_drugA": y_drugA,
        "y_drugB": y_drugB,
        "y_drugC": y_drugC,
        "y_drugX": y_drugX
    }
