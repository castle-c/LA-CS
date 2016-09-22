import json
import sqlite3
import urllib.request
import requests

parish_table = """ CREATE TABLE IF NOT EXISTS Parish (
                                      id integer PRIMARY KEY,
                                      parish_name text,
                                  ); """


companies_by_parish_table = """ CREATE TABLE IF NOT EXISTS CompaniesByParish (
                                      id integer PRIMARY KEY,
                                      city text,
                                      company_name text,
                                      state text,
                                      parish_key,
                                      FOREIGN KEY(parish_key) REFERENCES Parish(id),
                                      FOREIGN KEY(company_key) REFERENCES CompanyInfo(id)
                                  ); """



traffic = json.load(open('parish.json'))
company_id_list = []
for obj in traffic['results']:
  company_id_list = obj['id']
  parish_name = obj['name']
  parish_id = obj['id']
  # print(parish_id)


  with sqlite3.connect('CompanyData.db') as conn:
    c = conn.cursor()
    c.execute(parish_table)
    c.execute(companies_by_parish_table)

    c.execute("""
                insert into Parish (parish_name, parish_id)
                values (?)
              """,
                (parish_name))

    r = requests.get("http://www.lslbc.louisiana.gov/wp-admin/admin-ajax.php?api_action=advanced&contractor_parish=" + company_id_list + "&action=api_actions")
    company = r.json()
    # print(company)
    for res in company['results']:
      companyInfo = res
      # print(companyInfo)




      city = companyInfo['city']
      state = companyInfo['state']
      company_id = companyInfo['id']
      print(company_id)
      company_name = companyInfo['company_name']

      c.execute("SELECT id from Parish where parish_id = ?", (parish_id, ))
      parish_key = c.fetchone()[0]
      print('Parish DB id', parish_key)


      c.execute("SELECT id from CompanyInfo where company_id = ?", (company_id, ))
      company_key = c.fetchone()[0]
      print('Company DB id', company_key)

      c.execute("""
                  insert into CompaniesByParish (city, state, company_name, parish_key, company_key)
                  values (?, ?, ?, ?, ?)
                """,
                  (city, state, company_name, parish_key, company_key))
      conn.commit()

