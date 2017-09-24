# How to build RC Car with the esp8266. #

At the beginning my story I would like to say, that this was my first time to IOT topic.
I'm a complete beginner, but one thing I have is the desire  to known new technologies.

A month ago my colleague make presentation about #esp8266 and I was impressed this small board.
So I decided that I would like to known more about #esp8266 and similar stuff like #arduino.

I use Micropython (http://micropython.org/download) it is a firmware for the #esp8266 boards.

At the beginning I don't underestand how it works, but I have read a lot of webpages and articles about it.
The first success when I could turn on and turn off Led :)
Next I bought distance sensor, temperature and humidity sensor....

Next I bought the engine but I didn't know nothing about.
So I bought two engines SG90 but it turned out, that it is only the servo engine :(

Afterwards I was reading about engines and I bought two engines and motor shield (L298N)
<img src="https://github.com/dgolak/esp8266/blob/master/images/60.jpg">
<img src="https://github.com/dgolak/esp8266/blob/master/images/80.jpg">

### Together with my son (7years old) we used old lego car body and double sided tape :) ###

### In effect ? ###
<img src="https://github.com/dgolak/esp8266/blob/master/images/30.jpg" style="width:360px;">
<img src="https://github.com/dgolak/esp8266/blob/master/images/40.jpg" style="width:360px;">
<img src="https://github.com/dgolak/esp8266/blob/master/images/50.jpg" style="width:360px;">

### Then we used the battery 9V to power the mottor. ###
<img src="https://github.com/dgolak/esp8266/blob/master/images/90.jpg" style="width:360px;">

### Putting all together: ###
<img src="https://github.com/dgolak/esp8266/blob/master/images/100.jpg" style="width:360px;">
<img src="https://github.com/dgolak/esp8266/blob/master/images/110.jpg" style="width:360px;">
<img src="https://github.com/dgolak/esp8266/blob/master/images/120.jpg" style="width:360px;">

When it comes to steering and turning sideways I used trick.
For example if I wanted turn left I used left engine 30% power and right engine 80-100% power.

Next I connected red LED and two light green LED on the front of car

### Everything works fine in python console. ###
For instance, when I wanted to run I typed ** E.forward() **
when I wanted to stop car I had to type ** E.stop(). **

### Python code is on my github (please give me a star :) ): ###
https://github.com/dgolak/esp8266/blob/master/main.py
Afterwards I wrote wifi connection to my mobile phone, simple webserwer and web application to steering a car.

### Putting all together: ###
<img src="https://github.com/dgolak/esp8266/blob/master/images/10.jpg" style="width:360px;">
<img src="https://github.com/dgolak/esp8266/blob/master/images/20.jpg" style="width:360px;">
<img src="https://github.com/dgolak/esp8266/blob/master/images/65.jpg" style="width:360px;">
<img src="https://github.com/dgolak/esp8266/blob/master/images/75.jpg" style="width:360px;">

### To sum up. ###
It was a great time with my son, we made a simple car with the steering by mobile phone or any devices with the use of WIFI
