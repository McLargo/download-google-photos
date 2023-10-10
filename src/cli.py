from src.google_photos import GooglePhotos


def main() -> None:
    google_photos: GooglePhotos = GooglePhotos()
    albums: dict = google_photos.get_albums()
    for album in albums["albums"]:
        # TODO: pretty print with format
        print(album["title"])
