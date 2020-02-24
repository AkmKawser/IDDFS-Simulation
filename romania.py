import pygame
import math

class Romania:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        width = 1000
        height = 694
        self.gameDisplay = pygame.display.set_mode((width,height))
        self.image =pygame.image.load('rom.jpg').convert_alpha()
        self.font = pygame.font.SysFont(None, 30)
        self.msg_source = self.font.render('Source: ', True, (0, 0, 0))
        self.msg_destination = self.font.render('Destination: ', True, (0, 0, 0))

        self.locations = {'Sighetu Marmatiei': (393, 54), 'Satu Mare': (287, 73), 'Baia Mare': (362, 93),
                'Oradea': (194, 186), 'Zalau': (308, 165), 'Cluj-Napoca': (365, 226), 'Bistrita': (452, 171),
                'Radauti': (593, 68), 'Suceava': (631, 95), 'Botosani': (670, 83), 'Vatra Dornei': (538, 142),
                'Iasi': (765, 167), 'Piatra Neamt': (641, 202), 'Turda': (382, 257), 'Targu Mures': (457, 259),
                'Arad': (134, 311), 'Bacau': (695, 255), 'Vaslui': (775, 243), 'Timisoara': (122, 373),
                'Deva': (295, 357), 'Alba lulia': (360,328), 'Sighisoara': (483, 306), 'Onesti': (681, 298),
                'Barlad': (770, 305), 'Resita': (190, 437), 'Hunedoara': (293, 372), 'Sibiu': (415, 367),
                'Sfantu Gheorghe': (582, 356), 'Focsani': (721, 381), 'Galati': (804, 419), 'Targu Jiu': (329, 476),
                'Ramnicu Valcea': (440, 465), 'Sinaia': (559, 433), 'Braila': (799, 442),
                'Drobeta-Turnu Severin': (269, 531),
                'Pitesti': (490, 499), 'Targoviste': (548, 493), 'Ploiesti': (604, 490), 'Buzau': (684, 460),
                'Craiova': (381, 573), 'Slatina': (440, 560), 'Bucharest': (613, 561), 'Calarasi': (734, 592),
                'Constanta': (866, 599), 'Mangalia': (860, 646), 'Eforie Nord': (866, 612), 'Tulcea': (883, 457)
                }
        self.connected_cities = {
            'Sighetu Marmatiei': ['Baia Mare', 'Satu Mare'],
            'Satu Mare': ['Oradea', 'Zalau', 'Baia Mare'],
            'Baia Mare': ['Satu Mare', 'Sighetu Marmatiei', 'Bistrita', 'Cluj-Napoca'],
            'Oradea': ['Satu Mare', 'Arad', 'Deva', 'Cluj-Napoca', 'Turda'],
            'Zalau': ['Satu Mare', 'Cluj-Napoca'],
            'Cluj-Napoca': ['Zalau', 'Baia Mare', 'Oradea', 'Turda', 'Bistrita'],
            'Bistrita': ['Baia Mare', 'Vatra Dornei', 'Cluj-Napoca', 'Sfantu Gheorghe'],
            'Radauti': ['Vatra Dornei', 'Suceava'],
            'Suceava': ['Radauti', 'Botosani', 'Vatra Dornei', 'Bacau', 'Iasi'],
            'Botosani': ['Suceava', 'Iasi', 'Bacau'],
            'Vatra Dornei': ['Suceava', 'Bistrita'],
            'Iasi': ['Botosani', 'Suceava', 'Bacau', 'Vaslui'],
            'Piatra Neamt': ['Bacau', 'Vaslui'],
            'Turda': ['Cluj-Napoca', 'Oradea', 'Targu Mures', 'Alba lulia'],
            'Targu Mures': ['Turda', 'Sighisoara'],
            'Arad': ['Oradea', 'Timisoara', 'Deva'],
            'Bacau': ['Piatra Neamt', 'Iasi', 'Suceava', 'Botosani', 'Vaslui', 'Onesti', 'Focsani', 'Barlad'],
            'Vaslui': ['Bacau', 'Barlad'],
            'Timisoara': ['Arad', 'Deva', 'Drobeta-Turnu Severin', 'Resita'],
            'Deva': ['Timisoara', 'Sibiu', 'Hunedoara', 'Alba lulia'],
            'Alba lulia': ['Turda', 'Deva', 'Sibiu'],
            'Sighisoara': ['Targu Mures', 'Sfantu Gheorghe'],
            'Onesti': ['Bacau', 'Sfantu Gheorghe'],
            'Barlad': ['Focsani', 'Bacau'],
            'Resita': ['Timisoara', 'Drobeta-Turnu Severin'],
            'Hunedoara': ['Deva', 'Targu Jiu'],
            'Sibiu': ['Alba lulia', 'Deva', 'Ramnicu Valcea'],
            'Sfantu Gheorghe': ['Onesti', 'Bistrita', 'Sighisoara', 'Sinaia', 'Pitesti'],
            'Focsani': ['Barlad', 'Bacau', 'Buzau', 'Galati'],
            'Galati': ['Braila', 'Focsani'],
            'Targu Jiu': ['Hunedoara', 'Craiova', 'Drobeta-Turnu Severin'],
            'Ramnicu Valcea': ['Sibiu', 'Pitesti'],
            'Sinaia': ['Sfantu Gheorghe', 'Ploiesti'],
            'Braila': ['Galati', 'Calarasi', 'Tulcea'],
            'Drobeta-Turnu Severin': ['Craiova', 'Timisoara', 'Resita', 'Targu Jiu'],
            'Pitesti': ['Ramnicu Valcea', 'Slatina', 'Targoviste', 'Bucharest'],
            'Targoviste': ['Pitesti', 'Bucharest'],
            'Ploiesti': ['Sinaia', 'Buzau', 'Bucharest', 'Calarasi', 'Constanta'],
            'Buzau': ['Ploiesti', 'Focsani', 'Bucharest', 'Calarasi', 'Constanta'],
            'Craiova': ['Drobeta-Turnu Severin', 'Targu Jiu', 'Slatina', 'Bucharest'],
            'Slatina': ['Craiova', 'Pitesti'],
            'Bucharest': ['Craiova', 'Pitesti', 'Targoviste', 'Ploiesti', 'Buzau', 'Calarasi','Eforie Nord'],
            'Calarasi': ['Braila', 'Bucharest','Ploiesti', 'Buzau'],
            'Constanta': ['Ploiesti', 'Buzau', 'Tulcea'],
            'Mangalia': ['Eforie Nord'],
            'Eforie Nord': ['Bucharest', 'Mangalia'],
            'Tulcea': ['Braila', 'Constanta']
        }
        i = IDDFS('Oradea',4)
        self.drawLines()
        self.gameLoop()
    def drawLines(self):
        for city,connections in self.connected_cities.items():
            x1,y1 = self.locations[city]
            for connection in connections:
                x2,y2 = self.locations[connection]
                pygame.draw.line(self.gameDisplay,(27,112,8),(x1,y1),(x2,y2),2)
                pygame.draw.line(self.gameDisplay,(0,0,255),(x1,y1),(x1,y1),2)


    def gameLoop(self):
        source_selected = False
        destination_selected = False
        gameExit = False
        while not gameExit:
            self.gameDisplay.blit(self.image, [0, 0])
            self.drawLines()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
                    location = self.get_closest_location(x,y)
                    if not source_selected and not destination_selected:
                        source = location
                        source_x,source_y = self.locations[location]
                        self.msg_source = self.font.render('Source: '+str(source), True, (0, 0, 0))
                        source_selected = True
                    elif source_selected and not destination_selected:
                        destination = location
                        desti_x, desti_y = self.locations[location]
                        self.msg_destination = self.font.render('Destination: '+str(destination), True, (0, 0, 0))
                        destination_selected = True

            self.gameDisplay.blit(self.msg_source, [20, 20])
            self.gameDisplay.blit(self.msg_destination, [20, 60])
            if source_selected:
                pygame.draw.circle(self.gameDisplay, (0, 0, 255), (source_x,source_y), 8)
            if destination_selected:
                pygame.draw.circle(self.gameDisplay, (255, 0, 0), (desti_x,desti_y), 8)
            pygame.display.update()
            self.clock.tick(30)
        pygame.display.quit()
        pygame.quit()
        quit()

    def get_distance(self,x1,y1,x2,y2):
        return math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2))

    def get_closest_location(self,x1,y1):
        min_distance = math.inf
        for location,coordinates in self.locations.items():
            x2,y2 = coordinates
            distance = self.get_distance(x1,y1,x2,y2)
            if distance<min_distance:
                min_distance = distance
                close_location = location
        return close_location

class IDDFS:
    def __init__(self,source,max_height):
        self.iddfs(source,max_height)
    def DLS(self,source,depth):

        start=Romania.connected_cities[source]
        print(source, end=' ')
        if start[0] is None:
            return
        if depth==0:
            return
        else:
            for location in start:
                listt = location
                for place in listt:
                    self.DLS(place,depth-1)

    def iddfs(self,source,max_height):
        for i in range(max_height+1):
            print('depth '+str(i)+': ',end=' ')
            self.DLS(source,i)
            print()
r = Romania()


