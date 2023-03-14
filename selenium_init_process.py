'''
Seleniumを利用する際の初期処理
'''

import subprocess

shell_command = '''
cat > /etc/apt/sources.list.d/debian.list <<'EOF'
deb [arch=amd64 signed-by=/usr/share/keyrings/debian-buster.gpg] http://deb.debian.org/debian buster main
deb [arch=amd64 signed-by=/usr/share/keyrings/debian-buster-updates.gpg] http://deb.debian.org/debian buster-updates main
deb [arch=amd64 signed-by=/usr/share/keyrings/debian-security-buster.gpg] http://deb.debian.org/debian-security buster/updates main
EOF


apt-key adv --keyserver keyserver.ubuntu.com --recv-keys DCC9EFBF77E11517
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 648ACFD622F3D138
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 112695A0E562B32A

apt-key export 77E11517 | gpg --dearmour -o /usr/share/keyrings/debian-buster.gpg 
apt-key export 22F3D138 | gpg --dearmour -o /usr/share/keyrings/debian-buster-updates.gpg 
apt-key export E562B32A | gpg --dearmour -o /usr/share/keyrings/debian-security-buster.gpg 


cat > /etc/apt/preferences.d/chromium.pref << 'EOF'
Package: *
Pin: release a=eoan
Pin-Priority: 500


Package: *
Pin: origin "deb.debian.org"
Pin-Priority: 300


Package: chromium*
Pin: origin "deb.debian.org"
Pin-Priority: 700
EOF

apt-get update | tail -n -1
apt-get install chromium chromium-driver | tail -n -1

pip install -q selenium | tail -n -1
'''

subprocess.run(shell_command, shell=True)

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# ブラウザをheadlessモード実行
options = webdriver.ChromeOptions()

#ヘッドレスモード（バックグラウンドで起動）で実行。コラボの場合、必須。
options.add_argument('--headless')

#サンドボックスモードの解除。これも必須。
options.add_argument('--no-sandbox')

# /dev/shmパーティションの使用を禁止し、
# パーティションが小さすぎることによる、クラッシュを回避する。
options.add_argument('--disable-dev-shm-usage')
