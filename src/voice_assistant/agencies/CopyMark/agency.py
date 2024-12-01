from agency_swarm import Agency
from .content_manager import ContentManager
from .trend_analyzer_agent import TrendAnalyzerAgent
from .youtube_analyzer_agent import YouTubeAnalyzerAgent

content_manager = ContentManager()
trend_analyzer = TrendAnalyzerAgent()
youtube_analyzer = YouTubeAnalyzerAgent()

agency = Agency([
        content_manager,  # Content Manager will be the entry point for communication with the user
        [content_manager, trend_analyzer],  # Content Manager can initiate communication with Trend Analyzer
        [content_manager, youtube_analyzer],  # Content Manager can initiate communication with YouTube Analyzer
        [trend_analyzer, content_manager],  # Trend Analyzer can send reports to Content Manager
        [youtube_analyzer, content_manager],  # YouTube Analyzer can send reports to Content Manager
    ],
    shared_instructions='agency_manifesto.md',  # shared instructions for all agents
    temperature=0.5,  # default temperature for all agents
    max_prompt_tokens=25000  # default max tokens in conversation history
)

if __name__ == "__main__":
    agency.run_demo()  # starts the agency in terminal