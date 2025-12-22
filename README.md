# ============================================
# Kafka Python Tutorial - Simplified
# ============================================

# 1. Start Docker Desktop
# Make sure Docker Desktop is running.

# 2. Clone the repository
git clone https://github.com/raalrwai/KafkaPython.git
cd kafka-python-tutorial

# 3. Create a Python 3.10 virtual environment
python -m venv env310

# 4. Activate the virtual environment
.\env310\Scripts\Activate.ps1
# (If using cmd.exe, use: .\env310\Scripts\activate.bat)

# 5. Upgrade pip
python -m pip install --upgrade pip

# 6. Install Python dependencies
pip install -r requirements.txt

# 7. Start Kafka and Zookeeper
docker-compose up -d

# 8. Start the producer (in one PowerShell window)
python .\producer\producer.py

# 9. Start the consumer (in another PowerShell window)
python .\consumer\consumer.py

# 10. Stop all Docker containers when done
docker-compose down

# 11. Deactivate the virtual environment
deactivate
