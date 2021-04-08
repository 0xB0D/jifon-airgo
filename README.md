# jifon-airgo

Usage of script on raspberry-pi

0. Install pip3
   sudo apt-get install python3-pip

1. Install minimal modbus
   sudo pip3 install -U minimalmodbus

2. Amend the ttyUSBx
   /dev/ttyUSB0
   /dev/ttyUSB1

3. Set the correct modbus address
   The example script uses address #2

4. Run the script
   cd examples/
   chmod +x simple-test.py
   ./simple-test.py
