import tkinter.messagebox as tkmsg

def mobchk(chk):
    if chk.isdigit():
        if len(str(chk)) == 10:
            return chk
        else:
            tkmsg.showwarning('Attention!',"Write Proper Mobile No.!")
    else:
        tkmsg.showwarning('Attention!',"Write Proper Mobile No.!")

def mailchk(chk):
    if chk == '':
        return True
    else:
        if '@' in chk:
            at = chk.index('@')
            domain = chk[at+1:]
            if '.' in domain:
                return chk
            else:
                tkmsg.showwarning('Attention!',"Write Proper Mail Id!")
        else:
            tkmsg.showwarning('Attention!',"Write Proper Mail Id!")

if __name__ == '__main__':
    mobchk()
    mobchk()