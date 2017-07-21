Feature: TestTable

  Scenario: To test behave table
    Given Users visited
      |Name     |Company  |
      |Shalini  |Planview |
      |Vibhor   |Cisco    |
    When i checked
    #    And created time_report payload for "cards"
#    And time_report created for "1" week
#    And created time_report payload for "planlets1"
#    And time_report created for "1" week
#    And created time_report payload for "planlets1"
#    And time_report created for "1" week


      And task created at level PPL+1
    And task created at level PPL+2
    And task created at level PPL+3



        And verify planlets at level PPL+1
    And verify planlets at level PPL+2
    And verify planlets at level PPL+3