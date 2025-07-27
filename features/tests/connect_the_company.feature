# Created by mason at 7/15/2025
Feature: The user can click on “Connect the company” on the left side of the main page


  @smoke
  Scenario: The user can click on “Connect the company” on the left side of the main page
    Given Open login page
    When Enter masonou@hotmail.com into email
    When Enter Password@30 into password
    Then click Continue
    Then Click on “Connect the developer”
    Then verify correct tab opens
    And verify the URL


Scenario: Mobile The user can click on “Connect the company” on the left side of the main page
    Given Open login page
    When Enter masonou@hotmail.com into email
    When Enter Password@30 into password
    Then click Continue
    Then click mobile menu
    Then Click on mobile connect button
    Then verify correct tab opens
    And verify the URL