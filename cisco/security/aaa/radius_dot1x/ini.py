from ipaddress import ip_interface
pcap_file0 = "test0.pcap"
pcap_file1 = "test1.pcap"
wpa_supplicant_path = "/etc/wpa_supplicant/wpa_supplicant.conf"

class ex_conn0:
   pass

class ex_conn1:
   pass
class sw_0:
   pass
class iosvl2_0:
   class vlan:
      num = 10
      ip_addr = ip_interface("192.168.1.100/24")
   class g0_0:
      name = "GigabitEthernet0/0"
   class g0_1:
      name = "GigabitEthernet0/1"
      # no switchport
      ip_addr = ip_interface("192.168.0.254/24")
      class radius_auth:
         group_name = "RAD-GROUP"
         server_name = "RADIUS-SERVER01"
         password = "secret02"
         key = "key002"
   class g0_2:
      name = "GigabitEthernet0/2"
      # no switchport
      ip_addr = ip_interface("192.168.2.254/24")

class radius:
   init_password = "testing123"
   user_id = "alice"
   password = "password01"
   auth_port = 1812
   acc_port = 1813

class ubuntu_0:
    class ens2:
       pass
    class ens3:
      ip_addr = ip_interface("192.168.0.1/24")
class ubuntu_1:
    class ens2:
       pass
    class ens3:
      ip_addr = ip_interface("192.168.1.2/24")
      class radius_auth:
         key = "key003"

class server_0:
   class eth0:
      ip_addr = ip_interface("192.168.2.1/24")