import json
import logging
import os
import re
from typing import Any, Dict, List

from langchain_community.vectorstores import AzureSearch
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings

# import state schemas
from backend.src.langgraph.state import ComplianceNote, VideoReviewState
