from agency_swarm import Agency
from .content_manager import ContentManager
from .narration_agent import NarrationAgent
from .visual_generator_agent import VisualGeneratorAgent
from .synchronization_agent import SynchronizationAgent
from .editing_agent import EditingAgent
from .performance_analyzer_agent import PerformanceAnalyzerAgent

content_manager = ContentManager()
narration_agent = NarrationAgent()
visual_generator = VisualGeneratorAgent()
synchronization_agent = SynchronizationAgent()
editing_agent = EditingAgent()
performance_analyzer = PerformanceAnalyzerAgent()

agency = Agency([
        content_manager,  # Content Manager will be the entry point for communication with the user
        [content_manager, narration_agent],  # Content Manager can initiate communication with Narration Agent
        [content_manager, visual_generator],  # Content Manager can initiate communication with Visual Generator
        [content_manager, synchronization_agent],  # Content Manager can initiate communication with Synchronization Agent
        [content_manager, editing_agent],  # Content Manager can initiate communication with Editing Agent
        [content_manager, performance_analyzer],  # Content Manager can initiate communication with Performance Analyzer
    ],
    shared_instructions='agency_manifesto.md',  # shared instructions for all agents
    temperature=0.5,  # default temperature for all agents
    max_prompt_tokens=25000  # default max tokens in conversation history
)

if __name__ == "__main__":
    agency.run_demo()  # starts the agency in terminal 