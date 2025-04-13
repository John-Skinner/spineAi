from math import frexp
from urllib import response
import json
import numpy as np
import matplotlib.pyplot as plt

from flask import Flask
from flask import request
from flask_cors import CORS
import base64

app = Flask(__name__)
CORS(app)

def point(x,y):
    return {'x': x, 'y': y}
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!\n'
@app.route('/getautospinelabels', methods=['PUT'])
def autospinelabel():

    body = request.get_json()
#    outfile = open('/tmp/spineRequest.json', 'w')
#    outfile.write(json.dumps(body))
#    outfile.close()

    print('getautospinelabels')
    pixels = body['pixels']
    viewportId = body['viewportId']
    print('pixels length: {}'.format(len(pixels)))
    width = body['width']
    height = body['height']


    decodedpixelbytes = base64.b64decode(pixels)
    print('decodedpixelbytes length: {}'.format(len(decodedpixelbytes)))
    print('pixel 3 bytes: {}'.format(decodedpixelbytes[3]))
    shorts = np.zeros((width,height), np.int16)
    numBrites = 0
    for ix in range(width):
        for iy in range(height):
            shortIndex = iy*width + ix
            byteIndex = shortIndex*2
            byteLow =  decodedpixelbytes[byteIndex]
            byteHigh = decodedpixelbytes[byteIndex+1]
            shorts[ix,iy] = byteHigh*256 + byteLow
            if shorts[ix,iy] == 10000:
                numBrites += 1


    print('numBrites: {}'.format(numBrites))
    plt.imshow(shorts)
    plt.colorbar()
    plt.title('downloaded image')
    plt.show()
    return_points = []
    return_points.append(point(10,10))
    return_points.append(point(width/2,height/2))
    return_points.append(point(width-10,10))
    response_data = {
        'viewportId': viewportId,
        'points': return_points
    }

    return response_data, 200



if __name__ == '__main__':
    app.run()
