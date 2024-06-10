import csv
import re

combine = """
232678 (3.34)                                232730 (3.39) 232732 (3.19) 232741 (2.99)
232749 (2.91) 232761 (3.37) 232762 (2.85) 232768 (3.07)
232769 (3.02) 232779 (3.10) 232781 (2.59) 232783 (3.31)
232789 (2.91) 232811 (3.15) 232814 (3.40) 232815 (3.08)
232820 (3.05) 232824 (3.30)

232729 { 1421 (T) } 232738 { 1421 (T) } 232739 { 1421 (T) } 232744 { 1421 (T) }
232746 { 1421 (T) } 232751 { 1421 (T) } 232755 { 1421 (T) } 232756 { 1421 (T) }
232757 { 1421 (T) } 232764 { 1421 (T) } 232765 { 1421 (T), 1422 (T) } 232767 { 1421 (T) }
232773 { 1421 (T) } 232778 { 1421 (T) } 232782 { 1421 (T) } 232791 { 1421 (T), 1422 (T) }
232793 { 1421 (T) } 232796 { 1421 (T), 1422 (T) } 232802 { 1421 (T), 2823 (T) } 232805 { 1421 (T), 2823 (T) }
232807 { 1421 (T) } 232809 { 1421 (T), 1422 (T), 2823 (T) } 232810 { 1421 (T) } 232816 { 1421 (T), 1422 (T) }
232818 { 1421 (T) } 232822 { 1421 (T) } 232823 { 1421 (T), 1422 (T), 2823 (T) } 232825 { 1421 (T), 2823 (T) }
232828 { 1421 (T) } 232835 { 1421 (T), 1422 (T), 2823 (T) } 232840 { 1421 (T) }
"""


def write_to_csv(filename, header: list, rows: list):
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(header)
        csvwriter.writerows(rows)


def write_passed_result():
    results = re.findall("(\d+)\s+\((\d+\.\d+)\)", combine)
    header = ["Roll", "Point"]
    rows: list = []
    for result in results:
        rows.append([result[0], result[1]])
    write_to_csv("passed_result.csv", header, rows)


def write_failed_result():
    results = re.findall("(\d+)\s+\{\s+([\d+\s+\(\w\),*\s*]*)\s+\}", combine)
    subject_wise_role = {}
    for result in results:
        roll = result[0]
        subject = result[1]

        extract_subject = re.findall("(\d+)", subject)
        for subject in extract_subject:
            if subject not in subject_wise_role:
                subject_wise_role[subject] = []
            subject_wise_role[subject].append(roll)

    header = []
    rows = []
    max_row = 0
    for subject in subject_wise_role:
        total_row = len(subject_wise_role[subject])
        if total_row > max_row:
            max_row = total_row
        header.append(f"{subject} ({total_row})")

    for index in range(max_row):
        row = []
        for subject in subject_wise_role:
            try:
                row.append(subject_wise_role[subject][index])
            except:
                row.append("")
        rows.append(row)
    write_to_csv("failed_result.csv", header, rows)


write_passed_result()
write_failed_result()
