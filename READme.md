<h1>BU Daily Dose of Weather</h1>
<h2>1. Set Up</h2>
<h5>At the beginning of the program, this text dialogue is shown to the user to gather the user requirements as well as user information</h5>
<ul>
<li>“Hi! Welcome to your Automatic Wardrobe, what’s your name?”
<li>“Hi {name}! At what temperature do you think that fits these categories? ”
<li>“Hot (in celcius): ”
<li>“Cool (in celcius): ”
<li>“Cold (in celsius): ”
<li>“Cool! Can we get your number by the way? *wink wink*: ”
<li>Alright {name}, we will send you a notification about the weather every morning at 8am, smell ya later!
</ul>

<h2>2. SMS Notification Dialogue</h2>
/ Dear Ben /
<br>Today is (hot/cool/cold) , at 35 Celcius. 

In the afternoon, it will rise/drop to 20 Celcius.

At night, it will rise/drop to 15 Celcius.

It’s (sunny/cloudy/rainy/windy/snowy) , 
don’t forget to bring (umbrella/sunscreen/wind-breaker/gloves).

We recommend wearing:
<ul>
<li>T-shirt
<li>Short
<li>Hoodie
<li>Trousers
<li>Jacket
<li>Multiple layers of clothing
</ul>

<h2>3. Technicality</h2>
<br> - OpenWeather API 
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Format: weather/time/min temp/max temp/feels like temp/wind speed/feels like afternoon/feels like night/
<br><br> - SMTP Email Message Library
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Format: user addressed/main body notification/phone number
<br><br> - CSV File Reading/Writing
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Format: name/hot temp preference/cold temp preference/phone number/general weather/
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;more descriptive weather/current time and date/min temp/max temp/feels like temp/wind speed
