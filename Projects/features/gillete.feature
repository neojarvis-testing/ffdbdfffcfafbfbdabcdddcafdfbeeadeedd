Feature: Gillette Website Tests

  Scenario: I am on the Gillette website to search for Razor
    Given I am on the Gillette website
    When I search for "Razor" using the search option
    Then I should see "Results For Razor'" at the top of the search results

  Scenario:I am on the Gillette website to search for styling
    Given I am on the Gillette website to look for styling
    When I click on "Styling" under "Learn" in the footer
    Then I should see "Facial Hair Styles: The Anchor Beard" under the list of articles under styling