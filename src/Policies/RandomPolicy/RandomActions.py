import random


class RandomActions:
    # Ideas of actions : Attack, Block

    def __init__(self, agent):
        self.agent = agent
        self.enemy_coord = []

    @staticmethod
    def random_pos(size):
        return random.randint(0, size), random.randint(0, size)

    def random_around_enemy(self, x, y):
        if x != 0:
            x -= 1
        else:
            x = 0
        if y != 0:
            y -= 1
        else:
            y = 0

        pos = random.randint(x, x + 1), random.randint(y, y + 1)
        while self.agent.is_pos_free(pos) is not True:
            pos = random.randint(x, x + 1), random.randint(y, y + 1)
        self.agent.place_piece(pos, 2)
        return pos

    def random_move(self):
        map_size = self.agent.map_size
        pos = self.random_pos(map_size)
        while self.agent.is_pos_free(pos) is not True:
            pos = self.random_pos(map_size - 1)
        self.agent.place_piece(pos, 2)
        return pos
