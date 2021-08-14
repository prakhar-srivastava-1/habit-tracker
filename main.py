from pixela import Pixela
import datetime as dt

GRAPH_ID = "graph1"
GRAPH_NAME = "Gym Workout"

# make an API call to create a new user - call once
pixela = Pixela()
# print(pixela.create_user_account())

# make a new call to create graph - call once
# print(pixela.create_graph(GRAPH_ID, GRAPH_NAME))

# post a new pixel
# activity_date = dt.datetime.now().strftime("%Y%m%d")
# activity_time = '1.0'
# print(pixela.create_pixel(GRAPH_ID, activity_date, activity_time))
