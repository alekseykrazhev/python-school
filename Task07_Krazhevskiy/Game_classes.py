class Warrior:
    def __init__(self, health=30, attack=5):
        self.health = health
        self.attack = attack

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    is_alive = property(is_alive)

    def hit(self, enemy, enemy1=None):
        if isinstance(enemy, Mage):
            if self.attack > enemy.magic:
                enemy.health -= self.attack - enemy.magic
        else:
            enemy.health -= self.attack

    def fight(self, opponent, next_opponent=None):
        if not self.is_alive:
            return False

        if not opponent.is_alive:
            return True

        while self.is_alive and opponent.is_alive:
            self.hit(opponent, next_opponent)
            if not opponent.is_alive:
                return True
            opponent.hit(self, next_opponent)
            if not self.is_alive:
                return False

    def __str__(self):
        return f"Warrior: health = {self.health}, attack = {self.attack}"

    def __add__(self, num):
        self.health += num
        self.attack += num
        return self

    def __mul__(self, num):
        self.health *= num
        self.attack *= num
        return self


class Fighter(Warrior):
    def __init__(self):
        super().__init__(30, 7)

    def __str__(self):
        return f"Fighter: health = {self.health}, attack = {self.attack}"


class Army:
    def __init__(self):
        self.army = []

    def add_members(self, n, type_of_warrior):
        for i in range(n):
            temp = type_of_warrior()
            self.army.append(temp)

    def __str__(self):
        return f"Army: {[str(i) for i in self.army]}"

    def __add__(self, num):
        for i in self.army:
            i.attack += num
            i.health += num
        return self

    def __mul__(self, num):
        for i in self.army:
            i.attack *= num
            i.health *= num
        return self


class Battle:
    def __init__(self):
        self.winner = None

    def fight(self, player1, player2):
        while len(player1.army) > 0 and len(player2.army) > 0:
            next_ = None
            if player2.army[0]:
                next_ = player2.army[0]
            if player1.army[0].fight(player2.army[0], next_):
                del player2.army[0]
            else:
                del player1.army[0]

        if len(player1.army) > 0:
            self.winner = player1
            return True
        else:
            self.winner = player2
            return False

    def __str__(self):
        return f"Winner: {self.winner}"


class Mage(Warrior):
    def __init__(self):
        super().__init__(40, 3)
        self.magic = 6

    def hit(self, enemy, enemy1=None):
        if enemy.attack < self.magic:
            enemy.health -= self.attack + self.magic
        else:
            enemy.health -= self.attack

    def __str__(self):
        return f"Mage: health = {self.health}, attack = {self.attack}, magic = {self.magic}"


class Paladin(Warrior):
    def __init__(self):
        super().__init__(50, 6)

    def hit(self, enemy, enemy1=None):
        enemy.health -= self.attack
        enemy1.health -= 0.5 * self.attack

    def __str__(self):
        return f"Paladin: health = {self.health}, attack = {self.attack}"


# tests for classes
if __name__ == '__main__':
    first = Warrior()
    second = Warrior()

    print(f"second vs first: {second.fight(first)}")
    print("is first alive: ", first.is_alive)
    print("is second alive: ", second.is_alive)

    print(f"first vs second: {first.fight(second)}")
    print("is first alive: ", first.is_alive)
    print("is second alive: ", second.is_alive)

    army1 = Army()
    army2 = Army()

    army1.add_members(15, Warrior)
    army2.add_members(10, Mage)
    army1.add_members(9, Paladin)

    battle = Battle()

    print(f"Battle result: {battle.fight(army2, army1)}")

    print(f"Before adding 2: {first}")
    first = first + 2
    print(f"After: {first}")

    print(f"Before multiplication by 5 : {second}")
    second = second * 5
    print(f"After: {second}")

    print(f"Before adding 2: {battle.winner}")
    battle.winner += 2
    print(f"After: {battle.winner}")

    print(f"Before multiplication by 5 : {battle.winner}")
    battle.winner *= 5
    print(f"After: {battle.winner}")

