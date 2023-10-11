import os
from shutil import copyfileobj
from urllib.request import Request, urlopen

import click

from src.config import DEFAULT_DOWNLOAD_PATH, MOCK_GOOGLE_PHOTOS_LIBRARY
from src.google_photos import GooglePhotos
from src.models import GoogleAlbum, GoogleMediaItem


@click.command()
def cli() -> None:
    google_photos: GooglePhotos = GooglePhotos(
        mock_photos_library=MOCK_GOOGLE_PHOTOS_LIBRARY,
    )
    albums: list[GoogleAlbum] = google_photos.get_albums()
    if not albums:
        click.echo("No albums found in your google photos account.")
        return

    click.echo("See your google albums below:")
    for x in range(len(albums)):
        click.echo(f"{x+1}: {albums[x].title}")

    prompt = click.prompt(
        "Enter id of the album to download. 0 to exit: ",
        type=click.INT,
        default=0,
    )
    if prompt == 0:
        click.echo("Exiting.")
        return

    if prompt > len(albums):
        click.echo("Invalid album id.")
        return

    # reduce prompt in one to match list index
    prompt -= 1

    # create new folder in Desktop
    path = os.path.join(DEFAULT_DOWNLOAD_PATH, albums[prompt].title)
    os.mkdir(path)

    # get media items from album and download to the new folder
    media_items: list[
        GoogleMediaItem
    ] = google_photos.get_media_items_by_album_id(
        album_id=albums[prompt].id,
    )
    click.echo(
        f"Downloading album {albums[prompt].title} ({len(media_items)} items).",
    )
    click.echo(f"Your photos will available in folder {path}")

    for media_item in media_items:
        filename_path = os.path.join(path, media_item.filename)
        try:
            if media_item.product_url.lower().startswith("http"):
                request = Request(media_item.product_url)
                with urlopen(request) as in_stream, open(  # nosec
                    filename_path,
                    "wb",
                ) as out_file:
                    copyfileobj(in_stream, out_file)
            else:
                click.echo(f"Invalid URL: {media_item.product_url}")

        except Exception as e:
            click.echo(f"Error downloading {media_item.product_url}. {e}")
