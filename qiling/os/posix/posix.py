#!/usr/bin/env python3
# 
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
# Built on top of Unicorn emulator (www.unicorn-engine.org) 

from unicorn.arm64_const import *
from unicorn.arm_const import *
from unicorn.mips_const import *
from unicorn.x86_const import *

from qiling.const import *

class QlPosixManager:
    
    def __init__(self, ql):
        self.ql = ql
    
    # get syscall
    def get_syscall(self):
        if self.ql.arch == QL_ARM64:
            if self.ql.ostype == QL_MACOS:
                syscall_num = UC_ARM64_REG_X16
            else:
                syscall_num = UC_ARM64_REG_X8
        elif self.ql.arch == QL_ARM:
            syscall_num = UC_ARM_REG_R7
        elif self.ql.arch == QL_MIPS32:
            syscall_num = UC_MIPS_REG_V0        
        elif self.ql.arch == QL_X86:
            syscall_num = UC_X86_REG_EAX
        elif self.ql.arch == QL_X8664:
            syscall_num = UC_X86_REG_RAX           

        return self.ql.register(syscall_num)
    
    # get syscall
    def get_syscall_param(self):
        if self.ql.arch == QL_ARM64:
            param0 = self.ql.register(UC_ARM64_REG_X0)
            param1 = self.ql.register(UC_ARM64_REG_X1)
            param2 = self.ql.register(UC_ARM64_REG_X2)
            param3 = self.ql.register(UC_ARM64_REG_X3)
            param4 = self.ql.register(UC_ARM64_REG_X4)
            param5 = self.ql.register(UC_ARM64_REG_X5)
        elif self.ql.arch == QL_ARM:
            param0 = self.ql.register(UC_ARM_REG_R0)
            param1 = self.ql.register(UC_ARM_REG_R1)
            param2 = self.ql.register(UC_ARM_REG_R2)
            param3 = self.ql.register(UC_ARM_REG_R3)
            param4 = self.ql.register(UC_ARM_REG_R4)
            param5 = self.ql.register(UC_ARM_REG_R5)
        elif self.ql.arch == QL_MIPS32:
            param0 = self.ql.register(UC_MIPS_REG_A0)
            param1 = self.ql.register(UC_MIPS_REG_A1)
            param2 = self.ql.register(UC_MIPS_REG_A2)
            param3 = self.ql.register(UC_MIPS_REG_A3)
            param4 = self.ql.register(UC_MIPS_REG_SP)
            param4 = param4 + 0x10
            param5 = self.ql.register(UC_MIPS_REG_SP)
            param5 = param5 + 0x14
        elif self.ql.arch == QL_X86:
            param0 = self.ql.register(UC_X86_REG_EBX)
            param1 = self.ql.register(UC_X86_REG_ECX)
            param2 = self.ql.register(UC_X86_REG_EDX)
            param3 = self.ql.register(UC_X86_REG_ESI)
            param4 = self.ql.register(UC_X86_REG_EDI)
            param5 = self.ql.register(UC_X86_REG_EBP)
        elif self.ql.arch == QL_X8664:
            param0 = self.ql.register(UC_X86_REG_RDI)
            param1 = self.ql.register(UC_X86_REG_RSI)
            param2 = self.ql.register(UC_X86_REG_RDX)
            param3 = self.ql.register(UC_X86_REG_R10)
            param4 = self.ql.register(UC_X86_REG_R8)
            param5 = self.ql.register(UC_X86_REG_R9)                    
        
        return param0, param1, param2, param3, param4, param5