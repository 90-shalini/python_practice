Feature: Test Behave

  Scenario:Test multiple parameters
    Given I go to the meeting
    When I meet "Alice", "Bob", "Charly", "Dodo"
    and i want to meet "Alice, Bob"
#    and I test cardinality with Alice, Bob, Charly
#    and my details "name":"Shalini", "age":23
