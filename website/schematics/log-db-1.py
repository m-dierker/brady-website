import SchemDraw as sch
import SchemDraw.elements as e

d = sch.Drawing()
Vsource = d.add(e.SOURCE_V, label='5V')
d.add(e.SOURCE_V, label='5V')
d.push()
d.add(e.GND, d='left')

d.pop()
d.add( e.LINE, d='right', l=d.unit)
d.add( e.RES, d='down', l=d.unit*2)
d.add( e.LINE, to=Vsource.start)
d.draw()


# save both for browser incompatibility 
d.save('/home/brady/website/website/static/images/schematics/' + __file__[:-3] + '.png')
d.save('/home/brady/website/website/static/images/schematics/' + __file__[:-3] + '.svg')
