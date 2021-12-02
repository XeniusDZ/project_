from dataclasses import dataclass
import pygame, pytmx, pyscroll

class Portal:
    def __init__(self,from_world,origin_point,to_world,teleport_point):
        self.from_world = from_world
        self.origin_point = origin_point
        self.to_world = to_world
        self.teleport_point = teleport_point


@dataclass
class Map:
    name: str
    walls: list
    group: pyscroll.PyscrollGroup
    tmx: pytmx.TiledMap
    portals: list

class MapManager:
    def __init__(self, screen,player):
        self.player = player
        self.screen = screen
        self.maps = dict()
        self.current_map = "map"

        self.register_map("map",portals=[Portal(from_world="map",origin_point = "enter_bib", to_world = "house",teleport_point= "spawn_to_bib"),
        Portal(from_world="map", origin_point="to_map2", to_world="map2", teleport_point="from_map"),
        Portal(from_world="map", origin_point="to_map5", to_world="map5", teleport_point="from_map1"),
        Portal(from_world="map", origin_point="to_map4", to_world="map4", teleport_point="from_map1"),
        Portal(from_world="map", origin_point="to_map3", to_world="map3", teleport_point="from_map1"),
        Portal(from_world="map",origin_point = "to_small_house", to_world = "small_house",teleport_point= "from_map1")])

        self.register_map("map2",portals=[Portal(from_world="map2",origin_point = "to_map", to_world = "map",teleport_point= "from_map2")])
        self.register_map("map3",portals = [Portal(from_world="map3", origin_point="to_map1", to_world="map", teleport_point="from_map3")])
        self.register_map("map4",portals=[
            Portal(from_world="map4", origin_point="to_map1", to_world="map", teleport_point="from_map4")])
        self.register_map("map5", portals=[
            Portal(from_world="map5", origin_point="to_map1", to_world="map", teleport_point="from_map5")])
        self.register_map("small_house",portals= [Portal(from_world="small_house",origin_point = "to_map1", to_world = "map",teleport_point= "from_small_house")])
        self.register_map("house",portals=[Portal(from_world="house",origin_point = "exit_bib", to_world = "map",teleport_point= "spawn_from_bib")])


        self.teleport_player("spawn")

    def teleport_player(self, name):
        point = self.get_object(name)
        self.player.position[0] = point.x
        self.player.position[1] = point.y
        self.player.save_location()

    def check_collisions(self):
        for portal in self.get_map().portals:
            if portal.from_world == self.current_map:
                point = self.get_object(portal.origin_point)
                rect = pygame.Rect(point.x,point.y, point.width, point.height)
                if self.player.feet.colliderect(rect):
                    copy_portal = portal
                    self.current_map = portal.to_world
                    self.teleport_player(copy_portal.teleport_point)

        for sprite in self.get_group().sprites():
            if sprite.feet.collidelist(self.get_walls()) > -1:
                sprite.move_back()

    def register_map(self, name, portals=[]):
        tmx = pytmx.util_pygame.load_pygame(f'../maps/{name}.tmx')
        map = pyscroll.data.TiledMapData(tmx)
        map_layer = pyscroll.orthographic.BufferedRenderer(map, self.screen.get_size())
        map_layer.zoom = 2

        # collisions
        walls = []

        for object in tmx.objects:
            if object.type == "collision":
                walls.append(pygame.Rect(object.x, object.y, object.width, object.height))


        # draw layers
        group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        group.add(self.player)

        #Create an object
        self.maps[name] = Map(name,walls,group,tmx,portals)
    def get_map(self): return self.maps[self.current_map]

    def get_group(self): return self.get_map().group

    def get_walls(self): return self.get_map().walls

    def get_object(self, name): return self.get_map().tmx.get_object_by_name(name)

    def draw(self):
        self.get_group().draw(self.screen)
        self.get_group().center(self.player.rect.center)

    def update(self):
        self.get_group().update()
        self.check_collisions()


