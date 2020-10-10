#!/usr/bin/env python

__author__ = '''Tracy DeWitt,
Piero Madar,
Manuel Velasco,
https://timestamp.online/article
/how-to-convert-timestamp-to-datetime-in-python,
https://realpython.com/python-f-strings/
'''

import requests
import time
import turtle


def astronauts_info():
    # Using this public API, write a Python program to obtain a
    # list of the astronauts who are currently in space.
    # Print their full names, the spacecraft they are currently
    # on board, and the total number of astronauts in space.

    current_astronauts_info = requests.get(
        'http://api.open-notify.org/astros.json').json()["people"]

    for value in current_astronauts_info:
        print(f'{value["name"]} aboard the {value["craft"]}')

    print(f'Number of astronauts in space {len(current_astronauts_info)}')


def current_geo_coords():
    # Using this public API, obtain the current geographic coordinates
    # (lat/lon) of the space station, along with a timestamp.

    current_location = requests.get(
        'http://api.open-notify.org/iss-now.json').json()
    ["iss_position"]
    print(current_location['iss_position'])
    print(f'Timestamp: {time.ctime(current_location["timestamp"])}')
    return current_location['iss_position']


def map_coords():
    # With the turtle graphics library (part of Python's standard library),
    # create a graphics screen with the world map background image,
    # map.gif. Use turtle methods such as Screen(), setup(),
    # bgpic(), and setworldcoordinates().
    # Register an icon image for the ISS within the turtle screen context,
    # and create a turtle.Turtle() to move the ISS to its current lat/lon
    # on the map. Use methods such as shape(), setheading(), penup(),
    # and goto().

    curr_loc = current_geo_coords()
    print(curr_loc)

    win_map = turtle.Screen()
    win_map.setup(width=730, height=350)
    win_map.bgpic('map.gif')

    win_map.setworldcoordinates(-180, -90, 180, 90)

    win_map.addshape('iss.gif')
    indy_loc()

    i = turtle.Turtle()
    i.penup()
    i.goto(float(curr_loc['longitude']), float(curr_loc['latitude']))
    i.shape('iss.gif')
    i.pendown()
    turtle.done()


def time_over_indy():
    # You will need to supply the lat/lon coordinates as query
    # parameters to this URL. The passover times are returned as
    # timestamps, so you will need to use the time.ctime()
    # method to convert them to human-readable text. Render the next
    # passover time next to the Indianapolis location dot
    # that you plotted earlier.
    req = requests.get(
        f'http://api.open-notify.org/iss-pass.json?'
        f'lat={39.7684}&lon={-86.1581}')
    t = req.json()['response'][0]['risetime']
    return time.ctime(t)


def indy_loc():
    # Find out the next time that the ISS will be overhead of
    # Indianapolis, Indiana. Use the geographic lat/lon
    # of Indianapolis, Indiana to plot a yellow dot on the map.
    # Use [this public API](http://api.open-notify.org/iss-pass.json)
    # to query the next pass.
    stamp = time_over_indy()

    indy = turtle.Turtle()
    indy.penup()
    lat = 39.7684
    lon = -86.1581
    indy.goto(lon, lat)

    indy.dot(15, 'yellow')
    indy.color('red')

    indy.write(stamp, font=20)
    print(stamp)
    indy.hideturtle()


def main():
    astronauts_info()
    map_coords()


if __name__ == '__main__':
    main()
