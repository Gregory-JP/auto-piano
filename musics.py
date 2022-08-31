import pyautogui as pg
from time import sleep

def asaBranca():
        notas = [71, 72, 74, 76, 76, 74, 75, 75,
                71, 72, 74, 76, 76, 75, 74,
                71, 71, 74, 72, 76, 76, 75, 74, 71, 75,
                74, 74, 72, 72, 74, 72, 72, 71, 71]

        notas = [chr(x) for x in notas]
        pg.hotkey('alt', 'tab')
        sleep(2)

        for x in notas:
                pg.sleep(0.3)
                pg.keyDown(x)
                pg.sleep(0.1)
                pg.keyUp(x)
        
        return True


def nonaSinfonia():
        notas = [74, 74, 75, 76, 76, 75, 74, 72, 71, 71, 72, 74, 74, 72, 72,
                74, 74, 75, 76, 76, 75, 74, 72, 71, 71, 72, 72, 72, 71, 71,
                72, 72, 74, 71, 72, 74, 75, 74, 71, 72, 74, 75, 74, 72, 71, 72, 76,
                74, 74, 75, 76, 76, 76, 75, 74, 72, 71, 71, 72, 74, 72, 71, 71]

        notas = [chr(x) for x in notas]
        pg.hotkey('alt', 'tab')
        sleep(2)

        for x in notas:
                pg.sleep(0.3)
                pg.keyDown(x)
                pg.sleep(0.1)
                pg.keyUp(x)
        
        return True



def choramAsRosas():
        notas = [85, 89, 84, 79, 89,
                89, 85, 74, 74, 74, 74, 80, 79, 74, 74, 85, 85,
                84, 89, 85, 79, 74, 85, 89, 79, 80, 79, 85, 74,
                85, 89, 85, 85, 84]

        notas = [chr(x) for x in notas]
        pg.hotkey('alt', 'tab')
        sleep(2)

        for x in notas:
                pg.sleep(0.3)
                pg.keyDown(x)
                pg.sleep(0.1)
                pg.keyUp(x)

        return True


def pauNoGato():
        notas = [71, 70, 68, 83, 68, 70, 71, 71, 71,
                72, 71, 70, 70, 70,
                71, 70, 68, 68, 68,
                70, 71, 72, 72, 72,
                74, 72, 71, 71, 71,
                68, 70, 71, 68, 70, 71, 71, 70, 68, 83, 65]

        notas = [chr(x) for x in notas]
        pg.hotkey('alt', 'tab')
        sleep(2)

        for x in notas:
                pg.sleep(0.3)
                pg.keyDown(x)
                pg.sleep(0.1)
                pg.keyUp(x)

        return True


def brasiliaAmarela():
        notas = [74, 79, 80, 79, 74, 80, 80,
                74, 79, 80, 79, 74, 59,
                59, 59, 59, 80, 74, 79, 79,
                80, 59, 59, 80, 80, 79, 74,
                74, 79, 80, 79, 74, 80, 80,
                74, 79, 80, 79, 74, 59, 59,
                59, 59, 59, 59, 80, 74, 79,
                80, 59, 80, 79, 79, 74]

        notas = [chr(x) for x in notas]
        pg.hotkey('alt', 'tab')
        sleep(2)

        for x in notas:
                pg.sleep(0.3)
                pg.keyDown(x)
                pg.sleep(0.1)
                pg.keyUp(x)

        return True


def hinoNacional():
        notas = [65, 70, 68, 70, 71, 72, 71, 72, 74, 74, 75, 70,
                65, 70, 68, 71, 70, 72, 71, 85, 72, 84, 71,
                83, 71, 84, 71, 72, 85, 72, 85, 75, 79, 76, 71,
                65, 71, 84, 72, 71, 85, 72, 75, 74, 89, 72,
                72, 72, 85, 72, 72, 85, 72, 72, 76,
                75, 75, 85, 85, 72, 72, 71, 71, 70, 70, 68, 68, 83,
                71, 71, 72, 71, 71, 72, 71, 71, 75,
                74, 72, 72, 71, 71, 70, 70, 68, 68, 83, 83, 65,
                65, 68, 71, 85,
                65, 68, 71, 85,
                65, 68, 71, 85, 85,
                65, 70, 68, 70, 71, 72, 71, 72, 74, 74, 75, 70,
                65, 70, 68, 71, 70, 72, 71, 85, 72, 84, 71,
                83, 71, 84, 71, 72, 85, 72, 85, 75, 79, 76, 71,
                83, 71, 70, 72, 71, 85, 72, 75, 85, 89, 72,
                70, 71, 70, 68, 70, 68, 70, 71, 70, 70, 85,
                71, 72, 71, 84, 71, 84, 71, 72, 72, 71, 71, 75,
                72, 85, 72, 71, 72, 89, 72, 85, 72, 72, 76,
                75, 85, 71, 71, 70,
                68, 70, 71, 85, 71, 68, 70, 83, 85, 85, 85, 71, 71, 70,
                71, 72, 85, 74, 75, 72, 70, 83, 85, 72,
                71, 70, 65, 83, 68, 70]

        notas = [chr(x) for x in notas]
        pg.hotkey('alt', 'tab')
        sleep(2)

        for x in notas:
                pg.sleep(0.3)
                pg.keyDown(x)
                pg.sleep(0.1)
                pg.keyUp(x)

        return True