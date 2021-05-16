import csv

with open('./country.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            data = "INSERT INTO `country` (`id`, `created`, `updated`, `uuid`, `is_deleted`, `is_active`, `name`, `iso_code`, `iso_code2`, `phone_code`, `internet_tld`) VALUES ("
            data += str(line_count) + ", now(), now(), UUID(), 0, 1, '" + row[0] + "', '" + row[1] + "', '" + row[2] + "', '" + row[3] + "', '" + row[4].replace(".", "") + "' " + ");"
            # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            print(data)
            line_count += 1
    print(f'Processed {line_count} lines.')

