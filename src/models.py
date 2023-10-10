from pydantic import BaseModel, ConfigDict, Field


class Album(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    product_url: str = Field(alias="productUrl")


class Albums(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    albums: list[Album]
    next_page_token: str = Field(alias="nextPageToken")
