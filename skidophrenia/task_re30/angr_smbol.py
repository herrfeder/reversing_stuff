import angr
import claripy


def main():

	proj = angr.Project("re30") # load_options={'auto_load_libs': False}
	argv1 = claripy.BVS("argv1",11111111)

	initial_state = proj.factory.entry_state(args=["./re30",argv1])

	sm = proj.factory.simgr(initial_state)

	sm.explore(find=0x400654)

	found = sm.found[0]

	solution = found.se.any_str(argv1)

	print repr(solution)

	print solution



if __name__ == '__main__':

	print(repr(main()))
