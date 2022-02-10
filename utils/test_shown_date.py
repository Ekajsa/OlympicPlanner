from datetime import datetime


def main():
    shown_date = ""
    date_action = "Next"

    date_strings = ["2022-02-02", "2022-02-03", "2022-02-04", "2022-02-05", "2022-02-06",
                    "2022-02-07", "2022-02-08", "2022-02-09", "2022-02-10", "2022-02-11",
                    "2022-02-12", "2022-02-13", "2022-02-14", "2022-02-15", "2022-02-16",
                    "2022-02-17", "2022-02-18", "2022-02-19", "2022-02-20"]

    if shown_date == "":
        shown_date = datetime.today().strftime("%Y-%m-%d")
        return print(shown_date)
    if date_action == "":
        return print(shown_date)

    shown_date_index = date_strings.index(shown_date)
    if date_action == "Next":
        shown_date_index = min(shown_date_index + 1, 18)
        shown_date = date_strings[shown_date_index]
        return print(shown_date)
    elif date_action == "Previous":
        shown_date_index = max(shown_date_index - 1, 0)
        shown_date = date_strings[shown_date_index]
        return print(shown_date)
    else:
        shown_date = "2022-02-02"
        return print(shown_date)


if __name__ == '__main__':
    main()
