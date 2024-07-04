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

def check_existing_information():
    print("\nExisting Information:")
    for i, source in enumerate(data_sources, start=1):
        metric_info = f"Metric: {source['metric']}" if source['metric'] else "Metric: Not calculated"
        print(f"{i}) Datasource: {source['file_path']} | {metric_info}")


def calculate_metric():
    if not data_sources:
        print("No data sources available. Please add a data source first.")
        return

    print("\nSelect data source:")
    for i, source in enumerate(data_sources, start=1):
        print(f"{i}. {source['file_path']}")

    try:
        choice = int(input("Select data source: ").strip())
        if choice < 1 or choice > len(data_sources):
            raise ValueError
    except ValueError:
        print("Invalid choice. Please select a valid data source number.")
        return