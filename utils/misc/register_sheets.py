import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import os
import json
import ioggg
jsondata = [{
  "type": "service_account",
  "project_id": "paxtaoboditcenterbot",
  "private_key_id": "973363c24c8bd787dba045b955efb34ee97868bb",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC4EvrUTZnprRDT\nrrcO4tMtb7iCvmIX/XjgnSxwHl5lVGMRF27CCSx0sR4rfvjyNlD8uVxqian9S2V6\nZPpM3IbY6kMrsAXoZZfxmzQBfVyUYh3urNQK6Y0760iMxxjhv7tJfWrpd1y0r8Tf\nt5ZQRcjw8iAaKsp9I43Gsfq4WtABHDeDkZSAXgxC/pgq6w8T3LZv8+vRTYBisrcs\n3/zFgPODpbcIdSMW8jplDLeRJELJq/Cl9dpT/IhdNXHnWKlIZP3RJXxcsCtpUNUo\n399L/1vaPzdAoDYplzvFwDoYtpUaIm2IJPcUqKprIz2CyxDUFAcfvwyB4nktVV24\nEEmikJPtAgMBAAECggEAID+1AaJp02pubwOmTx2WnVh8JS3JHkZaWdG3ghoT9CE9\nbPZjwWtdhkEslba8UyUIecpYwlKFfVqq9+8+ed5N4q1iIMKJOm6oGNxV12f44wcw\nksrlKFdEFuoQ7xcHiS9v1r96DlaK354GuiIeG8iqHGpzDNqP2K40rcmrMQa59+OG\nrX3sTeGBmOsVnZ7+Ol4qp98EBbVzitD3OReIpckjU12sofyV3oAIJlATt3wib6GO\nzroIA+zs5lPbBuC5j1iqRQMNK99Fv+Wlb0MlVgRrYRS1ERNNDdt/qJXYu0+/JOKN\nOTVC7EZdH3fXI4fYkQta2V5I1NksDe6776o31p4dOQKBgQD3r5Q77X9P+RdEQThG\n5JlvJ5HXz90Lh52R7DLBunUy61VUPqrBBayxeV4rbTNxwRT6tzs6qVC2tU5DBdVC\nCGkftC/Mksh5BjbUsVGTjSjcQvo00x/pnVucJ8RrSSup2EDgKdoTNj627uUaGHnx\n2D+mUDen2a9NvraacyCfN1t6RQKBgQC+QMVTXFq4ScblqhtmPBXjaVJvIvTrIaZq\ndumDrV4OdBJKdZ4J/tACCY8v5NLEvg2vG5NwLqTdzqjOmbmSzdglfZnqsnTLwxVs\nd25xiLJnMAk2lWGG/QGUlvoW7Kag7gr0NacCfe0PmVzJqLaZqmwStor+wpwWO0sX\n61RmbKhhiQKBgQDKfC6aA2GmNoPP1+WzByVsWpP/Mz6JM3gcmFUyTUWMuBkNAyJD\nJGl2uTrEE8UPxQJqqKryHQMQKw5s+nLKRefy9DJzcrgTQIJIxSFkl+0EjHjSAJtB\nN9Rxx4zrDGl2s4Tt/Sj7tcf1cz22ZLYkgV4fj8rAHNUUoMnVYDMWFoJhZQKBgBiJ\nOemaS4jg2unbmlUBAsGlX6A9neCFInUwiMUWor6ycXlw2cToO+NHYFQI6rW83P7s\nS4N4QILqmBKs+KXaLjoHjMYb5bwxmJ24eWHjAz8TjtyfP0itcHq9TduPAZ5XlMoR\n8Uv8+Ym9eZ34SDRhKjbvm9VnO8ISO4kGLIhZEw4hAoGBANj7KqL68C68wlxr54ZB\neqTB8GVYQIE+3LYYtsdadt5Sgvus80CyIPsb3wGmaq3kGnnqNXIQ9Ek+WmtC6uD4\n8hNxnFvyXtlW+aTDcjtE1gTmF0ihZWQj82wRMG0xz5/2/U7oN/VttnBAY+Njil9I\nV5JtPz2jY+12DcglYGjIgMCj\n-----END PRIVATE KEY-----\n",
  "client_email": "paxtaoboditcenterbot@paxtaoboditcenterbot.iam.gserviceaccount.com",
  "client_id": "112438283403445386721",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/paxtaoboditcenterbot%40paxtaoboditcenterbot.iam.gserviceaccount.com"
}]
# def register_func(ism,familiya,telefon,yonalish):
#
#     scope = [
#         'https://www.googleapis.com/auth/spreadsheets',
#         'https://www.googleapis.com/auth/drive'
#     ]
#     creds = ServiceAccountCredentials.from_json_keyfile_name("/home/fayzullo/Desktop/aiogram-bot-template-clone-master/data/paxtaoboditcenterbot.json", scope)
#
#     client = gspread.authorize(creds)
#     spreadsheet = client.open("PaxtaobodITCenterBot")
#     worksheet = spreadsheet.get_worksheet(0)
#     varoq = spreadsheet.worksheet("Sheet1")
#     malumotlar = varoq.get_all_records()
#     new_time=str(datetime.now())
#     print(varoq.row_count)
#     worksheet.update_cell(len(malumotlar)+2, 1,ism)
#     worksheet.update_cell(len(malumotlar)+2,2,familiya)
#     worksheet.update_cell(len(malumotlar)+2,3,telefon)
#     worksheet.update_cell(len(malumotlar)+2,4,yonalish)
#     worksheet.update_cell(len(malumotlar)+2,5,f"M-{len(malumotlar)+1}")
#     worksheet.update_cell(len(malumotlar)+2,6,new_time)

scope = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]
# creds = ServiceAccountCredentials.from_json_keyfile_name("/home/fayzullo/Desktop/aiogram-bot-template-clone-master/data/paxtaoboditcenterbot.json", scope)

creds = ServiceAccountCredentials.from_json_keyfile_name(os.PathLike(jsondata), scope)



client = gspread.authorize(creds)
spreadsheet = client.open("PaxtaobodITCenterBot")
worksheet = spreadsheet.get_worksheet(0)
varoq = spreadsheet.worksheet("Sheet1")
malumotlar = varoq.get_all_records()
new_time=str(datetime.now())
print(varoq)