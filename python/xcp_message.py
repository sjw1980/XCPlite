
# 상수 정의
XCPTL_MAX_CTO_SIZE = 252  # 예시 크기

# 구조체 정의
class tXcpCtoMessage:
    def __init__(self, ctr, packet):
        self.dlc = len(packet)
        self.ctr = ctr
        self.packet = packet
        
		# 패킷 크기가 XCPTL_MAX_CTO_SIZE를 초과하지 않도록 함
        if self.dlc > XCPTL_MAX_CTO_SIZE:
            raise ValueError(f"패킷의 길이가 {XCPTL_MAX_CTO_SIZE} 바이트를 초과합니다.")

    def to_bytes(self):
        # dlc와 ctr을 2바이트로 변환
        dlc_bytes = self.dlc.to_bytes(2, byteorder='little')
        ctr_bytes = self.ctr.to_bytes(2, byteorder='little')
        
        # dlc, ctr, packet을 결합하여 반환
        return dlc_bytes + ctr_bytes + self.packet