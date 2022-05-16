from invoke import task
from os import path
import json

get_conf_dir = lambda: path.normpath(path.join(path.dirname(__file__), "..", "confs"))
get_conf_file_path = lambda x: path.join(get_conf_dir(), x)


@task
def resources(c):
    """
    List a bunch of very useful external resources, to improve your node's
    ranking.
    """
    info = json.loads(c.run("lncli getinfo", hide=True).stdout)
    oneml = f"https://1ml.com/node/{info['identity_pubkey']}"

    import urwid
    import urwid.raw_display

    blank = urwid.Divider()

    def main():
        text_header = (
            f"{info['alias']}  " "UP / DOWN / PAGE UP / PAGE DOWN scroll.  F8 exits."
        )

        def button_press(button):
            frame.footer = urwid.AttrWrap(
                urwid.Text(["Pressed: ", button.get_label()]), "header"
            )

        radio_button_group = []

        listbox_content = [
            blank,
            urwid.Padding(
                urwid.Text(
                    [
                        f"This is an experimental UI.",
                    ]
                )
            ),
            blank,
            urwid.Padding(
                urwid.Text(
                    [
                        f"lnd version: {info['version']}",
                    ]
                )
            ),
            blank,
            urwid.Padding(
                urwid.Text(
                    [
                        f"Public Key Identity: {info['identity_pubkey']}",
                    ]
                )
            ),
            blank,
            urwid.Padding(
                urwid.Text(
                    [
                        f"Pending channels: {info['num_pending_channels']}",
                    ]
                )
            ),
            urwid.Padding(
                urwid.Text(
                    [
                        f"Active channels: {info['num_active_channels']}",
                    ]
                )
            ),
            urwid.Padding(
                urwid.Text(
                    [
                        f"Inactive channels: {info['num_inactive_channels']}",
                    ]
                )
            ),
            urwid.Padding(
                urwid.Text(
                    [
                        f"Peers: {info['num_peers']}",
                    ]
                )
            ),
            blank,
            urwid.Padding(
                urwid.Text(
                    [
                        ("important", oneml),
                        f"Good place to get started, to become visible to the network. We recommend opening a 200k satoshis channel with them.",
                    ]
                ),
                left=2,
                right=2,
                min_width=20,
            ),
            blank,
            urwid.Padding(
                urwid.Text(
                    [
                        "Excellent place to give you actionable feedback to improve your node's ranking ",
                        (
                            "important",
                            f"https://terminal.lightning.engineering/#/{info['identity_pubkey']}",
                        ),
                    ]
                ),
                left=2,
                right=2,
                min_width=20,
            ),
            blank,
            urwid.Padding(
                urwid.Text(
                    [
                        "Provides you with a ton of information about your node, and channels ",
                        (
                            "important",
                            f"https://amboss.space/node/{info['identity_pubkey']}",
                        ),
                    ]
                ),
                left=2,
                right=2,
                min_width=20,
            ),
            blank,
            urwid.Padding(
                urwid.Text(
                    [
                        "Get insights in to your Terminal score and improve your ranking. ",
                        (
                            "important",
                            f"https://lnrouter.app/scores/terminal?id={info['identity_pubkey']}",
                        ),
                    ]
                ),
                left=2,
                right=2,
                min_width=20,
            ),
            blank,
            urwid.Padding(
                urwid.Text(
                    [
                        "Creates an great chart, and simulates changes to centrality when connecting to other peers ",
                        (
                            "important",
                            f"https://lnnodeinsight.com/?peer_network={info['alias']}",
                        ),
                    ]
                ),
                left=2,
                right=2,
                min_width=20,
            ),
        ]

        header = urwid.AttrWrap(urwid.Text(text_header), "header")
        listbox = urwid.ListBox(urwid.SimpleListWalker(listbox_content))
        frame = urwid.Frame(urwid.AttrWrap(listbox, "body"), header=header)

        palette = [
            ("body", "black", "light gray", "standout"),
            ("reverse", "light gray", "black"),
            ("header", "white", "dark red", "bold"),
            ("important", "dark blue", "light gray", ("standout", "underline")),
            ("editfc", "white", "dark blue", "bold"),
            ("editbx", "light gray", "dark blue"),
            ("editcp", "black", "light gray", "standout"),
            ("bright", "dark gray", "light gray", ("bold", "standout")),
            ("buttn", "black", "dark cyan"),
            ("buttnf", "white", "dark blue", "bold"),
        ]

        def unhandled(key):
            if key == "f8":
                raise urwid.ExitMainLoop()

        urwid.MainLoop(frame, palette, unhandled_input=unhandled).run()

    main()


@task()
def suez(c):
    """
    Run the suez app from src/suez
    to find out more: https://github.com/prusnak/suez
    """
    with c.cd("src/suez"):
        c.run("poetry run ./suez")


@task()
def stream_htlcs(c):
    with c.cd("src/stream-lnd-htlcs"):
        c.run("python3 ./stream-lnd-htlcs.py")


@task(
    help=dict(
        from_path="the source path, on remote host",
        to_path="the dest path, on local host",
    )
)
def get(c, from_path, to_path):
    """
    Transfer a file from remote to local
    """

    c.get(from_path, to_path)


@task
def update_fees(c):
    """
    Run a fee update with policy on every channel
    """
    from tabulate import tabulate

    lerp = lambda a, b, t: a + (b - a) * t
    table = []

    channels = json.loads(c.run("lncli listchannels", hide=True).stdout)
    peers = json.loads(c.run("lncli listpeers", hide=True).stdout)
    for chan in channels["channels"]:
        lb, rb = int(chan["local_balance"]), int(chan["remote_balance"])
        ca = lb + rb
        if ca:
            r = rb / ca
            fee_rate = lerp(0, 2000, r)
            table.append([lb, rb, ca, r, fee_rate])
            if (
                chan["remote_pubkey"]
                == "021c97a90a411ff2b10dc2a8e32de2f29d2fa49d41bfbb52bd416e460db0747d0d"
            ):
                c.run(
                    f"""lncli updatechanpolicy --base_fee_msat 0 --fee_rate {2500/1e6} --time_lock_delta 144 --chan_point {chan['channel_point']}"""
                )
            else:
                c.run(
                    f"""lncli updatechanpolicy --base_fee_msat 0 --fee_rate {fee_rate/1e6} --time_lock_delta 144 --chan_point {chan['channel_point']}"""
                )

    print(tabulate(table, headers=["local", "remote", "cap", "ratio", "fee rate"]))


@task
def channel_balance(c):
    """
    Report on whether node liquidity is balanced
    """
    total_in, total_out, channels = (
        0,
        0,
        json.loads(c.run("lncli listchannels", hide=True).stdout),
    )
    for chan in channels["channels"]:
        total_out += int(chan["local_balance"])
        total_in += int(chan["remote_balance"])
    print(f"inbound:  {total_in:,}, outbound: {total_out:,}")
    if total_in > total_out:
        print("Inbound liquidity is higher than outbound")
    else:
        print("Outbound liquidity is higher than inbound")
    print(
        f"Please increase {['in','out'][total_in > total_out]}bound liquidity by, or decrease {['in','out'][total_in < total_out]}bound by: 丰{abs(total_in-total_out):,}"
    )
