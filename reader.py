import csv
import sys
import os


# przykładowe dane: wejsciowe ds_salaries.csv ds_salaries2.csv 10 5 test

class FileCsv:
    def __init__(self, name, outputfile):
        if not os.path.exists(name):
            print("File not exist")
            self.exist = False
            current_directory = '.'  # Current directory
            files = os.listdir()
            print("Files in the current directory:")
            for file in files:
                print(file)
        else:
            self.exist = True

        self.name = name
        self.output_file = outputfile

    def editValue(self, row_num, column_num, newValue):
        if self.exist:
            with open(self.name, 'r') as csv_file:
                csv_data = csv.reader(csv_file)
                data = list(csv_data)

                if row_num < len(data) and column_num < len(data[row_num]):
                    data[row_num][column_num] = newValue
                else:
                    print("Invalid arguments")

                with open(self.output_file, 'w', newline='') as output_csv_file:
                    csv_writer = csv.writer(output_csv_file)
                    csv_writer.writerows(data)
        else:
            print("File not exist")

arguments = sys.argv

file = FileCsv(arguments[1],arguments[2])
file.editValue(int(arguments[3]), int(arguments[4]), arguments[5])



