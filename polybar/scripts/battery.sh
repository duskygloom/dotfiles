#!/usr/bin/env bash

power_supply="/sys/class/power_supply"

charging=$(cat "$power_supply/ADP1/online")
capacity=$(cat "$power_supply/BAT1/capacity")

if [ $charging -eq 1 ]
then
	icon="%{B#61C766}"
else
	icon="%{B#EC6798}"
fi

if [ $capacity -gt 90 ]
then
	icon="$icon  "
elif [ $capacity -gt 50 ]
then
	icon="$icon  "
elif [ $capacity -gt 10 ]
then
	icon="$icon  "
else
	icon="$icon  "
fi

echo "$icon %{B#C4C7C5} $capacity% "

