import csv
import sys


class Cookies:

    def __init__(self):
        self.date = 0

    # binary search to find first and last occurrence of date
    # reference: geeksforgeeks
    # x: target value
    # n: length
    def first(self, arr, low, high, x, n):
        if high >= low:
            mid = low + (high - low) // 2

            if (mid == 0 or x < arr[mid - 1][1][0:10]) and arr[mid][1][0:10] == x:
                return mid
            elif x < arr[mid][1][0:10]:
                return self.first(arr, (mid + 1), high, x, n)
            else:
                return self.first(arr, low, (mid - 1), x, n)

        return -1

    def last(self, arr, low, high, x, n):
        if high >= low:
            mid = low + (high - low) // 2
            if (mid == n - 1 or x > arr[mid + 1][1][0:10]) and arr[mid][1][0:10] == x:
                return mid
            elif x > arr[mid][1][0:10]:
                return self.last(arr, low, (mid - 1), x, n)
            else:
                return self.last(arr, (mid + 1), high, x, n)

        return -1

    # find most active cookie with given range
    def find_most_active(self, arr, first, last):
        maxn = 1
        results = []
        cookies_dict = {}
        for i in range(first, last + 1):
            key = arr[i][0]
            if key in cookies_dict.keys():
                cookies_dict[key] = 1 + cookies_dict[key]
            else:
                cookies_dict[key] = 1

            if cookies_dict[key] > maxn:
                maxn = cookies_dict[key]
                results.clear()
                results.append(key)
            elif cookies_dict[key] == maxn:
                results.append(key)
            else:
                print('do nothing')

        return results

        # main method

    def main(self, file, x):
        with open(file) as f:
            data = list(csv.reader(f))  # conversion o(n)?

        first_occurrence = self.first(data, 0, len(data) - 1, x, len(data))

        if first_occurrence == -1:
            print('No cookies found. Try a different date')
            return
        # else
        last_occurrence = self.last(data, 0, len(data) - 1, x, len(data))
        # print(last_occurrence)

        most_active = self.find_most_active(data, first_occurrence, last_occurrence)

        for i in range(len(most_active)):
            print(most_active[i])


if __name__ == '__main__':
    cookie = Cookies()
    if len(sys.argv) < 4:
        print("enter arguments {file_name.csv} -d {YYYY-MM-DD}")
        exit()
    target_file = sys.argv[1]
    target_date = sys.argv[3]
    cookie.main(target_file, target_date)
