#!/usr/bin/python
from __future__ import print_function
from INA260_MINIMAL import INA260
import time
from datetime import datetime

def main():
    ina260 = INA260(dev_address=0x40);
    ina260.reset_chip()
    time.sleep(1)

    try:
        while True:
            bus_voltage = ina260.get_bus_voltage()
            charge_current = ina260.get_current()
            print("V = %02f V, I = %02f A" % (bus_voltage,charge_current))
            time.sleep(1)
    except KeyboardInterrupt:
        print("end.")

if __name__ == '__main__':
    main()
