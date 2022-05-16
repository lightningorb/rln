from __future__ import print_function, absolute_import, division
import json
from invoke import task
import arrow
import requests

try:
    from urwid import *
    import json
    from collections import defaultdict
    import urwid
    import os
except:
    pass

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
        raise ExitMainLoop()


@task
def balance(c):

    info = json.loads(c.run("lncli getinfo", hide=True).stdout)
    walletbal = json.loads(c.run("lncli walletbalance", hide=True).stdout)
    chanbal = json.loads(c.run("lncli channelbalance", hide=True).stdout)
    price = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()[
        "bpi"
    ]["USD"]["rate_float"]

    blank = Divider()

    chan_items = []

    for k, v in chanbal.items():
        sats = v["sat"] if type(v) is dict else v
        if sats != "0":
            chan_items.append(
                Text([k, ": ", f"丰{int(sats):,}"]),
            )

    gt = (
        int(chanbal["balance"])
        + int(walletbal["total_balance"])
        + int(chanbal["pending_open_balance"])
    )
    gtusd = gt / 1e8 * price

    items = (
        [
            AttrWrap(Divider("=", 1), "bright"),
            Text([f"On-Chain:"]),
            AttrWrap(Divider("-", 0, 1), "bright"),
            Text(f"Total balance: 丰{int(walletbal['total_balance']):,}"),
            Text(f"Confirmed balance: 丰{int(walletbal['confirmed_balance']):,}"),
            Text(f"Unconfirmed balance: 丰{int(walletbal['unconfirmed_balance']):,}"),
            AttrWrap(Divider("=", 1), "bright"),
            Text([f"Channel:"]),
            AttrWrap(Divider("-", 0, 1), "bright"),
        ]
        + chan_items
        + [
            AttrWrap(Divider("-", 0, 1), "bright"),
            Text([f"Grand Total balance: "]),
            Padding(
                Text(
                    [
                        (
                            "important",
                            f"丰{gt:,}",
                        ),
                    ]
                ),
                left=20,
            ),
            Padding(
                Text(
                    [
                        (
                            "important",
                            f" ${gtusd:,.2f}",
                        ),
                    ]
                ),
                left=20,
            ),
        ]
    )

    frame = Frame(
        AttrWrap(
            ListBox(SimpleListWalker(items)),
            "body",
        ),
        header=AttrWrap(
            Text((f"{info['alias']}  " " F8 exits.")),
            "header",
        ),
    )

    MainLoop(frame, palette, unhandled_input=unhandled).run()


@task
def forwards(c):
    price = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()[
        "bpi"
    ]["USD"]["rate_float"]
    info = json.loads(c.run("lncli getinfo", hide=True).stdout)
    blank = Divider()

    hist = json.loads(
        c.run(
            "lncli fwdinghistory --start_time=-6M --max_events=100000", hide=True
        ).stdout
    )["forwarding_events"]

    # hist = json.loads(open("data/forwards.json").read())["forwarding_events"]

    items = []
    total = 0

    for h in hist:
        dt = arrow.get(int(h["timestamp"])).format("YYYY-MM-DD HH:mm")
        total += (int(h["fee"]) / 1e8) * price
        items.append(
            Button(
                f"{dt:<10}          丰{int(h['fee']):<10,}      丰{int(h['amt_out']):<10,}       ${total:.2f}"
            )
        )

    items.append(
        Text(
            "Date                        Fee               Amount             Tot Fees"
        )
    )
    items = items[::-1]

    frame = Frame(
        AttrWrap(
            ListBox(SimpleListWalker(items)),
            "body",
        ),
        header=AttrWrap(
            Text((f"{info['alias']}  " " F8 exits.")),
            "header",
        ),
    )

    loop = MainLoop(frame, palette, unhandled_input=unhandled)
    loop.run()


@task
def connect(c):
    info = json.loads(c.run("lncli getinfo", hide=True).stdout)
    blank = Divider()

    def button_press(button):
        frame.footer = AttrWrap(Text(["Connecting..."]), "header")
        loop.draw_screen()
        cmd = c.run(f"lncli connect {edit.text}", hide=True, warn=True)
        if cmd.stderr:
            frame.footer = AttrWrap(Text([cmd.stderr.strip()]), "header")
        else:
            r = json.loads(cmd.stdout)
            if not r:
                frame.footer = AttrWrap(Text(["connected"]), "header")
            else:
                print(r)

    edit = Edit()

    frame = Frame(
        AttrWrap(
            ListBox(
                SimpleListWalker(
                    [
                        AttrWrap(Divider("=", 1), "bright"),
                        Text([f"Connect"]),
                        blank,
                        Text([f"Address: "]),
                        AttrWrap(
                            edit,
                            "editbx",
                            "editfc",
                        ),
                        AttrWrap(Divider("-", 0, 1), "bright"),
                        AttrWrap(Button("connect", button_press), "buttn", "buttnf"),
                    ]
                )
            ),
            "body",
        ),
        header=AttrWrap(
            Text((f"{info['alias']}  " " F8 exits.")),
            "header",
        ),
    )

    loop = MainLoop(frame, palette, unhandled_input=unhandled)
    loop.run()


@task
def open_channel(c):
    """
    Open a channel with another node, uses lncli
    """
    info = json.loads(c.run("lncli getinfo", hide=True).stdout)
    blank = Divider()

    def button_press(button):
        frame.footer = AttrWrap(Text(["Connecting..."]), "header")
        loop.draw_screen()
        cmd_str = f"lncli openchannel --node_key={node_key.text} --local_amt={local_amt.text} --sat_per_vbyte={sat_per_vbyte.text}"
        frame.footer = AttrWrap(Text([cmd_str]), "header")
        cmd = c.run(
            cmd_str,
            hide=True,
            warn=True,
        )
        if cmd.stderr:
            frame.footer = AttrWrap(Text([cmd.stderr.strip()]), "header")
        elif cmd.stdout:
            frame.footer = AttrWrap(Text([cmd.stdout.strip()]), "header")
        else:
            frame.footer = AttrWrap(Text(["No output"]), "header")

    node_key = Edit()
    local_amt = Edit()
    sat_per_vbyte = Edit("1")

    debug = urwid.Text("")

    def handler(widget, newtext):
        try:
            debug.set_text(f"丰{int(newtext):,}")
        except:
            pass

    key = connect_signal(local_amt, "change", handler)

    pad = lambda x: [Padding(Pile(x), left=2, right=2, min_width=20)]

    frame = Frame(
        AttrWrap(
            ListBox(
                SimpleListWalker(
                    [
                        AttrWrap(Divider("=", 1), "bright"),
                        Text([f"Open Channel"]),
                        blank,
                    ]
                    + pad(
                        [
                            Text([f"Node Key: "]),
                            blank,
                            Padding(
                                AttrWrap(
                                    node_key,
                                    "editbx",
                                    "editfc",
                                ),
                                width=67,
                            ),
                        ]
                    )
                    + [
                        blank,
                        AttrWrap(Divider("-", 0, 1), "bright"),
                    ]
                    + pad(
                        [
                            Text([f"Local Amount: "]),
                            blank,
                            Padding(
                                AttrWrap(
                                    local_amt,
                                    "editbx",
                                    "editfc",
                                ),
                                width=15,
                            ),
                            debug,
                        ]
                    )
                    + [blank, AttrWrap(Divider("-", 0, 1), "bright"), blank]
                    + pad(
                        [
                            Text([f"Sat per VByte: "]),
                            blank,
                            Padding(
                                AttrWrap(
                                    sat_per_vbyte,
                                    "editbx",
                                    "editfc",
                                ),
                                width=5,
                            ),
                        ]
                    )
                    + [
                        blank,
                        AttrWrap(Divider("-", 0, 1), "bright"),
                        blank,
                        Padding(
                            AttrWrap(
                                Button("Open Channel", button_press), "buttn", "buttnf"
                            ),
                            width=20,
                        ),
                    ]
                )
            ),
            "body",
        ),
        header=AttrWrap(
            Text((f"{info['alias']}  " " F8 exits.")),
            "header",
        ),
    )

    loop = MainLoop(frame, palette, unhandled_input=unhandled)
    loop.run()


@task
def close_channel(c):
    """
    Close a channel
    """
    info = json.loads(c.run("lncli getinfo", hide=True).stdout)
    blank = Divider()
    sat_per_vbyte = Edit("")

    pad = lambda x: [Padding(Pile(x), left=2, right=2, min_width=20)]

    channels = json.loads(c.run("lncli listchannels", hide=True).stdout)
    nodes = {
        n["pub_key"]: n for n in json.loads(open("data/graph.json").read())["nodes"]
    }
    items = pad(
        [
            Text([f"Sat per VByte: "]),
            blank,
            Padding(
                AttrWrap(
                    sat_per_vbyte,
                    "editbx",
                    "editfc",
                ),
                width=5,
            ),
            blank,
        ]
    )

    def button_press(b):
        frame.footer = AttrWrap(Text(["Closing..."]), "header")
        loop.draw_screen()
        txid, oi = b.channel_point.split(":")
        cmd = f"lncli closechannel --funding_txid {txid} --output_index {oi} --sat_per_vbyte {sat_per_vbyte.text}"
        frame.footer = AttrWrap(Text([cmd]), "header")
        loop.draw_screen()
        out = c.run(
            cmd,
            hide=True,
            warn=True,
        )
        if out.stderr:
            frame.footer = AttrWrap(Text([out.stderr.strip()]), "header")
        else:
            frame.footer = AttrWrap(Text([out.stdout.strip()]), "header")

    for ch in channels["channels"]:
        key = ch["remote_pubkey"]
        b = Button(nodes[key]["alias"], button_press)
        b.pubkey = key
        b.channel_point = ch["channel_point"]
        items.append(b)

    frame = Frame(AttrWrap(ListBox(SimpleListWalker(items)), "body"))

    loop = MainLoop(frame, palette, unhandled_input=unhandled)
    loop.run()
