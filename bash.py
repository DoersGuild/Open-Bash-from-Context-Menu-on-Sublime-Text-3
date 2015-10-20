import os, sublime_plugin, subprocess
class BashCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        current_directory = os.path.dirname(os.path.realpath(self.view.file_name()))
        os.chdir(current_directory)
        # os.system('start "' + r'C:\Program Files\Git\bin\bash.exe' + ' --login -i"')
        # subprocess.Popen([os.path.join(r'C:\Program Files','Git','bin','bash.exe'), '--login', '-i'])
        subprocess.Popen(['bash', '--login', '-i'])
