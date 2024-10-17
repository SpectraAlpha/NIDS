git clone https://gitlab.abo.fi/tahmad/cicflowmeter-py
cd cicflowmeter-py

sudo apt-get install python3-pip
pip install -r requirements.txt
sudo apt-get install python3-distutils
# use "python3 setup.py install" if fails ( If not install make file)
make install
