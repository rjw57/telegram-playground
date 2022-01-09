# Simple Telegram monitor script
socat -d -d /dev/ttyUSB0,b38400,raw,echo=0 exec:$(which monitor),pty
