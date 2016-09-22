import json
import sqlite3
import urllib.request
import requests

sql_table = """ CREATE TABLE IF NOT EXISTS CompanyInfo (
                                      id integer PRIMARY KEY,
                                      company_name text,
                                      owner text,
                                      email text,
                                      address text,
                                      city text,
                                      state text,
                                      zipcode integer,
                                      phone integer
                                  ); """



traffic = json.load(open('workingLCB.json'))
companyList = []
for obj in traffic['results']:
  companyList = obj['id']
  print(companyList)

  with sqlite3.connect('CompanyData.db') as conn:
    c = conn.cursor()
    c.execute(sql_table)
    r = requests.get("http://www.lslbc.louisiana.gov/wp-admin/admin-ajax.php?action=api_actions&api_action=company_details&company_id=" + companyList)
    companyInfo = r.json()
    # print(companyInfo)

    if companyInfo['classifications'] == []:
      qual_party = None
    elif companyInfo['classifications'] != []:
      qual_party = companyInfo['classifications'][0]['qualifying_party']
    else:
      qual_party = None



    name = companyInfo['company_name']
    email = companyInfo['email_address']
    companyID = companyInfo['id']
    address = companyInfo['mailing_address2']
    city = companyInfo['mailing_city']
    zipcode = companyInfo['mailing_zip']
    phone = companyInfo['phone_number']
    state = companyInfo['mailing_state']




    c.execute("""
                insert into CompanyInfo (company_name, owner, email, address, city, state, zipcode, phone)
                values (?, ?, ?, ?, ?, ?, ?, ?)
              """,
                (name, qual_party, email, companyID, address, city, state, zipcode, phone))
    conn.commit()


