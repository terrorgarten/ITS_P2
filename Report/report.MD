# Report for OpenCart testing

## 1 Intro
This document describes the failiures found in the system during preparation of automated tests.
These failures should be resolved before the testing can be brought to full coverage of the system. Refer to the sections 2 and 3 for details.


The testing was performed on the demo website
```http://mys01.fit.vutbr.cz:8084/``` running ```OpenCart 4.0.1```, but  any self-hosted OpenCart Docker image can be usd
---
## 2 Main known issues
- The system is missing shipping and payment method which user could use to finish the order of his items and neither can user add them in his account information.
    - ![Alt text](./img/checkout.png)
    - *Resolution*: Add a payment gate through the OpenCart admin panel - navigate to Extensions, select desired gate and 
      integrate it. (PayPal is a valid contender, because the integration is free)
    - Refer to Scenario  ```Customer places an order for product in their shopping card.``` at ```ITS_P2/features/shop.feature:31```

## 3 Secondary issues
- The notification popups cannot be manipulated by the user.
    - ![Alt text](./img/popup.png)
    - *Resolution*: Direct UI reimplementation or system update to OpenCart 5.0 *(Warning - this would require reimplementation of some tests)*.
    - Note: This was a direct observation and no test is provided, since the notification popup cannot be detected by Selenium.