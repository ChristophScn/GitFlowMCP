"""
FastMCP quickstart example.

cd to the `examples/snippets/clients` directory and run:
    uv run server fastmcp_quickstart stdio
"""

from mcp.server.fastmcp import FastMCP

import textwrap
import subprocess
import typer

# Create an MCP server
mcp = FastMCP("GitFlowMCP")

def run_command(command: str) -> tuple[str, str]:
    """Run a shell command and return the stdout and stderr"""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip(), result.stderr.strip()

@mcp.prompt()
def create_commit() -> str:
    """Create a git commit"""
    
    return textwrap.dedent("""
            Create a commit by:
                1. Stage all changes
                2. Get the changes made using diff
                3. Write a concise summary of the changes
                4. Commit the changes with a git title and description
            """)


@mcp.tool()
def git_stage() -> str:
    """Stage all changes in the working directory"""
    stdout, stderr = run_command("git add .")
    return stdout


@mcp.tool()
def git_diff() -> str:
    """Get the changes made in the working directory"""
    stdout, stderr = run_command("git --no-pager diff --staged")
    return stdout

@mcp.tool()
def git_commit(title: str, message: str) -> str:
    """Commit the staged changes with a message"""
    stdout, stderr = run_command(f"git commit -m '{title}' -m '{message}'")
    return stdout

@mcp.tool()
def cwd() -> str:
    """Get the current working directory"""
    stdout, stderr = run_command("cd $DIRECTORY && pwd")
    return stdout

# Typer CLI app
cli = typer.Typer()

@cli.command()
def run():
    """Run the mcp server"""
    mcp.run()

if __name__ == "__main__":
    cli()