from agency_swarm import Agency
from .podcast_manager import PodcastManager
from .download_agent import DownloadAgent
from .audio_extraction_agent import AudioExtractionAgent
from .audio_editing_agent import AudioEditingAgent
from .podcast_formatting_agent import PodcastFormattingAgent
from .publishing_agent import PublishingAgent
from .performance_analyzer_agent import PerformanceAnalyzerAgent

podcast_manager = PodcastManager()
download_agent = DownloadAgent()
audio_extraction_agent = AudioExtractionAgent()
audio_editing_agent = AudioEditingAgent()
podcast_formatting_agent = PodcastFormattingAgent()
publishing_agent = PublishingAgent()
performance_analyzer = PerformanceAnalyzerAgent()

agency = Agency([
        podcast_manager,  # Podcast Manager will be the entry point for communication with the user
        [podcast_manager, download_agent],  # Podcast Manager can initiate communication with Download Agent
        [podcast_manager, audio_extraction_agent],  # Podcast Manager can initiate communication with Audio Extraction Agent
        [podcast_manager, audio_editing_agent],  # Podcast Manager can initiate communication with Audio Editing Agent
        [podcast_manager, podcast_formatting_agent],  # Podcast Manager can initiate communication with Podcast Formatting Agent
        [podcast_manager, publishing_agent],  # Podcast Manager can initiate communication with Publishing Agent
        [podcast_manager, performance_analyzer],  # Podcast Manager can initiate communication with Performance Analyzer
    ],
    shared_instructions='agency_manifesto.md',  # shared instructions for all agents
    temperature=0.5,  # default temperature for all agents
    max_prompt_tokens=25000  # default max tokens in conversation history
)

if __name__ == "__main__":
    agency.run_demo()  # starts the agency in terminal 