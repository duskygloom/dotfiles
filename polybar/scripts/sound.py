#!/usr/bin/env python3


import subprocess


def sink_mute() -> bool:
    command = ["pactl", "get-sink-mute", "@DEFAULT_SINK@"]
    result = subprocess.run(command, stdout=subprocess.PIPE)
    output = result.stdout.decode().strip()
    return output.endswith("yes")

def get_sink_volume() -> list[int]:
    command = ["pactl", "get-sink-volume", "@DEFAULT_SINK@"]
    result = subprocess.run(command, stdout=subprocess.PIPE)
    output = result.stdout.decode()
    volumes = [int(i.rstrip("%")) for i in output.split() if i.endswith("%")]
    return volumes


def src_mute() -> bool:
    command = ["pactl", "get-source-mute", "@DEFAULT_SOURCE@"]
    result = subprocess.run(command, stdout=subprocess.PIPE)
    output = result.stdout.decode().strip()
    return output.endswith("yes")

def get_src_volume() -> list[int]:
    command = ["pactl", "get-source-volume", "@DEFAULT_SOURCE@"]
    result = subprocess.run(command, stdout=subprocess.PIPE)
    output = result.stdout.decode()
    volumes = [int(i.rstrip("%")) for i in output.split() if i.endswith("%")]
    return volumes


def main():
    # sink volume
    sink_volume = get_sink_volume() or [0]
    sink = sink_volume[0]
    if sink_mute():
        sink_label = "%{B#EC7875} %{T3}󰖁 %{T-} %{O-6}"
    elif sink <= 10:
        sink_label = "%{B#EC6798} %{T3} %{T-} %{O-9}"
    elif sink <= 50:
        sink_label = "%{B#EC6798} %{T3}󰖀 %{T-} %{O-9}"
    else:
        sink_label = "%{B#61C766} %{T3}󰕾 %{T-} %{O-6}"
    sink_label = f"{sink_label}{sink}% "
    # source volume
    src_volume = get_src_volume() or [0]
    src = src_volume[0]
    if src_mute():
        src_label = f"%{{B#EC7875}} {src}% %{{O+3}}%{{T3}}󰍭%{{T-}} %{{O+1}}"
    elif src <= 20:
        src_label = f"%{{B#EC6798}} {src}% %{{O+3}}%{{T3}}󰍮%{{T-}} %{{O+1}}"
    else:
        src_label = f"%{{B#61C766}} {src}% %{{O+3}}%{{T3}}󰍬%{{T-}} %{{O+1}}"
    src_label = f"{src_label}"
    # print(f"%{{A1:pavucontrol -t 3:}}{sink_icon}%{{B#C4C7C5}} {sink}% %{{A}}%{{B#202020}} %{{A1:pavucontrol -t 4:}}{src_icon}%{{B#C4C7C5}} {src}% %{{A}}")
    print(f"%{{A1:pavucontrol -t 3:}}{sink_label}%{{A}}%{{O+3}}%{{B#202020}} %{{O-7}}%{{A1:pavucontrol -t 4:}}{src_label}%{{A}}")


if __name__ == "__main__":
    main()

