# Container is the wrapper for ELF, PE, ...
from miasm2.analysis.binary import Container
# Machine is the wrapper for managing multiple architecture
from miasm2.analysis.machine import Machine

cont = Container.from_stream(open("re30"))
# Bin stream is a view on the mapped binary
bin_stream = cont.bin_stream

# 'cont.arch' is "x86_32", extracted from the ELF header
print cont.arch
machine = Machine(cont.arch)
# Disassembly engine associated with the current binary
mdis = machine.dis_engine(bin_stream)
# Disassemble the main function
blocks = mdis.dis_multiblock(cont.entry_point)
# Get back the CFG as a dot file
open("cfg.dot", "w").write(blocks.dot())

