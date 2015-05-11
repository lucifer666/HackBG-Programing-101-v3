from Songs import Song
import copy, random, json, time
from tabulate import tabulate


class Playlist:

    def __init__(self, name, repeat, shuffle):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.song_list = []
        self.list_of_songs = []
        self.copy_list_of_songs = []
        self.count_len = 0

    def add_song(self, song):
        self.song_list.append(song)

    def remove_song(self, song):
        self.song_list.remove(song)

    def add_songs(self, songs):
        if type(songs) is not list:
            self.list_of_songs.append(songs)
            self.copy_list_of_songs = copy.deepcopy(self.list_of_songs)
            return
        self.list_of_songs += [song for song in songs]
        self.copy_list_of_songs = copy.deepcopy(self.list_of_songs)

    def total_length(self):
        length_playlist_in_seconds = 0

        for songs in self.song_list:

            length_playlist_in_seconds += songs.get_length(seconds = True)

        return str(length_playlist_in_seconds)

    def artists(self):
        artists_histogram = {}
        count_songs = 0
        list_artists = [] # събираме в един списък всички артисти от плейлиста(+ повторенията им)
        for songs in range(0, len(self.song_list)):
               list_artists.append(self.song_list[songs].artist)

        for artists in list_artists:
            count_songs = list_artists.count(artists)
            if artists not in artists_histogram:
                artists_histogram[artists] = count_songs
        return artists_histogram


    def next_song(self):
        length_of_playlist = len(self.copy_list_of_songs)

        if self.repeat == False and self.shuffle == False:
            for song in self.copy_list_of_songs:
                if self.count_len == length_of_playlist:
                    break
                return_song = self.copy_list_of_songs.pop(0)
                self.copy_list_of_songs.append(return_song)
                self.count_len += 1
                return return_song

        elif self.repeat == True and self.shuffle == False:
           for song in self.copy_list_of_songs:
                return_song = self.copy_list_of_songs.pop(0)
                self.copy_list_of_songs.append(return_song)
                return return_song

        elif self.repeat == False and self.shuffle == True:
            if self.copy_list_of_songs == []:
               return
            for song in self.copy_list_of_songs:
                return_song = random.choice(self.copy_list_of_songs)
                self.copy_list_of_songs.remove(return_song)
                return return_song

        elif self.repeat == True and self.shuffle == True:
            if self.copy_list_of_songs == []:
              self.copy_list_of_songs = copy.deepcopy(self.list_of_songs)
            for song in self.copy_list_of_songs:
                return_song = random.choice(self.copy_list_of_songs)
                self.copy_list_of_songs.remove(return_song)
                return return_song

    def pprint_playlist(self):
        table = []
        for songs in self.list_of_songs:
            table += [[songs.artist, songs.title, songs.album, songs.length]]

        print (tabulate( table,headers = ['Artist', 'Song','Album','Length']))

    def prepare_to_json(self):
        playlist = {
                "Name" : self.name,
                "Songs" : [songs.prepare_json() for songs in self.list_of_songs]
                }
        return playlist

    def save_playlist(self):
        filename = self.name.replace(" ","-") + ".json"
        fwrite = open(filename, "w")
        json.dump(self.prepare_to_json(),fwrite, indent=4)
        fwrite.close()

    @staticmethod
    def load_playlist(filename):
        with open(filename, "r") as f:

            data = json.loads(f.read())

            p = Playlist(data["Songs"], shuffle=False, repeat=True)
            for dict_song in data["Songs"]:
                song = Song(artist=dict_song["artist"], title=dict_song["title"], album=dict_song["album"], length=dict_song["length"])
                p.add_songs(song)
            return p

















