import machine
import time
LED_PIN=15
led=machine.Pin(LED_PIN,machine.Pin.OUT)
led.off()
LIGHT_PIN_L=13
light_l=machine.Pin(LIGHT_PIN_L,machine.Pin.OUT)
light_l.off()
LIGHT_PIN_R=2
light_r=machine.Pin(LIGHT_PIN_R,machine.Pin.OUT)
light_r.off()
class engines:
    def __init__(self, machine):
        self.machine = machine
        self.left_first_pin = 0
        self.left_second_pin = 5
        self.right_first_pin = 14
        self.right_second_pin = 12
    def forward(self, duty=1000):
        self.stop()
        e1=machine.PWM(self.machine.Pin(self.left_first_pin),freq=100,duty=duty)
        e2=machine.PWM(self.machine.Pin(self.right_first_pin),freq=100,duty=duty)
    def backward(self, duty=1000):
        self.stop()
        e1=machine.PWM(self.machine.Pin(self.left_second_pin),freq=100,duty=duty)
        e2=machine.PWM(self.machine.Pin(self.right_second_pin),freq=100,duty=duty)
    def left_up(self):
        self.stop()
        e1=machine.PWM(self.machine.Pin(self.left_first_pin), freq=100, duty=400)
        e2=machine.PWM(machine.Pin(self.right_first_pin), freq=100, duty=1000)
    def right_up(self):
        self.stop()
        e1=machine.PWM(self.machine.Pin(self.left_first_pin),freq=100,duty=1000)
        e2=machine.PWM(self.machine.Pin(self.right_first_pin),freq=100,duty=400)
    def left_down(self):
        self.stop()
        e1=machine.PWM(self.machine.Pin(self.left_second_pin), freq=100, duty=400)
        e2=machine.PWM(machine.Pin(self.right_second_pin), freq=100, duty=1000)
    def right_down(self):
        self.stop()
        e1=machine.PWM(self.machine.Pin(self.left_second_pin),freq=100,duty=1000)
        e2=machine.PWM(self.machine.Pin(self.right_second_pin),freq=100,duty=400)
    def stop(self):
        machine.PWM(self.machine.Pin(self.left_first_pin),freq=0,duty=0)
        machine.PWM(self.machine.Pin(self.right_second_pin),freq=0,duty=0)
        machine.PWM(self.machine.Pin(self.left_second_pin),freq=0,duty=0)
        machine.PWM(self.machine.Pin(self.right_first_pin),freq=0,duty=0)
E=engines(machine)
try:
    import usocket as socket
except:
    import socket
CONTENT = b"""\
HTTP/1.0 200 OK
Hello #%d
"""
CONTENT = b"""\
HTTP/1.0 200 OK
Content-Type: text/html\n\r
<html>
  <script src="http://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js" type="text/javascript" charset="utf-8">
  </script>
<head>
<script type="text/javascript">
var DEVICE_URL = 'http://%s'
function iotAction(action){
    if(action=='change_led'){
        if(document.getElementById('led_value').value==1){
            action='led_off'
            document.getElementById('led_value').value=0
            document.getElementById('led_control').style.backgroundImage="url('https://raw.githubusercontent.com/dgolak/esp8266/master/images/alarm_off.jpg')"
        }else if(document.getElementById('led_value').value==0){
            action='led_on'
            document.getElementById('led_value').value=1
            document.getElementById('led_control').style.backgroundImage="url('https://raw.githubusercontent.com/dgolak/esp8266/master/images/alarm_on.jpg')"
        }else{
            action="led_on"
        }
    }
    if(action=='change_light'){
        if(document.getElementById('light_value').value==1){
            action='light_off'
            document.getElementById('light_value').value=0
            document.getElementById('light_control').style.backgroundImage="url('https://raw.githubusercontent.com/dgolak/esp8266/master/images/light_off.jpg')"
        }else if(document.getElementById('light_value').value==0){
            action='light_on'
            document.getElementById('light_value').value=1
            document.getElementById('light_control').style.backgroundImage="url('https://raw.githubusercontent.com/dgolak/esp8266/master/images/light_on.jpg')"
        }else{
            action="light_on"
        }
    }
    var requestURL = DEVICE_URL + "/?action="+action
    $.get (requestURL)
}
</script>
<style>
#container{
    width:800px;
    height:1300px;
    background-image:url("https://raw.githubusercontent.com/dgolak/esp8266/master/images/navi2.png");
    background-position:40px 110px;
    background-size:720px;
    background-repeat: no-repeat;
    -webkit-user-select: none;
    padding-top:100px;
}
button{
    background-color:transparent;
    border-color:transparent;
    border:0px solid red
}
</style>
</head>
<center>
<div id="container">
<table cellpadding="0" cellspacing="0">
<tr>
<td style="padding-left:130px;" colspan="3">
<button style="width:440px;height:150px" ontouchstart="iotAction('forward')" ontouchend="iotAction('stop')"/>
</td>
</tr>
<tr>
<td><button style="width:180px;height:190px" ontouchstart="iotAction('left_up')" ontouchend="iotAction('stop')"/></td>
<td rowspan="2"><button style="width:350px;height:370px" ontouchstart="iotAction('stop')" ontouchend="iotAction('stop')"/></td>
<td><button style="width:180px;height:190px" ontouchstart="iotAction('right_up')" ontouchend="iotAction('stop')"/></td>
</tr>
<tr>
<td><button style="width:180px;height:220px" ontouchstart="iotAction('left_down')" ontouchend="iotAction('stop')"/></td>
<td><button style="width:180px;height:220px" ontouchstart="iotAction('right_down')" ontouchend="iotAction('stop')"/></td>
</tr>
<tr>
<td style="padding-left:130px;" colspan="3">
<button style="width:440px;height:150px" ontouchstart="iotAction('backward')" ontouchend="iotAction('stop')"/>
</td>
</tr>
</table>
<br/><br/>
<table>
<tr>
<td>
<input type="hidden" id="light_value" value="0"/>
<button id="light_control" style="width:200px;height:200px;background-image:url('https://raw.githubusercontent.com/dgolak/esp8266/master/images/light_off.jpg');background-size:200px;"" ontouchstart="iotAction('change_light')"></button>
</td>
<td>
<input type="hidden" id="led_value" value="0"/>
<button id="led_control" style="margin-left:20px;width:200px;height:200px;background-image:url('https://raw.githubusercontent.com/dgolak/esp8266/master/images/%s');background-size:200px;"" ontouchstart="iotAction('change_led')"></button>
</td>
</tr>
</table>
</div>
</center>
</html>
"""

def main(E,micropython_optimize=False):
    s = socket.socket()
    ai = socket.getaddrinfo("172.20.10.10", 80)
    addr = ai[0][-1]
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(5)
    while True:
        res = s.accept()
        client_sock=res[0]
        if not micropython_optimize:
            client_stream = client_sock.makefile("rwb")
        else:
            client_stream = client_sock
        req = client_stream.readline()
        get = req.split()[1].decode('utf-8')
        if get == '/?action=forward':
            E.forward()
        elif get == '/?action=left_up':
            E.left_up()
        elif get == '/?action=right_up':
            E.right_up()
        elif get == '/?action=left_down':
            E.left_down()
        elif get == '/?action=right_down':
            E.right_down()
        elif get == '/?action=backward':
            E.backward()
        elif get == '/?action=stop':
            E.stop()
        elif get == '/?action=led_on':
            led.on()
        elif get == '/?action=led_off':
            led.off()
        elif get == '/?action=light_on':
            light_l.on()
            light_r.on()
        elif get == '/?action=light_off':
            light_l.off()
            light_r.off()
        else:
            pass
        while True:
            h = client_stream.readline()
            if h == b"" or h == b"\r\n":
                break
        if led.value() == 1:
            led_icon="alarm_on.jpg"
        else:
            led_icon = "alarm_off.jpg"
        client_stream.write(CONTENT % (wlan.ifconfig()[0],led_icon))
        client_stream.close()
        if not micropython_optimize:
            client_sock.close()
main(E)
