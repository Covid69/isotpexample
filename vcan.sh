#!/bin/bash
# Make sure the script runs with super user privileges.
[ "$UID" -eq 0 ] || exec sudo bash "$0" "$@"
# Load the kernel module.
modprobe vcan
# Create the virtual CAN interface.
ip link add dev vcan0 type vcan
# Bring the virtual CAN interface online.
ip link set up vcan0

# Create the virtual CAN interface.
ip link add dev vcan1 type vcan
# Bring the virtual CAN interface online.
ip link set up vcan1

sudo cangw -A -s vcan0 -d vcan1 -e

sudo systemctl start systemd-networkd

sudo systemctl enable systemd-networkd
