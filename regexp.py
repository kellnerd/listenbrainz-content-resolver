#!/usr/bin/env python3

import re

#Purple Light Feat. Antonia - Dub Mix
#Water Lilies feat. Sol Monk
#Take It There (feat. Replife)
#When We're Asleep (feat. Mike Tempesta & John Tempest)
#For The Love feat. Amy True
#Wind Up Your Waist feat. Shiffa Dan, RTKal & G.O.L.D
#For The Love feat. Amy True (Matta Remix)
#Bones (feat. Bayo Akomolafe)
#Tabula Rasa (feat. Lorraine Weiss)
#Love feat. Rebel Sun


EXPRESSIONS = [
    # Track name (guff #1) (guff #2)
    [r"([^(]+)\((?:(\w+))\)", 1],
    # Tabula Rasa (feat. Lorraine Weiss)
    # For The Love feat. Amy True
    # For The Love ft. Amy True
    # For The Love ft Amy True
    [r"(.+?)(?:\s*?)(feat\.?|ft\.?)(?:\s*)(.+)", 1],
]


def detune(text: str):

    if len(EXPRESSIONS[0]) == 2:
        for exp in EXPRESSIONS:
            exp.append(re.compile(exp[0], re.IGNORECASE))

    print(text)
    for i, exp in enumerate(EXPRESSIONS):
        m = exp[2].match(text)
        if m is not None:
            print(f" {i} ", end="")
            for g in m.groups():
                print(f"'{g}' ", end="")

            print()
            print()

            return

    print(f"FAIL: {text}")


def process_file(file_name: str):
    
    with open(file_name, "r") as f:
        while True:
            line = f.readline()
            if not line:
                break

            line = line.strip()
            detune(line)

if __name__ == "__main__":
    process_file("recording_feat.txt")
