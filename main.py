#!/usr/bin/env python3

import requests
import pandas as pd


def parse_url():
    with open("url.txt") as f:
        url = f.readline().strip()
    [_, params] = url.split("?")
    params = params.split("&")
    param_dict = {}
    for param in params:
        split = param.split("=")
        if len(split) == 1:
            (key, value) = (split[0], "")
        elif len(split) == 2:
            [key, value] = split
        else:
            raise ValueError

        param_dict[key] = value

    return param_dict


def get_courses(year=2025):
    base_url = "https://programsandcourses.anu.edu.au/data/CourseSearch/GetCourses"
    params = {
        "AppliedFilter": "FilterByCourses",
        "Source": "",
        "ShowAll": "true",
        "PageIndex": "0",
        "MaxPageSize": "10",
        "PageSize": "Infinity",
        "SortColumn": "",
        "SortDirection": "",
        "InitailSearchRequestedFromExternalPage": "false",
        "SearchText": "",
        "SelectedYear": str(year),
        "Careers[0]": "",
        "Careers[1]": "",
        "Careers[2]": "",
        "Careers[3]": "",
        "OtherCriteria[0]": "",
        "OtherCriteria[1]": "",
        "Sessions[0]": "",
        "Sessions[1]": "",
        "Sessions[2]": "",
        "Sessions[3]": "",
        "Sessions[4]": "",
        "Sessions[5]": "",
        "DegreeIdentifiers[0]": "",
        "DegreeIdentifiers[1]": "",
        "DegreeIdentifiers[2]": "",
        "FilterByMajors": "",
        "FilterByMinors": "",
    }
    resp = requests.get(base_url, params=params)
    return resp.json()["Items"]


def save_to_csv(year=2025, outfile=None):
    if outfile is None:
        outfile = "./" + str(year) + ".csv"
    courses = get_courses(year)
    df = pd.DataFrame.from_dict(courses)
    df.to_csv(outfile)


def main():
    for year in range(2014, 2026):
        save_to_csv(year)


if __name__ == "__main__":
    main()
