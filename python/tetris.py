from threading import Thread
from threading import Event
import keyboard
import tkinter as tk
import random
from enum import Enum
import copy
import datetime

####### <MAIN CLASS> ########

class tetris():
    config = {
        "gameAreaSize": [10,18],
        "resolutions": [[160,144],[128,128]],
        "tileSizes": [[8,8],[4,4]],
        "tileResolutions": [[20,18],[16,16]],
        "console": False,
        "resolution": 0,
        "tileSize": 0,
        "scale": 3,
        "base64IntroScreen": ["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"],
        "gameClock": 0.01,
        "refreshRate": 60,
        "pieceDropScore": 5, # * level
        "lineScore": 10, # * lineCount * level
        "keyMapping": {
            "rotate": 'up',
            "moveRight": 'right',
            "drop": 'down',
            "moveLeft": 'left',
            "exit": 'esc',
            "start": 'shift'         
        }
    }

    gameStatus = {
        "isStarted": False,
        "isLost": False,
        "isPaused": False,
        "level": 0,
        "score": 0,
        "overlayText": [],
        "gameArray": [],
        "tetrominoe": {
            "type": None,
            "pos": 0,
            "state": 0
        },
        "nextTetrominoe": {
            "type": None,
            "pos": 0,
            "state": 0            
        }
    }

    commandBuffer = []

    ## Game threads ##
    backgroundKeyListenerThread = None
    backgroundGameLoopThread = None
    screenThread = None

    def __init__(self):
        self.initBackgroundLoopThread()

    def initBackgroundLoopThread(self):
        self.backgroundKeyListenerThread = backgroundKeyListener(Event(), self.config, self.gameStatus, self.commandBuffer)     
        self.backgroundGameLoopThread = backgroundGameLoop(Event(), self.config, self.gameStatus, self.commandBuffer) 

        self.backgroundKeyListenerThread.start()
        self.backgroundGameLoopThread.start()

        self.screenThread = screen(self.config, self.gameStatus, self.commandBuffer)

###### </MAIN CLASS> ########
###### <GAME THREADS> #######

class screen():
    TILE_MAP = ["noBlock","iBlock","jBlock","lBlock","oBlock","sBlock","tBlock","zBlock","marginBlock", "staticBlock"]
    _config = None
    _stopped = None

    blockColors = {
        "iBlock" : {
            "baseColor": "00FFFF",
            "brightColor": "FFFFFF",
            "darkColor": "00BBBB" 
        },
        "jBlock" : {
            "baseColor": "0000FF",
            "brightColor": "5555FF",
            "darkColor": "0000BB"
        },
        "lBlock" : {
            "baseColor": "FFAA00",
            "brightColor": "FFEEAA",
            "darkColor": "BB5500"
        },
        "oBlock" : {
            "baseColor": "FFFF00",
            "brightColor": "FFFFCC",
            "darkColor": "BBBB00"
        },
        "sBlock" : {
            "baseColor": "00FF00",
            "brightColor": "CCFFCC",
            "darkColor": "00BB00"
        },
        "tBlock" : {
            "baseColor": "9900FF",
            "brightColor": "C878FF",
            "darkColor": "4400BB"
        },
        "zBlock" : {
            "baseColor": "FF0000",
            "brightColor": "FFCCCC",
            "darkColor": "BB0000"
        },
        "marginBlock" : {
            "baseColor": "F0A080",
            "brightColor": "F0D0D0",
            "darkColor": "B05030"
        },
        "staticBlock" : {
            "baseColor": "CCCCCC",
            "brightColor": "777777",
            "darkColor": "FFFFFF" 
        },
        "noBlock" : {
            "baseColor": "141414",
            "brightColor": "3C3C50",
            "darkColor": "141414"
        }
    }

    gameStatus = None
    commandBuffer = None

    root = None
    context = None

    def __init__(self, config, gameStatus, commandBuffer):
        self._config = config
        self.context = None

        self.gameStatus = gameStatus
        self.commandBuffer = commandBuffer
  
        self.root = tk.Tk()
        self.root.title("Tetris")
    
        self.context = None

        self.gameCanvas = tk.Canvas(self.root, width=self._config['resolutions'][self._config['resolution']][0] * self._config['scale'], height=self._config['resolutions'][self._config['resolution']][1] * self._config['scale'])
        self.gameCanvas.pack()

        self.introScreenCanvas = tk.Canvas(self.root, width=self._config['resolutions'][self._config['resolution']][0] * self._config['scale'], height=self._config['resolutions'][self._config['resolution']][1] * self._config['scale'])
        self.introScreenCanvas.pack()
        self.scaledIntroScreen = None
    
        self.refresh()
        self.root.mainloop()

    def refresh(self):
        if self.gameStatus['isStarted']:
            if self.context is not self.gameCanvas:
                self.context = self.gameCanvas
                self.introScreenCanvas.pack_forget()
            self.drawScreen(self.buildScreen())
        else:
            if self.context is not self.introScreenCanvas:
                self.context = self.introScreenCanvas
                self.gameCanvas.pack_forget()
            self.drawScreen(None)

        self.root.after(int(round(1000/self._config['refreshRate'], 3)), self.refresh)
                
    def run(self):
        while not self._stopped.wait(round(1/self._config['refreshRate'], 4)):
            self.drawScreen(self.buildScreen())

    def getGameBlankScreen(self):
        emptyScreen = [8]*(self._config['tileResolutions'][self._config['resolution']][0]*self._config['tileResolutions'][self._config['resolution']][1])
        gameArea = [0]*(self._config['gameAreaSize'][0]*self._config['gameAreaSize'][1])

        newScreen = self.translateArray(gameArea, self._config['gameAreaSize'][0],
                                        emptyScreen, self._config['tileResolutions'][self._config['resolution']][0], 5, False)
        
        return newScreen

    def drawScreen(self, blockArray):
        self.context.delete("all")
        size = [self._config['tileSizes'][self._config['tileSize']][0] * self._config['scale'], self._config['tileSizes'][self._config['tileSize']][1] * self._config['scale']]
        
        if blockArray is not None:
            for index, block in enumerate(blockArray):
                x = (index % self._config['tileResolutions'][self._config['resolution']][0]) * size[0]
                y = (index // self._config['tileResolutions'][self._config['resolution']][0]) * size[1]

                self.drawTile([x,y], size, self.TILE_MAP[block])
        else:
            introScreen = tk.PhotoImage(data=self._config['base64IntroScreen'][0])

            self.scaledIntroScreen = introScreen.zoom(self._config['scale'], self._config['scale'])
            self.context.create_image(0, 0, anchor=tk.NW, image=self.scaledIntroScreen)           
        
        for text in self.gameStatus['overlayText']:
            self.drawOverlayText(text['position'][self._config['resolution']],
                self._config['tileSizes'][self._config['tileSize']], text['text'], text['color'])
            
        self.context.pack()      

    def drawTile(self, location, size, colorCode):
        baseColor = self.RGBtoColorCode(self.blockColors[colorCode]['baseColor'])
        brightColor = self.RGBtoColorCode(self.blockColors[colorCode]['brightColor'])
        darkColor = self.RGBtoColorCode(self.blockColors[colorCode]['darkColor'])
        self.context.create_rectangle(location[0], location[1], location[0]+size[0], location[1]+size[1], fill="#"+self.blockColors[colorCode]['baseColor'], outline="")

        self.context.create_line(location[0]+size[0]-1, location[1], location[0]+size[0]-1, location[1]+size[1], fill="#"+self.blockColors[colorCode]['darkColor'], width=1)
        self.context.create_line(location[0]+size[0]-2, location[1]+1, location[0]+size[0]-2, location[1]+size[1]-1, fill="#"+self.blockColors[colorCode]['darkColor'], width=1)
        self.context.create_line(location[0], location[1]-1, location[0]+size[0], location[1]-1, fill="#"+self.blockColors[colorCode]['darkColor'], width=1)
        self.context.create_line(location[0]+1, location[1]-2, location[0]+size[0]-2, location[1]-2, fill="#"+self.blockColors[colorCode]['darkColor'], width=1)

        self.context.create_line(location[0]+1, location[1], location[0]+1, location[1]+size[1], fill="#"+self.blockColors[colorCode]['brightColor'], width=1)
        self.context.create_line(location[0]+2, location[1]+1, location[0]+2, location[1]+size[1]-2, fill="#"+self.blockColors[colorCode]['brightColor'], width=1)
        self.context.create_line(location[0], location[1]+1, location[0]+size[0], location[1]+1, fill="#"+self.blockColors[colorCode]['brightColor'], width=1)
        self.context.create_line(location[0]+1, location[1]+2, location[0]+size[0]-2, location[1]+2, fill="#"+self.blockColors[colorCode]['brightColor'], width=1)

    def drawOverlayChar(self, location, charBitmap, color):
        for y, hex_value in enumerate(charBitmap):
            binary_value = bin(hex_value)[2:].zfill(8)  # Convierte a binario y rellena con ceros
            for x, bit in enumerate(binary_value[::-1]):
                if bit == '1':
                    scale = self._config['scale']
                    self.context.create_rectangle(location[0]+(x*scale), location[1]+(y*scale), location[0]+((x+1)*scale), location[1]+((y+1)*scale), fill=color, outline="")

    def drawOverlayText(self, screenPos, size, textArray, color="#FFFFFF"):
        charArray = []
        for char in textArray:
            if self._config['tileSize'] == 0:
                charArray.append(gameFont['_8x8'].value[char])
            if self._config['tileSize'] == 1:
                charArray.append(gameFont['_4x4'].value[char])

        for index, charBitman in enumerate(charArray):
            x = ((screenPos+index) % self._config['tileResolutions'][self._config['resolution']][0]) * size[0] * self._config['scale']
            y = ((screenPos+index) // self._config['tileResolutions'][self._config['resolution']][0]) * size[1] * self._config['scale']

            self.drawOverlayChar([x,y], charBitman, color)

    def RGBtoColorCode(self, RGB):
        return tuple(int(RGB[i:i+2], 16) for i in (0, 2, 4))

    def translateArray(self, sourceArray, sourceColumnNumber, destinationArray, destinationColumnNumber, pos, transparency):
        newArray = destinationArray
        for index, element in enumerate(sourceArray): 
            newPos = pos + (index % sourceColumnNumber) + ((index // sourceColumnNumber) * destinationColumnNumber)
            if newPos < len(newArray):
                if not transparency:
                    newArray[newPos] = element
                else:
                    if element != 0:
                        newArray[newPos] = element

        return newArray

    def traslateTetrominoeToGameArea(self):
        playedTetrominoeType = copy.copy(self.gameStatus['tetrominoe']['type'])
        if playedTetrominoeType is not None:
            playedTetrominoe = tetrominoe[playedTetrominoeType].value

            aTetrominoe = copy.copy(playedTetrominoe['state'][self.gameStatus['tetrominoe']['state']])
            for index, element in enumerate(aTetrominoe):
                if element > 0:
                    aTetrominoe[index] = 9
                      
        newGameArea = self.translateArray(aTetrominoe, playedTetrominoe['width'], 
                                          self.gameStatus['gameArray'], 
                                          self._config['gameAreaSize'][0],
                                          playedTetrominoe['pos'], True)
        
        self.gameStatus['gameArray'] = newGameArea

        self.gameStatus['tetrominoe'] = {
            "type": None,
            "pos": 0,
            "state": 0
        }

    def buildScreen(self):
        offLimitsScreen = [8]*(self._config['tileResolutions'][self._config['resolution']][0]*self._config['tileResolutions'][self._config['resolution']][1])
        
        screenColumns = self._config['tileResolutions'][self._config['resolution']][0]
        blankIndexes = [screenColumns+14,screenColumns+15,screenColumns+16,screenColumns+17,screenColumns+18,
                        (screenColumns*3)+14,(screenColumns*3)+15,(screenColumns*3)+16,(screenColumns*3)+17,(screenColumns*3)+18,
                        (screenColumns*4)+14,(screenColumns*4)+15,(screenColumns*4)+16,(screenColumns*4)+17,(screenColumns*4)+18,
                        (screenColumns*6)+14,(screenColumns*6)+15,(screenColumns*6)+16,(screenColumns*6)+17,(screenColumns*6)+18,
                        (screenColumns*7)+14,(screenColumns*7)+15,(screenColumns*7)+16,(screenColumns*7)+17,(screenColumns*7)+18]
        offLimitsScreen = [0 if index in blankIndexes else value for index, value in enumerate(offLimitsScreen)]
        gameArea = copy.copy(self.gameStatus['gameArray'])

        if self.gameStatus['nextTetrominoe']['type'] is not None:
            nextTetrominoeType = copy.copy(self.gameStatus['nextTetrominoe']['type'])
            nextTetrominoeState = copy.copy(self.gameStatus['nextTetrominoe']['state'])
            nextTetrominoePos = copy.copy(self.gameStatus['nextTetrominoe']['pos'])
            nextTetrominoeArray = copy.copy(tetrominoe[nextTetrominoeType].value['state'][nextTetrominoeState])
            nextTetrominoeWidth = copy.copy(tetrominoe[nextTetrominoeType].value['width'])

            offLimitsScreen = self.translateArray(nextTetrominoeArray, nextTetrominoeWidth,
                                    offLimitsScreen, self._config['tileResolutions'][self._config['resolution']][0], nextTetrominoePos, True)
        
        if self.gameStatus['tetrominoe']['type'] is not None:
            tetrominoeType = copy.copy(self.gameStatus['tetrominoe']['type'])
            tetrominoeState = copy.copy(self.gameStatus['tetrominoe']['state'])
            tetrominoePos = copy.copy(self.gameStatus['tetrominoe']['pos'])
            tetrominoeArray = copy.copy(tetrominoe[tetrominoeType].value['state'][tetrominoeState])
            tetrominoeWidth = copy.copy(tetrominoe[tetrominoeType].value['width'])

            gameArea = self.translateArray(tetrominoeArray, tetrominoeWidth,
                                        gameArea, self._config['gameAreaSize'][0], tetrominoePos, True)

        gameScreen = self.translateArray(gameArea, self._config['gameAreaSize'][0],
                                    offLimitsScreen, self._config['tileResolutions'][self._config['resolution']][0], 3, False)

        return gameScreen

class backgroundGameLoop(Thread):
    _exit = False
    _stopped = None

    ### GAME RULES ###
    # CPU will move every level
    # 1.0s - (level/10)

    cpuTurn = 1
    cpuReady = False
    cpuNextTurn = 0
    isGameOn = False
    hasPlayerLost = False
    isPaused = False
    fallingPiece = False

    gameStatus = None
    commandBuffer = []

    overlayTexts = {
        "score": {
            "text": ["S","c","o","r","e"],
            "position": [74,74],
            "color": "#FFFFFF" 
        },
        "level": {
            "text": ["L","v","l","colon"],
            "position": [34,34],
            "color": "#FFFFFF"
        },
        "levelNum": {
            "text": [""],
            "position": [38,38],
            "color": "#FFFFFF"
        },
        "scoreNum":  {
            "text": [""],
            "position": [94,94],
            "color": "#FFFFFF"
        },
        "pressStart":  {
            "text": ["P","R","E","S","S","space","S","T","A","R","T"],
            "position": [185,185],
            "color": "#FFFFFF"
        },
        "pause": {
            "text": ["P","A","U","S","E"],
            "position": [188,188],
            "color": "#FFFFFF"            
        },
        "gameOver":  {
            "text": ["G","A","M","E","space","O","V","E","R"],
            "position": [186,186],
            "color": "#FFFFFF"
        }
    }

    def __init__(self, event, config, gameStatus, commandBuffer):
        self._stopped = event

        self.config = config
        self.gameStatus = gameStatus
        self.commandBuffer = commandBuffer
        Thread.__init__(self)

    def run(self):
        self.globalLoop()

    def globalLoop(self):
        self.resetGameScreen()
        while not self._stopped.wait(self.config['gameClock']):
            if not self.gameStatus['isStarted']:
                overlayText = []
                currentTime = datetime.datetime.now()
                if (currentTime.second % 2) == 0:
                    overlayText.append(self.overlayTexts['pressStart'])            
                self.gameStatus['overlayText'] = overlayText

                while self.commandBuffer:
                    newCommand = self.commandBuffer.pop()
                    if newCommand is command.START:
                        self.gameStatus['isStarted'] = True         
            else:
                self.refreshLevel()
                self.setInGameTexts()

                if not self.gameStatus['isPaused'] and not self.gameStatus['isLost']:
                    if self.cpuReady:
                        self.cpuAction()

                        self.cpuReady = False
                        if self.gameStatus['level']<9:
                            self.cpuNextTurn = (1 - (self.gameStatus['level']/10))
                        else:
                            self.cpuNextTurn = 0.01
                    else:
                        if self.cpuNextTurn > 0:
                            self.cpuNextTurn -= self.config['gameClock']
                        else:
                            self.cpuReady = True
                self.playerAction()

    def setInGameTexts(self):
        overlayText = []
        overlayText.append(self.overlayTexts['score'])
        overlayText.append(self.overlayTexts['level'])

        overlayLevelNum = copy.copy(self.overlayTexts['levelNum'])
        overlayLevelNum['text'] = str(self.gameStatus['level'])
        overlayScoreNum = copy.copy(self.overlayTexts['scoreNum'])
        if self.gameStatus['score'] < 100000:
            overlayScoreNum['text'] = str(self.gameStatus['score']).zfill(5)
        else:
            overlayScoreNum['text'] = "99999"

        overlayText.append(overlayLevelNum)
        overlayText.append(overlayScoreNum)

        if self.gameStatus['isPaused']:
            currentTime = datetime.datetime.now()
            if (currentTime.second % 2) == 0:
                overlayText.append(self.overlayTexts['pause'])

        if self.gameStatus['isLost']:
            overlayText.append(self.overlayTexts['gameOver'])
        
        self.gameStatus['overlayText'] = overlayText

    def refreshLevel(self):
        # 100, 300, 600, 1000, 1500, 2100, 2800, 3600, 4500
        score = self.gameStatus['score']
        if score < 100:
            self.gameStatus['level'] = 0
        if score >= 100 and score < 300:
            self.gameStatus['level'] = 1
        if score >= 300 and score < 600:
            self.gameStatus['level'] = 2
        if score >= 600 and score < 1000:
            self.gameStatus['level'] = 3
        if score >= 1000 and score < 1500:
            self.gameStatus['level'] = 4
        if score >= 1500 and score < 2100:
            self.gameStatus['level'] = 5
        if score >= 2100 and score < 2800:
            self.gameStatus['level'] = 6
        if score >= 2800 and score < 3600:
            self.gameStatus['level'] = 7
        if score >= 3600 and score < 4500:
            self.gameStatus['level'] = 8
        if score >= 4500:
            self.gameStatus['level'] = 9

    def resetGameScreen(self):
        gameArea = [0]*(self.config['gameAreaSize'][0]*self.config['gameAreaSize'][1])
        self.gameStatus['gameArray'] = gameArea 

    def cpuAction(self):
        lineCount = self.countLines()
        if lineCount > 0:
            self.deleteLines()
            self.gameStatus['score'] += self.config['lineScore'] * lineCount * (self.gameStatus['level']+1)

        if self.gameStatus['tetrominoe']['type'] is None:
            self.getNewTetrominoe()
        else: 
            self.dropTetrominoe()

    def playerAction(self):
        while self.commandBuffer:
            newCommand = self.commandBuffer.pop()

            if newCommand is command.ROTATE and self.gameStatus['tetrominoe']['type'] is not None and not self.gameStatus['isPaused'] and not self.gameStatus['isLost']:
                self.playerSpinsTetrominoe()
            if newCommand is command.RIGHT and self.gameStatus['tetrominoe']['type'] is not None and not self.gameStatus['isPaused'] and not self.gameStatus['isLost']:
                self.playerMovesTetrominoe(True)
            if newCommand is command.LEFT and self.gameStatus['tetrominoe']['type'] is not None and not self.gameStatus['isPaused'] and not self.gameStatus['isLost']:
                self.playerMovesTetrominoe(False)
            if newCommand is command.DROP and self.gameStatus['tetrominoe']['type'] is not None and not self.gameStatus['isPaused'] and not self.gameStatus['isLost']:
                self.playerDropsTetrominoe()
            if newCommand is command.START:
                if not self.gameStatus['isLost']:
                    self.playerPauses()
                else:
                    self.playerRestarts()

    def newNextTetrominoe(self):
        self.gameStatus['nextTetrominoe']['type'] = list(tetrominoe)[random.randint(0, 6)].name
        self.gameStatus['nextTetrominoe']['pos'] = 135
        self.gameStatus['nextTetrominoe']['state'] = 0

    def getNewTetrominoe(self):
        if self.gameStatus['nextTetrominoe']['type'] is None:
            self.newNextTetrominoe()

        self.gameStatus['tetrominoe']['type'] = self.gameStatus['nextTetrominoe']['type']
        self.gameStatus['tetrominoe']['pos'] = 3
        self.gameStatus['tetrominoe']['state'] = 0

        self.newNextTetrominoe()

    def newTetrominoe(self):
        self.gameStatus['tetrominoe']['type'] = list(tetrominoe)[random.randint(0, 6)].name
        self.gameStatus['tetrominoe']['pos'] = 0
        self.gameStatus['tetrominoe']['state'] = 0

    def dropTetrominoe(self):
        newTetrominoe = copy.copy(self.gameStatus['tetrominoe'])
        newGameArea = copy.copy(self.gameStatus['gameArray'])
        newTetrominoe['pos'] += self.config['gameAreaSize'][0]

        if (self.detectColision(newGameArea, newTetrominoe) == False):
            self.gameStatus['tetrominoe'] = copy.copy(newTetrominoe)
        else:
            self.traslateTetrominoeToGameArea()
            self.gameStatus['score'] += self.config['pieceDropScore'] * (self.gameStatus['level']+1)
            if newTetrominoe['pos'] < (self.config['gameAreaSize'][0]*2):
                self.gameStatus['isLost'] = True

    def countLines(self):
        count = 0
        gameArea = self.gameStatus['gameArray']
        for row in range(self.config['gameAreaSize'][1]-1, 0, -1):
            if all(gameArea[i] == 0 for i in range(row*self.config['gameAreaSize'][0], (row*self.config['gameAreaSize'][0])+self.config['gameAreaSize'][0])):
                return count
            if all(gameArea[i] == 9 for i in range(row*self.config['gameAreaSize'][0], (row*self.config['gameAreaSize'][0])+self.config['gameAreaSize'][0])):
                count += 1
        return count

    def deleteLines(self):
        gameArea = copy.copy(self.gameStatus['gameArray'])
        arrayIndex = self.config['gameAreaSize'][1]-1
        while arrayIndex > 0:
            if all(gameArea[i] == 9 for i in range(arrayIndex*self.config['gameAreaSize'][0], (arrayIndex*self.config['gameAreaSize'][0])+self.config['gameAreaSize'][0])):
                for blockIndex in range(arrayIndex*self.config['gameAreaSize'][0]-1, 0, -1):
                    gameArea[blockIndex+self.config['gameAreaSize'][0]] = gameArea[blockIndex]
                for blockIndex in range(0, self.config['gameAreaSize'][0]):
                    gameArea[blockIndex] = 0
                arrayIndex+=1 
            arrayIndex-=1           
        self.gameStatus['gameArray'] = copy.copy(gameArea)       

    def playerMovesTetrominoe(self, isRight):
        newTetrominoe = copy.copy(self.gameStatus['tetrominoe'])
        newGameArea = copy.copy(self.gameStatus['gameArray'])
        if isRight:
            newTetrominoe['pos'] += 1
        else:
            newTetrominoe['pos'] -= 1

        ##### EXCEPTIONS #####

        exception = False
        if (newTetrominoe['type'] == 'I'):
            if newTetrominoe['state'] == 1:
                if isRight:
                    if newTetrominoe['pos']%self.config['gameAreaSize'][0] == 8:
                        exception = True
                else:
                    if newTetrominoe['pos']%self.config['gameAreaSize'][0] == 7:
                        exception = True
            elif newTetrominoe['state'] == 3:
                if isRight:
                    if newTetrominoe['pos']%self.config['gameAreaSize'][0] == 9:
                        exception = True
                else:
                    if newTetrominoe['pos']%self.config['gameAreaSize'][0] == 8:
                        exception = True
            else:
                pass

        ######################

        if (self.detectColision(newGameArea, newTetrominoe) == False and not exception):
            self.gameStatus['tetrominoe'] = copy.copy(newTetrominoe)

    def playerSpinsTetrominoe(self):
        newTetrominoe = copy.copy(self.gameStatus['tetrominoe'])
        newGameArea = copy.copy(self.gameStatus['gameArray'])
        newTetrominoe['state'] = ((newTetrominoe['state'] + 1) 
                                  % len(tetrominoe[newTetrominoe['type']].value['state']))

        if (self.detectColision(newGameArea, newTetrominoe) == False):
            self.gameStatus['tetrominoe'] = copy.copy(newTetrominoe)

    def playerDropsTetrominoe(self):
        newTetrominoe = copy.copy(self.gameStatus['tetrominoe'])
        newGameArea = copy.copy(self.gameStatus['gameArray'])

        while(self.detectColision(newGameArea, newTetrominoe) == False):
            newTetrominoe['pos'] += self.config['gameAreaSize'][0]

        newTetrominoe['pos'] -= self.config['gameAreaSize'][0]
        self.gameStatus['tetrominoe'] = copy.copy(newTetrominoe)
        self.traslateTetrominoeToGameArea()
        self.gameStatus['score'] += self.config['pieceDropScore'] * (self.gameStatus['level'] + 1)
        if newTetrominoe['pos'] < (self.config['gameAreaSize'][0]*2):
            self.gameStatus['isLost'] = True

    def playerPauses(self):
        self.gameStatus['isPaused'] = not self.gameStatus['isPaused']

    def playerRestarts(self):
        self.gameStatus['isStarted'] = False
        self.gameStatus['isLost'] = False
        self.gameStatus['isPaused'] = False
        self.gameStatus['level'] = 0
        self.gameStatus['score'] = 0
        self.gameStatus['overlayText'] = []
        self.gameStatus['gameArray'] = []
        self.gameStatus['tetrominoe']['type'] = None
        self.gameStatus['tetrominoe']['pos'] = 0
        self.gameStatus['tetrominoe']['state'] = 0
        self.gameStatus['nextTetrominoe']['type'] = None
        self.gameStatus['nextTetrominoe']['pos'] = 0
        self.gameStatus['nextTetrominoe']['state'] = 0
        self.resetGameScreen()

    def detectColision(self, newGameArea, newTetrominoe):
        sourceArray = tetrominoe[newTetrominoe['type']].value['state'][newTetrominoe['state']]
        sourceColumnNumber = tetrominoe[newTetrominoe['type']].value['width']
        destinationArray = newGameArea
        destinationColumnNumber = self.config['gameAreaSize'][0]
        pos = newTetrominoe['pos']

        blockList = []

        for index, element in enumerate(sourceArray):
            if element > 0:
                newPos = pos + (index % sourceColumnNumber) + ((index // sourceColumnNumber) * destinationColumnNumber)

                if newPos >= len(destinationArray):
                    return True
                if destinationArray[newPos] > 0:
                    return True
                for array in blockList:
                    if abs((newPos % destinationColumnNumber) - (array[1] % destinationColumnNumber)) > sourceColumnNumber:
                        return True
                blockList.append([index, newPos])
        return False
    
    def translateArray(self, sourceArray, sourceColumnNumber, destinationArray, destinationColumnNumber, pos, transparency):
        newArray = destinationArray
        for index, element in enumerate(sourceArray): 
            #if ((pos % destinationColumnNumber) + (index % sourceColumnNumber)) < destinationColumnNumber:
            newPos = pos + (index % sourceColumnNumber) + ((index // sourceColumnNumber) * destinationColumnNumber)
            if newPos < len(newArray):
                if not transparency:
                    newArray[newPos] = element
                else:
                    if element != 0:
                        newArray[newPos] = element  

        return newArray

    def traslateTetrominoeToGameArea(self):
        playedTetrominoeType = copy.copy(self.gameStatus['tetrominoe']['type'])
        if playedTetrominoeType is not None:
            playedTetrominoe = copy.copy(tetrominoe[playedTetrominoeType].value)
            TetrominoeInGame = copy.copy(self.gameStatus['tetrominoe'])

            aTetrominoe = copy.copy(playedTetrominoe['state'][self.gameStatus['tetrominoe']['state']])
            for index, element in enumerate(aTetrominoe):
                if element > 0:
                    aTetrominoe[index] = 9
                      
            newGameArea = self.translateArray(aTetrominoe, playedTetrominoe['width'], 
                                            self.gameStatus['gameArray'], 
                                            self.config['gameAreaSize'][0],
                                            TetrominoeInGame['pos'], True)  
            
            self.gameStatus['gameArray'] = newGameArea

            self.gameStatus['tetrominoe'] = {
                "type": None,
                "pos": 0,
                "state": 0
            }
        
class backgroundKeyListener(Thread):
    _exit = False
    _stopped = None
    _config = None
    _pressedKeys = [0,0,0,0]

    gameStatus = None
    commandBuffer = []

    def __init__(self, event, config, gameStatus, commandBuffer):
        self._stopped = event
        self._config = config

        self.gameStatus = gameStatus
        self.commandBuffer = commandBuffer
        Thread.__init__(self)

    def run(self):
        self.pressedKeys = [False,False,False,False,False,False]
        while not self._stopped.wait(self._config['gameClock']):
            if keyboard.is_pressed(self._config['keyMapping']['rotate']):
                if not self.pressedKeys[command['ROTATE'].value]:
                    self.pressedKeys[command['ROTATE'].value] = True 
                    self.commandBuffer.append(command.ROTATE)
            else:
                self.pressedKeys[command['ROTATE'].value] = False              

            if keyboard.is_pressed(self._config['keyMapping']['moveRight']):
                if not self.pressedKeys[command['RIGHT'].value]:
                    self.pressedKeys[command['RIGHT'].value] = True 
                    self.commandBuffer.append(command.RIGHT)
            else:
                self.pressedKeys[command['RIGHT'].value] = False

            if keyboard.is_pressed(self._config['keyMapping']['drop']):
                if not self.pressedKeys[command['DROP'].value]:
                    self.pressedKeys[command['DROP'].value] = True 
                    self.commandBuffer.append(command.DROP)
            else:
                self.pressedKeys[command['DROP'].value] = False              

            if keyboard.is_pressed(self._config['keyMapping']['moveLeft']):
                if not self.pressedKeys[command['LEFT'].value]:
                    self.pressedKeys[command['LEFT'].value] = True 
                    self.commandBuffer.append(command.LEFT)
            else:
                self.pressedKeys[command['LEFT'].value] = False 

            if keyboard.is_pressed(self._config['keyMapping']['start']):
                if not self.pressedKeys[command['START'].value]:
                    self.pressedKeys[command['START'].value] = True 
                    self.commandBuffer.append(command.START)
            else:
                self.pressedKeys[command['START'].value] = False 

            if keyboard.is_pressed(self._config['keyMapping']['exit']):
                if not self.pressedKeys[command['CANCEL'].value]:
                    self.pressedKeys[command['CANCEL'].value] = True 
                    self.commandBuffer.append(command.CANCEL)
            else:
                self.pressedKeys[command['CANCEL'].value] = False 

        print("Exiting...")

###### </GAME THREADS> ######
########## <ENUMS> ##########

class command(Enum):
    ROTATE = 0
    RIGHT = 1
    DROP = 2
    LEFT = 3
    START = 4
    CANCEL = 5

class tetrominoe(Enum):
    I = {
        "name": "I-Piece",
        "colorCode": "iBlock",
        "width": 4,
        "state": [[0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0],
        [0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0],
        [0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0],
        [0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0]] 
    }
    J = { 
       "name": "J-Piece",
       "colorCode": "jBlock",
       "width": 3,
       "state": [[2,0,0,2,2,2,0,0,0],
       [0,2,2,0,2,0,0,2,0],
       [0,0,0,2,2,2,0,0,2],
       [0,2,0,0,2,0,2,2,0]]
    }
    L = { 
       "name": "L-Piece",
       "colorCode": "lBlock",
       "width": 3,
       "state": [[0,0,3,3,3,3,0,0,0],
       [0,3,0,0,3,0,0,3,3],
       [0,0,0,3,3,3,3,0,0],
       [3,3,0,0,3,0,0,3,0]]
    }
    O = { 
       "name": "O-Piece",
       "colorCode": "oBlock",
       "width": 4,
       "state": [[0,4,4,0,0,4,4,0,0,0,0,0,0,0,0,0],
       [0,4,4,0,0,4,4,0,0,0,0,0,0,0,0,0],
       [0,4,4,0,0,4,4,0,0,0,0,0,0,0,0,0],
       [0,4,4,0,0,4,4,0,0,0,0,0,0,0,0,0]]
    }
    S = { 
       "name": "S-Piece",
       "colorCode": "sBlock",
       "width": 3,
       "state": [[0,5,5,5,5,0,0,0,0],
       [0,5,0,0,5,5,0,0,5],
       [0,0,0,0,5,5,5,5,0],
       [5,0,0,5,5,0,0,5,0]]
    }
    T = { 
       "name": "T-Piece",
       "colorCode": "tBlock",
       "width": 3,
       "state": [[0,6,0,6,6,6,0,0,0],
       [0,6,0,0,6,6,0,6,0],
       [0,0,0,6,6,6,0,6,0],
       [0,6,0,6,6,0,0,6,0]]
    }
    Z = { 
       "name": "Z-Piece",
       "colorCode": "zBlock",
       "width": 3,
       "state": [[7,7,0,0,7,7,0,0,0],
       [0,0,7,0,7,7,0,7,0],
       [0,0,0,7,7,0,0,7,7],
       [0,7,0,7,7,0,7,0,0]]
    }

class gameFont(Enum):
    _8x8 = {
        "space": [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
        "exclamation": [0x18, 0x3C, 0x3C, 0x18, 0x18, 0x00, 0x18, 0x00],
        "quotation": [0x36, 0x36, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
        "numberSign": [0x36, 0x36, 0x7F, 0x36, 0x7F, 0x36, 0x36, 0x00],
        "dollar": [0x0C, 0x3E, 0x03, 0x1E, 0x30, 0x1F, 0x0C, 0x00],
        "percent": [0x00, 0x63, 0x33, 0x18, 0x0C, 0x66, 0x63, 0x00],
        "ampersand": [0x1C, 0x36, 0x1C, 0x6E, 0x3B, 0x33, 0x6E, 0x00],
        "apostrophe": [0x06, 0x06, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00],
        "leftParenthesis": [0x18, 0x0C, 0x06, 0x06, 0x06, 0x0C, 0x18, 0x00],
        "rightParenthesis": [0x06, 0x0C, 0x18, 0x18, 0x18, 0x0C, 0x06, 0x00],
        "asterisk": [0x00, 0x66, 0x3C, 0xFF, 0x3C, 0x66, 0x00, 0x00],
        "plus": [0x00, 0x0C, 0x0C, 0x3F, 0x0C, 0x0C, 0x00, 0x00],
        "comma": [0x00, 0x00, 0x00, 0x00, 0x00, 0x0C, 0x0C, 0x06],
        "minus": [0x00, 0x00, 0x00, 0x3F, 0x00, 0x00, 0x00, 0x00],
        "fullStop": [0x00, 0x00, 0x00, 0x00, 0x00, 0x0C, 0x0C, 0x00],
        "solidus": [0x60, 0x30, 0x18, 0x0C, 0x06, 0x03, 0x01, 0x00],
        "0": [0x3E, 0x63, 0x73, 0x7B, 0x6F, 0x67, 0x3E, 0x00],
        "1": [0x0C, 0x0E, 0x0C, 0x0C, 0x0C, 0x0C, 0x3F, 0x00],
        "2": [0x1E, 0x33, 0x30, 0x1C, 0x06, 0x33, 0x3F, 0x00],
        "3": [0x1E, 0x33, 0x30, 0x1C, 0x30, 0x33, 0x1E, 0x00],
        "4": [0x38, 0x3C, 0x36, 0x33, 0x7F, 0x30, 0x78, 0x00],
        "5": [0x3F, 0x03, 0x1F, 0x30, 0x30, 0x33, 0x1E, 0x00],
        "6": [0x1C, 0x06, 0x03, 0x1F, 0x33, 0x33, 0x1E, 0x00],
        "7": [0x3F, 0x33, 0x30, 0x18, 0x0C, 0x0C, 0x0C, 0x00],
        "8": [0x1E, 0x33, 0x33, 0x1E, 0x33, 0x33, 0x1E, 0x00],
        "9": [0x1E, 0x33, 0x33, 0x3E, 0x30, 0x18, 0x0E, 0x00],
        "colon": [0x00, 0x0C, 0x0C, 0x00, 0x00, 0x0C, 0x0C, 0x00],
        "semicolon": [0x00, 0x0C, 0x0C, 0x00, 0x00, 0x0C, 0x0C, 0x06],
        "lessThan": [0x18, 0x0C, 0x06, 0x03, 0x06, 0x0C, 0x18, 0x00],
        "equal": [0x00, 0x00, 0x3F, 0x00, 0x00, 0x3F, 0x00, 0x00],
        "greaterThan": [0x06, 0x0C, 0x18, 0x30, 0x18, 0x0C, 0x06, 0x00],
        "questionMark": [0x1E, 0x33, 0x30, 0x18, 0x0C, 0x00, 0x0C, 0x00],
        "at": [0x3E, 0x63, 0x7B, 0x7B, 0x7B, 0x03, 0x1E, 0x00],
        "A": [0x0C, 0x1E, 0x33, 0x33, 0x3F, 0x33, 0x33, 0x00],
        "B": [0x3F, 0x66, 0x66, 0x3E, 0x66, 0x66, 0x3F, 0x00],
        "C": [0x3C, 0x66, 0x03, 0x03, 0x03, 0x66, 0x3C, 0x00],
        "D": [0x1F, 0x36, 0x66, 0x66, 0x66, 0x36, 0x1F, 0x00],
        "E": [0x7F, 0x46, 0x16, 0x1E, 0x16, 0x46, 0x7F, 0x00],
        "F": [0x7F, 0x46, 0x16, 0x1E, 0x16, 0x06, 0x0F, 0x00],
        "G": [0x3C, 0x66, 0x03, 0x03, 0x73, 0x66, 0x7C, 0x00],
        "H": [0x33, 0x33, 0x33, 0x3F, 0x33, 0x33, 0x33, 0x00],
        "I": [0x1E, 0x0C, 0x0C, 0x0C, 0x0C, 0x0C, 0x1E, 0x00],
        "J": [0x78, 0x30, 0x30, 0x30, 0x33, 0x33, 0x1E, 0x00],
        "K": [0x67, 0x66, 0x36, 0x1E, 0x36, 0x66, 0x67, 0x00],
        "L": [0x0F, 0x06, 0x06, 0x06, 0x46, 0x66, 0x7F, 0x00],
        "M": [0x63, 0x77, 0x7F, 0x7F, 0x6B, 0x63, 0x63, 0x00],
        "N": [0x63, 0x67, 0x6F, 0x7B, 0x73, 0x63, 0x63, 0x00],
        "O": [0x1C, 0x36, 0x63, 0x63, 0x63, 0x36, 0x1C, 0x00],
        "P": [0x3F, 0x66, 0x66, 0x3E, 0x06, 0x06, 0x0F, 0x00],
        "Q": [0x1E, 0x33, 0x33, 0x33, 0x3B, 0x1E, 0x38, 0x00],
        "R": [0x3F, 0x66, 0x66, 0x3E, 0x36, 0x66, 0x67, 0x00],
        "S": [0x1E, 0x33, 0x07, 0x0E, 0x38, 0x33, 0x1E, 0x00],
        "T": [0x3F, 0x2D, 0x0C, 0x0C, 0x0C, 0x0C, 0x1E, 0x00],
        "U": [0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x3F, 0x00],
        "V": [0x33, 0x33, 0x33, 0x33, 0x33, 0x1E, 0x0C, 0x00],
        "W": [0x63, 0x63, 0x63, 0x6B, 0x7F, 0x77, 0x63, 0x00],
        "X": [0x63, 0x63, 0x36, 0x1C, 0x1C, 0x36, 0x63, 0x00],
        "Y": [0x33, 0x33, 0x33, 0x1E, 0x0C, 0x0C, 0x1E, 0x00],
        "Z": [0x7F, 0x63, 0x31, 0x18, 0x4C, 0x66, 0x7F, 0x00],
        "leftBracket": [0x1E, 0x06, 0x06, 0x06, 0x06, 0x06, 0x1E, 0x00],
        "reverseSolidus": [0x03, 0x06, 0x0C, 0x18, 0x30, 0x60, 0x40, 0x00],
        "rightBracket": [0x1E, 0x18, 0x18, 0x18, 0x18, 0x18, 0x1E, 0x00],
        "circumflex": [0x08, 0x1C, 0x36, 0x63, 0x00, 0x00, 0x00, 0x00],
        "lowLine": [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF],
        "graveAccent": [0x0C, 0x0C, 0x18, 0x00, 0x00, 0x00, 0x00, 0x00],
        "a": [0x00, 0x00, 0x1E, 0x30, 0x3E, 0x33, 0x6E, 0x00],
        "b": [0x07, 0x06, 0x06, 0x3E, 0x66, 0x66, 0x3B, 0x00],
        "c": [0x00, 0x00, 0x1E, 0x33, 0x03, 0x33, 0x1E, 0x00],
        "d": [0x38, 0x30, 0x30, 0x3e, 0x33, 0x33, 0x6E, 0x00],
        "e": [0x00, 0x00, 0x1E, 0x33, 0x3f, 0x03, 0x1E, 0x00],
        "f": [0x1C, 0x36, 0x06, 0x0f, 0x06, 0x06, 0x0F, 0x00],
        "g": [0x00, 0x00, 0x6E, 0x33, 0x33, 0x3E, 0x30, 0x1F],
        "h": [0x07, 0x06, 0x36, 0x6E, 0x66, 0x66, 0x67, 0x00],
        "i": [0x0C, 0x00, 0x0E, 0x0C, 0x0C, 0x0C, 0x1E, 0x00],
        "j": [0x30, 0x00, 0x30, 0x30, 0x30, 0x33, 0x33, 0x1E],
        "k": [0x07, 0x06, 0x66, 0x36, 0x1E, 0x36, 0x67, 0x00],
        "l": [0x0E, 0x0C, 0x0C, 0x0C, 0x0C, 0x0C, 0x1E, 0x00],
        "m": [0x00, 0x00, 0x33, 0x7F, 0x7F, 0x6B, 0x63, 0x00],
        "n": [0x00, 0x00, 0x1F, 0x33, 0x33, 0x33, 0x33, 0x00],
        "o": [0x00, 0x00, 0x1E, 0x33, 0x33, 0x33, 0x1E, 0x00],
        "p": [0x00, 0x00, 0x3B, 0x66, 0x66, 0x3E, 0x06, 0x0F],
        "q": [0x00, 0x00, 0x6E, 0x33, 0x33, 0x3E, 0x30, 0x78],
        "r": [0x00, 0x00, 0x3B, 0x6E, 0x66, 0x06, 0x0F, 0x00],
        "s": [0x00, 0x00, 0x3E, 0x03, 0x1E, 0x30, 0x1F, 0x00],
        "t": [0x08, 0x0C, 0x3E, 0x0C, 0x0C, 0x2C, 0x18, 0x00],
        "u": [0x00, 0x00, 0x33, 0x33, 0x33, 0x33, 0x6E, 0x00],
        "v": [0x00, 0x00, 0x33, 0x33, 0x33, 0x1E, 0x0C, 0x00],
        "w": [0x00, 0x00, 0x63, 0x6B, 0x7F, 0x7F, 0x36, 0x00],
        "x": [0x00, 0x00, 0x63, 0x36, 0x1C, 0x36, 0x63, 0x00],
        "y": [0x00, 0x00, 0x33, 0x33, 0x33, 0x3E, 0x30, 0x1F],
        "z": [0x00, 0x00, 0x3F, 0x19, 0x0C, 0x26, 0x3F, 0x00],
        "leftCurlyBracket": [0x38, 0x0C, 0x0C, 0x07, 0x0C, 0x0C, 0x38, 0x00],
        "verticalLine": [0x18, 0x18, 0x18, 0x00, 0x18, 0x18, 0x18, 0x00],
        "rightCurlyBracket": [0x07, 0x0C, 0x0C, 0x38, 0x0C, 0x0C, 0x07, 0x00],
        "tilde": [0x6E, 0x3B, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
    }
    _4x4 = {

    }

######### </ENUMS> ##########

tetris()