class Polygon:
    def __init__(self,totalPoints, coordX, coordY):
         self.coordX = coordX
         self.coordY = coordY
         self.TotalPoints = totalPoints;
         self.Ax = 0; self.Sx = 0; self.Sy = 0; self.Ix = 0; self.Iy = 0; self.Ixy = 0; self.Xt = 0; self.Yt = 0;

    def CalculateGeometricCharacteristics(self):
        for i in range(self.TotalPoints):
            self.Ax += ((self.coordX[i]+self.coordX[i-1])*(self.coordY[i]-self.coordY[i-1]))/2
            self.Sx += ((self.coordX[i]-self.coordX[i-1])*(self.coordY[i]**2 +self.coordY[i]*self.coordY[i-1] + self.coordY[i-1]**2))/(-6)
            self.Sy += ((self.coordY[i]-self.coordY[i-1])*(self.coordX[i]**2 +self.coordX[i]*self.coordX[i-1] + self.coordX[i-1]**2))/6
            self.Ix += ((self.coordX[i]-self.coordX[i-1])*
                (self.coordY[i]**3 + self.coordY[i-1]*self.coordY[i]**2 + self.coordY[i]*self.coordY[i-1]**2 + self.coordY[i-1]**3 ))/(-12)
            self.Iy += ((self.coordY[i]-self.coordY[i-1])*
                (self.coordX[i]**3 + self.coordX[i-1]*self.coordX[i]**2 + self.coordX[i]*self.coordX[i-1]**2 + self.coordX[i-1]**3 ))/(12)
            self.Ixy += ((self.coordY[i]-self.coordY[i-1])*
                (self.coordY[i]*(3*self.coordX[i]**2+2*self.coordX[i]*self.coordX[i-1]+self.coordX[i-1]**2)+
                self.coordY[i-1]*(3*self.coordX[i-1]**2+2*self.coordX[i]*self.coordX[i-1]+self.coordX[i]**2)))/(-24)

        self.Xt = self.Sy/self.Ax
        self.Yt = self.Sx/self.Ax
        self.Ixt = self.Ix - self.Ax*self.Yt**2
        self.Iyt = self.Iy - self.Ax*self.Xt**2
        self.Ixyt = self.Ixy + self.Xt*self.Yt*self.Ax

    def PrintGeometricCharacteristics(self):
        print("\nGeometric Characteristics")
        print("-" * 25)
        print("| Ax:   %.2f" % self.Ax)
        print("| Sx:   %.2f" % self.Sx)
        print("| Sy:   %.2f" % self.Sy)
        print("| Ix:   %.2f" % self.Ix)
        print("| Iy:   %.2f" % self.Iy)
        print("| Ixy:  %.2f" % self.Ixy)
        print("| Xt:   %.2f" % self.Xt)
        print("| Yt:   %.2f" % self.Yt)
        print("| Ixt:  %.2f" % self.Ixt)
        print("| Iyt:  %.2f" % self.Iyt)
        print("| Ixyt:  %.2f" % self.Ixyt)
    
    def PrintTableOfPoints(self):
        print(f"\n{'Point':>10} {'CoordX':>10} {'CoordY':>10}")
        print("-" * 35)
        for i in range(self.TotalPoints):
            print(f"{i+1:>8} {self.coordX[i]:>10} {self.coordY[i]:>10}")

def Main():

    totalPoints = int(input("Insert the number of points of your polygon: "))
    coordX = []
    coordY = []

    print("\nThe points[X;Y] shall be insert in counter clockwise to define your Polygon\n")
    count=1
    while(count<=totalPoints):
        point = input(f"Insert point {count}: ")
        xy = point.split(';')
        coordX.append(int(xy[0]))
        coordY.append(int(xy[1]))
        count+=1

    polygon = Polygon(totalPoints,coordX,coordY)
    polygon.PrintTableOfPoints()
    polygon.CalculateGeometricCharacteristics()
    polygon.PrintGeometricCharacteristics()
    
Main()

