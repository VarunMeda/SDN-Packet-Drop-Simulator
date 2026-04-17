from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

mac_to_port = {}

def _handle_ConnectionUp(event):
    log.info("Switch connected")

def _handle_PacketIn(event):
    packet = event.parsed
    dpid = event.connection.dpid
    in_port = event.port

    if not packet.parsed:
        return

    # Learn MAC
    mac_to_port[(dpid, packet.src)] = in_port

    ip = packet.find('ipv4')

    # 🚨 DROP RULE: h1 → h3
    if ip is not None:
        src = ip.srcip.toStr()
        dst = ip.dstip.toStr()

        if src == "10.0.0.1" and dst == "10.0.0.3":
            log.info(f"🚫 Installing DROP rule for {src} → {dst}")

            msg = of.ofp_flow_mod()
            msg.match = of.ofp_match()
            msg.match.dl_type = 0x0800  # IPv4
            msg.match.nw_src = ip.srcip
            msg.match.nw_dst = ip.dstip

            # No action = DROP
            event.connection.send(msg)
            return

    # ✅ NORMAL FORWARDING
    if (dpid, packet.dst) in mac_to_port:
        out_port = mac_to_port[(dpid, packet.dst)]

        # Install forwarding rule
        msg = of.ofp_flow_mod()
        msg.match = of.ofp_match.from_packet(packet, in_port)
        msg.actions.append(of.ofp_action_output(port=out_port))
        event.connection.send(msg)

    else:
        out_port = of.OFPP_FLOOD

    # Send packet
    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.in_port = in_port
    msg.actions.append(of.ofp_action_output(port=out_port))

    event.connection.send(msg)

def launch():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)