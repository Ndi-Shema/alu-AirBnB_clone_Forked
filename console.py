import cmd, sys
from  extra.codeunitest import check

class CmdShell(cmd.Cmd):
    intro = 'x will exit _:) (:_'
    prompt = '(hbnb) '
    file = None

    def do_exit(self, inp):
        '''exit the application'''
        return True

    def help_exit(self):
        print('exit the application. shorthand: Ctrl-C.')

    def do_list(self, inp):
        ''' just a test for doing even comparism '''
        print('Output of calling codeunitest is -> ::: {} '.format(check(int(inp))))

    def do_add(self, inp):
        '''arg : value '''
        print("adding '{}'".format(inp))

    def do_oddChecking(self, inp):
        '''arg : value'''
        print('arg : value')
        print('Right should be odd : {}'.format(check(int(inp))))

    def default(self, inp):
        if inp == 'x':
            return self.do_exit(inp)

    do_EOF = do_exit
    help_EOF = help_exit

if __name__ == '__main__':
    CmdShell().cmdloop()
