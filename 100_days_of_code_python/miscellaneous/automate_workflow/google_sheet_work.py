import os

import gspread
from google.oauth2.service_account import Credentials

# getthe file path from local machine
# Use os.path.expanduser to get the correct path to Downloads folder
service_account_json_path = os.path.expanduser("~/Downloads/gen-lang-client-0623010800-6d802fe03e22.json")
print(service_account_json_path)

# Add these scopes when creating credentials
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]


def put_content_to_google_sheet(prompt=None, func=None):
    google_sheet_link = ("https://docs.google.com/spreadsheets/d/1Awi4pty39rXu1QBqaSymaIrVV3QLtzh5IOThZx1NcPc/edit?usp"
                         "=sharing")
    content = func(prompt)

    # Authenticate and open the sheet
    creds = Credentials.from_service_account_file(service_account_json_path,
                                                  scopes=SCOPES)
    gc = gspread.authorize(creds)
    sh = gc.open_by_url(google_sheet_link)
    worksheet = sh.sheet1

    # Write content to the first empty row
    worksheet.append_row([content])

    # where we have appended the content we need to update the dropdown in column B of the same row

    # Find the last row with content
    last_row = len(worksheet.get_all_values())
    print(f"Last row with content: {last_row}")

    # Update cell B12 with one of the dropdown values
    dropdown_value = 'Social media'  # This should be one of the valid options from your dropdown
    worksheet.update(f"B{last_row}", [[dropdown_value]])

    # You can also validate the available options first
    all_values = worksheet.get_all_values()
    print(f"cell updated to: {dropdown_value}")

    worksheet.update_cell(last_row, 3, "tweet")

    dropdown_status = 'Under review'
    worksheet.update_cell(last_row, 5, dropdown_status)

    return True
