# Created by craig.herring at 4/24/25
Feature: Reelly

  Scenario: User can open market tab and go through the pagination
    Given Open reelly main page
    When Enter email
    And Enter password
    And Click continue button
    And Click on the “Market” tab at the left side menu
    Then Verify the right page opens
    #And Go to the final page using pagination
    #Then Go to the first page using pagination
