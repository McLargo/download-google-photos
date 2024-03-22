import os
from shutil import copyfileobj
from urllib.request import Request, urlopen

import click

from src.config import DEFAULT_DOWNLOAD_PATH, MOCK_GOOGLE_PHOTOS_LIBRARY
from src.google_photos import GooglePhotosClient
from src.models import GoogleAlbum, GoogleMediaItem


class Cli:
    client: GooglePhotosClient
    albums: list[GoogleAlbum]
    looping_albums: bool = True

    def __init__(self) -> None:
        self.client: GooglePhotosClient = GooglePhotosClient(
            mock_photos_library=MOCK_GOOGLE_PHOTOS_LIBRARY,
        )
        self.albums: list[GoogleAlbum] = self.client.get_albums()

    def display_albums(self) -> None:
        click.echo("See your google albums below:")
        for x in range(len(self.albums)):
            click.echo(f"{x+1}: {self.albums[x].title}")

        prompt: int = click.prompt(
                "Enter id of the album to download. 0 to exit: ",
                type=click.INT,
                default=0,
            )
        if prompt == 0:
            self.looping_albums = False
            return

        if prompt > len(self.albums):
            click.echo("Invalid album id.")
            return

        # reduce prompt in one to match list index
        prompt -= 1
        self.download_album(prompt)

    def download_album(self, prompt: int) -> None:
        # create new folder in Desktop
        path: str = os.path.join(DEFAULT_DOWNLOAD_PATH, self.albums[prompt].title)
        if not os.path.exists(path):
            os.mkdir(path)

        # get media items from album and download to the new folder
        media_items: list[
            GoogleMediaItem
        ] = self.client.get_media_items_by_album_id(
            album_id=self.albums[prompt].id,
        )

        click.echo(
            f"Downloading album {self.albums[prompt].title} ({len(media_items)} items)",
        )
        click.echo(f"Your photos will available in folder {path}")

        for media_item in media_items:
            filename_path: str = os.path.join(path, media_item.filename)
            try:
                media_item_url: str = media_item.download_url()
                request = Request(media_item_url)
                with urlopen(request) as in_stream, open(  # nosec
                    filename_path,
                    "wb",
                ) as out_file:
                    copyfileobj(in_stream, out_file)
            except Exception as exc:
                click.echo(f"Error downloading {media_item.base_url}. {exc}")


@click.command()
def cli() -> None:
    cli_instance = Cli()

    if not cli_instance.albums:
        click.echo("No albums found in your google photos account.")
        return

    while cli_instance.looping_albums:
        cli_instance.display_albums()

    click.echo("Exiting.")
