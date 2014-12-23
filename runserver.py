# basic bootup file for Flask
# needs to be a dir above in order to handle "circular" imports
from website import app
app.run()
