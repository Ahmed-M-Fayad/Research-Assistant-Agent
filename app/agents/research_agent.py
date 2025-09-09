# services/research_agent.py
"""
Research Agent Service with ChatPromptTemplate for Flask Integration
"""

import os
from typing import Dict, List
from dataclasses import dataclass
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langgraph.prebuilt import create_react_agent

# Import your tools
from app.agents.tools.wikipedia_tool import WikipediaTool


@dataclass
class PromptConfig:
    """Configuration class for prompt templates"""

    agent_name: str = "3aref"
    role: str = "professional research assistant"
    specialization: str = "conducting thorough, accurate, and evidence-based research"
    temperature: float = 0.1


class ResearchAgentService:
    """Service to handle research agent operations with ChatPromptTemplate"""

    def __init__(self, config: PromptConfig = None):
        self.config = config or PromptConfig()
        self.agent = None
        self.is_initialized = False
        self._initialize_agent()

    def _get_system_prompt_template(self) -> ChatPromptTemplate:
        """Create ChatPromptTemplate for system prompt"""
        template = """You are {agent_name}, a {role} with expertise in {specialization}.

CORE PRINCIPLES:
• ACCURACY FIRST: Prioritize factual accuracy over speed or convenience
• EVIDENCE-BASED: Base responses on credible sources and verifiable information  
• TRANSPARENCY: Clearly indicate information sources and methodology
• COMPREHENSIVE: Provide thorough coverage while maintaining focus

RESEARCH METHODOLOGY:
1. QUERY ANALYSIS: Break down complex questions into key components
2. TOOL SELECTION: Use Wikipedia for encyclopedic information, background context, definitions
3. INFORMATION SYNTHESIS: Combine sources logically and coherently
4. RESPONSE CONSTRUCTION: Lead with direct answer, provide supporting details and context

QUALITY STANDARDS:
• Source Attribution: Clearly cite when using tool-retrieved information
• Factual Distinction: Separate established facts from theories/debates
• Temporal Awareness: Acknowledge when information may be outdated
• Accessibility: Provide context for technical or specialized information
• Honesty: Acknowledge limitations or gaps in available information

Remember: Accuracy and evidence always take precedence over assumptions or speculation."""

        return ChatPromptTemplate.from_template(template)

    def _initialize_agent(self):
        """Initialize the research agent with ChatPromptTemplate"""
        try:
            # Load environment variables
            dotenv_path = "configs/.env"
            load_dotenv(dotenv_path)

            # Get API key
            api_key = os.getenv("GROQ_API_KEY")
            if not api_key:
                raise ValueError("GROQ_API_KEY not found in environment variables")

            # Initialize LLM
            model = ChatGroq(
                model="meta-llama/llama-4-scout-17b-16e-instruct",
                api_key=api_key,
                temperature=self.config.temperature,
            )

            # Initialize tools
            wiki_tool = WikipediaTool()

            # Create system prompt using ChatPromptTemplate
            prompt_template = self._get_system_prompt_template()
            system_prompt = prompt_template.format(
                agent_name=self.config.agent_name,
                role=self.config.role,
                specialization=self.config.specialization,
            )

            # Create agent with formatted prompt
            self.agent = create_react_agent(
                model=model,
                tools=[wiki_tool.run],
                prompt=system_prompt,
            )

            self.is_initialized = True
            print(
                f"✅ Research Agent '{self.config.agent_name}' initialized successfully"
            )

        except Exception as e:
            print(f"❌ Failed to initialize Research Agent: {str(e)}")
            self.is_initialized = False

    def search(self, query: str) -> Dict:
        """
        Process a research query

        Args:
            query (str): The research question

        Returns:
            Dict: Response containing answer and metadata
        """
        if not self.is_initialized:
            return {
                "success": False,
                "error": "Research agent not initialized",
                "answer": "Sorry, the research service is currently unavailable.",
            }

        if not query or not query.strip():
            return {
                "success": False,
                "error": "Empty query",
                "answer": "Please provide a valid research question.",
            }

        try:
            # Format query with research instructions
            formatted_query = f"""Research Question: {query.strip()}

Please approach this systematically:
1. ANALYZE: Break down what information is needed
2. INVESTIGATE: Use appropriate tools to gather reliable data  
3. SYNTHESIZE: Integrate information from multiple angles
4. DELIVER: Provide a clear, accurate, and well-structured response

Focus on delivering actionable insights with proper source attribution."""

            # Process query with agent
            response = self.agent.invoke(
                {"messages": [{"role": "user", "content": formatted_query}]}
            )

            # Extract answer
            answer = response["messages"][-1].content

            return {
                "success": True,
                "answer": answer,
                "query": query.strip(),
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "answer": f"Sorry, I encountered an error while researching: {str(e)}",
            }

    def health_check(self) -> Dict:
        """Health check for the agent"""
        if not self.is_initialized:
            return {"status": "unhealthy", "message": "Agent not initialized"}

        try:
            test_response = self.search("What is artificial intelligence?")

            if test_response["success"] and len(test_response["answer"]) > 50:
                return {
                    "status": "healthy",
                    "message": f"Agent '{self.config.agent_name}' operational",
                }
            else:
                return {
                    "status": "unhealthy",
                    "message": f"Agent test failed: {test_response.get('error', 'Insufficient response')}",
                }

        except Exception as e:
            return {"status": "unhealthy", "message": f"Health check failed: {str(e)}"}


# Global instance
research_agent = ResearchAgentService()
