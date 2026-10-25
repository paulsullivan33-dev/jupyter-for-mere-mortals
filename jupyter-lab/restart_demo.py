"""Show that a kernel holds state, and a restart destroys it."""
from jupyter_client.manager import KernelManager

km = KernelManager(kernel_name="python3")
km.start_kernel()
kc = km.client()
kc.start_channels()
kc.wait_for_ready()

def run(code):
    msg_id = kc.execute(code)
    out = []
    while True:
        msg = kc.get_iopub_msg()
        if msg["parent_header"].get("msg_id") != msg_id:
            continue
        kind = msg["msg_type"]
        if kind == "stream":
            out.append(msg["content"]["text"].strip())
        elif kind == "error":
            out.append(msg["content"]["ename"] + ": " +
                       msg["content"]["evalue"])
        elif kind == "status" and \
                msg["content"]["execution_state"] == "idle":
            break
    return " | ".join(out)

print('run  x = 41            ->', run("x = 41") or "(no output)")
print('run  print(x + 1)      ->', run("print(x + 1)"))
print("--- kernel restarts ---")
km.restart_kernel()
kc.wait_for_ready()
print('run  print(x)          ->', run("print(x)"))
km.shutdown_kernel()
print("the variable lived in the kernel, not in the notebook")
