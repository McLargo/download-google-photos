from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from httplib2 import Http
from oauth2client import client, file, tools


class GooglePhotos:
    SCOPES = [
        "https://www.googleapis.com/auth/photoslibrary",
        "https://www.googleapis.com/auth/photoslibrary.readonly",
        "https://www.googleapis.com/auth/photoslibrary.readonly.appcreateddata",
    ]
    albums_page_size = 10
    mediaitems_page_size = 10

    def __init__(self) -> None:
        self._discover_photos_library()

    def _discover_photos_library(self):
        store = file.Storage("oauth/token.json")
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(
                "oauth/credentials.json",
                self.SCOPES,
                redirect_uri="http://localhost:8080",
            )
            credentials = tools.run_flow(flow, store)

        try:
            self._photos_library = build(
                "photoslibrary",
                "v1",
                http=credentials.authorize(Http()),
                static_discovery=False,
            )
        except HttpError as err:
            # TODO: handle properly
            print(err)

    # TODO: response must be a model
    def get_albums(self) -> dict:
        return (
            self._photos_library.albums()
            .list(
                pageSize=self.albums_page_size,
            )
            .execute()
        )

    # TODO: implement method
    #     def get_items_from_album()
    # return  self._photos_library.mediaItems().search(
    # body={"pageSize": 10, "albumId": albums_id}).execute()
