from unittest.mock import patch

import pytest
from click.testing import CliRunner

from src.cli import cli
from src.factory import get_google_media_items

pytestmark = pytest.mark.functional


@patch("src.cli.MOCK_GOOGLE_PHOTOS_LIBRARY", True)
@patch("src.cli.GooglePhotosClient.get_albums")
def test_cli_no_albums(mock_get_albums):
    mock_get_albums.return_value = []
    runner = CliRunner()
    result = runner.invoke(cli)

    assert not result.exception
    assert result.output == "No albums found in your google photos account.\n"


@patch("src.cli.DEFAULT_DOWNLOAD_PATH", "/tmp")
@patch("src.cli.MOCK_GOOGLE_PHOTOS_LIBRARY", True)
def test_cli():
    runner = CliRunner()
    result = runner.invoke(cli, input="1")

    assert not result.exception
    assert "1: " in result.output
    assert "2: " in result.output
    assert "3: " in result.output
    assert "4: " in result.output
    assert "5: " in result.output
    assert "6: " not in result.output
    assert "Enter id of the album to download. 0 to exit: " in result.output
    assert "Downloading album" in result.output
    assert "Your photos will available in folder" in result.output


@patch("src.cli.DEFAULT_DOWNLOAD_PATH", "/tmp")
@patch("src.cli.MOCK_GOOGLE_PHOTOS_LIBRARY", True)
@patch("src.cli.urlopen")
def test_cli_exception_download(mock_url_open):
    mock_url_open.side_effect = Exception("Error downloading")
    runner = CliRunner()
    result = runner.invoke(cli, input="1")

    assert not result.exception
    assert "1: " in result.output
    assert "2: " in result.output
    assert "3: " in result.output
    assert "4: " in result.output
    assert "5: " in result.output
    assert "6: " not in result.output
    assert "Enter id of the album to download. 0 to exit: " in result.output
    assert "Downloading album" in result.output
    assert "Your photos will available in folder" in result.output
    assert "Error downloading" in result.output


@patch("src.cli.DEFAULT_DOWNLOAD_PATH", "/tmp")
@patch("src.cli.MOCK_GOOGLE_PHOTOS_LIBRARY", True)
@patch("src.cli.GooglePhotosClient.get_media_items_by_album_id")
def test_cli_base_url_not_http(mock_get_media_items):
    google_media_items = get_google_media_items(media_items_size=1)
    google_media_items.media_items[0].base_url = "invalid_url"
    mock_get_media_items.return_value = google_media_items.media_items

    runner = CliRunner()
    result = runner.invoke(cli, input="1")

    assert not result.exception
    assert "1: " in result.output
    assert "2: " in result.output
    assert "3: " in result.output
    assert "4: " in result.output
    assert "5: " in result.output
    assert "6: " not in result.output
    assert "Enter id of the album to download. 0 to exit: " in result.output
    assert "Downloading album" in result.output
    assert "Your photos will available in folder" in result.output
    assert "Error downloading" in result.output


@patch("src.cli.MOCK_GOOGLE_PHOTOS_LIBRARY", True)
def test_cli_prompt_exit():
    runner = CliRunner()
    result = runner.invoke(cli, input="0")

    assert not result.exception
    assert "1: " in result.output
    assert "2: " in result.output
    assert "3: " in result.output
    assert "4: " in result.output
    assert "5: " in result.output
    assert "6: " not in result.output
    assert "Enter id of the album to download. 0 to exit: " in result.output
    assert "Exiting." in result.output


@patch("src.cli.MOCK_GOOGLE_PHOTOS_LIBRARY", True)
def test_cli_prompt_greater_than_len():
    runner = CliRunner()
    result = runner.invoke(cli, input="25")

    assert not result.exception
    assert "1: " in result.output
    assert "2: " in result.output
    assert "3: " in result.output
    assert "4: " in result.output
    assert "5: " in result.output
    assert "6: " not in result.output
    assert "Enter id of the album to download. 0 to exit: " in result.output
    assert "Invalid album id." in result.output
