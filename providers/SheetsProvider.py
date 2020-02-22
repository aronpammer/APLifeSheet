import os

import gspread


class SheetsProvider:
    def __init__(self, doc_id):
        scopes = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.file",
                  "https://www.googleapis.com/auth/spreadsheets"]
        secret_file_path = os.path.join(os.getcwd(), 'secrets', 'credentials.json')

        self.gc = gspread.authorize(secret_file_path)
        self.sheet = self.gc.open_by_key(doc_id)

