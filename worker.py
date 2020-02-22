from providers.KeyProvider import KeyProvider
from providers.SheetsProvider import SheetsProvider

if __name__ == "__main__":
    keys = KeyProvider("secrets/.keys")
    sheets = SheetsProvider(keys.get_value("GOOGLE_SHEETS_DOC_ID"))
