import pygame
import math
import time
class Romania:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        width = 1000+300
        height = 694
        self.gameDisplay = pygame.display.set_mode((width,height))
        self.image =pygame.image.load('rom.jpg').convert_alpha()
        self.map = pygame.image.load('map2.jpg').convert_alpha()
        self.font = pygame.font.SysFont(None, 30)
        self.msg_source = self.font.render('Source: ', True, (0, 0, 0))
        self.msg_destination = self.font.render('Destination: ', True, (0, 0, 0))
        self.msg_depth = self.font.render('Depth: ', True, (0, 0, 0))
        self.font1 = pygame.font.SysFont(None, 25)
        self.button_msg = self.font1.render('Increase Depth',True,(255,255,255))
        pygame.display.set_caption("Romania IDDFS")
        self.loc_arr = []
        self.flag = 0
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
        self.connected_cities = {'Sighetu Marmatiei': ['Baia Mare'], 'Baia Mare': ['Sighetu Marmatiei', 'Satu Mare', 'Bistrita', 'Cluj-Napoca'], 'Satu Mare': ['Zalau', 'Baia Mare', 'Oradea'], 'Zalau': ['Satu Mare', 'Cluj-Napoca'], 'Bistrita': ['Baia Mare', 'Vatra Dornei', 'Targu Mures'], 'Cluj-Napoca': ['Baia Mare', 'Zalau', 'Turda'], 'Oradea': ['Arad', 'Satu Mare', 'Turda', 'Deva'], 'Arad': ['Oradea', 'Deva', 'Timisoara'], 'Turda': ['Oradea', 'Cluj-Napoca', 'Alba lulia', 'Targu Mures'], 'Deva': ['Oradea', 'Arad', 'Timisoara', 'Hunedoara', 'Alba lulia'], 'Vatra Dornei': ['Bistrita', 'Suceava'], 'Targu Mures': ['Bistrita', 'Turda', 'Sighisoara'], 'Radauti': ['Suceava'], 'Suceava': ['Radauti', 'Botosani', 'Piatra Neamt', 'Vatra Dornei'], 'Botosani': ['Suceava', 'Iasi'], 'Piatra Neamt': ['Suceava', 'Bacau'], 'Iasi': ['Botosani', 'Vaslui', 'Bacau'], 'Vaslui': ['Iasi', 'Bacau', 'Barlad'], 'Bacau': ['Iasi', 'Piatra Neamt', 'Onesti', 'Vaslui', 'Focsani'], 'Alba lulia': ['Turda', 'Deva', 'Sibiu'], 'Sighisoara': ['Targu Mures'], 'Timisoara': ['Arad', 'Resita', 'Deva', 'Drobeta-Turnu Severin'], 'Onesti': ['Bacau', 'Sfantu Gheorghe'], 'Focsani': ['Bacau', 'Barlad', 'Buzau'], 'Barlad': ['Vaslui', 'Focsani'], 'Resita': ['Timisoara'], 'Drobeta-Turnu Severin': ['Timisoara', 'Craiova'], 'Hunedoara': ['Deva', 'Targu Jiu'], 'Sibiu': ['Alba lulia', 'Ramnicu Valcea'], 'Sfantu Gheorghe': ['Onesti'], 'Targu Jiu': ['Hunedoara', 'Craiova'], 'Ramnicu Valcea': ['Sibiu', 'Pitesti'], 'Buzau': ['Focsani', 'Braila', 'Ploiesti', 'Bucharest'], 'Galati': ['Braila'], 'Braila': ['Galati', 'Buzau', 'Tulcea', 'Calarasi'], 'Tulcea': ['Braila', 'Constanta'], 'Calarasi': ['Braila', 'Bucharest', 'Constanta'], 'Pitesti': ['Ramnicu Valcea', 'Slatina', 'Bucharest'], 'Slatina': ['Pitesti', 'Craiova'], 'Ploiesti': ['Sinaia', 'Targoviste', 'Buzau', 'Bucharest'], 'Sinaia': ['Ploiesti'], 'Targoviste': ['Ploiesti'], 'Craiova': ['Targu Jiu', 'Drobeta-Turnu Severin', 'Slatina', 'Bucharest'], 'Bucharest': ['Buzau', 'Pitesti', 'Ploiesti', 'Craiova', 'Calarasi', 'Constanta', 'Eforie Nord'], 'Constanta': ['Calarasi', 'Bucharest', 'Mangalia', 'Tulcea'], 'Mangalia': ['Constanta', 'Eforie Nord'], 'Eforie Nord': ['Bucharest', 'Mangalia']}
        self.button =pygame.Rect(1050,300,200,50)
        # self.drawLines()
        self.gameLoop()
    # def drawLines(self):
    #     for city,connections in self.connected_cities.items():
    #         x1,y1 = self.locations[city]
    #         for connection in connections:
    #             x2,y2 = self.locations[connection]
    #             pygame.draw.line(self.gameDisplay,(27,112,8),(x1,y1),(x2,y2),2)
    #             pygame.draw.line(self.gameDisplay,(0,0,255),(x1,y1),(x1,y1),2)


    def gameLoop(self):
        depth = 0
        source_selected = False
        destination_selected = False
        gameExit = False
        self.gameDisplay.blit(self.image, [0, 0])
        # self.drawLines()
        while not gameExit:
            self.gameDisplay.blit(self.map, [1000, 0])
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
                    if self.button.collidepoint(x,y):
                        depth += 1
                        self.msg_depth = self.font.render('Depth: ' + str(depth), True, (0, 0, 0))
                        self.iddfs(source, destination, depth)


            self.gameDisplay.blit(self.msg_source, [1020, 20])
            self.gameDisplay.blit(self.msg_destination,[1020,45])
            self.gameDisplay.blit(self.msg_depth, [1020, 70])
            if source_selected:
                pygame.draw.circle(self.gameDisplay, (0, 0, 255), (source_x,source_y), 8)
            if destination_selected:
                pygame.draw.circle(self.gameDisplay, (255, 0, 0), (desti_x,desti_y), 8)
            pygame.draw.rect(self.gameDisplay, [31, 7, 8], self.button) # 45,51,47
            self.gameDisplay.blit(self.button_msg,[1090,315])
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

    def DLS(self,source,depth,destination):

        print(source,end=' ')

        start = self.connected_cities[source]
        if source not in self.loc_arr:
            self.loc_arr.append(source)
        if depth==0:
            return

        else:
            for location in start:
                if self.flag==1:
                    break
                self.DLS(location,depth-1,destination)
                if destination in self.loc_arr:
                    self.flag = 1
                    return
                if self.flag == 1:
                    return
    def iddfs(self,source,destination,depth):
        found = False
        for i in range(depth):
            self.gameDisplay.blit(self.image, [0, 0])
            print('depth '+str(i)+': ',end=' ')
            self.loc_arr =[]
            self.DLS(source,i,destination)
            for i in range(1,len(self.loc_arr)):
                pygame.draw.line(self.gameDisplay,(0,0,0),self.locations[self.loc_arr[i-1]],self.locations[self.loc_arr[i]],3)
            print()



r = Romania()


