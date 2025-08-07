import csv
import logging

logging.basicConfig(filename='violations.log',level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def parse_timing_report(report_path):
  violations=[]
  with open(report_path,'r') as file:
    for line in file:
      line=line.strip()
      if 'setup violation' in line.lower() or 'hold violation' in line.lower():
        if 'setup' in line.lower():
          violation_type='Setup'

        else:
          violation_type='Hold'
        violations.append({'type' : violation_type ,'detail':line})

  return violations

def write_csv(violations,csv_path):
  with open(csv_path,mode='w',newline='') as file:
    writer=csv.DictWriter(file, fieldnames=['type', 'detail'])
    writer.writeheader()
    writer.writerows(violations)


def main():
  report_file='timing_report.txt'
  output_csv='violations_summary.csv'

  print(" Parsing timing report...")
  violations=parse_timing_report(report_file)

  if violations:
    print(f" Found {len(violations)} violations.")
    write_csv(violations,output_csv)
    logging.info(f"{len(violations)} violations extracted and written to {output_csv}")
  else:
    print("No violations found ")
    logging.info("No violations found in report")  
                        

if __name__ == "__main__":
  main()