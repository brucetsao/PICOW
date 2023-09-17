import network
import ubinascii

def GetMAC():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    mac = ubinascii.hexlify(network.WLAN().config('mac')).decode()
    return mac.upper()


def GetMAC2(sepc):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    mac = ubinascii.hexlify(network.WLAN().config('mac'),sepc).decode()
    return mac.upper()


