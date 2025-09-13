# services/research_agent.py
"""
Minimal Research Agent Service with Full Tool Utilization
"""

import os
import json
from typing import Dict
from dataclasses import dataclass
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import ToolMessage
from langchain.prompts import ChatPromptTemplate
from langgraph.prebuilt import create_react_agent
from .tools.wikipedia_tool import wikipedia_tool
from .tools.arxiv_tool import arxiv_tool
from .tools.news_tool import news_tool

@dataclass
class PromptConfig:
    """Configuration class for prompt templates"""
    agent_name: str = "3aref"
    role: str = "professional research assistant"
    temperature: float = 0.1


class OutputFormatter:
    """Simple HTML formatter for research output"""
    
    @staticmethod
    def response_to_dict(response: dict) -> Dict:
        """Convert response from agent to JSON format"""
        messages = response['messages']
        
        # Extract tool calls
        tools_messages = [msg for msg in messages if isinstance(msg, ToolMessage)]
        
        # Messages & Tools map
        mapped_messages = {
            "Wikipedia": '...',
            "ArXiv Papers": [],
            "News Search": []
        }

        # Map tool messages
        for msg in tools_messages:
            tool_name = msg.name
            if tool_name == "ArXiv Papers" or tool_name == "News Search":
                json_str = msg.content
                try:
                    json_data = json.loads(json_str)
                    mapped_messages[tool_name] = json_data
                except json.JSONDecodeError:
                    mapped_messages[tool_name] = json_str
            else:
                mapped_messages[tool_name] = msg.content

        return mapped_messages

class ResearchAgentService:
    """Minimal Research Agent with Maximum Tool Usage"""

    def __init__(self, config: PromptConfig = None):
        self.config = config or PromptConfig()
        self.agent = None
        self.is_initialized = False
        self.formatter = OutputFormatter()
        self._initialize_agent()

    def _get_system_prompt_template(self) -> ChatPromptTemplate:
        """Create system prompt that FORCES tool usage"""
        template = """You are {agent_name}, an expert research assistant. 

CRITICAL INSTRUCTION: You can use MULTIPLE research tools for EVERY query to provide comprehensive results.

MANDATORY RESEARCH PROTOCOL:
1. First, Use Wikipedia tool for background/definitions
2. Second, Use ArXiv tool for scientific papers (if relevant)
3. Third, Use News tool for recent developments
4. Finally, order and format your findings clearly

TOOL USAGE REQUIREMENTS:
- Use the tools with the order provided for the query
- Include the results from each tool used

RESPONSE FORMAT: Make a JSON object representing the search
The results that should have fields for
- The Background From Wikipedia
- A List of Relevant Papers from ArXiv containing title, URL, and summary
- A List of Recent News Articles from News tool containing headline, source, and URL

Only return the JSON. Never return non-JSON text including backtack wrappers around the JSON.
"""
        return ChatPromptTemplate.from_template(template)

    def _initialize_agent(self):
        """Initialize agent with all tools"""
        try:
            dotenv_path = "configs/.env"
            load_dotenv(dotenv_path)

            api_key = os.getenv("GROQ_API_KEY")
            if not api_key:
                raise ValueError("GROQ_API_KEY not found")

            model = ChatGroq(
                model="meta-llama/llama-4-scout-17b-16e-instruct",
                api_key=api_key,
                temperature=self.config.temperature,
            )

            tools = [wikipedia_tool, arxiv_tool, news_tool]
            
            if not tools:
                print("⚠️ No tools loaded")
                return
                
            print(f"✅ Loaded {len(tools)} tools")

            prompt_template = self._get_system_prompt_template()
            system_prompt = prompt_template.format(
                agent_name=self.config.agent_name
            )

            self.agent = create_react_agent(
                model=model,
                tools=tools,
                prompt=system_prompt,
            )

            self.is_initialized = True
            print(f"✅ Agent initialized with {len(tools)} tools")

        except Exception as e:
            print(f"❌ Agent initialization failed: {str(e)}")
            self.is_initialized = False

    def search(self, query: str) -> Dict:
        """Process research query with forced tool usage"""
        if not self.is_initialized:
            return {
                "success": False,
                "error": "Agent not initialized",
                "answer": "Research service unavailable."
            }

        if not query or not query.strip():
            return {
                "success": False,
                "error": "Empty query",
                "answer": "Please provide a research question."
            }

        try:
            # Force comprehensive tool usage
            enhanced_query = f"""Research Query: {query.strip()}

RESEARCH INSTRUCTIONS:
1. First, Use Wikipedia tool to get background information
2. Then, Use ArXiv tool to find relevant research papers
3. Next, Use News tool to find recent articles and developments
4. Format your response clearly with sections for each tool's findings

Provide a comprehensive response using multiple research tools."""

            response = self.agent.invoke(
                {"messages": [{"role": "user", "content": enhanced_query}]}
            )

            mapped_response = self.formatter.response_to_dict(response)
            
            return {
                "success": True,
                "answer": mapped_response,
                "query": query.strip(),
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "answer": f"Research error: {str(e)}"
            }

# Global instance
research_agent = ResearchAgentService()