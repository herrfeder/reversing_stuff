import angr
import claripy
import pdb
from angr.procedures.stubs.UserHook import UserHook

start_addr = 0x8049242


p = angr.Project("neophyte.bin")

argv1 = claripy.BVS("argv1",41*8) 

#state = p.factory.blank_state(addr=start_addr)

state  = p.factory.entry_state(args=["./neophyte.bin",argv1])

sm = p.factory.simgr(state, immutable=False)

debug = True


eax_array = []	

while (debug==True):
	sm.step(1)
	register = sm.active[0].regs
	
	#pdb.set_trace()	
	print hex(register.eip.args[0])


	if register.eip.args[0] == int(0x80484ad):
		state = sm.step(1)
		eax_array.append(hex(register.eax.args[0]))
		print eax_array


#block = p.factory.block(0x8049242)
#block.capstone.pp() #Capstone object has pretty print and other data about the dissassembly
#block.vex.pp()      #Print vex representation




#def check_reg(state):
#	pdb.set_trace()	




#initial_state.inspect.b('call', when=angr.BP_AFTER, address=0x080484ad,action=check_reg )


'''

# translate and pretty-print a basic block starting at an address
irsb = proj.factory.block(0x80484ad).vex
irsb.pp()

print irsb.next

print irsb.jumpkind

irsb.next.pp()

for stmt in irsb.statements:
	stmt.pp()

import pyvex
for stmt in irsb.statements:
	if isinstance(stmt, pyvex.IRStmt.Store):
		print "Data:",
		stmt.data.pp()
		print ""
		print "Type:",
		print stmt.data.result_type
		print ""

# pretty-print the condition and jump target of every conditional exit from the basic block
for stmt in irsb.statements:
	if isinstance(stmt, pyvex.IRStmt.Exit):
		print "Condition:",
		stmt.guard.pp()
		print ""
		print "Target:",
		stmt.dst.pp()
		print ""

print irsb.tyenv.types

print irsb.tyenv.types[0]
'''
