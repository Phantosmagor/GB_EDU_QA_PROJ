import base64
import pickle
"""
#x = eval(zlib.decompress(base64.b64decode

"""
message = base64.b64decode('ZCvKP2qON0BLjzdAGpQ3QNaPN0BrjzdA1o83QDWQN0ACkTdAc5E3QB2RN0D1jTdAmJA3QPSQN0BYkDdAlpE3QIKQN0CWkTdAOY83QJaPN0DWjzdANZA3QFGPN0A2jjdAVJI3QNGTN0ASjTdA+ZM3QBKNN0ASjTdAEo03QBKNN0ASjTdAEo03QBKNN0ASjTdA75E3QBKNN0DpkjdA0ZM3QAQInwAAAAAAAAAYAQQIBQAAAAAAAAAIAQQIBgAAAAAAAAAAAQQIIQAAAAAAIAAAEQQI3AAAAAAAIAAAEQQIDAAAAAAAIAAAAQQIEgAAAAAAIAAAESAoDAAQAQAA",')

xbytes = pickle.dumps(message)
dict_obj = pickle.loads(xbytes)
# #print(dict_obj)

with open ('decoded4.bin', 'wb') as pick:
   pickle.dump(dict_obj, pick)