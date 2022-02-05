class AuroraCenterOutCommand: 
    led = None
    colors = [
        "#4dad4b", # greenish
        "#4dad4b", # greenish
        "#15d8ed", # light blue
        "#AB65DD", # purple
        "#FA4D7F", # pink
        "#AB65DD", # purple
        "#15d8ed", # light blue
        "#4dad4b",  # greenish
        "#4dad4b"  # greenish
    ]
    factCache = {}
    gradient = None

    def __init__(self, led):
        self.led = led
        n = 18
        halfGradient = self.bezier_gradient(self.colors, n)["gradient"]
        self.gradient = [None] * n

        for i in range(0, n):
            self.gradient[i] = [halfGradient["r"][i], halfGradient["g"][i], halfGradient["b"][i]]

        # if self.led.getBufferLength() % 2 == 0: 
        #     for i in range(0, len(halfGradient["r"])): 
        #         idx = len(halfGradient["r"]) - i - 1
        #         self.gradient[i] = [halfGradient["r"][idx], halfGradient["g"][idx], halfGradient["b"][idx]]
        #     for i in range(len(halfGradient["r"]), self.led.getBufferLength()): 
        #         idx = i - len(halfGradient["r"])
        #         self.gradient[i] = [halfGradient["r"][idx], halfGradient["g"][idx], halfGradient["b"][idx]]
        # else: 
        #     pass

        for grad in self.gradient:
            print(grad)

    def hex_to_RGB(self, hex):
        ''' "#FFFFFF" -> [255,255,255] '''
        # Pass 16 to the integer function for change of base
        return [int(hex[i:i+2], 16) for i in range(1,6,2)]

    def RGB_to_hex(self, RGB):
        ''' [255,255,255] -> "#FFFFFF" '''
        # Components need to be integers for hex to make sense
        RGB = [int(x) for x in RGB]
        return "#"+"".join(["0{0:x}".format(v) if v < 16 else
                    "{0:x}".format(v) for v in RGB])

    def color_dict(self, gradient):
        ''' Takes in a list of RGB sub-lists and returns dictionary of
            colors in RGB and hex form for use in a graphing function
            defined later on '''
        return {"hex":[self.RGB_to_hex(RGB) for RGB in gradient],
            "r":[RGB[0] for RGB in gradient],
            "g":[RGB[1] for RGB in gradient],
            "b":[RGB[2] for RGB in gradient]}

    def fact(self, n):
        ''' Memoized factorial function '''
        try:
            return self.factCache[n]
        except(KeyError):
            if n == 1 or n == 0:
                result = 1
            else:
                result = n*self.fact(n-1)
            self.factCache[n] = result
            return result


    def bernstein(self, t,n,i):
        ''' Bernstein coefficient '''
        binom = self.fact(n)/float(self.fact(i)*self.fact(n - i))
        return binom*((1-t)**(n-i))*(t**i)


    def bezier_gradient(self, colors, n_out=100):
        ''' Returns a "bezier gradient" dictionary
            using a given list of colors as control
            points. Dictionary also contains control
            colors/points. '''
        # RGB vectors for each color, use as control points
        RGB_list = [self.hex_to_RGB(color) for color in colors]
        n = len(RGB_list) - 1

        def bezier_interp(t):
            ''' Define an interpolation function
                for this specific curve'''
            # List of all summands
            summands = [
                list(map(lambda x: int(self.bernstein(t,n,i)*x), c))
                for i, c in enumerate(RGB_list)
            ]
            # Output color
            out = [0,0,0]
            # Add components of each summand together
            for vector in summands:
                for c in range(3):
                    out[c] += vector[c]
            return out

        gradient = [
            bezier_interp(float(t)/(n_out-1))
            for t in range(n_out)
        ]
        # Return all points requested for gradient
        return {
            "gradient": self.color_dict(gradient),
            "control": self.color_dict(RGB_list)
        }

    def execute(self): 
        for i in range(0, self.led.getBufferLength()):
            self.led.setRGB(i, self.gradient[i][0], self.gradient[i][1], self.gradient[i][2])
        self.led.sendData()
        mid = int(self.led.getBufferLength() / 2.0) if self.led.getBufferLength() % 2 == 0 else None
        
        self.gradient.insert(mid, self.gradient.pop(-1))
        self.gradient.insert(mid-1, self.gradient.pop(0))

    def end(self): 
        pass

    def isFinished(self):
        return False

    def getLED(self):
        return self.led
