# CloudLevelManager
A Pythonic way to maintain and generate cloud levels for the EdgeProX and MotiveWave trading platforms.
Use templates instead of cutting and pasting lines in a CSV file.

# The Basics
## Import the module:
'''
from CloudLevelManager import CloudLevels
'''
## The most basic example -- we'll talk about the structure a little bit later
'''
levels = {
    'support/resistance': [
        {'Price': 4309.50},
        {'Price': 4282.25},
        {'Price': 4249.50},
        ],
    }
# Create a CloudLevels object and write the CSV file
cl = CloudLevels('ES', levels, tick_size=0.25)
cl.to_csv('my_cloud_levels.csv')
'''
