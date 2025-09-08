# 🧠 Intelligent Research Assistant

<div align="center">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white" alt="LangChain">
  <img src="https://img.shields.io/badge/NVIDIA-76B900?style=for-the-badge&logo=nvidia&logoColor=white" alt="NVIDIA">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
</div>

<div align="center">
  <h3>🚀 <strong>AI-Powered Research Revolution</strong> 🚀</h3>
  <p><em>Intelligent agent system for comprehensive academic and web research</em></p>
</div>

---

## 🎯 Overview

An AI-powered research assistant that combines the power of advanced LLMs with multi-source integration to revolutionize how research is conducted. Built with Flask and LangChain, it provides an intelligent agent capable of gathering, analyzing, and synthesizing information from academic databases, news sources, and the web.

### ✨ Key Features

- **🤖 Intelligent Agent**: ReAct-based research agent with advanced reasoning
- **📚 Multi-Source Integration**: arXiv, Semantic Scholar, Wikipedia, news, and web search
- **💬 Interactive Chat**: Real-time conversation interface
- **📝 Auto-Citations**: Automatic source formatting and bibliography
- **📊 Export Tools**: Generate comprehensive research reports

---

## 🛠️ Technology Stack

| Component     | Technology                | Purpose                         |
| ------------- | ------------------------- | ------------------------------- |
| **Backend**   | Flask + LangChain         | Agent orchestration & API       |
| **AI Engine** | NVIDIA NIM/Llama 3.1      | Advanced language understanding |
| **Frontend**  | HTML5 + CSS3 + JavaScript | Interactive user interface      |
| **Database**  | Vector Store + SQLite     | Semantic search & caching       |
| **APIs**      | Academic + News + Web     | Multi-source data integration   |

---

## 🚀 Installation

### Quick Start

```bash
# Clone repository
git clone https://github.com/yourusername/intelligent-research-assistant.git
cd intelligent-research-assistant

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure API keys
cp configs/.env.example configs/.env
# Edit .env with your API keys

# Launch application
python run.py
```

---

## ⚙️ Configuration

Create `.env` file in `configs/` directory:

```env
# Core AI Configuration
NVIDIA_NIM_API_KEY=your_nvidia_nim_key
NVIDIA_NIM_BASE_URL=https://integrate.api.nvidia.com/v1

# Research Data Sources
ARXIV_API_BASE_URL=http://export.arxiv.org/api/query
SEMANTIC_SCHOLAR_API_KEY=your_semantic_scholar_key
NEWS_API_KEY=your_news_api_key
SERP_API_KEY=your_serp_api_key

# Application Security
SECRET_KEY=your_secret_key
FLASK_ENV=development
```

---

## 🌊 API Endpoints

### Research Interface

- `GET /` → Main research dashboard
- `POST /chat` → Send query to AI agent
- `POST /new-session` → Initialize research session

### Data Management

- `GET /research/<session_id>` → View research results
- `POST /export/<session_id>` → Export findings

---

## 💡 Usage Workflow

### 1. **Research Initiation** 🔍

Start with any research question or topic of interest

### 2. **AI Agent Processing** 🧠

The agent automatically selects and uses appropriate research tools

### 3. **Multi-Source Gathering** 📖

Information collected from academic papers, news, and web sources

### 4. **Synthesis & Export** 📝

Results synthesized with proper citations and exportable formats

---

## 🎯 Applications

### 📊 **Academic Research**

Literature reviews, citation discovery, research gap analysis

### 📰 **Journalism & Media**

Fact-checking, background research, trend analysis

### 🏢 **Business Intelligence**

Market research, competitive analysis, industry insights

### 🎓 **Educational Support**

Study assistance, concept exploration, source verification

---

## 🔧 Development Phases

### 🏗️ **Foundation** (Week 1)

- [x] Flask application architecture
- [x] Basic ReAct agent implementation
- [x] Wikipedia integration & chat interface

### ⚡ **Expansion** (Week 2)

- [x] arXiv & web search tools
- [x] Semantic Scholar & news integration
- [x] Enhanced UI with error handling

### 🚀 **Advanced Features**

- [ ] Database integration for persistence
- [ ] Advanced citation formatting (APA, MLA, Chicago)
- [ ] PDF/Word export capabilities
- [ ] Collaborative research features

---

## 🤝 Contributing

We welcome contributions! Here's how to get involved:

1. **Fork** the repository
2. **Create** feature branch (`git checkout -b feature/amazing-tool`)
3. **Commit** changes (`git commit -am 'Add amazing research tool'`)
4. **Push** to branch (`git push origin feature/amazing-tool`)
5. **Submit** Pull Request

---

## 🔍 Testing

```bash
# Run comprehensive tests
python -m pytest tests/

# Test specific components
python -m pytest tests/test_agents.py    # Agent functionality
python -m pytest tests/test_tools.py     # Tool integrations
```

---

## ⚠️ Troubleshooting

### Common Issues & Solutions

| Issue              | Solution                               |
| ------------------ | -------------------------------------- |
| **API Key Errors** | Verify all keys in `.env` file         |
| **Tool Failures**  | Check internet connection & API limits |
| **Agent Timeouts** | Review LLM configuration settings      |

---

## 📄 License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

- **🔗 LangChain Framework** for agent architecture
- **🚀 NVIDIA NIM** for advanced AI capabilities
- **📚 Academic APIs** (arXiv, Semantic Scholar)
- **🌐 Web Services** (SerpAPI, News APIs)

---

<div align="center">
  <strong>🔬 Revolutionizing Research with AI Intelligence</strong>
  <br><br>
  <img src="https://img.shields.io/badge/🎯_Status-Under_Development-orange?style=for-the-badge" alt="Under Development">
  <img src="https://img.shields.io/badge/🚀_Goal-Research_Revolution-blue?style=for-the-badge" alt="Research Revolution">
</div>
