import socket
import xcp_header
from xcp_message import tXcpCtoMessage


def create_xcp_connect_command():
    return tXcpCtoMessage(ctr=0, packet=xcp_header.CC_CONNECT.to_bytes(1, byteorder='little'))

# UDP 소켓 생성 및 데이터 전송
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 5555)

try:
    connect_message = create_xcp_connect_command()
    data = connect_message.to_bytes()    

    # 데이터 전송
    print(f'Sending: {data}')
    sent = sock.sendto(data, server_address)
finally:
    # 소켓 닫기
    print('Closing socket')
    sock.close()