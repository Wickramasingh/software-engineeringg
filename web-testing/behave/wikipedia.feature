eature: check inventors on invention pages

Scenario Outline:
     Given we have navigated to the wikipedia main page
      When we enter "<invention>" and click on the search button
      Then the resulting page will include "<inventor>"

  Examples: Electronics
    | invention | inventor |
    | Telephone | Alexander Graham Bell |
    | Transistor | Bardeen |
    | Light Bulb | Edison |
    | Phonograph | Edison |

  Examples: Transportation
    | invention | inventor |
    | Airplane | Wright |
    | Helicopter | Sikorsky |
