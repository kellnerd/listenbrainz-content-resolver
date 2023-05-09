#!/usr/bin/env python3

import re

from test_regexp import TEST_STRINGS

EXPRESSIONS = [
    # Track name (guff #1) (guff #2)
    # Tabula Rasa (feat. Lorraine Weiss)
    # TO STAY ALIVE [Feat. SkullyOSkully]
    [r"\s*?(?P<title>.+?)\s*?(?P<feat>(?:\[|\()?(?:feat(?:uring)?|ft)\.?)\s*?(?P<artists>.+)\s*", 0],

    # For The Love feat. Amy True
    # For The Love ft. Amy True
    # For The Love ft Amy True
    # Birds Without a Feather -> Nothing!
    [r"\s*?(?P<title>.+?)\s*?(?P<feat>\(?(?:feat(?:uring)?|ft)\.?)\s*?(?P<artists>.+)\s*", 0],

    # Don't Give up - 2001 remaster
    [r"\s*?(?P<title>.+?)(?:\s*?-)(?P<dash>.*)", 0],
]


def detune(text: str):

    if len(EXPRESSIONS[0]) == 2:
        for exp in EXPRESSIONS:
            exp.append(re.compile(exp[0], re.IGNORECASE))

    for i, exp in enumerate(EXPRESSIONS):
        m = exp[2].match(text)
        if m is not None:
#            print(f" {i} ", end="")
#            for g in m.groups():
#                print(f"'{g}' ", end="")
#
#            print()
#            print()

#            print("%-40s %s" % (text[:39], m.groups()[0]))
#            print()

            return m.groups()[0]

#    print(text)
#    print(f"FAIL: {text}\n")

    return text


def process_file(file_name: str):
    
    with open(file_name, "r") as f:
        while True:
            line = f.readline()
            if not line:
                break

            line = line.strip()
            detune(line)

def process_tests():

    passed = 0
    failed = 0
    for test_str, exp_detuned in TEST_STRINGS:
        detuned = detune(test_str)
        if detuned != exp_detuned:
            print("FAIL: %-40s %s" % (exp_detuned, detuned))
            failed += 1
        else:
            passed += 1

    print(f"{passed} passed, {failed} failed.")


if __name__ == "__main__":
#    process_file("recording_feat.txt")
    process_tests()
