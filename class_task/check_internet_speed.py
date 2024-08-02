"""

python -m venv venv

venv\Scripts\Activate

pip install `speedtest-cli`

"""


from speedtest import Speedtest


st = Speedtest()





print(round(st.download() / 1000000, 2))
print(round(st.upload() / 1000000, 2))
