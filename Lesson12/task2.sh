#!/bin/bash
systemctl status apache2 1> result.txt
cat result.txt