from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class GoogleAlbum(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str


class GoogleAlbums(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    albums: list[GoogleAlbum]
    next_page_token: Optional[str] = Field(default=None, alias="nextPageToken")


class GoogleMediaItem(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    base_url: str = Field(alias="baseUrl")
    filename: str
    mime_type: str = Field(alias="mimeType")

    def download_url(self) -> str:
        if not self.base_url.lower().startswith("http"):
            raise ValueError("Expected an http base_url")
        if self.mime_type.startswith("image"):
            return f"{self.base_url}=d"
        if self.mime_type.startswith("video"):
            return f"{self.base_url}=dv"
        raise ValueError("Unknown mime type")


class GoogleMediaItems(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    media_items: list[GoogleMediaItem] = Field(alias="mediaItems")
