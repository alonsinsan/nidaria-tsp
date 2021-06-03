# nidaria-tsp
Traveling Salesman problem for Nidaria's recollection route using Googe Distance Matrix API
## NIDARIA
Nidaria is a service for the correct disposal for organic waste. With a small weekly fee you get a kit to dispose the organic waste in your house and a twice-a-week collection service.
For more information visit [NIDARIA](https://nidaria.mx/)
## Problem
Given a list of addresses for the recollection service, this script gets ETA for the routes between the point with the [Google Distance Matrix API](https://developers.google.com/maps/documentation/distance-matrix/overview) and solves the Traveling Salesman Problem with the [python-tsp](https://pypi.org/project/python-tsp/) library.
# INPUT 
Plus codes for the addresses to visit with the first code being the initial and final destination.
# OUTPUT 
The list with the order to visit.
