import unittest

import mock

from createbillboardplaylist import PlaylistCreator


class CreatePlaylistTestCase(unittest.TestCase):
    def test_add_first_video_to_playlist(self):
        video_id = 'test-video-id'
        playlist_id = 'test-playlist'
        search_query = 'test artist - test song title'

        billboard = mock.Mock()
        youtube = mock.Mock()
        youtube.get_video_id_for_search.return_value = video_id

        playlist_creator = PlaylistCreator(youtube, billboard)
        playlist_creator.add_first_video_to_playlist(playlist_id, search_query)

        youtube.get_video_id_for_search.assert_called_with(search_query)
        youtube.add_video_to_playlist.assert_called_with(playlist_id, video_id)


if __name__ == '__main__':
    unittest.main()