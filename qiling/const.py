#!/usr/bin/env python3
# 
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
# Built on top of Unicorn emulator (www.unicorn-engine.org) 

QL_X86 = 1
QL_X8664 = 2
QL_ARM = 3
QL_ARM_THUMB = 4
QL_ARM64 = 5
QL_MIPS32 = 6

QL_ENDIAN_EB = 2
QL_ENDIAN_EL = 1

QL_LINUX = 1
QL_FREEBSD = 2
QL_MACOS = 3
QL_WINDOWS = 4
QL_POSIX = 5

QL_OUT_DEFAULT = 1
QL_OUT_DISASM = 2
QL_OUT_DEBUG = 3
QL_OUT_DUMP = 99

QL_GDB = 1
QL_IDAPRO = 2

QL_DEBUGGER = [QL_IDAPRO, QL_GDB]
QL_ARCH = [QL_ARM, QL_ARM64, QL_MIPS32, QL_X86, QL_X8664]
QL_ENDINABLE = [QL_MIPS32, QL_ARM]
QL_OS = [QL_LINUX, QL_FREEBSD, QL_MACOS, QL_WINDOWS]
QL_COMMOS = [QL_POSIX, QL_WINDOWS]
QL_OUTPUT = [QL_OUT_DEFAULT, QL_OUT_DEBUG, QL_OUT_DUMP, QL_OUT_DISASM]