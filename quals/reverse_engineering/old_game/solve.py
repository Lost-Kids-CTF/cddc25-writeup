from pwn import *

# context.log_level = 'debug'

def get_conn():
    conn = remote("cddc2025-challs-nlb-579269aea83cde66.elb.ap-southeast-1.amazonaws.com", 6666)
    conn.recvuntil(b"> ")
    return conn

def execute(command: str, conn: remote) -> str:
    sleep(0.01)  # Adding a small delay to avoid overwhelming the server
    conn.sendline(command.encode())
    response = conn.recvuntil([b"> ", b"}"]).decode()
    print(f"Executed command: {command}, received response: {response.strip()}")
    return response.strip()

def traverse_and_flag(conn: remote) -> str:
    for k in range(9):
        execute("up", conn)
    for k in range(9):
        execute("left", conn)
    for i in range(10):
        for j in range(10):
            execute("flag", conn)
            if j < 9:
                if i % 2 == 0:
                    execute("right", conn)
                else:
                    execute("left", conn)
            elif i < 9:
                    execute("down", conn)
    for k in range(9):
        execute("up", conn)

def try_traverse(conn: remote, index: int) -> str:
    for i in range(10):
        for j in range(10):
            result = check_result(execute("flag", conn))
            if index == 2 and "CDDC" in result:
                return i, j, result
            if f"{index + 2}/3" in result:
                return i, j, result
            execute("flag", conn)
            if j < 9:
                if i % 2 == 0:
                    execute("right", conn)
                else:
                    execute("left", conn)
            elif i < 9:
                execute("down", conn)
    raise Exception("Traversal failed, did not find the expected result.")

def check_result(result: str) -> str:
    regex = r"ROUND .{3}"
    match = re.search(regex, result)
    if match:
        return match.group(0)
    else:
        return result

conn = get_conn()

for i in range(3):
    traverse_and_flag(conn)
    result = try_traverse(conn, i)
    print(f"Result found: {result}")
