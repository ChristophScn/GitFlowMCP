from gitflowmcp import main

def test_run_command():
    stdout, stderr = main.run_command("echo hello")
    assert stdout == "hello"
    assert stderr == ""

    stdout, stderr = main.run_command(">&2 echo error")
    assert stdout == ""
    assert stderr == "error"

def test_environment_variables(monkeypatch):
    monkeypatch.setenv("DIRECTORY", "/etc")
    stdout, stderr = main.run_command("echo $DIRECTORY")
    assert stdout == "/etc"
    assert stderr == ""
