""" RouteQuery class"""
from typing import Literal
from langchain_core.pydantic_v1 import BaseModel, Field

class RouteQuery(BaseModel):
    """Route a user query to vector store or off-topic."""

    datasource: Literal["vectorstore", "off_topic"] = Field(
        ...,
        description="Given a user question choose to route it to web search or a vectorstore.",
    )

