from src.google_photos import GooglePhotos
from src.models import Album


def main() -> None:
    google_photos: GooglePhotos = GooglePhotos()
    albums: list[Album] = google_photos.get_albums()
    for album in albums:
        # TODO: pretty print with format
        print(album.title)
