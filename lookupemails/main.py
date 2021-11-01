import sys
import csv
import argparse

# create function to get and parse arguments
def get_args():
  parser = argparse.ArgumentParser(description="Lookup emails from a csv file")
  parser.add_argument("--anon-csv", required=True, help="your csv file")
  parser.add_argument("--emails", required=True, help="your list of emails")
  parser.add_argument("--output", default=sys.stdout, type=argparse.FileType("w"),  help="your output file")
  args = parser.parse_args()
  return args


required_fields = [
  'email', 
  'date_subscribed', 
  'lead_source'
]


if __name__ == "__main__":
  args = get_args()

  # set thre reader
  reader = csv.DictReader(open(args.anon_csv))
  # iterate over emails.txt
  with open(args.emails) as file:
    emails = set(line.strip() for line in file)
  writer = csv.DictWriter(args.output, fieldnames=required_fields)


  writer.writeheader()
  for row in reader:
    if row["Email"] in emails:
      row["email"] = row["Email"]
      ouput_row = {
        field: row[field]
        for field in required_fields
      }
      writer.writerow(ouput_row)
  
