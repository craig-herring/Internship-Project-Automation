from behave import given, when, then

@when("Click on the “Market” tab at the left side menu")
def click_market_button(context):
    context.app.SideNavigationPage.click_market_button()


@then("Verify the right page opens")
def verify_right_page(context):
    context.app.MarketPage_Page.verify_market_url()