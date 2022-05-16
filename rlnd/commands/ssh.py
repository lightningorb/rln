import os
from invoke import task


@task
def ssh(c):
    """
    ssh into the current node. This might not work with windows yet.
    """
    os.system(
        f"ssh -o ServerAliveInterval=5 -i {c.connect_kwargs['key_filename'][0]} {c.user}@{c.host}"
    )


@task
def mosh(c):
    """
    mosh into the current node. This might not work with windows yet.
    """
    ssh_cmd = (
        f"--ssh='ssh -i {c.connect_kwargs['key_filename'][0]}'"
        if c.connect_kwargs.get("key_filename")
        else ""
    )
    cmd = f"mosh --no-init --predict=experimental {ssh_cmd} --port 60000 {c.user}@{c.host}"
    print(cmd)
    os.system(cmd)


@task
def install_mosh(c):
    """
    Install mosh, and configure ufw to allow connection on port 60k.
    """
    c.sudo("apt-get install mosh -y")
    if c.run("test -f /usr/sbin/ufw", warn=True).ok:
        c.sudo("ufw allow 60000")


@task
def get(c, remote, local):
    c.get(remote, local)


@task
def put(c, local, remote):
    c.put(local, remote)
