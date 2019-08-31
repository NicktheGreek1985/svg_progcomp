class SVG(object):

    def __init__(self, filename):
        self.filename = filename + ('.svg' if not filename.endswith('.svg') else '')
        self.file = open(self.filename, 'w')

    def write_header(self):
        self.file.write('''<?xml version="1.0" encoding="iso-8859-1"?>
        <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20001102//EN"
         "http://www.w3.org/TR/2000/CR-SVG-20001102/DTD/svg-20001102.dtd">
         
         <svg width="600" height="400"
         xmlns="http://www.w3.org/2000/svg"
         xmlns:xlink="http://www.w3.org/1999/xlink">

         <defs>
         <style type="text/css">
         <![CDATA[
            text.C { text-anchor:middle; }
            text.R { text-anchor:end; }
            text.title { font-size:16px; font-weight:bold;
                   font-family:Arial,Helvetica,sansserif;
            }
            .bar { stroke:#888888; stroke-width:0.5px; }
            .unordered { fill:#E7CACA; stroke:#B54040; }
            .sep { stroke:#444444; stroke-width:0.8px; stroke-dasharray:5,3; }
            .border { stroke: #AAAAAA; stroke-width:3px; fill:#FFFFF0; }
        ]]> </style>
         <filter id="bevel"> ... </filter>
        </defs>

        ''')

    def close_svg(self):
        self.file.write('</svg>')
        self.file.close()

    def create_text(self, content=''):
        self.file.write('''
        <text class="title C" x="300" y="30">''' + content + '''</text>
        ''')

    def create_rect(self, x, y, width, height):
        self.file.write('''
        <rect id="bar0" class="bar unordered" filter="url(#bevel)"
        x="''' + str(x) + '''" y="''' + str(y) + '''"
        width="''' + str(width) + '''" height="''' + str(height) + '''" />
        ''')

    def create_line(self, x1, x2, y1, y2):
        self.file.write('''
        <line class="sep" x1="''' + str(x1) + '''" x2="''' + str(x2) + '''" y1="''' +
        str(y1) + '''" y2="''' + str(y2) + '''" />
        ''')

    
    def create_circle(self, cx, cy, r): 
        self.file.write('''
        <circle id="point99" class="dot" cx="''' + str(cx) + '''" cy="''' +
        str(cy) + '''" r="''' + str(r) + '''" />
        ''')
        
    def create_ellipse(self, x, y, rx, ry):
        self.file.write('''
        <ellipse class="oval" cx="''' + str(x) + '''" cy="''' + str(y) + '''" rx="''' +
        str(rx) + '''" ry="''' + str(ry) + '''"/>
        ''')

if __name__ == '__main__':
    my_svg = SVG('my_first_svg')
    my_svg.write_header()
    my_svg.create_text('Insertion Sort')
    my_svg.create_line(540.0, 540.0, 370.0, 42.0)
    my_svg.create_rect(30.0, 295.7, 20, 74.35)
    my_svg.create_circle(90, 120, 12.5)
    my_svg.create_ellipse(90, 120, 12.5, 15)
    my_svg.close_svg()
    
