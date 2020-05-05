import csv
import upload

db = upload.uploader()

with open('crime.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            #input()
            db.create_table("crime", row)
            line_count += 1
        else:
            #print(f'Column values are {", ".join(row)}')
            db.insert_row("crime",row)
            line_count += 1
            print(line_count)
    db.commit()
    print(f'Processed {line_count} lines.')
