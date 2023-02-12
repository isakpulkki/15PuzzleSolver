from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/app.py", pty=True)

@task
def test(ctx):
    ctx.run("python3 -m pytest src", pty=True)

@task
def build(ctx):
    ctx.run("python3 -m src.logic.builder", pty=True)