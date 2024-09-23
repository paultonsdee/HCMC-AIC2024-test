from uuid import uuid4

from pydantic import BaseModel, Field, field_validator

class VideoMetadata(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))  # Generate and convert UUID to string
    title: str = Field(..., description="Title of the YouTube video")
    description: str = Field(..., description="Description of the video")
    publish_date: str = Field(..., description="Publication date of the video")
    thumbnail_url: str = Field(..., description="URL of the video thumbnail")
    watch_url: str = Field(..., description="URL to watch the video")
    channel_id: str
    channel_url: str
    author: str
    keywords: str
    length: int
    channel_title: str = Field(None, alias="title")  # For consistency with other fields

    @field_validator('publish_date', mode='before')
    def validate_publish_date(cls, v):
        # Add custom validation for publish_date format if needed
        # For example, using a date parser library
        return v

    @field_validator('keywords', mode='before')
    def validate_keywords(cls, v):
        kw = ""
        v = list(set(v))
        for word in v: 
            kw += word + " | "
        # return list(set(v))
        return kw

    @field_validator('keywords', mode='before')
    def validate_keywords(cls, v):
        kw = ""
        v = list(set(v))
        for word in v: 
            kw += word + " | "
        # return list(set(v))
        return kw

class VideoObjects(BaseModel): 
    video_name: str = Field(..., description="The name of the video")
    dtd_objects: list[str] = Field(..., description="A list of detected objects in the video")
    no_dtd_objects: list[int] = Field(..., description="The number of detected objects in the video")