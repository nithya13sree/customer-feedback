import csv
from io import StringIO

print("===== CUSTOMER FEEDBACK MANAGEMENT SYSTEM =====")

feedback_data = []

n = int(input("Enter number of customer feedbacks: "))

for i in range(n):
    print("\nCustomer", i + 1)

    customer_id = input("Enter Customer ID: ")
    name = input("Enter Customer Name: ")
    rating = input("Enter Rating (1-5): ")
    feedback = input("Enter Feedback: ")

    feedback_data.append([customer_id, name, rating, feedback])

print("\n===== CUSTOMER FEEDBACK RECORDS =====")

print("Customer ID | Name | Rating | Feedback")
print("----------------------------------------")

for record in feedback_data:
    print(record[0], "|", record[1], "|", record[2], "|", record[3])

# Convert the data into CSV format
csv_data = StringIO()
writer = csv.writer(csv_data)

writer.writerow(["Customer ID", "Name", "Rating", "Feedback"])

for record in feedback_data:
    writer.writerow(record)

print("\n===== CSV FORMAT =====")
print(csv_data.getvalue())