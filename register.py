import gspread
from oauth2client.service_account import ServiceAccountCredentials

def register_func(ism,familiya,otasini_ismi,passport,telefon,yonalish,mahalla,murojaat,telegram_id):

    scope = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name("itcentermurojaatbot.json", scope)

    client = gspread.authorize(creds)
    spreadsheet = client.open("Murojaatbottest")
    id = 1
    worksheet = spreadsheet.get_worksheet(0)
    varoq = client.open("Murojaatbottest").worksheet("Sheet1")
    malumotlar = varoq.get_all_records()

    worksheet.update_cell(len(malumotlar)+2, 1,ism)
    worksheet.update_cell(len(malumotlar)+2,2,familiya)
    worksheet.update_cell(len(malumotlar)+2,3,otasini_ismi)
    worksheet.update_cell(len(malumotlar)+2,4,passport)
    worksheet.update_cell(len(malumotlar)+2,5,telefon)
    worksheet.update_cell(len(malumotlar)+2,6,mahalla)
    worksheet.update_cell(len(malumotlar)+2,7,yonalish)
    worksheet.update_cell(len(malumotlar)+2,8,murojaat)
    worksheet.update_cell(len(malumotlar)+2,9,f"M-{len(malumotlar)+1}")
    worksheet.update_cell(len(malumotlar)+2,10,telegram_id)