import sys

import matplotlib.path as mplPath
import numpy as np

'''
Read in csv
'''
def read_file(filename):
    headers = []
    dataset = []
    with open(filename, 'rU') as f:
        headers = f.readline().strip().split(',');
        for line in f:
            row = line.strip().split(",")
            dataset.append(row)
    return headers, dataset

class Coordinate(object):

  def __init__(self):
    self.__x = 0
    self.__y = 0
  
  def setXY(self, x, y):
    self.__x = x
    self.__y = y

  def getX(self):
    return self.__x
  
  def getY(self):
    return self.__y

  def __del__(self):
    pass

class Polygon(object):

  def __init__(self):
    self.__coordinates = []
    self.__nat_code = ''
    self.__number_of_entries = 0
    #self.__polypath
  
  def addCoordinate(self, c):
    self.__number_of_entries = self.__number_of_entries + 1
    self.__coordinates.append(c)
  
  def getCoordinates(self):
    return self.__coordinates
  
  def setNat(self, nat_code):
    self.__nat_code = nat_code
  
  def getNat(self):
    return self.__nat_code
  
  def createPolygon(self):
    list_of_points = []
    for c in self.__coordinates:
      point = []
      point.append(c.getX())
      point.append(c.getY())
      list_of_points.append(point)
    return mplPath.Path(np.array(list_of_points))
  
  def getNatfromCoordiante(self, c):
    polypath = self.createPolygon()
    if polypath.contains_point((c.getX(), c.getY())):
      print 'in'
      return self.__nat_code
    else:
      print 'out'
      return ''

  def __del__(self):
    pass


if __name__ == "__main__":
  
    nat_codes, zone_coordinates = read_file('geographic.csv')
    
    '''for entry in zone_coordinates:
      for long in entry:
        print long'''
      
    '''for entry in zone_coordinates[2]:
    
    for entry in zone_coordinates[2]:
      print entry'''
    
    '''print zone_coordinates[0][0]
    print zone_coordinates[1][0]
    print zone_coordinates[0][1]
    print zone_coordinates[1][1]'''
    
    
    '''for j in range(0,len(zone_coordinates)):
      if zone_coordinates[j][0] != '':
        print zone_coordinates[j][0]'''
    
    
    nat_zone_polygons = []
    for i in range(0,len(nat_codes)):
      p = Polygon()
      p.setNat(nat_codes[i])
      nat_zone_polygons.append(p)
    
    for j in range(0, len(zone_coordinates) - 2 , 2):
      for i in range(0,len(nat_codes)):
        if zone_coordinates[j][i] != '':
          c = Coordinate()
          c.setXY(zone_coordinates[j+1][i], zone_coordinates[j][i])
          nat_zone_polygons[i].addCoordinate(c)

    '''c = Coordinate()
    c.setXY(40.769,-73.9549)
    for p in nat_zone_polygons:
      if p.getNatfromCoordiante(c) != '':
        print p.getNatfromCoordiante(c)
        break'''


    '''cor = nat_zone_polygons[0].getCoordinates()
    for i in range(0, 10):
      print cor[i].getX() + ' ' + cor[i].getY()'''


    c = Coordinate()
    #c.setXY(40.6312841471042,-73.9760507905698)
    c.setXY(40.626,-73.96)
    print nat_zone_polygons[0].getNatfromCoordiante(c)

    #40.7666,-73.9531

    #c.setXY(40.769,-73.9549)

    '''for i in zone_coordinates[0]:
      print i
    for j in zone_coordinates[1]:
      print j'''

    #print len(zone_coordinates[1])
    #print len(zone_coordinates)
    
    #print zone_coordinates[2]
    ''' print len(nat_codes)
    
    nat_zone_polygons = []
    #for j in range(0, len(nat_codes)):

    p = Polygon()
    p.setNat(nat_codes[0])

    for i in range(0,len(zone_coordinates[1])):
      c = Coordinate()
      c.setXY(zone_coordinates[1][i], zone_coordinates[0][i])
      p.addCoordinate(c)
    
    nat_zone_polygons.append(p)

    c = Coordinate()
    c.setXY(-73.9760507905698,40.630) # coordinate to find
    for p in nat_zone_polygons:
      if p.getNatfromCoordiante(c) != '':
        print p.getNatfromCoordiante(c)
        break
'''


    '''for i in p.getCoordinates():
      print i.getX() + ', ' + i.getY()
      
    c = Coordinate()
    c.setXY(-73.9760507905698,40.630)
    print p.getNatfromCoordiante(c)'''

    #-73.9760507905698
    #40.6312841471042

    
    '''p = Polygon()
    c = Coordinate()
    c.setXY(0, 0)
    p.addCoordinate(c)
    
    c = Coordinate()
    c.setXY(-1, 0)
    p.addCoordinate(c)

    c = Coordinate()
    c.setXY(-1, -1)
    p.addCoordinate(c)

    c = Coordinate()
    c.setXY(0, -1)
    p.addCoordinate(c)
    
    p.setNat('test')
    #p.createPolygon()
    
    c = Coordinate()
    c.setXY(-0.2, -0.3)
    
    for i in p.getCoordinates():
      print i.getX()
      print i.getY()
      
    print p.getNatfromCoordiante(c)'''
    
    
    
    ''' uber_trips_2014_coordinates = []
    trash, coordinates = read_file('uber_trips_2014.csv')
    for entry in coordinates:
      c = Coordinate()
      c.setXY(entry[1], entry[2]) # lat, long
      uber_trips_2014_coordinates.append(c)'''
    
    
    #uber_trips_2014_coordinates[0].getX()
    #uber_trips_2014_coordinates[0].getY()

    
    #print nat_codes
    #print zone_coordinates[0]
    
    #print headers
    #print dataset[0]

    '''poly = [190, 50, 500, 310]
    
    a = [[poly[0], poly[1]],
                     [poly[1], poly[2]],
                     [poly[2], poly[3]],
                     [poly[3], poly[0]]]
    a = []
    a.append([poly[0], poly[1]])
    a.append([poly[0], poly[1]])
    
    bbPath = mplPath.Path(np.array(a))

    #print bbPath.contains_point((800, 100))'''

