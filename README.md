# First install all dependencys by running:
pip install -r requirements.txt

# run code by
python3 main.py %%thingsboard_host%% %%thingsboard_key_sensor%%

# !!!!! IF ERRORS MISSING DEPENDENCIES !!!!!
# missing pips in requirements
pip3 install adafruit-blinka
pip3 install adafruit-circuitpython-ads1x15