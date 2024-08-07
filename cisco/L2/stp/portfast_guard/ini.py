SUBNET_MASK_24 = "255.255.255.0"
INVERSE_MASK_24 = "0.0.0.255"
pcap01_file = "test01.pcap"
pcap12_file = "test12.pcap"
pcap20_file = "test20.pcap"
vlan_num = 10

class iosvl2_0:
   stp_priority = 4096
   class g0_0:
      name = "GigabitEthernet0/0"
   class g0_1:
      name = "GigabitEthernet0/1"
   class g0_2:
      name = "GigabitEthernet0/2"
   class g0_3:
      name = "GigabitEthernet0/3"

class iosvl2_1:
   stp_priority = 8192
   class g0_0:
      name = "GigabitEthernet0/0"
   class g0_1:
      name = "GigabitEthernet0/1"

class iosvl2_2:
   stp_priority = 12288
   class g0_0:
      name = "GigabitEthernet0/0"
   class g0_1:
      name = "GigabitEthernet0/1"
   class g0_2:
      name = "GigabitEthernet0/2"

class iosvl2_3:
   stp_priority = 0
   class g0_0:
      name = "GigabitEthernet0/0"


class server_0:
   class eth0:
      ip_addr = "192.168.0.1"
      subnet_mask = SUBNET_MASK_24

class server_1:
   class eth0:
      ip_addr = "192.168.0.2"
      subnet_mask = SUBNET_MASK_24