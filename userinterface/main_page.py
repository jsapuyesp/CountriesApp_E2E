from screenpy_selenium import Open, Target
from selenium.webdriver.common.by import By


class main:

  url = "http://localhost:4200/"

  search_country_button = Target.the("Search Country").located_by((By.XPATH, "/html/body/app-root/div/div[1]/app-sidebar/ul/li[1]"))  #Buscar País

  search_region_button = Target.the("Search Country").located_by((By.XPATH, "/html/body/app-root/div/div[1]/app-sidebar/ul/li[2]"))   #Bucar Region
  
  search_capital_button = Target.the("Search Country").located_by((By.XPATH, "/html/body/app-root/div/div[1]/app-sidebar/ul/li[3]"))  #Buscar capital

  south_america_region = Target.the("South America").located_by((By.XPATH, "/html/body/app-root/div/div[2]/app-by-region/div[1]/div/button[6]")) #Region Sur América

  search_field = Target.the("Search Field").located_by((By.NAME, "termino")) #Campo de búsqueda

  table_results = Target.the("Table Results").located_by((By.CSS_SELECTOR, "body > app-root > div > div.col > app-by-country > div:nth-child(5) > div > app-country-table > table")) #Resultados para país

  table_region = Target.the("Table Results Region").located_by((By.XPATH, "/html/body/app-root/div/div[2]/app-by-region/div[2]/div/app-country-table/table")) #Resultados para región

  table_capital = Target.the("Table Results Capital").located_by((By.CSS_SELECTOR, "body > app-root > div > div.col > app-by-capital > div:nth-child(4) > div > app-country-table > table")) #Resultados para capital

  colombia_result = Target.the("Colombia").located_by((By.XPATH, "/html/body/app-root/div/div[2]/app-by-country/div[2]/div/app-country-table/table/tbody/tr/td[3]")) #Campo Colombia en la tabla por país

  colombia_result_capital = Target.the("Colombia").located_by((By.XPATH, "/html/body/app-root/div/div[2]/app-by-capital/div[2]/div/app-country-table/table/tbody/tr/td[3]")) #Campo Colombia en la tabla por capital

  argentina_result = Target.the("Argentina Capital").located_by((By.XPATH, "/html/body/app-root/div/div[2]/app-by-region/div[2]/div/app-country-table/table/tbody/tr[1]/td[4]"))

  colombia = "Colombia"

  argentina = "Buenos Aires"


  def open(self):
      return Open(self.url)
