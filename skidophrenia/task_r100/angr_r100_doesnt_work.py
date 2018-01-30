#!/usr/bin/env python


'''
ais3_crackme has been developed by Tyler Nighswander (tylerni7) for ais3.

It is an easy crackme challenge. It checks the command line argument.
'''

import angr
import claripy
import logging

def solve_r100():

    # shutdown some warning produced by this example
    logging.getLogger('angr.engines.vex.irsb').setLevel(logging.ERROR)

    proj = angr.Project('./r100', load_options={'auto_load_libs':False})

    start = 0x4006fd
    false = 0x4007a1
    end = 0x00400795 

    #start = 0x4007e8
    #false =0x00400855 
    #end = 0x00400844

    # initial state is at the beginning of phase_one()
    state = proj.factory.blank_state(addr=start)

    # a symbolic input string with a length up to 128 bytes
    arg = state.se.BVS("input_string", 8 * 128)

    # read_line() reads a line from stdin and stores it a this address
    #bind_addr = 0x00400827

    # bind the symbolic string at this address
    #state.memory.store(bind_addr, arg)

    # phase_one reads the string [rdi]
    #state.add_constraints(state.regs.rdi == bind_addr)

    # Attempt to find a path to the end of the phase_1 function while avoiding the bomb_explode
    ex = proj.surveyors.Explorer(start=state, find=(end,),
                                 avoid=(false,),
                                 enable_veritesting=True)
    ex.run()

    if ex.found:
        found = ex.found[0]
        return found.se.eval(arg, cast_to=str).rstrip(chr(0)) # remove ending \0

    pass



def main():
    project = angr.Project("./r100")

    #create an initial state with a symbolic bit vector as argv1

    solution = solve_r100()

    print repr(solution)
    solution = solution[:solution.find("\x00")]
    print solution
    return solution



if __name__ == '__main__':
    print(repr(main()))


