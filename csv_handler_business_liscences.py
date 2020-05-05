import csv
import upload

db = upload.uploader()


with open('active_business_licenses.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        # if line_count == 0:
        #     print(f'Column names are {", ".join(row)}')
        #     db.create_table("business_licenses", row)
        #     line_count += 1
        print(f'Column values are {", ".join(row)}')
        db.insert_row("business_licenses",row)
        line_count += 1
    print(f'Processed {line_count} lines.')
