SUBNET_MASK_24 = "255.255.255.0"
SUBNET_MASK_32 = "255.255.255.255"
INVERSE_MASK_24 = "0.0.0.255"
pcap01_file = "test01.pcap"
pcap12_file = "test12.pcap"

class bgp0:
  as_num = 20
  class iosv_0:
    class g0_0:
      name = "GigabitEthernet0/0"
      slot = 0
      ip_addr = "192.168.0.1"
      subnet_mask = SUBNET_MASK_24
    
  class iosv_1:
    class g0_0:
      name = "GigabitEthernet0/0"
      slot = 0
      ip_addr = "192.168.0.2"
      subnet_mask = SUBNET_MASK_24
    class g0_1:
      name = "GigabitEthernet0/1"
      slot = 1
      ip_addr = "192.168.1.2"
      subnet_mask = SUBNET_MASK_24

class bgp1:
  as_num = 10
  class iosv_2:
    class g0_0:
      name = "GigabitEthernet0/0"
      slot = 0
      ip_addr = "192.168.1.3"
      subnet_mask = SUBNET_MASK_24
    class loopback0:
      name = "Loopback 0"
      ip_addr = "10.0.0.1"
      subnet_mask = SUBNET_MASK_32