#!/bin/bash
sudo ip route del 212.100.54.64/26 via 212.100.54.1
sudo ip route del 212.100.54.128/26 via 212.100.54.1
sudo ip route del 212.100.54.192/26 via 212.100.54.1