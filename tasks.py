from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/app.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest src/tests -s", pty=True)

@task
def build(ctx):
    ctx.run("python3 src/logic/builder.py", pty=True)

@task
def pylint(ctx):
    ctx.run("poetry run pylint src", pty=True)
