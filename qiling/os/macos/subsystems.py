#!/usr/bin/env python3
# 
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
# Built on top of Unicorn emulator (www.unicorn-engine.org)

# find source code in https://github.com/doadam/xnu-4570.1.46/master/BUILD/obj/RELEASE_X86_64/osfmk/RELEASE/mach/mach_host_server.c
from struct import pack, unpack
from qiling.os.macos.mach_port import *
from qiling.os.macos.const import *


class MachHostServer():

    def __init__(self, ql):
        self.ql = ql
        self.system_rpc = {
            200: self.host_info,
            206: self.host_get_clock_service
        }
        pass

    def host_info(self, in_header, in_content):
        # parse request
        out_msg = MachMsg(self.ql)
        if len(in_content) < 16:
            self.ql.nprint("Error in Host info SubSystem -hostinfo()")
            raise
        ndr = unpack("<Q", in_content[:8])[0]
        flavor = unpack("<L", in_content[8:12])[0]
        host_info_outCnt = unpack("<L", in_content[12:16])[0]
        # may be we need wapper a func in kernel func ,but it is also a huge projrct 
        # gen reply

        if flavor == HOST_BASIC_INFO:
            out_msg.header.msgh_bits = 4608
            out_msg.header.msgh_size = 88
            out_msg.header.msgh_remote_port = 0
            out_msg.header.msgh_local_port = self.ql.macho_mach_port.name
            out_msg.header.msgh_voucher_port = 0
            out_msg.header.msgh_id = 300

            out_msg.content += pack("<Q", 0x100000000)      # NDR
            out_msg.content += pack("<L", 0x0)              # ret code / KERN SUCCESS
            out_msg.content += pack("<L", host_info_outCnt) # host info output count 

            # host info out
            out_msg.content += pack("<L", 0x2)              # max_cpus
            out_msg.content += pack("<L", 0x2)              # avail_cpus
            out_msg.content += pack("<L", 0x80000000)       # memory_size
            out_msg.content += pack("<L", 0x7)              # cpu_type
            out_msg.content += pack("<L", 0x4)              # cpu_subtype
            if host_info_outCnt > 5:
                out_msg.content += pack("<L", 0x1)          # cpu_threadtype
                out_msg.content += pack("<L", 0x2)          # physical_cpu
                out_msg.content += pack("<L", 0x2)          # physical_cpu_max
                out_msg.content += pack("<L", 0x4)          # logic_cpu
                out_msg.content += pack("<L", 0x4)          # logic_cpu_max
                out_msg.content += pack("<Q", 0x400000000)  # max_mem
            
        elif flavor == HOST_PRIORITY_INFO:
            out_msg.header.msgh_bits = 4608
            out_msg.header.msgh_size = 72
            out_msg.header.msgh_remote_port = 0
            out_msg.header.msgh_local_port = self.ql.macho_mach_port.name
            out_msg.header.msgh_voucher_port = 0
            out_msg.header.msgh_id = 300

            out_msg.content += pack("<Q", 0x100000000)      # NDR
            out_msg.content += pack("<L", 0x0)              # ret code / KERN SUCCESS
            out_msg.content += pack("<L", host_info_outCnt) # host info output count 
            # host info out
            out_msg.content += pack("<L", 0x50)             # kernel_priority = MINPRI_KERNEL;
            out_msg.content += pack("<L", 0x50)             # system_priority = MINPRI_KERNEL;
            out_msg.content += pack("<L", 0x40)             # server_priority = MINPRI_RESERVED;
            out_msg.content += pack("<L", 0x1f)             # user_priority = BASEPRI_DEFAULT;
            out_msg.content += pack("<L", 0x0)              # depress_priority = DEPRESSPRI;
            out_msg.content += pack("<L", 0x0)              # idle_priority = IDLEPRI;
            out_msg.content += pack("<L", 0x0)              # minimum_priority = MINPRI_USER;
            out_msg.content += pack("<L", 0x4f)             # maximum_priority = MAXPRI_RESERVED
        else:
            self.ql.nprint("Host flavor not support")
            raise
        return out_msg

    def host_get_clock_service(self, in_header, in_content):
        out_msg = MachMsg(self.ql)

        out_msg.header.msgh_bits = 0x80001200
        out_msg.header.msgh_size = 0x00000028
        out_msg.header.msgh_remote_port = 0x00000000
        out_msg.header.msgh_local_port = self.ql.macho_mach_port.name
        out_msg.header.msgh_voucher_port = 0
        out_msg.header.msgh_id = 306

        out_msg.content = pack("<L", 0x1)

        out_msg.trailer = b''
        out_msg.trailer += pack("<L", self.ql.macho_port_manager.clock_port.name)       # clock port name 
        out_msg.trailer += pack("<L", 0x0)                                              # pad1
        out_msg.trailer += pack("<H", 0x0)                                              # pad2
        out_msg.trailer += pack("<B", 0x11)                                             # disposition
        out_msg.trailer += pack("<B", 0x0)                                              # type
        out_msg.trailer += pack("<L", 0x0)                                              # pad end
        
        return out_msg


class MachTaskServer():

    def __init__(self, ql):
        self.ql = ql

    def semaphore_create(self, in_header, in_content):
        out_msg = MachMsg(self.ql)

        out_msg.header.msgh_bits = 0x80001200
        out_msg.header.msgh_size = 0x00000028
        out_msg.header.msgh_remote_port = 0x00000000
        out_msg.header.msgh_local_port = self.ql.macho_mach_port.name
        out_msg.header.msgh_voucher_port = 0
        out_msg.header.msgh_id = 3518

        out_msg.content = pack("<L", 0x1)

        out_msg.trailer = b''
        out_msg.trailer += pack("<L", self.ql.macho_port_manager.semaphore_port.name)       # clock port name 
        out_msg.trailer += pack("<L", 0x0)                                                  # pad1
        out_msg.trailer += pack("<H", 0x0)                                                  # pad2
        out_msg.trailer += pack("<B", 0x11)                                                 # disposition
        out_msg.trailer += pack("<B", 0x0)                                                  # type
        out_msg.trailer += pack("<L", 0x0)                                                  # pad end

        return out_msg
