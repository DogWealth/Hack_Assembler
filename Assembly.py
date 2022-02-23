class Assembly:
    symbol_table = {}
    def __init__(self, assembly):
        self.assembly = assembly
    
    def construct(self):
        if self.is_aInstruction():
            return A_Assembly(self.assembly)
        else:
            return C_Assembly(self.assembly)

    def is_aInstruction(self):
        if self.assembly[0] == '@':
            return True
        return False

    def translate(self):
        pass
        
    def __repr__(self) -> str:
        return repr(self.assembly)


class A_Assembly(Assembly):
    def translate(self):
        s = self.assembly[1:]
        if not s.isdigit():
            return '0' + bin(int(self.symbol_table[s]))[2:].rjust(15, '0')
        return '0' + bin(int(self.assembly[1:]))[2:].rjust(15, '0')


class C_Assembly(Assembly):
    comp_dic = {}
    dest_dic = {}
    jump_dic = {}
    def translate(self):
        eq = self.assembly.find('=')
        se = self.assembly.find(';')
        if eq == -1 and se == -1:
            comp = self.assembly
            return '111' + self.comp_dic[comp] + '000000'
        elif eq == -1 and se != -1:
            comp = self.assembly[0:se]
            jump = self.assembly[se+1:]
            return '111' + self.comp_dic[comp] + '000' + self.jump_dic[jump]
        elif eq != -1 and se == -1:
            comp = self.assembly[eq+1:]
            dest = self.assembly[0:eq]
            return '111' + self.comp_dic[comp] + self.dest_dic[dest] + '000'
        else:
            comp = self.assembly[eq+1:se]
            dest = self.assembly[0:eq]
            jump = self.assembly[se+1:]
            return '111' + self.comp_dic[comp] + self.dest_dic[dest] + self.jump_dic[jump]

Assembly.symbol_table = {
    'R0':'0',
    'R1':'1',
    'R2':'2',
    'R3':'3',
    'R4':'4',
    'R5':'5',
    'R6':'6',
    'R7':'7',
    'R8':'8',
    'R9':'9',
    'R10':'10',
    'R11':'11',
    'R12':'12',
    'R13':'13',
    'R14':'14',
    'R15':'15',
    'SCREEN':'16384',
    'KBD':'24576',
    'SP':0,
    'LCL':'1',
    'ARG':'2',
    'THIS':'3',
    'THAT':'4'    
}

C_Assembly.comp_dic = {
    '0':'0101010',
    '1':'0111111',
    '-1':'0111010',
    'D':'0001100',
    'A':'0110000',
    'M':'1110000',
    '!D':'0001101',
    '!A':'0110001',
    '!M':'1110001',
    '-D':'0001111',
    '-A':'0110011',
    '-M':'1110011',
    'D+1':'0011111',
    'A+1':'0110111',
    'M+1':'1110111',
    'D-1':'0001110',
    'A-1':'0110010',
    'M-1':'1110010',
    'D+A':'0000010',
    'D+M':'1000010',
    'D-A':'0010011',
    'D-M':'1010011',
    'A-D':'0000111',
    'M-D':'1000111',
    'D&A':'0000000',
    'D&M':'1000000',
    'D|A':'0010101',
    'D|M':'1010101',
}

C_Assembly.dest_dic = {
    'M':'001',
    'D':'010',
    'MD':'011',
    'A':'100',
    'AM':'101',
    'AD':'110',
    'AMD':'111'
}

C_Assembly.jump_dic = {
    'JGT':'001',
    'JEQ':'010',
    'JGE':'011',
    'JLT':'100',
    'JNE':'101',
    'JLE':'110',
    'JMP':'111'
}