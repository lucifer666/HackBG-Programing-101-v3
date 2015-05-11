from Songs import Song
from playlist import Playlist
import unittest

class TestSong(unittest.TestCase):

    def test_init(self):
        song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        self.assertEqual(song.title, "Odin")
        self.assertEqual(song.artist, "Manowar")
        self.assertEqual(song.album, "The Sons of Odin")
        self.assertEqual(song.length, "3:44")

    def test_str(self):
         song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="1:30:44")
         result = "Manowar - Odin from The Sons of Odin - 1:30:44"
         self.assertEqual(str(song), result)

    def test_hash(self):
        song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        result = hash(song)
        self.assertTrue(isinstance(result, int))

    def test_eq(self):
        song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="1:30:44")
        other_song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="1:30:44")
        self.assertTrue(other_song == song)

    def test_get_length(self):
        song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="1:30:44")
        second_song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="30:44")
        third_song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="44")

        result = song.get_length(seconds=True)
        result1 = song.get_length(minutes=True)
        result2 = song.get_length(hours=True)
        self.assertEqual(song.get_length(seconds=True), result)
        self.assertEqual(song.get_length(minutes=True), result1)
        self.assertEqual(song.get_length(hours=True), result2)
        result = second_song.get_length(seconds=True)
        result1 = second_song.get_length(minutes=True)
        result2 = second_song.get_length(hours=True)
        self.assertEqual(second_song.get_length(seconds=True), result)
        self.assertEqual(second_song.get_length(minutes=True), result1)
        self.assertEqual(second_song.get_length(hours=True), result2)
        result = third_song.get_length(seconds=True)
        result1 = third_song.get_length(minutes=True)
        result2 = third_song.get_length(hours=True)
        self.assertEqual(third_song.get_length(seconds=True), result)
        self.assertEqual(third_song.get_length(minutes=True), result1)
        self.assertEqual(third_song.get_length(hours=True), result2)

    def test_init_playlist(self):
        code_songs = Playlist(name="Code", repeat=False, shuffle=False)
        self.assertEqual(code_songs.name, "Code")
        self.assertEqual(code_songs.repeat, False)
        self.assertEqual(code_songs.repeat, False)


    def test_add_song(self):
        song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="1:30:44")

        code_songs = Playlist(name="Code", repeat=False, shuffle=False)
        code_songs.add_song(song)
        self.assertTrue(song in code_songs.song_list)

    def test_remove_song(self):
         song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="1:30:44")
         code_songs = Playlist(name="Code", repeat=False, shuffle=False)
         code_songs.add_song(song)
         self.assertTrue(song in code_songs.song_list)
         code_songs.remove_song(song)
         self.assertTrue(song not in code_songs.song_list)

    def test_add_songs(self):
        song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="1:30:44")
        song2 = Song(title="Panda", artist="Grizli", album="Panda Dog", length="30:44")
        song3 = Song(title="Panda2", artist="Grizli2", album="Panda Dog2", length="44")
        song4 = Song(title="Loki", artist="Manowar", album="The Sons of Loki", length="2:30:44")
        song5 = Song(title="Tor", artist="Manowar", album="The Sons of Odin", length="35:44")
        code_songs = Playlist(name="Code", repeat=False, shuffle=False)
        code1_songs = Playlist(name="Code1", repeat=False, shuffle=False)
        code2_songs = Playlist(name="Code2", repeat=False, shuffle=False)
        code_songs.add_song(song)
        code_songs.add_song(song2)
        code_songs.add_song(song3)
        code_songs.add_song(song4)
        code1_songs.add_song(song)
        code1_songs.add_song(song5)

        code2_songs.add_songs(code_songs.song_list)
        code2_songs.add_songs(code1_songs.song_list)
        code_songs.song_list += code1_songs.song_list
        self.assertEqual(code2_songs.list_of_songs, code_songs.song_list)
        self.assertTrue(len(code2_songs.list_of_songs) == len(code_songs.song_list))

    def test_total_length(self):
         song = Song(title="Loki", artist="Manowar", album="The Sons of Odin", length="1:30:44")
         song2 = Song(title="Panda", artist="Grizli", album="Panda Dog", length="30:44")
         song3 = Song(title="Panda2", artist="Grizli2", album="Panda Dog2", length="44")
         code_songs = Playlist(name="Code", repeat=False, shuffle=False)
         code_songs.add_song(song)
         code_songs.add_song(song2)
         code_songs.add_song(song3)
         length_str = code_songs.total_length()
         self.assertEqual(code_songs.total_length(), length_str)

    def test_artists(self):
        song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="1:30:44")
        song2 = Song(title="Panda", artist="Grizli", album="Panda Dog", length="30:44")
        song3 = Song(title="Panda2", artist="Grizli2", album="Panda Dog2", length="44")
        song4 = Song(title="Loki", artist="Manowar", album="The Sons of Loki", length="2:30:44")
        code_songs = Playlist(name="Code", repeat=False, shuffle=False)
        code_songs.add_song(song)
        code_songs.add_song(song2)
        code_songs.add_song(song3)
        code_songs.add_song(song4)
        result = {'Grizli': 1, 'Grizli2': 1, 'Manowar': 2}
        self.assertEqual(code_songs.artists(), result)


    def test_next_song(self):
        song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="1:30:44")
        song2 = Song(title="Panda", artist="Grizli", album="Panda Dog", length="30:44")
        song3 = Song(title="Panda2", artist="Grizli2", album="Panda Dog2", length="44")
        song4 = Song(title="Thor", artist="Thor", album="The sons of Odin", length="44")
        code_songs = Playlist(name="Code", repeat=False, shuffle=False)
        code2_songs = Playlist(name="Code", repeat=False, shuffle=False)
        code_songs.add_song(song)
        code_songs.add_song(song2)
        code_songs.add_song(song3)
        code2_songs.add_songs(song4)
        code2_songs.add_songs(code_songs.song_list)
        result = code2_songs.next_song()
        result1 = code2_songs.next_song()
        result2 = code2_songs.next_song()
        result3 = code2_songs.next_song()
        result4 = code2_songs.next_song()

        self.assertEqual(code2_songs.list_of_songs[0], result)
        self.assertEqual(code2_songs.list_of_songs[1], result1)
        self.assertEqual(code2_songs.list_of_songs[2], result2)
        self.assertEqual(code2_songs.list_of_songs[3], result3)
        self.assertEqual(None, result4)


    def test_next_song_repeat_is_true(self):
        song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="1:30:44")
        song2 = Song(title="Panda", artist="Grizli", album="Panda Dog", length="30:44")
        song3 = Song(title="Panda2", artist="Grizli2", album="Panda Dog2", length="44")
        song4 = Song(title="Thor", artist="Thor", album="The sons of Odin", length="44")
        code_songs = Playlist(name="Code", repeat=False, shuffle=False)
        code2_songs = Playlist(name="Code", repeat=True, shuffle=False)
        code_songs.add_song(song)
        code_songs.add_song(song2)
        code_songs.add_song(song3)
        code2_songs.add_songs(song4)
        code2_songs.add_songs(code_songs.song_list)

        result = code2_songs.next_song()
        result2 = code2_songs.next_song()
        result3 = code2_songs.next_song()
        result4 = code2_songs.next_song()
        result5 = code2_songs.next_song()
        code2_songs.next_song()
        result7 = code2_songs.next_song()
        self.assertEqual(code2_songs.list_of_songs[0], result)
        self.assertEqual(code2_songs.list_of_songs[1], result2)
        self.assertEqual(code2_songs.list_of_songs[2], result3)
        self.assertEqual(code2_songs.list_of_songs[3], result4)
        self.assertEqual(code2_songs.list_of_songs[0], result5)
        self.assertEqual(code2_songs.list_of_songs[2], result7)

    def test_next_song_shuffle_is_true(self):
        song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="1:30:44")
        song2 = Song(title="Panda", artist="Grizli", album="Panda Dog", length="30:44")
        song3 = Song(title="Panda2", artist="Grizli2", album="Panda Dog2", length="44")
        song4 = Song(title="Thor", artist="Thor", album="The sons of Odin", length="44")
        code_songs = Playlist(name="Code", repeat=False, shuffle=False)
        code2_songs = Playlist(name="Code", repeat=False, shuffle=True)
        code_songs.add_song(song)
        code_songs.add_song(song2)
        code_songs.add_song(song3)
        code2_songs.add_songs(song4)
        code2_songs.add_songs(code_songs.song_list)

        code2_songs.next_song()
        code2_songs.next_song()
        code2_songs.next_song()
        code2_songs.next_song()
        result = code2_songs.next_song()
        self.assertEqual(None, result)

    def test_prepare_to_json(self):
        song = Song(title="Numb", artist="Linkin Park", album="Meteora", length="3:06")
        song2 = Song(title="Leave Out All the Rest", artist="Linkin Park", album=" Minutes to Midnight", length="3:24")
        song3 = Song(title="Californication", artist="Red Hot Chili Peppers", album="Californication", length="5:21")
        song4 = Song(title="It's My Life", artist="Bon Jovi", album="Crush", length="4:27")
        code_songs = Playlist(name="Code", repeat=False, shuffle=False)
        code2_songs = Playlist(name="Best Songs Ever", repeat=False, shuffle=False)
        code_songs.add_song(song)
        code_songs.add_song(song2)
        code_songs.add_song(song3)
        code2_songs.add_songs(song4)
        code2_songs.add_songs(code_songs.song_list)
        result = code2_songs.prepare_to_json()
        self.assertEqual(code2_songs.prepare_to_json(), result)

    def test_pprint_save_playlist(self):
        song = Song(title="Numb", artist="Linkin Park", album="Meteora", length="3:06")
        song2 = Song(title="Leave Out All the Rest", artist="Linkin Park", album=" Minutes to Midnight", length="3:24")
        song3 = Song(title="Californication", artist="Red Hot Chili Peppers", album="Californication", length="5:21")
        song4 = Song(title="It's My Life", artist="Bon Jovi", album="Crush", length="4:27")
        code_songs = Playlist(name="Code", repeat=False, shuffle=False)
        code2_songs = Playlist(name="Best Songs Ever", repeat=False, shuffle=False)
        code_songs.add_song(song)
        code_songs.add_song(song2)
        code_songs.add_song(song3)
        code2_songs.add_songs(song4)
        code2_songs.add_songs(code_songs.song_list)

        code2_songs.save_playlist()

        code2_songs.pprint_playlist()

    def test_load_playlist(self):
        p = Playlist.load_playlist("Best-Songs-Ever.json")
        try:
            while True:
                song = p.next_song()

                if song is None:
                    break
                print(str(song))
                time.sleep(1)
        except Exception as e:
            print(e)


















if __name__ == "__main__":
    unittest.main()
