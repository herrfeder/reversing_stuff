import angr
import pyvex

proj = angr.Project("./re30")

#irsb = proj.factory.block(proj.entry).vex
#irsb.pp()


irsb = proj.factory.block(0x400614)
irsb.pp()

#print irsb.next.pp()
#print irsb.jumpkind

for stmt in irsb.statements:
	if isinstance(stmt,pyvex.IRStmt.Store):
		print "Data:",
		stmt.data.pp()
		print ""
		print "Type:",
	        print stmt.data.result_type
		print "" 	


