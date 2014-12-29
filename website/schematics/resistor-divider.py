import SchemDraw as sch
import SchemDraw.elements as e

d = sch.Drawing()
Vsource = d.add(e.SOURCE_V, label='Vin')
d.add( e.RES, d='right', label='R1')

d.push()
d.add( e.LINE, d='right', l=d.unit/2)
d.add( e.DOT_OPEN, label='Vout')

d.pop()
d.add( e.RES, d='down', label='R2')
d.add( e.LINE, to=Vsource.start)

d.add (e.GND)
d.draw()

# save both for browser incompatibility 
d.save('../static/images/schematics/resistor-divider.svg')
d.save('../static/images/schematics/resistor-divider.png')
