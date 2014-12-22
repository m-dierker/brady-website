import bokeh
from bokeh.plotting import circle
from bokeh.resources import CDN
from bokeh.embed import file_html

plot = circle([1,2], [3,4])

html = file_html(plot, CDN, "my plot")
