class Champion:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.curr_xp = 0
        self.rem_xp = 1000
        self.equipment = []
        self.inventory = []
        self.actions = ["Skill", "Use item"]


class Tank(Champion):
    def __init__(self, name):
        super().__init__(name)
        self.hp = 500
        self.mp = 200
        self.max_hp = 500
        self.max_mp = 200
        self.skills = ["Lance attack", "Block"]


class Archer(Champion):
    def __init__(self, name):
        super().__init__(name)
        self.hp = 300
        self.mp = 200
        self.max_hp = 300
        self.max_mp = 200
        self.skills = ["Bow attack", "Arrow Volley"]


class Healer(Champion):
    def __init__(self, name):
        super().__init__(name)
        self.hp = 180
        self.mp = 400
        self.max_hp = 180
        self.max_mp = 400
        self.skills = ["Wand Attack", "Cure"]

