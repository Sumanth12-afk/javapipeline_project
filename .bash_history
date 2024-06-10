sudo apt update
sudo apt install -y python3 python3-pip
python3 --version
pip3 --version
vim password_generato
sudo apt update
python3 password_generator.py
vim to-dolist.py
python3 to-dolist.py
vim chatbot.py
python3 chatbot.py
vim responses.json
vim chatbot.py
python3 chatbot.py
vim chatbot.py
vim responses.json
rm responses.json
vim responses.json
python3 chatbot.py
vim chatbot.py
rm chatbot.py
vim chatbot.py
python3 chatbot.py
vim responses.json
cat responses.json
rm responses.json
vim responses.json
python3 chatbot.py
sudo yum update -y
sudo apt-get update
sudo apt-get upgrade -y
wget https://github.com/prometheus/prometheus/releases/download/v2.43.0/prometheus-2.43.0.linux-amd64.tar.gz
tar -xvf prometheus-2.43.0.linux-amd64.tar.gz
sudo mv prometheus-2.43.0.linux-amd64/prometheus /usr/local/bin/
sudo mv prometheus-2.43.0.linux-amd64/promtool /usr/local/bin/
sudo mkdir /etc/prometheus
sudo mkdir /var/lib/prometheus
sudo mv prometheus-2.43.0.linux-amd64/prometheus.yml /etc/prometheus/
sudo mv prometheus-2.43.0.linux-amd64/consoles /etc/prometheus/
sudo mv prometheus-2.43.0.linux-amd64/console_libraries /etc/prometheus/
sudo mv prometheus-2.43.0.linux-amd64/prometheus.yml /etc/prometheus/
sudo mv prometheus-2.43.0.linux-amd64/consoles /etc/prometheus/
sudo mv prometheus-2.43.0.linux-amd64/console_libraries /etc/prometheus/
sudo useradd --no-create-home --shell /bin/false prometheus
sudo chown -R prometheus:prometheus /etc/prometheus
sudo chown -R prometheus:prometheus /var/lib/prometheus
sudo chown prometheus:prometheus /usr/local/bin/prometheus
sudo chown prometheus:prometheus /usr/local/bin/promtool
sudo nano /etc/systemd/system/prometheus.service
sudo systemctl daemon-reload
sudo systemctl start prometheus
sudo systemctl enable prometheus
sudo systemctl status prometheus
sudo systemctl status node_exporter
