
class Game:

    def __init__(self):
        self.rect_collisions = {}
        self.num_rect = 0
        self.rect_position_x = {}
        self.rect_position_y = {}

    def rect_collide(self):
        for line in range(0, 3):
            for rect in range(0, 3):
                self.num_rect += 1
                self.rect_collisions[self.num_rect] = 133 * rect, 133 * line, 134, 134
                self.rect_position_x[self.num_rect] = 133 * rect + 66.5
                self.rect_position_y[self.num_rect] = 133 * line + 66.5
        self.num_rect = 0
        print(self.rect_collisions)
