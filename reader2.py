import json
import pickle
import csv
import sys

class FileConverter:
    def __init__(self, input_file):
        self.input_file = input_file
        self.data = None

    def read_data(self):
        raise NotImplementedError("read_data nie zaimplementowan")

    def to_csv(self, output_file):
        raise NotImplementedError("to_csv nie zaimplementowan")

    def to_json(self, output_file):
        raise NotImplementedError("to_json nie zaimplementowan")

    def to_txt(self, output_file):
        raise NotImplementedError("to_txt nie zaimplementowan")

    def to_pkl(self, output_file):
        raise NotImplementedError("to_pkl nie zaimplementowan")

    def change_value(self, row, column, new_value):
        if self.data is not None and 0 <= row < len(self.data):
            if column < len(self.data[row]):
                self.data[row][column] = new_value
            else:
                raise ValueError(f"nie ma takiej wartosci")
        else:
            raise ValueError(f"Invalid row index: {row}")


class CSVConverter(FileConverter):
    def read_data(self):
        with open(self.input_file, 'r') as f:
            csv_reader = csv.DictReader(f)
            self.data = list(csv_reader)

    def to_csv(self, output_file):
        with open(output_file, 'w', newline='') as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=self.data[0].keys())
            csv_writer.writeheader()
            csv_writer.writerows(self.data)

    def to_json(self, output_file):
        with open(output_file, 'w') as f:
            json.dump(self.data, f)

    def to_txt(self, output_file):
        with open(output_file, 'w') as f:
            for row in self.data:
                f.write(','.join(str(value) for value in row.values()) + '\n')

    def to_pkl(self, output_file):
        with open(output_file, 'wb') as f:
            pickle.dump(self.data, f)


class JSONConverter(FileConverter):
    def read_data(self):
        with open(self.input_file, 'r') as f:
            self.data = json.load(f)

    def to_csv(self, output_file):
        with open(output_file, 'w', newline='') as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=self.data[0].keys())
            csv_writer.writeheader()
            csv_writer.writerows(self.data)

    def to_json(self, output_file):
        with open(output_file, 'w') as f:
            json.dump(self.data, f)

    def to_txt(self, output_file):
        with open(output_file, 'w') as f:
            for row in self.data:
                f.write(','.join(str(value) for value in row.values()) + '\n')

    def to_pkl(self, output_file):
        with open(output_file, 'wb') as f:
            pickle.dump(self.data, f)


class TXTConverter(FileConverter):
    def read_data(self):
        with open(self.input_file, 'r') as f:
            self.data = [line.strip().split(',') for line in f.readlines()]

    def to_csv(self, output_file):
        with open(output_file, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerows(self.data)

    def to_json(self, output_file):
        with open(output_file, 'w') as f:
            json.dump(self.data, f)

    def to_txt(self, output_file):
        with open(output_file, 'w') as f:
            for row in self.data:
                f.write(','.join(str(value) for value in row) + '\n')

    def to_pkl(self, output_file):
        with open(output_file, 'wb') as f:
            pickle.dump(self.data, f)


class PKLConverter(FileConverter):
    def read_data(self):
        with open(self.input_file, 'rb') as f:
            self.data = pickle.load(f)

    def to_csv(self, output_file):
        with open(output_file, 'w', newline='') as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=self.data[0].keys())
            csv_writer.writeheader()
            csv_writer.writerows(self.data)

    def to_json(self, output_file):
        with open(output_file, 'w') as f:
            json.dump(self.data, f)

    def to_txt(self, output_file):
        with open(output_file, 'w') as f:
            for row in self.data:
                f.write(','.join(str(value) for value in row.values()) + '\n')

    def to_pkl(self, output_file):
        with open(output_file, 'wb') as f:
            pickle.dump(self.data, f)


arguments = sys.argv

if("csv" in arguments[1]):
    converter = CSVConverter(arguments[1])
elif("txt" in arguments[1]):
    converter = TXTConverter(arguments[1])
elif ("json" in arguments[1]):
    converter = JSONConverter(arguments[1])
elif ("pkl" in arguments[1]):
    converter = PKLConverter(arguments[1])

converter.read_data()
converter.change_value(int(arguments[3]), int(arguments[4]), arguments[5])

if("csv" in arguments[2]):
    converter.to_csv(arguments[2])
elif("txt" in arguments[2]):
    converter.to_txt(arguments[2])
elif ("json" in arguments[2]):
    converter.to_json(arguments[2])
elif ("pkl" in arguments[2]):
    converter.to_pkl(arguments[2])