from xml.dom.minidom import Element

def update_cell(values):
    for i, value in enumerate(values, start=1):
        Element(f"pos-{i}-x").add_class("hidden")
        Element(f"pos-{i}-o").add_class("hidden")
        Element(f"pos-{i}-none").add_class("hidden")
    if value == 0:
        Element(f"pos-{i}-x").remove_class("hidden")
    elif value == 1:
        Element(f"pos-{i}-o").remove_class("hidden")
    else:
        Element(f"pos-{i}-none").remove_class("hidden")

def display_message(value):
    Element("message").write(value)

class TicTocToe:
    def start(self):
        self.player = 0
        self.cells = [None] * 9
        self.game_running = True
        display_message("X Turn")
        update_cell(self.cells)

    def play_turn(self, position):
        if not self.game_running:
            return
        if self.cells[position] == None:
            display_message("Invalid position")
            return