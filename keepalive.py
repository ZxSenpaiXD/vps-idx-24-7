[Unit]
Description=My Python 24/7 Script
After=network.target

[Service]
ExecStart=/usr/bin/python3 /path/to/your_script.py
WorkingDirectory=/path/to/your/folder
StandardOutput=inherit
StandardError=inherit
Restart=always
User=your-username

[Install]
WantedBy=multi-user.target
