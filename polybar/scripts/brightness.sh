#!/usr/bin/env bash

actual_brightness=`cat /sys/class/backlight/amdgpu_bl1/actual_brightness`
max_brightness=`cat /sys/class/backlight/amdgpu_bl1/max_brightness`

echo $(($actual_brightness*100/$max_brightness))

