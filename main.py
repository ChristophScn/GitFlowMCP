"""
FastMCP quickstart example.

cd to the `examples/snippets/clients` directory and run:
    uv run server fastmcp_quickstart stdio
"""

from mcp.server.fastmcp import FastMCP

import textwrap
import os

# Create an MCP server
mcp = FastMCP("GitFlowMCP")

@mcp.prompt()
def create_commit() -> str:
    """Create a git commit"""
    
    return textwrap.dedent("""
            Create a commit message by:
                1. Stage all changes
                2. Get the changes made using diff
                3. Write a concise summary of the changes
                4. Commit the changes with a git title and description
            """)


@mcp.tool()
def git_stage() -> str:
    """Stage all changes in the working directory"""
    command = "git add ."
    result = os.popen(command).read()
    return result


@mcp.tool()
def git_diff() -> str:
    """Get the changes made in the working directory"""
    command = "git --no-pager diff --staged"
    result = os.popen(command).read()
    return result

@mcp.tool()
def git_commit(title: str, message: str) -> str:
    """Commit the staged changes with a message"""
    command = f"git commit -m '{title}' -m '{message}'"
    result = os.popen(command).read()
    return result

