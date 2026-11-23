---
name: linkedin
description: >
  LinkedIn MCP Server — Read LinkedIn profiles, research companies, search jobs,
  manage messages & connection requests directly from Antigravity using your
  local browser session. No official API key required; uses Patchright browser
  automation against your logged-in LinkedIn account.
triggers:
  - "linkedin"
  - "find profile"
  - "company research linkedin"
  - "linkedin jobs"
  - "send connection"
  - "linkedin message"
  - "mcp-server-linkedin"
---

# LinkedIn MCP Skill

## What It Does
Connects Antigravity to LinkedIn via the `mcp-server-linkedin` MCP server
(open-source, Apache 2.0, 4,285 ⭐). It drives your **local browser session**
(Patchright/Chromium) — so it uses your existing login with **no API keys**.

## Tools Provided
| Tool | Description |
|------|-------------|
| `read_profile` | Fetch full profile data for any LinkedIn URL |
| `research_company` | Pull company overview, headcount, industry, jobs |
| `find_jobs` | Search job listings by keyword, location, filters |
| `manage_conversations` | Read & send LinkedIn messages |
| `send_connection_request` | Send personalised connection requests |
| `get_my_profile` | Fetch your own profile summary |

## How to Trigger in Antigravity
Just describe what you need naturally:
- *"Look up the LinkedIn profile of [Name] at [Company]"*
- *"Find ML engineering jobs in Bangalore on LinkedIn"*
- *"Send a connection request to [Name] mentioning our shared interest in AI"*
- *"Research the company OpenAI on LinkedIn"*

## First-Time Setup
On first run a Chromium browser window opens automatically.  
**Log in to LinkedIn** in that window — your session is then cached at
`~/.linkedin-mcp/patchright-browsers` for future headless use.

## MCP Config Entry (already added to mcp_config.json)
```json
"mcp-server-linkedin": {
  "command": "uvx",
  "args": ["mcp-server-linkedin@latest"],
  "env": { "UV_HTTP_TIMEOUT": "300" }
}
```

## ⚠️ LinkedIn ToS Warning
This tool automates your personal LinkedIn session. LinkedIn's Terms of Service
prohibit automated scraping. Use responsibly:
- Do NOT run on a primary high-value account without understanding the ban risk
- Avoid bulk scraping hundreds of profiles in rapid succession
- Prefer personal research & networking tasks over mass automation

## Security Scan Result
- **OpenSSF Score**: 5.2/10 (community project, no CVEs)
- **SkillSpector Static Scan**: SAFE — no malicious code, no credential exfiltration, no reverse shell patterns
- **Supply Chain**: Apache 2.0, signed commits, PyPI-distributed

## Source
- GitHub: https://github.com/stickerdaniel/linkedin-mcp-server
- PyPI: https://pypi.org/project/mcp-server-linkedin/

