from flask import Flask, request, jsonify
from flask_cors import CORS
from astropy.coordinates import SkyCoord
from astropy import units as u
import matplotlib.pyplot as plt
import numpy as np



app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})



@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    data = file.read().decode('utf-8')
    lines = data.split('\n')

    IDs = [line.split()[0] for line in lines if line.strip()]
    
    gxy_ra = []
    gxy_dec = []
    for gxyID in IDs:
        ra = gxyID[0:2]+'h'+gxyID[2:4]+'m'+gxyID[4:6]+'.'+gxyID[6:8]+'s'
        dec = gxyID[8:11]+'d'+gxyID[11:13]+'m'+gxyID[13:15]+'.'+gxyID[15]+'s'
        coord = SkyCoord(ra, dec, frame='icrs')
        gxy_ra.append(coord.ra.deg)
        gxy_dec.append(coord.dec.deg)
    
    # Plotting code (Assuming matplotlib and appropriate setup)
    plt.figure(figsize=(12,10))
    ax = plt.axes(projection='mollweide')
    ax.plot(np.radians(gxy_ra), np.radians(gxy_dec), 'o', color='deepskyblue', alpha=0.6)
    plt.grid(True)
    plt.title("Galaxy Coordinates")
    plt.savefig('galaxy_coordinates.png')
    return 'File uploaded successfully', 200



if __name__ == '__main__':
    app.run(debug=True)
