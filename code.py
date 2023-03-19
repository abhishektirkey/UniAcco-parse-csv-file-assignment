import argparse
import csv
import math

#load file into the memory
def file(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)
    
#sort the rows
def srt_rws(data, column):
    return sorted(data, key=lambda row: row[column])

#count the number of rows
def count_rows(data):
    return len(data)

#filter the rows
def fil_rows(data, column, value):
    return [row for row in data if row[column] == value]

#calculate the mean
def cal_mean(data, column):
    column_sum = sum(float(row[column]) for row in data)
    return column_sum / len(data)

#calculate the standard deviation
def cal_sd(data, column):
    column_mean = cal_mean(data, column)
    column_values = [float(row[column]) for row in data]
    squared_differences = [(value - column_mean)**2 for value in column_values]
    variance = sum(squared_differences) / len(data)
    return math.sqrt(variance)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CSV Parser')
    parser.add_argument('file', help='CSV file to parse')
    args = parser.parse_args()

    data = file(args.file)

    while True:
        command = input('> ')

        if command.startswith('load'):
            parts = command.split(' ')
            filename = parts[1]
            data = file(filename)
            print(f'Loaded {len(data)} rows from {filename}')
        elif command == 'count':
            count = count_rows(data)
            print(f'{count} rows')
        elif command.startswith('mean'):
            parts = command.split(' ')
            column = parts[1]
            mean = cal_mean(data, column)
            print(f'Mean of {column}: {mean}')
        elif command.startswith('filter'):
            parts = command.split(' ')
            column = parts[1]
            value = parts[2]
            filtered_data = fil_rows(data, column, value)
            print(f'{len(filtered_data)} rows where {column} is {value}')
        elif command.startswith('sort'):
            parts = command.split(' ')
            column = parts[1]
            sorted_data = srt_rws(data, column)
            print(f'Sorted by {column}')
            for row in sorted_data:
                print(row)
        elif command.startswith('stddev'):
            parts = command.split(' ')
            column = parts[1]
            stddev = cal_sd(data, column)
            print(f'Standard deviation of {column}: {stddev}')
        elif command == 'exit':
            break
        else:
            print(f'Unknown command: {command}')

"""
-> This code defines several functions to manipulate CSV data, such as file to read a CSV file into memory and count_rows to count the number of rows in the data.

-> The main code block is guarded by the if __name__ == '__main__': condition, which ensures that the code is only executed if the script is run directly, and not imported as a module.

-> The code uses the argparse module to parse the command-line arguments, which should include the name of the CSV file to parse.

-> It then enters a loop where it waits for user input. The user can enter several commands, such as load, count, mean, filter, sort, stddev and exit. The program then calls the appropriate function to perform the requested operation on the CSV data.

-> For example, if the user enters load file.csv, the program will call the file function to read the data from file.csv and store it in memory.

-> If the user enters mean column_name, the program will call the cal_mean function to calculate the mean of the values in the specified column.

-> If the user enters filter column_name value, the program will call the fil_rows function to filter the data to only include rows where the specified column matches the specified value.

-> If the user enters exit, the program will exit the loop and terminate.

-> Overall, this code provides a basic command-line interface for manipulating CSV data, and could be extended with additional functionality as needed.

"""