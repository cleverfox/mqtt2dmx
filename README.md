# very simple mqtt to dmx bridge

upload
python3.10 webrepl_cli.py -p 1234 umqttsimple.py 192.168.1.42:/umqttsimple.py
python3.10 webrepl_cli.py -p 1234 main.py 192.168.1.42:/main.py
python3.10 webrepl_cli.py -p 1234 boot.py 192.168.1.42:/boot.py

cli
python3.10 webrepl_cli.py -p 1234 192.168.1.42

