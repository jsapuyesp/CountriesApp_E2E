import pytest
from screenpy import AnActor, ReadExactly, See, given, when, then
from screenpy_selenium import BrowseTheWeb, Click, Enter, Press, Text, Wait
from selenium.webdriver.common.keys import Keys


from userinterface.main_page import main

main = main()

@pytest.mark.usefixtures("driver")
def test_by_country(driver):
  actor = AnActor.named("User").who_can(BrowseTheWeb.using(driver))

  given(actor).was_able_to(main.open())  

  when(actor).attempts_to(
    Wait.for_the(main.search_field).to_appear(),
    Click.on_the(main.search_country_button),
    Enter.the_text("Colombia").into_the(main.search_field).then_press(Keys.ENTER),  
    Wait.for_the(main.table_results).to_appear()  
  )

  then(actor).should(See.the(Text.of_the(main.colombia_result), ReadExactly(main.colombia)))  


@pytest.mark.usefixtures("driver")
def test_by_region(driver):
  actor = AnActor.named("User").who_can(BrowseTheWeb.using(driver))

  given(actor).was_able_to(main.open())  

  when(actor).attempts_to(
    Wait.for_the(main.search_field).to_appear(),
    Click.on_the(main.search_region_button),
    Click.on_the(main.south_america_region),
    Wait.for_the(main.table_region).to_appear()  
  )

  then(actor).should(See.the(Text.of_the(main.argentina_result), ReadExactly(main.argentina)))  



@pytest.mark.usefixtures("driver")
def test_by_capital(driver):
  actor = AnActor.named("User").who_can(BrowseTheWeb.using(driver))

  given(actor).was_able_to(main.open())  

  when(actor).attempts_to(
    Wait.for_the(main.search_field).to_appear(),
    Click.on_the(main.search_capital_button),
    Enter.the_text("Bogota").into_the(main.search_field).then_press(Keys.ENTER),  
    Wait.for_the(main.table_capital).to_appear()  
  )

  then(actor).should(See.the(Text.of_the(main.colombia_result_capital), ReadExactly(main.colombia)))  

