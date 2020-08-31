import requests, time, os

#### AUTHOR // DEVITY
#### DESCRIPTION // DMs all your friends on alt (make sure full verified)

UserChannelsAPI = "users/@me/channels"
SendMessageAPI = "v8/channels/{}/messages" 



class API:

    def __init__(self, Token:str):

        self.BASEURL = "https://discord.com/api/"
        self.headers = {'authorization' : Token}

        self.req = requests.session()

        self.ChannelIDs = []

        chan_req = requests.get(self.BASEURL+UserChannelsAPI, headers=self.headers)

        for x in list(chan_req.json()):
            self.ChannelIDs.append(x)

    def Message(self, content:str):

        data = {"content":content,"tts":False}
        
        for x in self.ChannelIDs:
            message_req = self.req.post(self.BASEURL+SendMessageAPI.format(x["id"]), headers=self.headers, json=data)

            

            if message_req.status_code == 429:
                time.sleep(10)
            elif message_req.status_code == 200:
                print("[$] Sent {}".format(str(x["id"])))
                


        
def Main():
    print("[$] Enter Token")
    Token = input()
    
    print("[$] Enter Content To Send.")
    Content = input()

    print("-----")

    API(Token).Message(Content)

    os.system('cls')

    Main()



if __name__ == "__main__":
    Main()
