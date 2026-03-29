#!/usr/bin/env python3

import calendar
from datetime import datetime


def main():
    now = datetime.now()
    year = int(input(f"Enter year "))
    month = int(input(f"Enter Month "))

    print("Calendar for current month:\n")
    print(calendar.month(year, month))

if __name__ == "__main__":
    main()
