
# Exercises

[Getting Started with Minecraft on Raspberry Pi](https://www.raspberrypi.org/learning/getting-started-with-minecraft-pi/)

## Hello World

```
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

mc.postToChat("Hello world")
```

## Teleport

```
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x, y, z = mc.player.getPos()
mc.player.setPos(x, y+100, z)
```

## Create block

```
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

stone = 1
x, y, z = mc.player.getPos()
mc.setBlock(x+1, y, z, stone)
```

## Create blocks

```
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

lava_stationary = 11
x, y, z = mc.player.getPos()
mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, lava_stationary)
```

## Create shapes

```
from mcpi.minecraft import Minecraft
from mcpi.minecraftstuff import MinecraftDrawing
mc = Minecraft.create()
drawing = MinecraftDrawing(mc)

x, y, z = mc.player.getPos()
obsidian = 49
radius = 20
drawing.drawCircle(x, y, z, radius, obsidian)
drawing.drawHorizontalCircle(x, y, z, radius, obsidian)
```

## Path of destruction

```
from mcpi import minecraft
mc = minecraft.Minecraft.create()
tnt = 46

while True:
  x, y, z = mc.player.getPos()
  block_beneath = mc.getBlock(x, y-1, z)
  if block_beneath != tnt:
    mc.setBlock(x, y-1, z, tnt)

  sleep(0.1)
```

# Reference

Not a complete reference. See also:

[mcpi Reference (primary minecraft api)](http://www.stuffaboutcode.com/p/minecraft-api-reference.html)

[mcpi.minecraftstuff API reference (drawing and other utility methods)](https://github.com/martinohanlon/mcpi/blob/master/mcpi/minecraftstuff.py)

## Methods in Minecraft

```
getBlock(x, y, z)

getBlockWithData(x, y, z)

getBlocks(x0, y0, z0, x1, y1, z1)

setBlock(x, y, z, block_id, block_data)

setBlocks(x0, y0, z0, x1, y1, z1, block_id, block_data)

getHeight(world_x, world_z)

getPlayerEntityIds()

saveCheckpoint()

restoreCheckpoint()

postToChat(msg)

setting(setting, status)
```

## Methods in MinecraftDrawing

```
drawPoint3d(x, y, z, blockType, blockData=0)

drawFace(vertices, filled, blockType, blockData=0)
    
drawVertices(vertices, blockType, blockData=0)

drawLine(x1, y1, z1, x2, y2, z2, blockType, blockData=0)

drawSphere(x1, y1, z1, radius, blockType, blockData=0)

drawCircle(x0, y0, z, radius, blockType, blockData=0)

drawHorizontalCircle(x0, y, z0, radius, blockType, blockData=0)
```

## Block IDs

```
AIR                 0
STONE               1
GRASS               2
DIRT                3
COBBLESTONE         4
WOOD_PLANKS         5
SAPLING             6
BEDROCK             7
WATER_FLOWING       8
WATER_STATIONARY    9
LAVA_FLOWING        10
LAVA_STATIONARY     11
SAND                12
GRAVEL              13
GOLD_ORE            14
IRON_ORE            15
COAL_ORE            16
WOOD                17
LEAVES              18
GLASS               20
LAPIS_LAZULI_ORE    21
LAPIS_LAZULI_BLOCK  22
SANDSTONE           24
BED                 26
COBWEB              30
GRASS_TALL          31
WOOL                35
FLOWER_YELLOW       37
FLOWER_CYAN         38
MUSHROOM_BROWN      39
MUSHROOM_RED        40
GOLD_BLOCK          41
IRON_BLOCK          42
STONE_SLAB_DOUBLE   43
STONE_SLAB          44
BRICK_BLOCK         45
TNT                 46
BOOKSHELF           47
MOSS_STONE          48
OBSIDIAN            49
TORCH               50
FIRE                51
STAIRS_WOOD         53
CHEST               54
DIAMOND_ORE         56
DIAMOND_BLOCK       57
CRAFTING_TABLE      58
FARMLAND            60
FURNACE_INACTIVE    61
FURNACE_ACTIVE      62
DOOR_WOOD           64
LADDER              65
STAIRS_COBBLESTONE  67
DOOR_IRON           71
REDSTONE_ORE        73
SNOW                78
ICE                 79
SNOW_BLOCK          80
CACTUS              81
CLAY                82
SUGAR_CANE          83
FENCE               85
GLOWSTONE_BLOCK     89
BEDROCK_INVISIBLE   95
STONE_BRICK         98
GLASS_PANE          102
MELON               103
FENCE_GATE          107
GLOWING_OBSIDIAN    246
NETHER_REACTOR_CORE 247
```

## Block Data

**WOOL:**

```
0: White
1: Orange
2: Magenta
3: Light Blue
4: Yellow
5: Lime
6: Pink
7: Grey
8: Light grey
9: Cyan
10: Purple
11: Blue
12: Brown
13: Green
14: Red
15: Black
```

**WOOD:**

```
0: Oak (up/down)
1: Spruce (up/down)
2: Birch (up/down)
```

**SAPLING:**

```
0: Oak
1: Spruce
2: Birch
```

**GRASS_TALL:**

```
0: Shrub
1: Grass
2: Fern
```

**TORCH:**

```
1: Pointing east
2: Pointing west
3: Pointing south
4: Pointing north
5: Facing up
```

**STONE_BRICK:**

```
0: Stone brick
1: Mossy stone brick
2: Cracked stone brick
3: Chiseled stone brick
```

**STONE_SLAB / STONE_SLAB_DOUBLE:**

```
0: Stone
1: Sandstone
2: Wooden
3: Cobblestone
4: Brick
5: Stone Brick
```

