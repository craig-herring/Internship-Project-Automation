from time import sleep

from behave import given,when,then
from selenium import webdriver

@given("Open reelly main page")
def open_main_page(context):
    context.app.LoginPage.open_reelly_url()


@when("Enter email")
def enter_email(context):
    context.app.LoginPage.input_email()


@when("Enter password")
def enter_password(context):
    context.app.LoginPage.input_password()


@when("Click continue button")
def click_continue_button(context):
    context.app.LoginPage.click_continue()
