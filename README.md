This is a small program that will notify you on your phone if it will rain in the next 24 hours.
This progam uses 2 APIs to funtion:
1. https://api.openweathermap.org/data/2.5/forecast
   To gather the weather information of the next 24 hours.
   If you want to try it on your own you may need to create an account on their website to get their key, with that you just need to get your latitude and longitude which you can get from: https://www.latlong.net/

2. https://www.twilio.com/en-us
   In order to be notified through SMS you need to create an account with Twilio. Gather your ID, and token and a virtual number to be sent a message. For further assistance you can look through the Twilio documentation: https://www.twilio.com/docs/messaging#choose-your-messaging-channel
