from Object import * 
from functions import *

class HollowStone(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size, "hollow_stone")
        hollow_stone = get_hollow_stone(size)
        self.image.blit(hollow_stone, (0,0))
        self.mask = pygame.mask.from_surface(self.image)

class Box(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size, "box")
        box = get_box(size)
        self.image.blit(box, (0,0))
        self.mask = pygame.mask.from_surface(self.image)


class PortalBlock(Object): 
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size, "portal_block")
        portal_block = get_portal_block(size)
        self.image.blit(portal_block, (0,0))
        self.mask = pygame.mask.from_surface(self.image)

class Terrain(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size, "terrain")
        terrain = get_terrain(size)
        self.image.blit(terrain, (0,0))
        self.mask = pygame.mask.from_surface(self.image)

class NetherTerrain(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size, "nether_terrain")
        nether_terrain = get_nether_terrain(size)
        self.image.blit(nether_terrain, (0,0))
        self.mask = pygame.mask.from_surface(self.image)

class PinkTerrain(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size, "pink_terrain")
        pink_terrain = get_pink_terrain(size)
        self.image.blit(pink_terrain, (0,0))
        self.mask = pygame.mask.from_surface(self.image)

class ClayWall(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size, "clay_wall")
        clay_wall = get_clay_wall(size)
        self.image.blit(clay_wall, (0,0))
        self.mask = pygame.mask.from_surface(self.image)

class StoneWall(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size, "stone_wall")
        stone_wall = get_stone_wall(size)
        self.image.blit(stone_wall, (0,0))
        self.mask = pygame.mask.from_surface(self.image)

class OrangeWall(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size, "orange_wall")
        orange_wall = get_orange_wall(size)
        self.image.blit(orange_wall, (0,0))
        self.mask = pygame.mask.from_surface(self.image)

class Bricks(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size, "bricks")
        bricks = get_bricks(size)
        self.image.blit(bricks, (0,0))
        self.mask = pygame.mask.from_surface(self.image)

class GoldWall(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size, "gold_wall")
        gold_wall = get_gold_wall(size)
        self.image.blit(gold_wall, (0,0))
        self.mask = pygame.mask.from_surface(self.image)


#Functions the classes rely on
def get_hollow_stone(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(0, 0, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

def get_box(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(0, 64, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

def get_portal_block(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(0, 128, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

def get_terrain(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(96, 0, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

def get_nether_terrain(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(96, 64, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

def get_pink_terrain(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(96, 128, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

def get_clay_wall(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(192, 0, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

def get_stone_wall(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(192, 64, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

def get_orange_wall(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(192, 128, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)


def get_bricks(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(272, 64, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

def get_gold_wall(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(272, 128, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)