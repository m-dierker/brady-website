import bokeh
from bokeh.resources import CDN
from bokeh.embed import file_html, components
from bokeh.sampledata.iris import flowers
from bokeh.plotting import *

colormap = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
flowers['color'] = flowers['species'].map(lambda x: colormap[x])

output_file("iris.html", title="iris.py example")

p = figure(title = "Iris Morphology")
p.xaxis.axis_label = 'Petal Length'
p.yaxis.axis_label = 'Petal Width'

p.circle(flowers["petal_length"], flowers["petal_width"],
                color=flowers["color"], fill_alpha=0.2, size=10, )

script, div = components(p, CDN)
print script
f = open('testscript.html', 'w')
f.write(script)
f.close()
