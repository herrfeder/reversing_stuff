from miasm2.analysis.machine import Machine
from miasm2.analysis import binary

bi = binary.Container("./re30 aaaa")
machine = Machine('x86_64')
mn, dis_engine_cls, ira_cls = machine.mn, machine.dis_engine, machine.ira


BB_BEGIN = 0x00400614
BB_END =   0x0040064a

# Disassemble between BB_BEGIN and BB_END
dis_engine = dis_engine_cls(bs=bi.bs)
dis_engine.dont_dis = [BB_END]
bloc = dis_engine.dis_bloc(BB_BEGIN)
print '\n'.join(map(str, bloc.lines))

