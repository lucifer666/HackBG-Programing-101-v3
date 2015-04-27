
class Song:

    def __init__(self, title, artist, album, length):
            self.title = title
            self.artist = artist
            self.album = album
            self.length = length

    def __str__(self):
        return "{} - {} from {} - {}".format(self.artist, self.title, self.album, self.length)


    def __hash__(self):
        return hash(self.title + self.artist + self.album + self.length)

    def __eq__(self, other_song):
        tit = self.title == other_song.title
        art = self.artist == other_song.artist
        alb = self.album == other_song.album
        leng = self.length == other_song.length

        return tit and art and alb and leng

    def get_length(self, seconds = False, minutes = False, hours = False):
        if seconds == True:
            l = self.length.split(':')
            if (len(l) == 3):
                return int(l[0]) * 3600 + int(l[1]) * 60 + int(l[2])
            elif (len(l) == 2):
                return int(int(l[0]) * 60 + int(l[1]))
            elif (len(l) == 1):
                return int(l[0])
        if minutes == True:
            l = self.length.split(':')
            if (len(l) == 3):
                return int(int(l[0]) * 60 + int(l[1]))
            elif (len(l) == 2):
                return int(l[0])
            elif (len(l) == 1):
                return 0
        if hours == True:
            l = self.length.split(':')
            if (len(l) == 3):
                return int(l[0])
            elif len(l) == 2 or len(l) == 1:
                return 0
        if seconds == False and minutes == False and hours == False:
            return self.length

    def prepare_json(self): # подготвя обекта Song да бъде репрезентиран като речник чрез json
        song_dict = self.__dict__
        return {key : song_dict[key] for key in song_dict}







