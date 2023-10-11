from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from httplib2 import Http
from oauth2client import client, file, tools

from src.mocks import MockGooglePhotosLibrary
from src.models import (
    GoogleAlbum,
    GoogleAlbums,
    GoogleMediaItem,
    GoogleMediaItems,
)


class GooglePhotos:
    SCOPES = [
        "https://www.googleapis.com/auth/photoslibrary",
        "https://www.googleapis.com/auth/photoslibrary.readonly",
        "https://www.googleapis.com/auth/photoslibrary.readonly.appcreateddata",
    ]
    page_size_albums = 20
    page_size_media_item_per_album = 100

    def __init__(self, mock_photos_library: bool = False) -> None:
        if mock_photos_library:
            self._photos_library = MockGooglePhotosLibrary()
        else:
            self._discover_photos_library()

    def _get_credentials(self):
        store = file.Storage("oauth/token.json")
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(
                "oauth/credentials.json",
                self.SCOPES,
                redirect_uri="http://localhost:8080",
            )
            credentials = tools.run_flow(flow, store)
        return credentials

    def _discover_photos_library(self):
        credentials = self._get_credentials()
        try:
            self._photos_library = build(
                "photoslibrary",
                "v1",
                http=credentials.authorize(Http()),
                static_discovery=False,
            )
        except HttpError as err:
            raise err

    def get_albums(self) -> list[GoogleAlbum]:
        albums: list[GoogleAlbum] = []
        page_token = None
        while True:
            google_albums = (
                self._photos_library.albums()
                .list(
                    pageSize=self.page_size_albums,
                    pageToken=page_token,
                )
                .execute()
            )
            google_albums_model: GoogleAlbums = GoogleAlbums(**google_albums)
            albums.extend(google_albums_model.albums)
            if not google_albums_model.next_page_token:
                break
            page_token = google_albums_model.next_page_token

        return albums

    def get_media_items_by_album_id(
        self,
        album_id: str,
    ) -> list[GoogleMediaItem]:
        media_items = (
            self._photos_library.mediaItems()
            .search(
                body={
                    "albumId": album_id,
                },
            )
            .execute()
        )
        media_items_model: GoogleMediaItems = GoogleMediaItems(**media_items)
        return media_items_model.media_items
