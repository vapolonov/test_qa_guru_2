from conftest import *


def test_browser_search_selene(browser_open):
    query = browser.element('[name=q]')
    query.should(be.blank).type('Selene').press_enter()
    browser.element('#search').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_browser_search_selenide(browser_open):
    query = browser.element('[name=q]')
    query.should(be.blank).type('Selene').press_enter()
    browser.element('#search').should(have.no.text('SomeText123qweasdzxc'))
