# HTTPfiles
send files to and from a device via HTTP

## how?
#### first time setup
```bash
python -m venv venv
. venv/bin/activate
pip install flask
```
#### device -> workstation
```bash
sudo firewall-cmd --zone=public --add-port=5000/tcp
sudo firewall-cmd --reload
python app.py
```
#### workstation -> device
```bash
python -m http.server -d <folder> 5000
```

## why?
I was handed an iphone for temporary use and it's 2025 and there is still no proper way to send files from your device to workstation and vice versa.
#### what about icloud?
This is not file transfer between two devices physically next to each other, this is data transfer via multiple distant nodes all the way to a centralized server and back. For many reasons this is absurd.
#### USB? KDEConnect?
I only want to transfer files, not hardware metadata.