for i in range(0, 100):
    for j in range(0, 100):
        opcode = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,13,19,1,9,19,23,1,6,23,27,2,27,9,31,2,6,31,35,1,5,35,39,1,10,39,43,1,43,13,47,1,47,9,51,1,51,9,55,1,55,9,59,2,9,59,63,2,9,63,67,1,5,67,71,2,13,71,75,1,6,75,79,1,10,79,83,2,6,83,87,1,87,5,91,1,91,9,95,1,95,10,99,2,9,99,103,1,5,103,107,1,5,107,111,2,111,10,115,1,6,115,119,2,10,119,123,1,6,123,127,1,127,5,131,2,9,131,135,1,5,135,139,1,139,10,143,1,143,2,147,1,147,5,0,99,2,0,14,0]
        opcode[1] = i
        opcode[2] = j
        pointer = 0 #this will increment in 4s as we move through the opcode
        compute = True #does the loop continue?
        target = 19690720 #the output we're aiming for
        while compute == True:
            if opcode[pointer] == 99: #99 is our signal to stop.
                compute = False
            else:
                update = opcode[pointer+3]    #this is the opcode pointer we will be updating
                a = opcode[pointer+1]
                b = opcode[pointer+2]
                noun = opcode[opcode[pointer+1]]
                verb = opcode[opcode[pointer+2]]
                #print(noun, verb)
                if opcode[pointer] == 1:      #if 1, we add a + b, and store the result.
                    opcode[update] = noun + verb
                    pointer += 4
                elif opcode[pointer] == 2:    #if 2, we multiply a & b, and store the result.
                    opcode[update] = noun * verb
                    pointer += 4
                else:
                    print("Something went wrong.")
                if opcode[0] == target:
                    #I don't understand why I have to reset the noun and verb here, but apparently I do.
                    noun = opcode[1]
                    verb = opcode[2]
                    print(100*noun+verb)
                    
