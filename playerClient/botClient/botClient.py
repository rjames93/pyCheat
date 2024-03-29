import asyncio
import websockets

class Player():

    def __init__(self,  playerNumber, uri="ws://localhost:8765"):
        # Set important variables
        self.uri = uri
        self.playerNumber = playerNumber
        
        # Try register the player with the server
        if ( asyncio.run( registerPlayer() ) == False ):
            print("Init of Player Failed")
            return
        
        # So we have registered as Player {playerNumber} so we are done for now :)
        
    async def registerPlayer(self):
        async with websockets.connect(uri) as websocket:
            
            registerMessage = "I want to be Player {}".format(playerNumber)
            
            await websocket.send(registerMessage)
            
            reply = await websocket.recv()
            if (reply == "okay"):
                return True
            else:
                return False