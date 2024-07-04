import csv

data_sources = []


def add_new_data_source():
    file_path = input("Enter data source file path: ").strip()
    try:
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            headers = next(reader)
            records = sum(1 for record in headers)
            revenue = 0
            gross_profit = 0
            for row in reader:
                revenue += int(row[8])
                gross_profit += int(row[10])

        print(f"Datasource structure: {', '.join(headers)}")
        print(f"Total records: {records}")

        data_sources.append({'file_path': file_path, 'records': records, 'revenue': revenue,
                             'grossProfit': gross_profit, 'metric': None})
        print('\n\n\n\n\n', data_sources)
    except FileNotFoundError:
        print("File not found. Please enter a valid file path.")