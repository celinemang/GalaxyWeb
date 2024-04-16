from flask import Flask, jsonify
import pandas as pd
from astropy.coordinates import SkyCoord
import astropy.units as u

app = Flask(__name__)

# Define route for processing astronomical data
@app.route('/process-data')
def process_data():
    # Read CSV file containing astronomical data
    df = pd.read_csv('data/astronomical_data.csv')

    # Perform processing (example: extract RA, Dec coordinates)
    coordinates = []
    for index, row in df.iterrows():
        ra = row['RA'] * u.degree
        dec = row['Dec'] * u.degree
        coord = SkyCoord(ra=ra, dec=dec)
        coordinates.append(coord)

    # Convert coordinates to dictionary format for JSON serialization
    processed_data = [{'ra': coord.ra.deg, 'dec': coord.dec.deg} for coord in coordinates]

    # Return processed data as JSON
    return jsonify(processed_data)

if __name__ == '__main__':
    app.run(debug=True)
