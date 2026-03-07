import operator
from typing import Annotated, Any, Dict, List, Optional, TypedDict


class ComplianceNote(TypedDict):
    """
    Schema defining the data structure representing compliance results.
    """

    note_category: str
    note_description: str
    note_severity: str
    note_timecode: Optional[str]


# This defines the state in agentic workflow
class VideoReviewStage(TypedDict):
    """
    Schema defining the data structure used for LangGraph execution content.
    """

    video_url: str
    video_id: str

    # ingestion
    file_download_path: Optional[str]

    # extraction
    video_metadata: Dict[str, Any]
    video_transcript: Optional[str]
    ocr_text: List[str]

    # compliance notes
    review_results = Annotated[List[ComplianceNote], operator.add]  # pyright: ignore[reportGeneralTypeIssues]

    # conclusion
    conclusion: str
    conclusion_report: str

    # all errors and warnings
    errors: Annotated[List[str], operator.add]
