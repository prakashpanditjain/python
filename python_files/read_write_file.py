import csv
import os


def book_category(file_path: str, category, *args):
    """
    :param file_path: give the path of the file
    :param category: give the app category
    :return: This function returns category contains as per your wish
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        # read the file using csv method
        reader = csv.reader(file)

        # get the distinct category list from the csv
        category_list = set(list(row[1] for row in reader))

        # get the desired category name
        app_category_name = list(
            book_category for book_category in category_list if str(category) in book_category.lower())

    return (print(f"{category}_category_name = ",end=""), app_category_name, print(app_category_name))


def app_list(file_path: str, fun, *args):
    """
    :param file_path: give the path of the file
    :param fun: give the function name which returns the category name froom the file
    :param args:
    :return: This function returns all the app which falls under the mentioned category
    """

    # read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)

        # get the list of the apps
        app_list = (list((row[0], row[1]) for row in reader if row[1] == fun[1][0]))

    # return the app list
    return app_list


if __name__ == '__main__':

    # Get the file path
    file_path = f"{os.getcwd()}/googleplaystore.csv"

    # pass the varibles into function
    list_of_apps = app_list(str(file_path), book_category(file_path, "art"))

    print(list_of_apps)
