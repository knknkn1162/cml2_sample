from .device import Device
import time
from . import parse, wait
import sys

# populate
def populate_vlan(device: Device, count: int):
  @wait.retry(count=50, result=count, sleep_time=5)
  def _populate_vlan(device: Device):
    return parse.count_vlan(device)
  return _populate_vlan(device)

def populate_up(device: Device, count: int):
  @wait.retry(count=30, result=count, sleep_time=3)
  def _populate_up(device: Device):
    return parse.count_up_interfaces(device)
  
  return _populate_up(device)

def populate_rip(device: Device, count: int, sleep_time=5):
  @wait.retry(count=30, result=count, sleep_time=sleep_time)
  def _populate_rip(device: Device):
    return parse.count_route_code(device, 'rip')
  return _populate_rip(device)

@wait.retry(count=30, result=1, sleep_time=5)
def populate_static(device: Device):
  return parse.count_route_code(device, 'static')

def populate_ospf(device: Device, count: int):
  @wait.retry(count=30, result=count, sleep_time=5)
  def _populate_ospf(device: Device):
    device.show_ospf_neighbor()
    return parse.count_route_code(device, 'ospf')
  return _populate_ospf(device)

def populate_protocol(device: Device, code: str, count: int):
  @wait.retry(count=30, result=count, sleep_time=5)
  def _populate_protocol(device: Device):
    return parse.count_route_code(device, code=code)
  return _populate_protocol(device)

def populate_router_ping(device: Device, target_ip: str, sleep_time=3, hook:list[str]=[]):
  @wait.retry(count=30, result=0, sleep_time=sleep_time)
  def _populate_router_ping(device: Device):
    device.execs(hook)
    return parse.router_ping(device, target_ip)
  return _populate_router_ping(device)

def populate_server_ping(device: Device, target_ip: str, count=5):
  @wait.retry(count=30, result=0, sleep_time=3)
  def _server_ping(device: Device):
    return device.server_ping(target_ip, count)
  return _server_ping(device)

def populate_trunk(device: Device, count: int):
  @wait.retry(count=30, result=count, sleep_time=3)
  def _populate_trunk(device: Device):
    return parse.count_trunk(device)
  return _populate_trunk(device)

def _populate_stp_status(device: Device, vlan_num: int, count: int, status):
  @wait.retry(count=30, result=count, sleep_time=5)
  def __populate_stp_status(device: Device):
    return parse.count_stp_status(device, vlan_num, status)
  return __populate_stp_status(device)

def populate_stp_blocking(device: Device, vlan_num: int, count: int):
  return _populate_stp_status(device, vlan_num, count, status='blocking')

def populate_stp_forwarding(device: Device, vlan_num: int, count: int):
  return _populate_stp_status(device, vlan_num, count, status='forwarding')

def populate_stp(device: Device, vlan_num: int, count: int):
  @wait.retry(count=30, result=count, sleep_time=5)
  def _populate_stp(device: Device):
    return parse.count_stp_status(device, vlan_num, 'blocking') + parse.count_stp_status(device, vlan_num, 'forwarding')
  return _populate_stp(device)

def populate_etherchannel(device: Device, count: int, protocol: str):
  @wait.retry(count=30, result=count, sleep_time=5)
  def _populate_etherchannel(device: Device):
    return parse.count_etherchannel(device, status='P', protocol=protocol)
  return _populate_etherchannel(device)

def populate_eigrp(device: Device, group: int, count: int):
  @wait.retry(count=30, result=count, sleep_time=5)
  def _populate_eigrp(device: Device):
    return parse.count_eigrp_neighbors(device, group)
  return _populate_eigrp(device)

def seconds(secs):
  print(f"wait for {secs}[s]")
  sys.stdout.flush()
  time.sleep(secs)