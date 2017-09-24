import esp
#esp.osdebug(None)
import gc
import network

#network connection
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('WIFI_NAME','WIFI_PASSWORD')
ifcfg = wlan.ifconfig()

#webrepl
import webrepl
webrepl.start()
gc.collect()
