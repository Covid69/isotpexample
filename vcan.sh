#!/bin/bash 
echo "Enabling VirtualCan" 
modprobe can-gw 
echo "Creating vcan0, vcan1, vcan2" 
ip link add dev vcan0 type vcan 
ip link set up vcan0 mtu 72 
ip link add dev vcan1 type vcan 
ip link set up vcan1 mtu 72 
ip link add dev vcan2 type vcan 
ip link set up vcan2 mtu 72 
echo "Flushing can-gw" cangw -F 
echo "Connecting can channels" 
echo " " 
sudo cangw -A -s vcan0 -d vcan1 -e 
sudo cangw -A -s vcan1 -d vcan0 -e 
sudo cangw -A -s vcan0 -d vcan2 -e 
sudo cangw -A -s vcan1 -d vcan2 -e 
sudo cangw -A -s vcan2 -d vcan0 -e 
sudo cangw -A -s vcan2 -d vcan1 -e 
echo "Rules created:" 
cangw -L 
# echo "Testing transmittion from vcan0 to vcan1" 
# gnome-terminal -- bash -c "candump vcan1" 
# cansend vcan0 2AA#C0FFEE