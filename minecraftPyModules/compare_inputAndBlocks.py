def compareInputAndBlocks(userinput):
    USERINPUT = userinput.upper() # 사용자가 입력한 문자열을 전부 대문자로 변경함

    listBlockName = ['AIR', 'STONE', 'GRASS', 'DIRT', 'COBBLESTONE',
                     'WOOD_PLANKS', 'SAPLING', 'BEDROCK', 'WATER_FLOWING', 'WATER',
                     'WATER_STATIONARY', 'LAVA_FLOWING', 'LAVA', 'LAVA_STATIONARY', 'SAND',
                     'GRAVEL', 'GOLD_ORE', 'IRON_ORE', 'COAL_ORE', 'WOOD',
                     'LEAVES', 'GLASS', 'LAPIS_LAZULI_ORE', 'LAPIS_LAZULI_BLOCK', 'SANDSTONE',
                     'BED', 'COBWEB', 'GRASS_TALL', 'WOOL', 'FLOWER_YELLOW',
                     'FLOWER_CYAN', 'MUSHROOM_BROWN', 'MUSHROOM_RED', 'GOLD_BLOCK', 'IRON_BLOCK',
                     'STONE_SLAB_DOUBLE', 'STONE_SLAB', 'BRICK_BLOCK', 'TNT', 'BOOKSHELF',
                     'MOSS_STONE', 'OBSIDIAN', 'TORCH', 'FIRE', 'STAIRS_WOOD',
                     'CHEST', 'DIAMOND_ORE', 'DIAMOND_BLOCK', 'CRAFTING_TABLE', 'FARMLAND',
                     'FURNACE_INACTIVE', 'FURNACE_ACTIVE', 'DOOR_WOOD', 'LADDER', 'STAIRS_COBBLESTONE',
                     'DOOR_IRON', 'REDSTONE_ORE', 'SNOW', 'ICE', 'SNOW_BLOCK',
                     'CACTUS', 'CLAY', 'SUGAR_CANE', 'FENCE', 'GLOWSTONE_BLOCK',
                     'BEDROCK_INVISIBLE', 'STONE_BRICK', 'GLASS_PANE', 'MELON', 'FENCE_GATE',
                     'GLOWING_OBSIDIAN', 'NETHER_REACTOR_CORE', 'PAINTING', 'STONE_STAIRS', 'OAK_STAIRS',
                     'OAK_STAIRS', 'NETHERRACK', 'TRAPDOOR', 'MELON_SEEDS', 'BRICK_STAIRS',
                     'SANDSTONE_STAIRS', 'STONE_BRICK_STAIRS', 'NETHER_BRICK', 'NETHER_BRICK_STAIRS',
                     'QUARTZ_BLOCK', 'QUARTZ_STAIRS', 'STONE_CUTTER', 'BONE_MEAL']
    listBlockCode = [0, 1, 2, 3, 4,
                     5, 6, 7, 8, 8,
                     9, 10, 10, 11, 12,
                     13, 14, 15, 16, 17,
                     18, 20, 21, 22, 24,
                     26, 30, 31, 35, 37,
                     38, 39, 40, 41, 42,
                     43, 44, 45, 46, 47,
                     48, 49, 50, 51, 53,
                     54, 56, 57, 58, 60,
                     61, 62, 64, 65, 67,
                     71, 73, 78, 79, 80,
                     81, 82, 83, 85, 89,
                     95, 98, 102, 103, 107,
                     246, 247, 321, 67, 53,
                     59, 87, 96, 105, 108,
                     128, 109, 112, 114, 155,
                     156, 245, 351]

    compareList = 0 # 특정 조건이 되면 멈출 수 있도록 + 해당 숫자가 리스트의 인덱스 역할을 함.

    while compareList <= len(listBlockName): # 리스트의 전체 갯수만큼 while 문을 반복

        # 사용자가 입력한 문자열과 리스트 내부의 문자열 중 일치하는 것이 생기면
        if USERINPUT == listBlockName[compareList]:
            return listBlockCode[compareList] # 해당 리스트 인덱스 값의 코드 값을 리턴

        compareList = compareList + 1
